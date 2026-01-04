# DESIGN GUIDELINE (HƯỚNG DẪN THIẾT KẾ)

**Dự án:** Ứng dụng Học tiếng Nhật AI & Gamification
**Phiên bản:** 1.0
**Ngày lập:** 05/01/2026

---

## 1. NGUYÊN TẮC THIẾT KẾ (DESIGN PRINCIPLES)

1.  **Content-First:** Nội dung video và phụ đề là trung tâm. Giao diện (UI) xung quanh phải tối giản để không gây xao nhãng khi học.
2.  **RPG Inspiration:** Giao diện mang hơi hướng Game nhập vai (Mạo hiểm giả) nhưng vẫn giữ sự hiện đại, sạch sẽ (Clean UI). Không thiết kế quá rườm rà như game cổ điển.
3.  **Accessibility:** Tương phản màu sắc tốt, hỗ trợ Dark Mode hoàn hảo để học vào ban đêm.
4.  **Japanese Optimized:** Tối ưu hiển thị Kanji và Furigana (chữ nhỏ trên đầu) rõ ràng trên mọi kích thước màn hình.

---

## 2. MÀU SẮC (COLOR PALETTE)

Hệ thống màu sử dụng biến số (Variables) để dễ dàng chuyển đổi giữa Light Mode và Dark Mode.

### 2.1. Màu chủ đạo (Brand Colors)

Màu sắc mang lại cảm giác năng động nhưng tập trung.

| Tên biến         | Mã màu (Light)     | Mã màu (Dark) | Sử dụng                                      |
| :--------------- | :----------------- | :------------ | :------------------------------------------- |
| `primary-main`   | `#4F46E5` (Indigo) | `#6366F1`     | Nút chính (CTA), Thanh tiêu đề, Icon active. |
| `primary-hover`  | `#4338CA`          | `#818CF8`     | Trạng thái Hover của nút chính.              |
| `secondary-main` | `#EC4899` (Pink)   | `#F472B6`     | Các yếu tố Game (XP, Streak), Nút phụ.       |

### 2.2. Màu nền & Văn bản (Background & Text)

Quan trọng cho chế độ Đọc/Xem video.

| Tên biến         | Mã màu (Light)       | Mã màu (Dark)        | Sử dụng                        |
| :--------------- | :------------------- | :------------------- | :----------------------------- |
| `bg-page`        | `#F9FAFB` (Gray-50)  | `#111827` (Gray-900) | Nền trang tổng thể.            |
| `bg-card`        | `#FFFFFF` (White)    | `#1F2937` (Gray-800) | Nền thẻ từ vựng, khung player. |
| `text-primary`   | `#111827` (Gray-900) | `#F9FAFB` (Gray-50)  | Tiêu đề, nội dung chính.       |
| `text-secondary` | `#6B7280` (Gray-500) | `#9CA3AF` (Gray-400) | Phụ đề phụ, Furigana, Note.    |

### 2.3. Màu phân cấp trình độ (JLPT Level Colors)

Dùng để gắn tag video và từ vựng.

| Trình độ | Mã màu            | Ý nghĩa           |
| :------- | :---------------- | :---------------- |
| **N5**   | `#10B981` (Green) | Nhập môn (Dễ)     |
| **N4**   | `#14B8A6` (Teal)  | Sơ cấp            |
| **N3**   | `#3B82F6` (Blue)  | Trung cấp         |
| **N2**   | `#F59E0B` (Amber) | Cao cấp           |
| **N1**   | `#EF4444` (Red)   | Thượng thừa (Khó) |

### 2.4. Màu trạng thái (Feedback)

| **Success** | `#22C55E` (Xanh lá) | Trả lời đúng. |
| **Error** | `#EF4444` (Đỏ) | Trả lời sai. |
| **Warning** | `#F59E0B` (Vàng cam) | Cảnh báo / Gợi ý. |
| **Neutral** | `#3B82F6` (Xanh dương) | Đang chọn / Active. |

---

## 3. TYPOGRAPHY (KIỂU CHỮ)

Yêu cầu bắt buộc: Sử dụng Font hỗ trợ tiếng Nhật tốt, nét Kanji không bị dính khi hiển thị nhỏ.

### 3.1. Font Family

- **Tiếng Việt/Anh:** `Inter` hoặc `Roboto` (Dễ đọc, hiện đại).
- **Tiếng Nhật:** `Noto Sans JP` (Google Fonts). **Bắt buộc**.

### 3.2. Quy mô kích thước (Type Scale)

| Role          | Size (Mobile/Desktop) | Weight     | Line-height | Ghi chú                   |
| :------------ | :-------------------- | :--------- | :---------- | :------------------------ |
| **Heading 1** | 24px / 32px           | Bold (700) | 1.2         | Tiêu đề trang chính.      |
| **Heading 2** | 20px / 24px           | SemiBold   | 1.3         | Tiêu đề Section.          |
| **Body**      | 16px / 16px           | Regular    | 1.5         | Nội dung thông thường.    |
| **Subtitle**  | 18px / 20px           | Medium     | 1.6         | Phụ đề Video (Cần to rõ). |
| **Furigana**  | 10px / 12px           | Regular    | 1.0         | Chữ nhỏ trên đầu Kanji.   |

---

## 4. UI COMPONENTS (THÀNH PHẦN GIAO DIỆN)

### 4.1. Video Player & Transcript

Khu vực quan trọng nhất của ứng dụng.

- **Subtitle Container:**
  - Vị trí: Nổi bên trên video (Overlay) hoặc nằm dưới video (tùy chỉnh).
  - Background: `rgba(0, 0, 0, 0.6)` (Bán trong suốt để dễ đọc chữ trắng).
