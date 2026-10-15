"""Cắt ảnh bảng (chỉ khi bảng quá phức tạp để gõ lại) từ ảnh chụp/trang PDF đã render.
usage: python3 crop.py anh_goc.png ../images/T01-table.png x0 y0 x1 y1   (toạ độ tỉ lệ 0–1)
Ảnh ra rộng tối đa 900px, giữ PNG cho chữ số sắc nét."""
import sys
from PIL import Image
src, dst, *b = sys.argv[1:]
b = [float(v) for v in b]
im = Image.open(src); W, H = im.size
im = im.crop((int(b[0]*W), int(b[1]*H), int(b[2]*W), int(b[3]*H)))
im.thumbnail((900, 900)); im.save(dst, optimize=True); print(dst, im.size)
