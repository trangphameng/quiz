"""Dựng trang tự học IELTS Writing Task 1 dạng TABLE.

    python3 build.py      ->  ../Txx.html (mỗi file lessons/Txx.json) + ../index.html

Kiểm tra dữ liệu trước khi dựng; có lỗi thì dừng và in lỗi, không ghi file nào.
"""
import glob, html, json, os, re, sys
from itertools import groupby

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, '..'))
T = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()

# Khung 6 phần, đúng thứ tự: (kiểu, số câu, làm trước khi mở bài mẫu)
PARTS = [('questions', 4, True),   # Part 1 · Đọc bảng
         ('questions', 3, True),   # Part 2 · Đặc điểm chính (2 câu chọn ý + 1 câu overview)
         ('match', 3, True),       # Part 3 · Nhóm số liệu
         ('questions', 4, False),  # Part 4 · Ngôn ngữ số liệu
         ('questions', 3, False),  # Part 5 · Đúng với bảng không?
         ('gap', 3, False)]        # Part 6 · Hoàn thành bài mẫu


def check(d):
    e = []
    if not re.fullmatch(r'T\d{2}', d.get('id', '')):
        e.append('id phải dạng Txx, ví dụ T01')
    for k in ('id', 'pageTitle', 'eyebrow', 'heading', 'topic', 'book', 'source', 'prompt',
              'tables', 'words', 'sample', 'vocab', 'parts'):
        if not d.get(k):
            e.append(f'thiếu trường {k}')
    if e:
        return e
    for t in d['tables']:
        w = {len(r) for r in t['head'] + t['rows']}
        if len(w) != 1:
            e.append(f'bảng "{t.get("caption", "")}": các hàng không cùng số cột {sorted(w)}')
    if d.get('image') and not os.path.exists(os.path.join(SITE, d['image'])):
        e.append(f'không thấy ảnh {d["image"]}')
    keys = {v['key'] for v in d['vocab']}
    used = set()
    for p in d['sample']:
        for m in re.finditer(r'\{([^|}]+)\|([^}]+)\}', p['text']):
            used.add(m.group(2))
    if used - keys:
        e.append(f'từ trong bài mẫu chưa khai báo ở vocab: {sorted(used - keys)}')
    if keys - used:
        e.append(f'vocab khai báo nhưng không tô trong bài mẫu: {sorted(keys - used)}')
    for v in d['vocab']:
        for k in ('key', 'word', 'ipa', 'pos', 'vi'):
            if not v.get(k):
                e.append(f'vocab {v.get("key")}: thiếu {k}')
    if len(d['parts']) != len(PARTS):
        return e + [f'cần đúng {len(PARTS)} phần, đang có {len(d["parts"])}']
    total = 0
    for i, (part, (typ, cnt, before)) in enumerate(zip(d['parts'], PARTS), 1):
        if part['type'] != typ:
            e.append(f'Part {i}: kiểu phải là {typ}')
            continue
        if bool(part.get('before')) != before:
            e.append(f'Part {i}: before phải là {before}')
        items = part['questions'] if typ == 'questions' else part['items']
        if len(items) != cnt:
            e.append(f'Part {i}: cần {cnt} câu, đang có {len(items)}')
        total += len(items)
        for j, q in enumerate(items, 1):
            s = json.dumps(q, ensure_ascii=False)
            if '→' in s:
                e.append(f'Part {i} câu {j}: dùng "->" thay cho "→"')
            if not q.get('why'):
                e.append(f'Part {i} câu {j}: thiếu why')
            elif len(re.findall(r'[.!?](\s|$)', q['why'].strip())) > 3:
                e.append(f'Part {i} câu {j}: giải thích dài quá 3 câu')
            if typ == 'questions':
                o = q.get('options', [])
                if len(o) != 4 or len(set(o)) != 4:
                    e.append(f'Part {i} câu {j}: cần 4 phương án khác nhau')
                if q.get('answer', 0) != 0:
                    e.append(f'Part {i} câu {j}: đáp án đúng phải ở options[0]')
            elif not 0 <= q['answer'] < len(part['options']):
                e.append(f'Part {i} câu {j}: answer ngoài danh sách options')
        if typ == 'gap':
            if len(re.findall(r'\[\d+\]', part['text'])) != cnt:
                e.append(f'Part {i}: đoạn văn phải có đúng {cnt} chỗ trống [1]..[{cnt}]')
            if len(part['options']) != cnt + 2:
                e.append(f'Part {i}: cần {cnt + 2} lựa chọn (2 thừa)')
            if len({it['answer'] for it in part['items']}) != cnt:
                e.append(f'Part {i}: mỗi chỗ trống phải có đáp án khác nhau')
    if total != 20:
        e.append(f'tổng {total} câu, cần đúng 20')
    p5 = d['parts'][4].get('questions', [])
    if p5 and not any(q['options'][0] == 'Đúng' for q in p5):
        e.append('Part 5: phải có ít nhất 1 câu đáp án là "Đúng"')
    return e