- **Active Word (Highlight):**
  - Khi video chạy đến từ nào, từ đó đổi màu sang `primary-main` (Light mode) hoặc `#FBBF24` (Vàng - Dark mode).
  - Style: `Underline` hoặc `Background-highlight`.
- **Furigana Rendering:**
  - Sử dụng thẻ HTML `<ruby>` và `<rt>`.
  - CSS: `ruby-position: over;` (Đảm bảo luôn nằm trên).

### 4.2. Cards (Thẻ)

- **Video Card:**
  - Bo góc: `12px`.
  - Ảnh bìa (Thumbnail): Tỷ lệ 16:9.
  - Nhãn Level (Tag): Nằm góc trên phải.
- **Flashcard (Mặt trước/Sau):**
  - Kích thước lớn, canh giữa màn hình.
  - Hiệu ứng: Flip (Lật) 3D khi bấm vào.

### 4.3. Gamification Elements

- **XP Bar (Thanh kinh nghiệm):**
  - Màu: Gradient từ `#EC4899` đến `#8B5CF6`.
  - Hình dáng: Bo tròn, có hiệu ứng Glow (phát sáng).
- **Rank Badge:**
  - Icon vector các cấp bậc (Gỗ, Đồng, Bạc, Vàng, Kim Cương).

### 4.5. Quiz/Trắc nghiệm Components

- **Quiz Popup/Modal:**
  - Nền: `bg-card` (Trắng/Dark Gray).
  - Shadow: Lớn (`shadow-xl`) để nổi bật trên Video.
  - Layout: Câu hỏi ở trên, 4 phương án ở dưới.
- **Answer Option:**
  - Trạng thái thường: Border `text-secondary`, nền trong suốt.
  - Trạng thái Hover: Border `primary-main`, nền `primary-50`.
  - Trạng thái Selected: Nền `primary-main`, chữ trắng.
  - Trạng thái Correct: Nền `success`, chữ trắng.
  - Trạng thái Wrong: Nền `error`, chữ trắng, rung lắc (Animation).

### 4.4. Buttons & Controls

- **Primary Button:** Bo tròn `8px`. Màu nền `primary-main`. Chữ trắng.
- **Action Button (Lưu từ, Tra từ):** Icon button (Hình dấu cộng, kính lúp). Kích thước vùng chạm (Touch area) tối thiểu `44x44px` cho mobile.

---

## 5. HƯỚNG DẪN UX & TƯƠNG TÁC (INTERACTION)

### 5.1. Click-to-Lookup (Tra từ nhanh)

- **Trigger:** Người dùng chạm vào từ trong phụ đề.
- **Action:**
  1.  Video tự động `Pause`.
  2.  Hiện `Popover` (Máy tính) hoặc `Bottom Sheet` (Điện thoại) đè lên một phần màn hình.
  3.  Nội dung Popup: Từ vựng to, Nghĩa, Nút "Lưu".

### 5.2. Chế độ Luyện tập (Modes)

- **Shadowing UI:**
  - Hiển thị dạng sóng âm (Waveform).
  - Sóng trên: Audio gốc.
  - Sóng dưới: Audio ghi âm của user.
- **Dictation UI (Gõ lại):**
  - Ẩn toàn bộ phụ đề.
  - Hiển thị ô Input lớn.
  - Khi gõ sai: Chữ sai chuyển đỏ, hiển thị chữ đúng màu xanh ngay bên cạnh.

### 5.3. Hướng dẫn hiển thị Câu hỏi Trắc nghiệm (Quiz UX)

- **Trigger:** Khi video chạy đến Timestamp được đánh dấu là "Quiz Point", video tự động Pause.
- **Transition:** Fade in Quiz Modal từ giữa màn hình.
- **Interaction:**
  - Người dùng _bắt buộc_ phải chọn đáp án để tiếp tục (Blocking).
  - Chọn sai: Hiển thị giải thích ngắn gọn, cho phép thử lại hoặc bỏ qua (tùy setting).
  - Chọn đúng: Hiệu ứng Confetti (pháo giấy) nhỏ -> Tự động đóng Modal -> Video Resume.

---

## 6. ICONOGRAPHY & ASSETS

Sử dụng bộ icon **Phosphor Icons** hoặc **FontAwesome** (Rounded version).

- **Menu:** Home, Learn, Community, Profile.
- **Player:** Play, Pause, Forward 5s, Backward 5s, Settings (Gear), Speed (1x).
- **Gamification:**
  - XP: Hình ngôi sao hoặc viên ngọc.
  - Streak: Hình ngọn lửa.
  - Rank: Hình khiên hoặc huy hiệu.

---

## 7. RESPONSIVE GUIDELINE (ĐA THIẾT BỊ)

- **Mobile (Màn hình dọc):**
  - Video Player: Dính chặt trên cùng (Sticky top).
  - Transcript: Chiếm phần còn lại phía dưới, cuộn dọc.
- **Desktop (Màn hình ngang):**
  - Layout chia 2 cột.
  - Cột trái (70%): Video Player lớn.
  - Cột phải (30%): Transcript cuộn dọc + Chatbot AI.

---

## 8. CẤU TRÚC CSS/TAILWIND (GỢI Ý CHO DEV)

Nếu sử dụng Tailwind CSS, hãy config `tailwind.config.js` như sau:

```javascript
module.exports = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#4F46E5",
          dark: "#6366F1",
        },
        level: {
          n5: "#10B981",
          n1: "#EF4444",
        },
      },
      fontFamily: {
        jp: ['"Noto Sans JP"', "sans-serif"],
      },
    },
  },
};
```
