# Công cụ dựng bài Manners Reading

Thư mục này không hiện trên trang web (GitHub Pages bỏ qua thư mục bắt đầu bằng `_`).

- `lessons/Lxx.json` – dữ liệu từng bài (bài đọc, từ mới, 20 câu).
- `gen/helpers.py` – hàm soạn bài; `gen/bm.py`, `gs.py`, `gp.py` – nguồn của L01–L12 (3 quyển đầu).
- `template.html` – giao diện chung (nhập tên/lớp, nộp bài về Google Form của cô).
- `build.py` – dựng `../Lxx.html` và `../index.html` từ `lessons/` (trộn thứ tự tiêu đề, kiểm tra 20 câu/bài).
- `crop.py` – cắt tranh minh hoạ, lưu vào `../images/`.

Thêm bài mới: viết `gen/<sách>.py` dùng `helpers.lesson(...)` → `python3 gen/<sách>.py` → `python3 build.py`.
