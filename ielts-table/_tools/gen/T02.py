"""T02 – Indian students at UK universities (IELTS Liz). Chạy: python3 gen/T02.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {gives information about|info} how many full-time students coming from India studied at six British universities in two academic years (2020/21 and 2021/22), {as well as|aswell} the change in numbers and the percentage increase."},
    {"label": "Overview", "text": "Overall, the greatest percentage increase in Indian students {could be seen|seen} at Sheffield University, {while|while} BPP University showed the lowest increase over the two years. The university with the most students from India was BPP University in the first year and Coventry University in the second year."},
    {"label": "Thân bài 1", "text": "Sheffield University saw {a dramatic rise|dramatic} of 187.7% in Indian students, reaching 2,345 in 2021/22. {Likewise|likewise}, the number also {climbed considerably|climbed} for Coventry University by 2,900 students (121.3%) {to hit|hit} 5,290 students in 2021/22. Another significant increase was seen at Leicester University, from 1,175 to 2,390 students, {a rise of|riseof} 103.4%."},
    {"label": "Thân bài 2", "text": "All other universities saw an increase of {under 100%|under} in the number of Indian students from 2020/21 to 2021/22. The number of students going to the University of Greenwich and Anglia Ruskin University rose by 2,085 students (84.9%) and 1,340 (69.6%) {respectively|resp}. {Regarding|regarding} BPP University, the number of students {remained high|remained} in both years at 3,505 and 5,145, which was {a growth of only|growth} 46.8%."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "info", "word": "give information about", "ipa": "/ɡɪv ˌɪnfəˈmeɪʃn əˈbaʊt/", "pos": "v phrase", "vi": "cung cấp thông tin về"},
    {"key": "aswell", "word": "as well as", "ipa": "/əz wel əz/", "pos": "conj", "vi": "cũng như, cùng với"},
    {"key": "seen", "word": "could be seen (at)", "ipa": "/kʊd bi siːn/", "pos": "v phrase", "vi": "có thể thấy (ở)"},
    {"key": "while", "word": "while", "ipa": "/waɪl/", "pos": "conj", "vi": "trong khi (đối lập)"},
    {"key": "dramatic", "word": "a dramatic rise", "ipa": "/ə drəˈmætɪk raɪz/", "pos": "n phrase", "vi": "sự tăng vọt"},
    {"key": "likewise", "word": "likewise", "ipa": "/ˈlaɪkwaɪz/", "pos": "adv", "vi": "tương tự như vậy"},
    {"key": "climbed", "word": "climb considerably", "ipa": "/klaɪm kənˈsɪdərəbli/", "pos": "v phrase", "vi": "tăng đáng kể"},
    {"key": "hit", "word": "(rise) to hit", "ipa": "/tə hɪt/", "pos": "v", "vi": "chạm mức, đạt tới"},
    {"key": "riseof", "word": "a rise of (+ %)", "ipa": "/ə raɪz əv/", "pos": "n phrase", "vi": "mức tăng là"},
    {"key": "under", "word": "under 100%", "ipa": "/ˈʌndə(r)/", "pos": "prep", "vi": "dưới 100%"},
    {"key": "resp", "word": "respectively", "ipa": "/rɪˈspektɪvli/", "pos": "adv", "vi": "lần lượt là (đúng thứ tự đã nêu)"},
    {"key": "regarding", "word": "regarding", "ipa": "/rɪˈɡɑːdɪŋ/", "pos": "prep", "vi": "về phần, đối với"},
    {"key": "remained", "word": "remain high", "ipa": "/rɪˈmeɪn haɪ/", "pos": "v phrase", "vi": "vẫn ở mức cao"},
    {"key": "growth", "word": "a growth of only", "ipa": "/ə ɡrəʊθ əv ˈəʊnli/", "pos": "n phrase", "vi": "mức tăng chỉ có"},
]

def mc(tag, q, options, why, ctx=None, long=False):
    d = {"type": "mc", "tag": tag, "q": q, "options": options, "why": why}
    if ctx: d["ctx"] = ctx
    if long: d["long"] = True
    return d

CHECK = "Câu này có đúng với bảng không?"
parts = [
    {"type": "questions", "before": True, "title": "Part 1 · Đọc bảng",
     "instr": "Nhìn bảng rồi trả lời. Chưa cần xem bài mẫu.",
     "questions": [
        mc("Đọc bảng", "Năm **2021/22**, trường nào có nhiều sinh viên Ấn Độ nhất?",
           ["Coventry", "BPP", "Greenwich", "Sheffield"],
           "Năm 2021/22 Coventry có 5,290, nhiều hơn BPP (5,145). BPP chỉ đông nhất ở năm 2020/21 (3,505), nên phải nhìn đúng cột năm."),
        mc("Đọc bảng", "Trường nào có **% tăng** thấp nhất?",
           ["BPP", "Leicester", "Anglia Ruskin", "Greenwich"],
           "Cột % Increase: BPP thấp nhất (46.8%). Leicester có số người tăng ít nhất (1,215) nhưng % tăng lại cao (103.4%) vì xuất phát từ số nhỏ."),
        mc("Thì", "Bảng có 2 năm học đã qua (2020/21 và 2021/22). Bài viết nên dùng thì nào?",
           ["Quá khứ đơn (rose, saw)", "Hiện tại đơn (rises, sees)", "Hiện tại hoàn thành (has risen)", "Tương lai (will rise)"],
           "Số liệu thuộc các năm đã qua nên dùng **quá khứ đơn**. Hiện tại hoàn thành không đi với mốc thời gian cụ thể như *in 2021/22*."),
        mc("Đơn vị", "Số **2,900** ở cột *Change* của Coventry nghĩa là gì?",
           ["Số sinh viên tăng thêm 2,900 người", "Số sinh viên tăng 2,900%", "Tổng số sinh viên năm 2021/22", "Số sinh viên năm 2020/21"],
           "*Change* = 5,290 − 2,390 = 2,900 người, là số tuyệt đối. Phần trăm nằm ở cột bên cạnh (121.3%). Viết *rose by 2,900 students*.", long=True),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Bảng có 30 con số, không thể nêu hết.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Sheffield tăng mạnh nhất theo %, BPP tăng ít nhất", "Anglia Ruskin tăng thêm 1,340 sinh viên", "Greenwich có 2,455 sinh viên năm 2020/21", "Leicester tăng 103.4%"],
           "Overview nêu điểm nổi bật nhất: cao nhất, thấp nhất, xu hướng chung. Các ý còn lại là chi tiết có số, để ở thân bài.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["Anglia Ruskin có 1,925 sinh viên năm 2020/21", "Coventry đông nhất năm 2021/22", "BPP đông nhất năm 2020/21", "Sheffield tăng mạnh nhất theo %"],
           "Ba ý kia đều là cao nhất hoặc tăng mạnh nhất. Số của Anglia Ruskin năm đầu không nổi bật, chỉ cần nhắc qua hoặc bỏ.", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, the number of Indian students rose at all six universities, with Sheffield showing the greatest percentage increase and BPP the smallest.",
            "Overall, Sheffield University rose by 187.7%, from 815 to 2,345 students.",
            "Overall, Indian students prefer Coventry because it offers better courses.",
            "Overall, Coventry had 5,290 students, Greenwich had 4,540 and BPP had 5,145."],
           "Overview tốt nêu xu hướng chung (cả 6 trường đều tăng) và điểm nổi bật, không có số. Các câu kia: có số liệu, nêu lý do ngoài bảng, hoặc liệt kê từng hàng.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu chia các trường theo mức tăng. Mỗi nhóm nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Overview"],
     "items": [
        {"label": "Sheffield, Coventry, Leicester (tăng trên 100%)", "answer": 0,
         "why": "Ba trường tăng hơn gấp đôi được gộp vào **Thân bài 1**: Sheffield 187.7%, Coventry 121.3%, Leicester 103.4%."},
        {"label": "Greenwich, Anglia Ruskin, BPP (tăng dưới 100%)", "answer": 1,
         "why": "Ba trường tăng dưới 100% vào **Thân bài 2**. Nhóm theo mức tăng giúp so sánh, thay vì đi lần lượt từng hàng như trong bảng."},
        {"label": "Cả 6 trường đều tăng; BPP đông nhất năm đầu, Coventry đông nhất năm sau", "answer": 2,
         "why": "Đây là xu hướng chung và điểm cao nhất, không cần số cụ thể, nên đặt ở **Overview**."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("Chủ ngữ", "The number of Indian students at Anglia Ruskin ___ by 1,340.",
           ["rose", "were rose", "were risen", "rised"],
           "**The number of** + động từ số ít; *rise* là động từ bất quy tắc (rise – rose – risen) và không dùng bị động. *were* là lỗi chia theo *students*."),
        mc("Giới từ", "Coventry's figure climbed ___ 2,900 students ___ 5,290.",
           ["by / to", "to / by", "with / at", "for / to"],
           "**by** + mức thay đổi (tăng thêm 2,900), **to** + mức cuối (lên 5,290). *with* là dịch từ \"tăng với\"."),
        mc("So sánh", "Leicester tăng từ 1,175 lên 2,390. Cách nói nào đúng?",
           ["roughly doubled", "increased twice more", "rose two times as", "was double than"],
           "2,390 : 1,175 ≈ 2, nên **roughly doubled** (tăng gần gấp đôi). *twice more* là dịch từ \"tăng gấp đôi hơn\"; *double than* sai cấu trúc."),
        mc("respectively", "Trong câu này, *respectively* cho biết điều gì?",
           ["Greenwich +2,085, Anglia Ruskin +1,340", "Greenwich +1,340, Anglia Ruskin +2,085", "Cả hai trường đều +2,085", "Hai trường tăng tổng cộng 3,425"],
           "**respectively** = lần lượt: số thứ nhất đi với trường nhắc trước, số thứ hai với trường nhắc sau. Viết sai thứ tự là sai số liệu.",
           ctx="The number of students at Greenwich and Anglia Ruskin rose by 2,085 and 1,340, respectively."),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: Greenwich đông nhất (2,455)", "Sai: Coventry đông nhất (2,390)", "Sai: Sheffield đông nhất"],
           "Năm 2020/21: BPP 3,505 là cao nhất, hơn Greenwich (2,455) và Coventry (2,390). Câu đúng.",
           ctx="BPP University had the most Indian students in 2020/21."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: BPP tăng ít nhất theo % (46.8%)", "Đúng", "Sai: Anglia Ruskin tăng ít nhất (69.6%)", "Sai: Sheffield tăng ít nhất"],
           "*in percentage terms* = xét theo %. Leicester tăng 103.4%, khá cao. Leicester chỉ có **số người** tăng ít nhất (1,215), đừng nhầm cột *Change* với cột *% Increase*.",
           ctx="The University of Leicester saw the smallest increase in percentage terms."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: BPP nhiều hơn (5,145 so với 4,540)", "Đúng", "Sai: hai trường bằng nhau", "Sai: Greenwich chỉ hơn BPP ở năm 2020/21"],
           "Năm 2021/22: BPP 5,145 > Greenwich 4,540. Năm 2020/21 BPP cũng nhiều hơn (3,505 so với 2,455).",
           ctx="Greenwich had more Indian students than BPP in 2021/22."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 1. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Coventry and Leicester",
     "text": "Likewise, the number also [1] for Coventry University [2] 2,900 students (121.3%) to hit 5,290 students in 2021/22. Another significant increase was seen at Leicester University, from 1,175 to 2,390 students, [3] 103.4%.",
     "options": ["climbed considerably", "by", "a rise of", "climbed considerable", "with"],
     "items": [
        {"answer": 0, "why": "Bổ nghĩa cho động từ *climbed* cần trạng từ **considerably**. *considerable* là tính từ."},
        {"answer": 1, "why": "**by** + mức thay đổi. *with 2,900* là dịch từ \"tăng với 2,900\"."},
        {"answer": 2, "why": "**a rise of** + % = mức tăng là. Cụm danh từ này đứng sau dấu phẩy, bổ sung cho cả mệnh đề trước."},
     ]},
]

L = {
    "id": "T02",
    "pageTitle": "Task 1 Table T02 · Indian students in UK universities",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T02",
    "heading": "Full-time students from India at UK universities",
    "topic": "Indian students in UK universities",
    "kind": "Bảng thay đổi · 2020/21 -> 2021/22",
    "book": "IELTS Liz (ieltsliz.com)",
    "source": "Đề và bài mẫu: IELTS Liz, https://ieltsliz.com/ielts-table-band-9-model-answer/ (Model Answer 1, có chỉnh sửa nhỏ). Dùng cho mục đích học tập.",
    "prompt": [
        "The table below shows the number of full-time students from India who studied at various universities in the UK in 2020/21 and 2021/22.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Full-time Students from India",
         "head": [["University", "2020/21", "2021/22", "Change", "% Increase"]],
         "rows": [
            ["Coventry University", "2,390", "5,290", "2,900", "121.3"],
            ["The University of Greenwich", "2,455", "4,540", "2,085", "84.9"],
            ["BPP University", "3,505", "5,145", "1,640", "46.8"],
            ["Sheffield University", "815", "2,345", "1,530", "187.7"],
            ["Anglia Ruskin University", "1,925", "3,265", "1,340", "69.6"],
            ["The University of Leicester", "1,175", "2,390", "1,215", "103.4"],
         ],
         "note": "Source: www.ieltsliz.com"},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T02.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T02.json –", words, "từ")
