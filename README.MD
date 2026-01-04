# YARU - Nền tảng Học tiếng Nhật (Tích hợp AI)

Dự án YARU là một ứng dụng học tiếng Nhật theo phong cách "vừa học vừa chơi" (gamified), sử dụng AI để tự động xử lý video, tạo phụ đề và cung cấp các tính năng học tập tương tác.

## 📁 Cấu trúc Dự án

Đây là một Monorepo bao gồm:

- **`frontend/`**: Next.js 14, TypeScript, Tailwind CSS.
- **`backend/`**: Python FastAPI, Các module xử lý AI.
- **`docs/`**: Tài liệu dự án (PRD, Design System, Tech Stack, v.v.).
- **`docker/`**: Cấu hình Docker.

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
