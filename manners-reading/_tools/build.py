"""Build GitHub Pages site: python3 build.py  ->  site/Lxx.html + site/index.html"""
import json, glob, os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
T = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
# Site output = the folder that contains _tools/ (i.e. manners-reading/ in the quiz repo)
SITE = os.path.abspath(os.path.join(HERE, '..')) if os.path.basename(HERE) == '_tools' else os.path.join(HERE, 'site')
os.makedirs(SITE, exist_ok=True)

def validate(d, f):
    keys = {v['key'] for v in d['vocab']}
    for p in d['reading']['paras']:
        for m in re.finditer(r'\{([^|}]+)\|([^}]+)\}', p['text']):
            assert m.group(2) in keys, (f, m.group(2))
    n = 0
    for part in d['parts']:
        if part['type'] == 'questions':
            for q in part['questions']:
                n += 1
                assert q.get('why'), (f, q['q'])
                if q['type'] == 'mc':
                    assert len(set(q['options'])) == len(q['options']) == 4, (f, q['q'])
                else:
                    assert isinstance(q['answer'], bool), (f, q['q'])
                if q.get('image'):
                    assert os.path.exists(os.path.join(SITE, q['image'])), (f, q['image'])
        else:
            for it in part['items']:
                n += 1
                assert 0 <= it['answer'] < len(part['options']) and it.get('why'), (f, it)
            if part['type'] == 'gap':
                assert len(re.findall(r'\[\d+\]', part['text'])) == len(part['items']), f
    assert n == 20, (f, n)

lessons = []
for f in sorted(glob.glob(os.path.join(HERE, 'lessons', 'L*.json'))):
    d = json.load(open(f, encoding='utf-8')); validate(d, f)
    # shuffle heading options (non-plain match parts) so their order never follows the paragraphs
    import random
    for part in d['parts']:
        if part['type'] == 'match' and not part.get('plain'):
            rnd = random.Random(d['id'] + part['title'])
            n = len(part['options']); idx = list(range(n))
            while True:
                rnd.shuffle(idx)
                if sum(idx[it['answer']] == k for k, it in enumerate(part['items'])) <= 1: break
            part['options'] = [part['options'][i] for i in idx]
            for it in part['items']: it['answer'] = idx.index(it['answer'])
    page = T.replace('__TITLE__', html.escape(d['pageTitle'])).replace('__DATA__', json.dumps(d, ensure_ascii=False))
    open(os.path.join(SITE, d['id'] + '.html'), 'w', encoding='utf-8').write(page)
    lessons.append(d); print('built', d['id'])

from itertools import groupby
def card(d):
    return (f'<a class="card" href="{d["id"]}.html"><span class="code">{d["id"]}</span>'
            f'<b>{html.escape(d["heading"])}</b><span class="meta">{html.escape(d["reading"]["title"])}</span></a>')
cards = ''.join('<h2>' + html.escape(b) + '</h2><div class="grid">' + ''.join(card(d) for d in g) + '</div>'
                for b, g in groupby(lessons, key=lambda d: d.get('book', '')))
INDEX = f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Good Manners Reading</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700&family=Literata:opsz,wght@7..72,600&display=swap">
<style>
:root{{--bg:#EDF1F6;--sheet:#fff;--ink:#1A2333;--muted:#5B667A;--line:#D5DCE7;--accent:#2C4A9E}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111722;--sheet:#1A2230;--ink:#E6EBF4;--muted:#9BA6B9;--line:#2D374A;--accent:#93AAFF;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111722;--sheet:#1A2230;--ink:#E6EBF4;--muted:#9BA6B9;--line:#2D374A;--accent:#93AAFF;color-scheme:dark}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Be Vietnam Pro",system-ui,sans-serif;padding:40px 16px 60px}}
.wrap{{max-width:960px;margin:0 auto}}.eyebrow{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
h1{{font-family:Literata,Georgia,serif;font-size:clamp(28px,6vw,40px);margin:6px 0 8px}}p{{color:var(--muted);margin:0 0 24px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}
.card{{display:flex;flex-direction:column;gap:4px;background:var(--sheet);border:1px solid var(--line);border-radius:12px;padding:16px 18px;text-decoration:none;color:inherit}}
.card:hover{{border-color:var(--accent)}}.code{{font-size:12px;font-weight:700;color:var(--accent)}}.card b{{font-family:Literata,Georgia,serif;font-size:20px}}.meta{{font-size:13px;color:var(--muted)}}h2{{font-family:Literata,Georgia,serif;font-size:22px;margin:28px 0 12px}}
</style></head><body><div class="wrap">
<div class="eyebrow">Reading · B1</div><h1>Good Manners Reading</h1>
<p>Chọn một bài để bắt đầu. Mỗi bài có bài đọc, từ mới và 20 câu hỏi. Làm xong, bấm <b>Nộp bài</b> để gửi điểm cho cô.</p>
{cards}<p style="margin-top:32px;font-size:12px">Bài đọc phỏng theo bộ sách của Ann Ingalls; tranh minh hoạ: Ronnie Rooney (The Child&#39;s World, 2013). Dùng cho mục đích học tập.</p></div></body></html>'''
open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(INDEX)
print('index ok')
