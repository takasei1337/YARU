# PRODUCT REQUIREMENTS DOCUMENT (PRD)

**Tên dự án:** YARU
**Phiên bản:** 1.0
**Ngày lập:** 05/01/2026

---

## 1. TỔNG QUAN (OVERVIEW)

### 1.1. Mục tiêu

Xây dựng nền tảng học tiếng Nhật qua video tích hợp AI, tập trung vào trải nghiệm "Vừa học vừa chơi" (Gamification) với chủ đề Mạo hiểm giả. Hệ thống tự động hóa việc tạo tài liệu học (transcript, dịch, từ vựng) từ nguồn video phong phú, kết hợp các phương pháp học sâu như Shadowing và Spaced Repetition.

### 1.2. Đối tượng người dùng

- Người học tiếng Nhật mọi cấp độ (N5-N1).
- Người yêu thích văn hóa Nhật (Anime, Drama) muốn học qua nội dung thực tế.

---

## 2. CHỨC NĂNG CHI TIẾT (FUNCTIONAL REQUIREMENTS)

### 2.1. Phân hệ Quản lý & Xử lý Video (Video Management & AI Processing)

Đây là lõi xử lý backend để tạo dữ liệu học tập.

| ID         | Tính năng                        | Mô tả chi tiết                                                                                                  | Ưu tiên    |
| :--------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :--------- |
| **VID-01** | **Import Video**                 | - Upload file từ thiết bị (mp4).<br>- Nhập link từ YouTube, TikTok (cần xử lý download/stream).                 | Cao        |
| **VID-02** | **AI Pipeline: STT & Alignment** | - Sử dụng AI (VD: Whisper) để tạo transcript.<br>- Yêu cầu: Timestamp chính xác đến từng câu/từ.                | Cao        |
| **VID-03** | **NLP Processing**               | - Tự động tách từ (Tokenization).<br>- Gắn Furigana cho Kanji.<br>- Gắn nhãn cao độ (Pitch Accent) cho từng từ. | Cao        |
| **VID-04** | **AI Translation**               | Dịch song ngữ câu thoại (Nhật -> Việt/Anh) và lưu vào DB.                                                       | Trung bình |
| **VID-05** | **Vector Embeddings**            | Tạo vector embeddings cho nội dung transcript để phục vụ tính năng tìm kiếm ngữ nghĩa sau này.                  | Cao        |

### 2.2. Phân hệ Trình chơi Video & Học tập (Interactive Player)

Giao diện chính nơi người dùng tương tác.

| ID         | Tính năng                                  | Mô tả chi tiết                                                                                                                         | Ưu tiên    |
| :--------- | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| **PLY-01** | **Điều khiển cơ bản**                      | Play, Pause, Tua (+/- 5s), Loop (lặp lại đoạn A-B), Chỉnh tốc độ (0.5x - 2.0x).                                                        | Cao        |
| **PLY-02** | **Smart Transcript**                       | - Hiển thị phụ đề chạy dọc/ngang.<br>- **Auto-scroll:** Cuộn tự động theo giọng nói.<br>- **Highlight:** Tô sáng từ đang được phát âm. | Cao        |
| **PLY-03** | **Interactive Dictionary**                 | - Click vào từ bất kỳ trên phụ đề để hiện Popup.<br>- Popup chứa: Nghĩa, Furigana, Pitch Accent, Ví dụ, nút "Lưu từ".                  | Cao        |
| **PLY-04** | **Tùy biến hiển thị**                      | - Bật/tắt Furigana.<br>- Chế độ phụ đề: Chỉ Nhật, Song ngữ, Ẩn hoàn toàn (để luyện nghe).                                              | Cao        |
| **PLY-05** | **Trả lời trắc nghiệm (Interactive Quiz)** | Video tự dừng tại các điểm chốt, hiện câu hỏi trắc nghiệm (Multiple Choice/Fill-in) về nội dung vừa xem.                               | Trung bình |

### 2.3. Các Chế độ Luyện tập (Study Modes)

| ID         | Tính năng                 | Mô tả chi tiết                                                                                                            | Ưu tiên    |
| :--------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------------ | :--------- |
| **STD-01** | **Shadowing**             | - Nghe câu mẫu -> Ghi âm giọng người dùng -> Phát lại song song để so sánh.                                               | Trung bình |
| **STD-02** | **Dictation (Nghe chép)** | - Video tự pause sau mỗi câu.<br>- Người dùng gõ lại nội dung nghe được.<br>- Hệ thống so khớp text và chấm điểm lỗi sai. | Cao        |
| **STD-03** | **Pronunciation**         | Sử dụng AI để chấm điểm phát âm của người dùng dựa trên mẫu gốc.                                                          | Thấp       |

### 2.4. Phân hệ Từ vựng & Flashcard (Vocabulary System)