lessons, bad = [], False
for f in sorted(glob.glob(os.path.join(HERE, 'lessons', 'T*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    errs = check(d)
    for m in errs:
        print(f'[{os.path.basename(f)}] LỖI: {m}')
    bad |= bool(errs)
    lessons.append(d)
if bad:
    sys.exit('Dừng: sửa lỗi dữ liệu rồi chạy lại.')

for d in lessons:
    page = T.replace('__TITLE__', html.escape(d['pageTitle'])).replace(
        '__DATA__', json.dumps(d, ensure_ascii=False).replace('</', '<\\/'))
    open(os.path.join(SITE, d['id'] + '.html'), 'w', encoding='utf-8').write(page)
    print('built', d['id'], '-', d['topic'])


def card(d):
    return (f'<a class="card" href="{d["id"]}.html"><span class="code">{d["id"]}</span>'
            f'<b>{html.escape(d["topic"])}</b><span class="meta">{html.escape(d.get("kind", ""))}</span></a>')


groups = ''.join('<h2>' + html.escape(b) + '</h2><div class="grid">' + ''.join(card(d) for d in g) + '</div>'
                 for b, g in groupby(lessons, key=lambda d: d['book']))
if not groups:
    groups = '<p>Chưa có đề nào. Cô sẽ thêm đề sớm nhé.</p>'
INDEX = f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>IELTS Task 1 Tables</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700&family=Literata:opsz,wght@7..72,600&display=swap">
<style>
:root{{--bg:#EEF2F0;--sheet:#fff;--ink:#18241F;--muted:#56665E;--line:#D3DDD8;--accent:#1F6B57}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#101815;--sheet:#18221E;--ink:#E4ECE8;--muted:#98A9A1;--line:#2B3A34;--accent:#6FD0B1;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#101815;--sheet:#18221E;--ink:#E4ECE8;--muted:#98A9A1;--line:#2B3A34;--accent:#6FD0B1;color-scheme:dark}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Be Vietnam Pro",system-ui,sans-serif;padding:40px 16px 60px}}
.wrap{{max-width:960px;margin:0 auto}}.eyebrow{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
h1{{font-family:Literata,Georgia,serif;font-size:clamp(28px,6vw,40px);margin:6px 0 8px}}p{{color:var(--muted);margin:0 0 24px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}}
.card{{display:flex;flex-direction:column;gap:4px;background:var(--sheet);border:1px solid var(--line);border-radius:12px;padding:16px 18px;text-decoration:none;color:inherit}}
.card:hover{{border-color:var(--accent)}}.code{{font-size:12px;font-weight:700;color:var(--accent)}}.card b{{font-family:Literata,Georgia,serif;font-size:19px;line-height:1.3}}.meta{{font-size:13px;color:var(--muted)}}h2{{font-family:Literata,Georgia,serif;font-size:21px;margin:28px 0 12px}}
</style></head><body><div class="wrap">
<div class="eyebrow">IELTS Writing Task 1 · Table</div><h1>Tự học Task 1 dạng bảng</h1>
<p>Chọn một đề để bắt đầu. Mỗi đề có 20 câu: đọc bảng, chọn ý chính, nhóm số liệu, rồi học ngôn ngữ từ bài mẫu. Làm xong, bấm <b>Nộp bài</b> để gửi điểm cho cô.</p>
{groups}<p style="margin-top:32px;font-size:12px">Bài mẫu lấy từ các sách ghi ở từng đề, chỉ dùng cho mục đích học tập.</p></div></body></html>'''
open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(INDEX)
print('index ok –', len(lessons), 'đề')
