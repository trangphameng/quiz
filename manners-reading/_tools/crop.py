"""Cắt tranh minh hoạ từ một trang PDF đã render (pdftoppm -r 110 -jpeg book.pdf pages/p).
usage: python3 crop.py pages/p-07.jpg ../images/xx-name.jpg x0 y0 x1 y1   (toạ độ tỉ lệ 0–1 của trang)
Ảnh ra rộng tối đa 480px (hiển thị ~240px)."""
import sys
from PIL import Image
src, dst, *b = sys.argv[1:]
b = [float(v) for v in b]
im = Image.open(src); W, H = im.size
im = im.crop((int(b[0]*W), int(b[1]*H), int(b[2]*W), int(b[3]*H)))
im.thumbnail((480, 480)); im.save(dst, quality=80); print(dst, im.size)
