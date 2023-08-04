# game-controller-with-visual-recognition
Mô tả Project: Chương trình điều khiển trò chơi thông qua nhận diện thủ ngữ.
# 1. Thư mục Main :
- Folder đã được đóng gói thành app, có file exe để chạy chương trình.
# 2. ASL.spec :
- Sử dụng câu lệnh pyinstaller ASL.spec trong terminal của thư mục để tiến hành đóng gói chương trình, sau khi chạy xong sẽ khởi tạo thư mục Main.
# 3. Setup: Hướng dẫn khởi tạo lại chương trình, model,..

# 3.1/ Tạo Dataset:

 3.1.1/ Tạo thư mục train_dataset, bên trong tạo thêm các subfolder với tên là các nhãn cần phân loại.
 
 3.1.2/ Capturing Images.py: sử dụng file để chụp ảnh. Trước đó, thay đổi các thông số total_pic (tổng số ảnh sẽ được chụp trong một lần chạy) và path (đường dẫn đến folder cần được tạo dataset) cho mỗi lần chụp.
 
 3.1.3/ Để tiến hành chụp, ta sẽ đặt tay vào khung xanh và nhấn C để bắt đầu chụp. Khi chụp xong, chương trình sẽ tự động kết thúc. Làm lần lượt cho đến khi chụp đủ hình cho các subfolder.
 
# 3.2/ Trích xuất đặc trưng:

  File sử dụng : trainingdata.ipynb
  
  3.2.1/ Sử dụng tf.keras.preprocessing.image_dataset_from_directory để thực hiện việc load bộ dataset đã được chụp (không cần phải chia các tập train, test và validation).
  
  3.2.1/* Có thể thêm data augmentation để tăng thêm độ đa dạng (Optional).
  
  3.2.2/ Trích xuất 21 landmarks từ bàn tay, sau đó ta sẽ slicing và lấy các landmarks cần thiết, label của mỗi bàn tay là tên của folder ảnh đang được trích xuất.
  
  3.2.3/ Vì label có dạng String, sử dụng LabelEncoder() và to_categorical() trên tập label.
  
  3.2.4/ Slicing tập train và label, sau cùng gộp lại bằng tf.data.Dataset.from_tensor_slices.
  
  3.2.5/ Tiến hành train bằng mô hình LSTM trên các tập được gộp bằng tf.data.Dataset.from_tensor_slices.
 
