# PROJECT SOURCE CODE STRUCTURE

**Dự án:** YARU

**Kiến trúc:** Client-Server (Frontend: Next.js | Backend: Python FastAPI)

**Mô hình:** Monorepo

**Ngày lập:** 05/01/2026

---

## 1. TỔNG QUAN KIẾN TRÚC

Dự án được chia tách rõ ràng để tối ưu hóa thế mạnh của từng ngôn ngữ:

1.  **Backend (Python/FastAPI):** Xử lý nghiệp vụ nặng, AI (Whisper, NLP), Database và Background Jobs.
2.  **Frontend (TypeScript/Next.js):** Xử lý giao diện tương tác cao (Video Player, Real-time highlighting) và SEO.
3.  **Infrastructure:** Dockerized môi trường phát triển.

---

## 2. CẤU TRÚC THƯ MỤC GỐC (ROOT)

```text
yaru/
├── backend/                # Server API & AI Workers (Python)
├── frontend/               # Web Application (Next.js 14+)
├── docker/                 # Cấu hình Docker (Nginx, Database)
├── docs/                   # Tài liệu dự án (PRD, Design, API Spec)
├── .gitignore
├── docker-compose.yml      # Orchestration cho local development
└── README.md               # Hướng dẫn cài đặt & chạy dự án
```

---

## 3. CHI TIẾT BACKEND (PYTHON / FASTAPI)

Backend áp dụng **Clean Architecture** để dễ dàng bảo trì và mở rộng các module AI.

```text
backend/
├── app/
│   ├── api/                    # API Endpoints (Controllers)
│   │   ├── v1/
│   │   │   ├── auth.py         # Login, Register, OAuth
│   │   │   ├── videos.py       # Upload, CRUD Video
│   │   │   ├── learning.py     # Submit kết quả Shadowing/Dictation
│   │   │   ├── vocab.py        # Quản lý từ vựng, SRS Logic
│   │   │   ├── gamification.py # XP, Streak, Ranking Leaderboard
│   │   │   ├── quiz.py         # Xử lý Logic Quiz, tạo câu hỏi
│   │   │   └── search.py       # Semantic search (Vector Search)
│   │   └── deps.py             # Dependency Injection (DB Session, Current User)
│   │
│   ├── core/                   # Cấu hình hệ thống
│   │   ├── config.py           # Load biến môi trường (.env)
│   │   ├── security.py         # JWT Handling, Password Hashing
│   │   └── celery_app.py       # Cấu hình Background Worker
│   │
│   ├── models/                 # Database Models (SQLAlchemy/Tortoise ORM)
│   │   ├── user.py
│   │   ├── video.py
│   │   ├── transcript.py       # Chứa JSONB cho nội dung phụ đề
│   │   └── vocabulary.py
│   │
│   ├── schemas/                # Pydantic Schemas (Data Validation & Serialization)
│   │   ├── video.py
│   │   ├── transcript.py
│   │   └── user.py
│   │
│   ├── services/               # BUSINESS LOGIC LAYERS (Core)
│   │   ├── ai/                 # Các module xử lý AI
│   │   │   ├── whisper_svc.py  # Wrapper cho OpenAI Whisper (STT)
│   │   │   ├── nlp_svc.py      # Tokenizer (MeCab), Pitch Accent extraction
│   │   │   └── llm_svc.py      # Tích hợp GPT để giải thích ngữ pháp
│   │   ├── vector/             # Xử lý Embeddings
│   │   │   ├── openai_emb.py   # Tạo vector từ text
│   │   │   └── qdrant_svc.py   # Kết nối Vector DB (Qdrant/Pinecone)
│   │   ├── srs_algo.py         # Thuật toán lặp lại ngắt quãng (FSRS/SM-2)
│   │   └── export_svc.py       # Xuất file .apkg (Genanki)
│   │
│   └── workers/                # Background Tasks (Celery)
│       └── video_tasks.py      # Task xử lý video: Upload -> Extract Audio -> AI Process
│
├── alembic/                    # Database Migrations
├── tests/                      # Unit & Integration Tests
├── requirements.txt            # Python dependencies
├── main.py                     # Entry point (FastAPI App)
└── Dockerfile

```

### Điểm nhấn kỹ thuật Backend:

- **`services/ai/`**: Tách biệt logic AI. Nếu thay đổi model (ví dụ từ Whisper sang Google STT), chỉ cần sửa file service mà không ảnh hưởng Controller.
- **`workers/video_tasks.py`**: Xử lý video là tác vụ tốn thời gian (Long-running), bắt buộc chạy dưới dạng Background Job qua Redis/Celery để không chặn Request của người dùng.

---

## 4. CHI TIẾT FRONTEND (NEXT.JS + TYPESCRIPT)

Frontend tập trung vào Component tái sử dụng và quản lý State phức tạp của Video Player.

