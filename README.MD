# YARU - Nền tảng Học tiếng Nhật (Tích hợp AI)

Dự án YARU là một ứng dụng học tiếng Nhật theo phong cách "vừa học vừa chơi" (gamified), sử dụng AI để tự động xử lý video, tạo phụ đề và cung cấp các tính năng học tập tương tác.

## 📁 Cấu trúc Dự án

Đây là một Monorepo bao gồm:

- **`frontend/`**: Next.js 14, TypeScript, Tailwind CSS.
- **`backend/`**: Python FastAPI, Các module xử lý AI.
- **`docs/`**: Tài liệu dự án (PRD, Design System, Tech Stack, v.v.).
- **`docker/`**: Cấu hình Docker.

## 🚀 Lộ trình Phát triển (MVP Roadmap)

### MVP 1: Nền Tảng Video & Transcript (Foundation)
*Mục tiêu: Người xem có thể upload video và xem với phụ đề thô.*

- [ ] **1.1. Backend Setup**: Cấu trúc project FastAPI, kết nối Database PostgreSQL.
- [ ] **1.2. Upload API**: API upload video (`.mp4`) và lưu trữ (Local/S3).
- [ ] **1.3. AI Processing (Basic)**: Tích hợp `OpenAI Whisper` để tạo file transcript từ video video.
- [ ] **1.4. Frontend Player (Basic)**: Video Player hiển thị video + danh sách phụ đề bên cạnh (chưa cần highlight từng từ).
- [ ] **1.5. Data Sync**: Đồng bộ thời gian video để highlight dòng phụ đề hiện tại.

### MVP 2: Học tương tác & AI (Core Learning)
*Mục tiêu: Người dùng có thể tra từ, lưu từ và học sâu.*

- [ ] **2.1. NLP Pipeline**: Tích hợp `MeCab` (tách từ) và từ điển để lấy nghĩa, Furigana.
- [ ] **2.2. Interactive Dictionary**: Click vào từ trên phụ đề -> Hiện popup nghĩa & Furigana.
- [ ] **2.3. Save Vocabulary**: API lưu từ vựng kèm ngữ cảnh (câu, thời gian video) vào DB.
- [ ] **2.4. Pitch Accent**: Hiển thị cao độ (nếu có thể tích hợp thư viện NLP phù hợp).
- [ ] **2.5. Search**: Tìm kiếm video theo tiêu đề đơn giản.

### MVP 3: Gamification & Quiz (Engagement)
*Mục tiêu: Giữ chân người dùng bằng game hóa và bài tập.*

- [ ] **3.1. Quiz System**: Backend tạo câu hỏi trắc nghiệm tự động (hoặc thủ công) tại các điểm chốt.
- [ ] **3.2. Quiz UI**: Popup trắc nghiệm khi video dừng, chặn xem tiếp nếu chưa trả lời (tùy chọn).
- [ ] **3.3. XP & Streak**: Hệ thống tính điểm XP khi xem xong video/trả lời đúng.
- [ ] **3.4. User Profile**: Trang cá nhân hiển thị Level, Rank, Số ngày học liên tục.

### MVP 4: Cộng đồng & AI Nâng cao (Community & Advanced)
*Mục tiêu: Mở rộng kết nối và tính năng thông minh.*

- [ ] **4.1. Community Feed**: Bảng tin chia sẻ thành tích, bình luận dưới video.
- [ ] **4.2. Chatbot AI**: Tích hợp LLM để giải thích ngữ pháp khi user hỏi.
- [ ] **4.3. Shadowing Mode**: Thu âm giọng người dùng và phát lại so sánh.

---

## 🚀 Bắt đầu (Getting Started)

### Yêu cầu cài đặt (Prerequisites)

- **Node.js** (v18+)
- **Python** (3.10+)
- **Docker** (Tùy chọn, để chạy full stack với Database)

### 1. Cài đặt Backend (FastAPI)

```bash
cd backend

# Tạo môi trường ảo (Virtual Environment)
python -m venv venv

# Kích hoạt (Windows)
.\venv\Scripts\activate
# Kích hoạt (Mac/Linux)
# source venv/bin/activate

# Cài đặt thư viện dependencies
pip install -r requirements.txt

# Chạy Server
uvicorn main:app --reload
```

> Backend sẽ chạy tại: `http://localhost:8000`
> Tài liệu API (Swagger): `http://localhost:8000/docs`

### 2. Cài đặt Frontend (Next.js)

```bash
cd frontend

# Cài đặt dependencies
npm install

# Chạy Server Development
npm run dev
```

> Frontend sẽ chạy tại: `http://localhost:3000`

## 📚 Tài liệu tham khảo

Xem thư mục `docs/` để biết thông tin chi tiết:

- [PRD (Yêu cầu sản phẩm)](./docs/PRD.MD)
- [Design System (Hệ thống thiết kế)](./docs/DesignSystem.MD)
- [Project Structure (Cấu trúc dự án)](./docs/ProjectStructure.MD)
- [Tech Stack (Công nghệ sử dụng)](./docs/TECHSTACK.MD)
- [User Flow (Luồng người dùng)](./docs/USERFLOW.MD)

## 🛠 Tính năng chính

- **Gamification**: Hệ thống XP, Rank, Chuỗi ngày học (Streak).
- **Video Learning**: Phụ đề thông minh, Furigana, Cao độ (Pitch Accent).
- **Tích hợp AI**: Whisper (STT), GPT-4o-mini (Giải thích ngữ pháp), Vector Search.
- **Cộng đồng**: Thảo luận & Chia sẻ thành tích.