| ID         | Tính năng             | Mô tả chi tiết                                                                                  | Ưu tiên    |
| :--------- | :-------------------- | :---------------------------------------------------------------------------------------------- | :--------- |
| **VOC-01** | **Contextual Saving** | Khi lưu từ, hệ thống lưu snapshot gồm: Từ vựng, Câu chứa từ đó, Link Video, Timecode xuất hiện. | Cao        |
| **VOC-02** | **SRS Review**        | Ôn tập từ vựng theo thuật toán Lặp lại ngắt quãng (Spaced Repetition).                          | Cao        |
| **VOC-03** | **Export Data**       | Cho phép xuất danh sách từ vựng ra file `.apkg` (Anki standard).                                | Trung bình |

### 2.5. Hệ thống Mạo hiểm giả (Gamification)

| ID         | Tính năng               | Mô tả chi tiết                                                                                                          | Ưu tiên    |
| :--------- | :---------------------- | :---------------------------------------------------------------------------------------------------------------------- | :--------- |
| **GAM-01** | **Hệ thống XP & Rank**  | - Tính điểm XP dựa trên số video xem, số từ học thuộc.<br>- Rank: Phân cấp (VD: Tập sự, Đồng, Bạc, Vàng, Kim cương...). | Trung bình |
| **GAM-02** | **Streak (Chuỗi ngày)** | Đếm số ngày học liên tục. Có cơ chế "đóng băng" streak nếu người dùng bận.                                              | Trung bình |
| **GAM-03** | **Nhiệm vụ (Quest)**    | Các nhiệm vụ hàng ngày/tuần (VD: Xem 3 video, Học 20 từ).                                                               | Thấp       |

### 2.6. AI Nâng cao & Chatbot

| ID        | Tính năng                       | Mô tả chi tiết                                                                                             | Ưu tiên    |
| :-------- | :------------------------------ | :--------------------------------------------------------------------------------------------------------- | :--------- |
| **AI-01** | **Semantic Search**             | Tìm kiếm video có chứa câu thoại _mang ý nghĩa tương tự_ câu đang học (Sử dụng Vector DB).                 | Cao        |
| **AI-02** | **AI Context Explainer**        | Chatbot bên cạnh video giải thích ngữ pháp cụ thể trong câu, sắc thái của từ vựng trong ngữ cảnh đó.       | Cao        |
| **AI-03** | **Video Auto Leveling**         | AI phân tích độ khó của từ vựng trong video để gắn tag trình độ (N5-N1) và tô màu cảnh báo.                | Trung bình |
| **AI-04** | **User Proficiency Assessment** | **Phân cấp trình độ:** AI phân tích lịch sử học, kết quả quiz để đánh giá lại trình độ người dùng định kỳ. | Trung bình |

### 2.7. Người dùng & Cộng đồng (User & Community)

| ID         | Tính năng              | Mô tả chi tiết                                                                          | Ưu tiên |
| :--------- | :--------------------- | :-------------------------------------------------------------------------------------- | :------ |
| **USR-01** | **Profile & Settings** | - Quản lý thông tin, avatar.<br>- Cài đặt giao diện: Darkmode, Cỡ chữ, Màu sắc chủ đạo. | Cao     |
| **USR-02** | **Dashboard**          | Biểu đồ tiến độ học tập, lịch sử hoạt động, lộ trình đề xuất.                           | Cao     |

### 2.8. Phân hệ Cộng đồng (Community System)

| ID         | Tính năng                 | Mô tả chi tiết                                              | Ưu tiên |
| :--------- | :------------------------ | :---------------------------------------------------------- | :------ |
| **COM-01** | **Discussion & Comments** | Khu vực bình luận dưới video để hỏi đáp, chia sẻ kiến thức. | Thấp    |
| **COM-02** | **Q&A Forum**             | Diễn đàn hỏi đáp chung về tiếng Nhật.                       | Thấp    |
| **COM-03** | **Achievement Sharing**   | Chia sẻ thành tích (Rank, Badge) lên Feed cộng đồng.        | Thấp    |

---

## 3. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL)

1.  **Performance:**
    - Thời gian load video và transcript đồng bộ < 2 giây.
    - Tìm kiếm ngữ nghĩa (Vector Search) phản hồi < 1 giây.
2.  **Compatibility:**
    - Responsive hoàn toàn trên Mobile (Vertical layout cho player) và Desktop.
3.  **Scalability:**
    - Hỗ trợ lưu trữ lượng lớn video và metadata transcript.
4.  **UI/UX:**
    - Tối ưu hóa thao tác tra từ (ít click nhất có thể).
    - Giao diện mang phong cách Game RPG (nếu theo hướng Mạo hiểm giả).

---

## 4. KIẾN TRÚC SƠ BỘ (SUGGESTED TECH STACK)

- **Frontend:** Next.js (React), Tailwind CSS.
- **Backend:** Python (FastAPI/Django) - Ưu tiên Python vì thư viện AI mạnh.
- **Database:**
  - PostgreSQL (User, Progress).
  - Vector Database (Pinecone/pgvector) cho Embeddings.
- **AI Models:**
  - STT: OpenAI Whisper.
  - LLM: GPT-4o-mini (cho Chatbot/Translation).
  - Tokenizers: MeCab/Sudachi.

---