```text
frontend/
├── app/                        # Next.js 14 App Router
│   ├── (auth)/                 # Route Group: Login, Register
│   ├── (dashboard)/            # Route Group: Có Sidebar & Header
│   │   ├── page.tsx            # Dashboard chính (Tiến độ, Streak)
│   │   ├── videos/             # Danh sách video
│   │   └── vocab/              # Sổ tay từ vựng & Review
│   ├── watch/
│   │   └── [videoId]/          # Trang Player chính
│   │       └── page.tsx
│   ├── practice/               # Các chế độ luyện tập
│   │   ├── shadowing/
│   │   └── dictation/
│   ├── globals.css             # Tailwind imports
│   └── layout.tsx              # Root Layout
│
├── components/                 # UI Components
│   ├── ui/                     # Atomic Components (Button, Input, Modal - Shadcn/UI)
│   ├── player/                 # COMPONENT QUAN TRỌNG NHẤT
│   │   ├── VideoPlayer.tsx     # Wrapper thẻ <video> hoặc ReactPlayer
│   │   ├── TranscriptList.tsx  # Danh sách câu thoại bên cạnh
│   │   ├── SubtitleOverlay.tsx # Phụ đề đè lên video
│   │   ├── FuriganaWord.tsx    # Component render thẻ <ruby> chuẩn
│   │   └── QuizPopup.tsx       # Popup trắc nghiệm hiện đè lên video
│   ├── gamification/           # XP Bar, Level Badge, Daily Streak
│   ├── community/              # Components cho Cộng đồng
│   │   └── CommunitySection.tsx
│   └── shared/                 # Navbar, Sidebar, Footer
│
├── lib/                        # Utilities & Helpers
│   ├── axios.ts                # Cấu hình API Client
│   ├── utils.ts                # Hàm hỗ trợ (Format time, cn classnames)
│   └── hooks/                  # Custom React Hooks
│       ├── useVideoTime.ts     # Sync thời gian video
│       └── useAudioRecorder.ts # Xử lý ghi âm cho Shadowing
│
├── store/                      # Global State (Zustand)
│   ├── useUserStore.ts         # User info, settings (Darkmode)
│   └── usePlayerStore.ts       # Trạng thái Player (Playing, CurrentTime, CaptionMode)
│
├── types/                      # TypeScript Interfaces
│   ├── video.d.ts              # Định nghĩa cấu trúc Video, TranscriptSegment
│   └── api.d.ts                # Định nghĩa API Response
│
├── public/                     # Static assets (Images, Fonts)
├── tailwind.config.ts          # Config màu sắc, Fonts
└── package.json

```

### Điểm nhấn kỹ thuật Frontend:

- **`components/player/FuriganaWord.tsx`**: Component chuyên biệt để xử lý hiển thị `<ruby><rb>Kanji</rb><rt>Furigana</rt></ruby>`, đảm bảo hiển thị đúng trên mọi trình duyệt và không bị vỡ layout khi xuống dòng.
- **`store/usePlayerStore.ts`**: Quản lý `currentTime` của video. TranscriptList sẽ lắng nghe biến này để tự động cuộn (Auto-scroll) và Highlight từ đang nói.

---

## 5. DATABASE SCHEMA (CẤU TRÚC DỮ LIỆU)

### Bảng `users`

- `id` (UUID, PK)
- `email`, `password_hash`
- `xp` (Integer), `level` (Integer), `streak` (Integer)
- `settings` (JSONB): Lưu cấu hình Darkmode, cỡ chữ, màu sắc.

### Bảng `videos`

- `id` (UUID, PK)
- `title`, `url`, `thumbnail_url`
- `duration` (Float)
- `difficulty_level` (Enum: N5-N1)
- `status` (Enum: PROCESSING, READY, ERROR)

### Bảng `transcripts`

- `id` (PK)
- `video_id` (FK -> videos)
- `content` (JSONB): Lưu cấu trúc chi tiết.

```json
[
  {
    "start": 0.5,
    "end": 2.1,
    "text": "こんにちは",
    "tokens": [
      {
        "word": "こんにちは",
        "reading": "konnichiwa",
        "pitch": "01000",
        "type": "greeting"
      }
    ],
    "translation": "Xin chào"
  }
]
```

### Bảng `vocabularies` (User lưu từ)

- `id` (PK)
- `user_id` (FK)
- `video_id` (FK) - Lưu nguồn gốc
- `word` (String)
- `context_sentence` (Text) - Câu văn chứa từ đó
- `context_time` (Float) - Thời gian xuất hiện
- `srs_stage` (Integer), `next_review_at` (Datetime)

---

## 6. TECH STACK ĐỀ XUẤT (CÔNG NGHỆ)

| Thành phần         | Công nghệ                                          | Lý do chọn                                                   |
| ------------------ | -------------------------------------------------- | ------------------------------------------------------------ |
| **Frontend**       | Next.js 14, TypeScript, Tailwind CSS               | SEO tốt, Type safe, dễ dàng tùy biến giao diện.              |
| **State Mngt**     | Zustand                                            | Nhẹ hơn Redux, phù hợp quản lý state của Video Player.       |
| **Backend**        | Python, FastAPI                                    | Hiệu năng cao (Async), hệ sinh thái AI phong phú nhất.       |
| **Database**       | PostgreSQL                                         | Mạnh mẽ, hỗ trợ JSONB (lưu transcript linh hoạt).            |
| **Vector DB**      | Qdrant / Pgvector                                  | Để thực hiện tính năng tìm kiếm ngữ nghĩa (Semantic Search). |
| **AI Models**      | OpenAI Whisper (STT), SudachiPy (NLP), GPT-4o-mini | Bộ stack chuẩn cho xử lý tiếng Nhật hiện nay.                |
| **Infrastructure** | Docker, Nginx, Redis                               | Dễ dàng triển khai và mở rộng.                               |
