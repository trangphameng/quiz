import json, os, re

BOOKS = {
    'BM': ('Basic Manners', 'Basic Manners'),
    'GS': ('Good Manners at School', 'At School'),
    'GP': ('Good Manners in Public', 'In Public'),
}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lessons')

def mc(tag, q, opts, why, image=None, alt=''):
    d = {"type": "mc", "tag": tag, "q": q, "options": opts, "why": why}
    if image: d.update(image="images/" + image + ".jpg", alt=alt)
    return d

def tf(q, ans, why):
    return {"type": "tf", "tag": "Đúng / Sai", "q": q, "answer": ans, "why": why}

def pic(image, alt, q, opts, why, tag="Hình ảnh"):
    return mc(tag, q, opts, why, image, alt)

def headings(options, answers, title="Part 1 · Matching headings"):
    n_extra = len(options) - len(answers)
    return {"type": "match", "title": title,
            "instr": (f"Chọn tiêu đề phù hợp nhất cho mỗi đoạn. Có {n_extra} tiêu đề thừa." if n_extra
                      else "Chọn tiêu đề phù hợp cho mỗi đoạn. Mỗi tiêu đề dùng một lần."),
            "options": options,
            "items": [{"label": f"Paragraph {p}", "para": p, "answer": a, "tag": "Ý chính", "why": w} for p, a, w in answers]}

def which(items, letters="ABCDE", title="Part 1 · Which paragraph?"):
    return {"type": "match", "plain": True, "title": title, "pick": "Chọn đoạn",
            "instr": "Đoạn nào (A–E) chứa thông tin dưới đây?",
            "options": [f"Paragraph {c}" for c in letters],
            "items": [{"label": s, "answer": letters.index(p), "tag": "Tìm thông tin", "why": w} for s, p, w in items]}

def questions(title, instr, qs):
    return {"type": "questions", "title": title, "instr": instr, "questions": qs}

def gap(text_title, text, options, answers):
    return {"type": "gap", "title": "Part 4 · Gapped text",
            "instr": f"Đọc đoạn văn ngắn và chọn câu phù hợp cho mỗi chỗ trống. Có {len(options) - len(answers)} câu thừa.",
            "textTitle": text_title, "text": text, "options": options,
            "items": [{"answer": a, "tag": "Liên kết", "why": w} for a, w in answers]}

def lesson(num, book, pages, heading, title, paras, vocab, parts):
    name, short = BOOKS[book]
    ps = []
    for lb, t in zip("ABCDEFG", paras):
        t = re.sub(r'\{([^|}]+)\}', lambda m: '{%s|%s}' % (m.group(1), m.group(1).lower()), t)
        ps.append({"label": lb, "text": t})
    d = {"id": f"L{num:02d}", "book": name,
         "pageTitle": f"Lesson {num:02d} · {heading}",
         "eyebrow": f"Lesson {num:02d} · B1 · {name} · 20 câu",
         "heading": heading,
         "source": f"Bài đọc phỏng theo {name} – Ann Ingalls (The Child's World, 2013), tr. {pages}.",
         "credit": f"Tranh minh hoạ: Ronnie Rooney, trong {name} (The Child's World, 2013). Dùng cho mục đích học tập.",
         "reading": {"title": title, "paras": ps},
         "vocab": [{"key": k.lower(), "word": w, "ipa": i, "pos": p, "vi": v} for k, w, i, p, v in vocab],
         "parts": parts}
    os.makedirs(OUT, exist_ok=True)
    json.dump(d, open(os.path.join(OUT, d["id"] + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", d["id"])
