# game-controller-with-visual-recognition
Mô tả Project: Chương trình điều khiển trò chơi thông qua nhận diện thủ ngữ.
# 1. Thư mục Main :
- Folder đã được đóng gói thành app, có file exe để chạy chương trình.
# 2. ASL.spec :
- Sử dụng câu lệnh <code> pyinstaller ASL.spec </code> trong terminal của thư mục để tiến hành đóng gói chương trình, sau khi chạy xong sẽ khởi tạo thư mục Main.
# 3. Setup: Hướng dẫn khởi tạo lại chương trình, model,..

# 3.1/ Tạo Dataset:

 3.1.1/ Tạo thư mục train_dataset, bên trong tạo thêm các subfolder với tên là các nhãn cần phân loại.
 
 3.1.2/ Capturing Images.py: sử dụng file để chụp ảnh. Trước đó, thay đổi các thông số total_pic (tổng số ảnh sẽ được chụp trong một lần chạy) và path (đường dẫn đến folder cần được tạo dataset) cho mỗi lần chụp.
 
 3.1.3/ Để tiến hành chụp, ta sẽ đặt tay vào khung xanh và nhấn C để bắt đầu chụp. Khi chụp xong, chương trình sẽ tự động kết thúc. Làm lần lượt cho đến khi chụp đủ hình cho các subfolder.
 
# 3.2/ Trích xuất đặc trưng:

  File sử dụng : trainingdata.ipynb
  
  3.2.1/ Sử dụng tf.keras.preprocessing.image_dataset_from_directory để thực hiện việc load bộ dataset đã được chụp (không cần phải chia các tập train, test và validation).
 
<pre> 
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size_model)</pre>
  
  3.2.1/* Có thể thêm data augmentation để tăng thêm độ đa dạng (Optional).
  
  <pre>
data_augmentation = Sequential([
  RandomFlip("horizontal"),
  RandomRotation(0.1),
  RandomZoom(0.1),
  RandomBrightness(0.2)]) 
train_ds = train_ds.map(lambda x, y: (data_augmentation(x), y)) </pre>
  
  3.2.2/ Trích xuất 21 landmarks từ bàn tay, sau đó ta sẽ slicing và lấy các landmarks cần thiết, label của mỗi bàn tay là tên của folder ảnh đang được trích xuất.

<pre>
def process(self, path: str):
   img = self.__read_img(path)
   results = super().process(img)
   if not results.multi_hand_world_landmarks:
       return None
   for hand_world_landmarks in results.multi_hand_world_landmarks:
       hand = (
           np.array([[res.x, res.y, res.z] for res in hand_world_landmarks.landmark])
           .transpose()
           .flatten())
   return hand
def process_all(self, rootdir: str):
   labels = os.listdir(rootdir)
   labels.sort()
   X = list()
   y = list()
   for label in labels:
       list_img_paths = [os.path.join(rootdir, label, img) for img in os.listdir(os.path.join(rootdir, label))]
       for path in list_img_paths:
           landmarks = self.process(path)
           if landmarks is None:
               continue
           X.append(landmarks[np.r_[0:3, 15:18, 24:27, 27:30, 36:39, 39:42, 48:51, 51:54, 57:60, 60:63]]) 
           y.append(label)</pre>
  
  3.2.3/ Vì label có dạng String, sử dụng LabelEncoder() và to_categorical() trên tập label.
    <pre>le = LabelEncoder()
    y_encode = le.fit_transform(y)
    y_encode = to_categorical(y_encode, num_classes)</pre>
  
  3.2.4/ Slicing tập train và label, sau cùng gộp lại bằng tf.data.Dataset.from_tensor_slices.
<pre> X_train, X_test, y_train, y_test = train_test_split(X, y_encode, test_size=0.2, random_state=42)
 X_val, X_test, y_val, y_test=train_test_split(X_test, y_test, test_size=0.5, random_state=42)
 
 X_train = np.reshape(X_train, (len(X_train), 1, 30))
 X_val = np.reshape(X_val, (len(X_val), 1, 30))
 X_test = np.reshape(X_test, (len(X_test), 1, 30))
 train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(batch_size_model)
 val_ds = tf.data.Dataset.from_tensor_slices((X_val, y_val)).batch(batch_size_model)
 test_ds = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(batch_size_model)
 input_shape=((1, X_train.shape[1],))</pre>
  
  3.2.5/ Tiến hành train bằng mô hình LSTM trên các tập được gộp bằng tf.data.Dataset.from_tensor_slices.
 <pre> from tensorflow import keras
callback = keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=3)
model = Sequential()
model.add(layers.LSTM(512, return_sequences=True, input_shape=(1,30)))
model.add(layers.LSTM(512, return_sequences=True))
model.add(layers.LSTM(256, return_sequences=True))

model.add(layers.LSTM(256))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))
model.compile(loss='CategoricalCrossentropy', optimizer='adam', metrics=["accuracy"]) </pre>
