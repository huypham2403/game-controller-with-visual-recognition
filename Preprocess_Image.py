# coding: utf-8
import cv2
import numpy as np
from keras.models import load_model
import os 
import mediapipe as mp

def process_image(image, hands):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = hands.process(image)
  if not results.multi_hand_world_landmarks:
    return None

  for hand_world_landmarks in results.multi_hand_world_landmarks:
    hand = (
      np.array(
        [[res.x, res.y, res.z] for res in hand_world_landmarks.landmark]
      )
      .transpose()
      .flatten()
    )
    hand = hand[np.r_[0:3, 15:18, 24:27, 27:30, 36:39, 39:42, 48:51, 51:54, 57:60, 60:63]]
  return hand

hands = mp.solutions.hands.Hands(static_image_mode=False, min_detection_confidence=0.5)


model = load_model("model.h5", compile=False)
data_dir = "train_data"
class_names = os.listdir(data_dir)

frames = []
landmarks = []

def detect(camera_image, batch_size = 32):
  global frames, landmarks
  cropped = camera_image[160:290, 160:290]
  landmark = process_image(cropped, hands) 
  if landmark is not None:
    frames.append(cropped)
    landmarks.append(landmark)
    if len(frames) == batch_size:
      landmarks = np.array(landmarks).reshape(batch_size,1, -1)
      logits = model.predict(landmarks)
      label_counts = {}
      for logit in logits:
        index = np.argmax(logit)
        name = class_names[index]
        label_counts[name] = label_counts.get(name, 0) + 1
      most_predicted_label = max(label_counts, key=label_counts.get)
      frames = []
      landmarks = []
      return most_predicted_label
  return None
