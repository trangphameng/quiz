# Công cụ dựng IELTS Task 1 – Table

Thư mục này không hiện trên trang web (GitHub Pages bỏ qua thư mục bắt đầu bằng `_`).
Trang: https://trangphameng.github.io/quiz/ielts-table/

- `lessons/Txx.json` – dữ liệu từng đề (đề bài, bảng gõ lại, bài mẫu, từ vựng, 20 câu). Đọc `example.json` để xem đủ định dạng.
- `gen/Txx.py` – script nhỏ viết ra `lessons/Txx.json` (để dễ sửa sau).
- `template.html` – giao diện chung: trái là thẻ “Đề bài” (đề + bảng) và “Bài mẫu” (khoá đến khi xong Phần 1–3); phải là 6 phần; nhập tên/lớp, nộp điểm về Google Form của cô (chung sheet với game từ vựng, cột Bài = `Task 1 Table Txx · topic`).
- `build.py` – kiểm tra dữ liệu (khung 6 phần 4-3-3-4-3-3 = 20 câu, đáp án đúng ở options[0], vocab khớp bài mẫu…) rồi dựng `../Txx.html` + `../index.html`.
- `test.py` – thử 1 đề trong Chromium ở 1280px và 390px (chặn docs.google.com).
- `crop.py` – cắt ảnh bảng gốc khi bảng quá phức tạp để gõ lại (lưu `../images/`).

Thêm đề: viết `gen/Txx.py` → `python3 gen/Txx.py` → `python3 build.py` → `python3 test.py .. Txx`.
