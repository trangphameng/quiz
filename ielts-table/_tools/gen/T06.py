"""T06 – Cars crossing four bridges in New Stratford (Lessons for IELTS Advanced Writing). Chạy: python3 gen/T06.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {indicates|indicate} {usage|usage} of four bridges over a 16-hour period on a typical day in New Stratford."},
    {"label": "Overview", "text": "{In general|general}, {traffic volumes|volume} decrease at night and are highest in the morning and afternoon."},
    {"label": "Thân bài 1", "text": "The Harbour Bridge is {the busiest|busiest} bridge. At {peak morning rush hour|rush}, 12,500 vehicles cross the bridge, and this {declines only slightly|slightly} over the day. By 8 p.m., however, usage {drops by nearly half|half}, and it drops again to 2,550 by midnight. The River Bridge has smaller volumes but {a similar pattern|pattern}. At 4 p.m., about 8,500 vehicles cross this bridge, and this {almost halves|halves} to 4,450 vehicles by 8 p.m., with a bigger midnight drop."},
    {"label": "Thân bài 2", "text": "The City Bridge has heavy daytime use at an average of {just over|justover} 6,000 vehicles, and {unlike|unlike} the other two, usage rises to a peak at midday, with 6,800 vehicles. However, in the evening and at night, {far fewer|fewer} vehicles cross this bridge. The Smith Bridge is the least used one and has its highest usage at 4 p.m., with 3,330 vehicles. {Similar to|similar} the City Bridge, this bridge does not have heavy use at night."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "indicate", "word": "indicate", "ipa": "/ˈɪndɪkeɪt/", "pos": "v", "vi": "cho thấy, thể hiện"},
    {"key": "usage", "word": "usage", "ipa": "/ˈjuːsɪdʒ/", "pos": "n", "vi": "mức độ sử dụng"},
    {"key": "general", "word": "in general", "ipa": "/ɪn ˈdʒenrəl/", "pos": "phrase", "vi": "nhìn chung"},
    {"key": "volume", "word": "traffic volume", "ipa": "/ˈtræfɪk ˈvɒljuːm/", "pos": "n", "vi": "lưu lượng xe"},
    {"key": "busiest", "word": "the busiest", "ipa": "/ðə ˈbɪziɪst/", "pos": "adj", "vi": "đông đúc nhất"},
    {"key": "rush", "word": "rush hour", "ipa": "/ˈrʌʃ aʊə(r)/", "pos": "n", "vi": "giờ cao điểm"},
    {"key": "slightly", "word": "decline slightly", "ipa": "/dɪˈklaɪn ˈslaɪtli/", "pos": "phrase", "vi": "giảm nhẹ"},
    {"key": "half", "word": "drop by nearly half", "ipa": "/drɒp baɪ ˈnɪəli hɑːf/", "pos": "phrase", "vi": "giảm gần một nửa"},
    {"key": "pattern", "word": "a similar pattern", "ipa": "/ə ˈsɪmələ(r) ˈpætn/", "pos": "n phrase", "vi": "xu hướng tương tự"},
    {"key": "halves", "word": "halve", "ipa": "/hɑːv/", "pos": "v", "vi": "giảm một nửa"},
    {"key": "justover", "word": "just over", "ipa": "/dʒʌst ˈəʊvə(r)/", "pos": "phrase", "vi": "hơn một chút"},
    {"key": "unlike", "word": "unlike", "ipa": "/ˌʌnˈlaɪk/", "pos": "prep", "vi": "không giống, khác với"},
    {"key": "fewer", "word": "far fewer", "ipa": "/fɑː ˈfjuːə(r)/", "pos": "phrase", "vi": "ít hơn nhiều (danh từ đếm được)"},
    {"key": "similar", "word": "similar to", "ipa": "/ˈsɪmələ(r) tə/", "pos": "adj", "vi": "giống với"},
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
        mc("Đọc bảng", "Cầu nào đông xe nhất ở **mọi** mốc giờ?",
           ["Harbour Bridge", "River Bridge", "City Bridge", "Smith Bridge"],
           "Harbour Bridge cao nhất ở cả 5 cột (từ 12,500 lúc 8 giờ sáng đến 2,550 lúc nửa đêm)."),
        mc("So sánh", "Lúc 8 giờ sáng, Harbour Bridge (12,500) đông gấp khoảng mấy lần Smith Bridge (2,350)?",
           ["Khoảng 5 lần", "Khoảng 2 lần", "Khoảng 3 lần", "Khoảng 10 lần"],
           "12,500 : 2,350 ≈ 5.3, nên **khoảng 5 lần** (*about five times as many cars as*)."),
        mc("Thì", "Bảng không có năm, chỉ có giờ trong một ngày. Bài nên dùng thì nào?",
           ["Hiện tại đơn (cross, drops)", "Quá khứ đơn (crossed, dropped)", "Tương lai (will cross)", "Hiện tại hoàn thành (have crossed)"],
           "Không có năm nên bảng mô tả một ngày điển hình, dùng **hiện tại đơn**. Bài mẫu viết *cross*, *drops*, *rises*.", long=True),
        mc("Đơn vị", "Số **12,500** ở hàng Harbour Bridge, cột 8 a.m. nghĩa là gì?",
           ["Có 12,500 xe qua cầu trong một giờ, lúc 8 giờ sáng", "Có 12,500 xe qua cầu từ nửa đêm đến 8 giờ sáng", "Có 12,500 người đi bộ qua cầu lúc 8 giờ sáng", "Lượng xe tăng thêm 12,500 lúc 8 giờ sáng"],
           "Đề ghi *number of cars per hour*: số **xe ô tô mỗi giờ** tại mốc đó, không phải tổng cộng dồn hay mức tăng.", long=True),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Bảng có 20 ô, không thể nêu hết.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Cầu nào cũng đông ban ngày và vắng hẳn về đêm", "River Bridge có 6,490 xe lúc 12 giờ trưa", "Smith Bridge có 1,225 xe lúc 8 giờ tối", "City Bridge có 6,150 xe lúc 4 giờ chiều"],
           "Overview nêu xu hướng chung của **cả 4 cầu**. Các ý kia là số lẻ của một ô.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["River Bridge có 6,490 xe lúc 12 giờ trưa", "Harbour Bridge đông nhất, 12,500 xe lúc 8 giờ sáng", "City Bridge đông nhất vào buổi trưa, khác các cầu khác", "Smith Bridge chỉ có 430 xe lúc nửa đêm"],
           "Ba ý kia là đỉnh, đáy hoặc ngoại lệ. 6,490 lúc trưa không nổi bật, bài mẫu bỏ qua.", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, traffic on all four bridges is heaviest during the day and falls sharply at night, with the Harbour Bridge being the busiest.",
            "Overall, 12,500 cars cross the Harbour Bridge at 8 a.m.",
            "Overall, the city should build a new bridge to reduce traffic jams.",
            "Overall, the Smith Bridge has 2,350, 2,125, 3,330, 1,225 and 430 cars per hour."],
           "Overview tốt nêu xu hướng chung và cầu nổi bật nhất, không có số. Các câu kia: có số liệu, nêu ý kiến ngoài bảng, hoặc liệt kê một hàng.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu nhóm các cầu có số liệu gần nhau. Mỗi nhóm nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Không cần nêu riêng"],
     "items": [
        {"label": "Harbour và River (nhiều xe nhất, cùng xu hướng)", "answer": 0,
         "why": "Hai cầu đông nhất, cùng giảm mạnh sau 4 giờ chiều, nên gộp ở **Thân bài 1**."},
        {"label": "City và Smith (ít xe hơn, đêm rất vắng)", "answer": 1,
         "why": "Hai cầu vắng hơn, đều gần như không có xe về đêm, nên gộp ở **Thân bài 2**."},
        {"label": "Tổng số xe qua cả 4 cầu trong ngày", "answer": 2,
         "why": "Bảng không cho tổng; tự cộng ra số mới không cần thiết và dễ sai. **Không cần nêu**."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("Thay đổi", "Harbour: 12,500 (8 a.m.) -> 6,400 (8 p.m.). By 8 p.m., usage ...",
           ["drops by nearly half", "drops nearly two times", "drops by nearly twice", "drops to nearly double"],
           "Giảm từ 12,500 xuống 6,400 là **giảm gần một nửa** -> *drops by nearly half*. *two times / twice / double* chỉ dùng khi tăng gấp đôi."),
        mc("Chủ ngữ", "Câu nào đúng?",
           ["The number of cars crossing the Smith Bridge at midnight is 430.",
            "The number of cars crossing the Smith Bridge at midnight are 430.",
            "The Smith Bridge at midnight is 430 cars.",
            "A number of cars crossing the Smith Bridge at midnight is 430."],
           "**The number of** + động từ số ít (*is*). *A number of* nghĩa là \"nhiều\", không dùng để nêu số liệu. Cây cầu không thể \"là 430 xe\".", long=True),
        mc("fewer / less", "In the evening, ___ vehicles cross the City Bridge.",
           ["far fewer", "far less", "more fewer", "far few"],
           "*vehicles* là danh từ **đếm được** -> **fewer**. *less* dùng cho danh từ không đếm được (*less traffic*). *more fewer* thừa so sánh."),
        mc("Mở bài", "Chọn câu mở bài tốt nhất.",
           ["The table indicates how many cars cross the four main bridges in New Stratford each hour at five different times of day.",
            "The table below shows the number of cars per hour crossing the four major bridges in New Stratford at 8 a.m., 12 noon, 4 p.m., 8 p.m., and midnight.",
            "The graph shows how many cars cross the four main bridges in New Stratford at five times of day.",
            "The table indicated how many cars crossed the four main bridges in New Stratford at five times of day."],
           "Mở bài tốt viết lại đề bằng lời mình, đúng thì hiện tại. Các câu kia: chép nguyên đề, gọi table là *graph*, hoặc dùng quá khứ khi bảng không có năm.", long=True),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: đông nhất lúc 8 giờ sáng (6,225)", "Sai: đông nhất lúc 4 giờ chiều (8,500)", "Sai: đông nhất lúc 8 giờ tối"],
           "Hàng City: 12 giờ trưa 6,800 là cao nhất. Câu đúng. 8,500 là số của River Bridge (nhầm hàng).",
           ctx="The City Bridge is busiest at midday."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: Harbour nhiều hơn (11,750 so với 8,500)", "Đúng", "Sai: hai cầu bằng nhau", "Sai: River chỉ có 6,490 xe"],
           "Cột 4 p.m.: Harbour 11,750 > River 8,500. 6,490 là số của River lúc 12 giờ trưa (nhầm cột).",
           ctx="At 4 p.m., the River Bridge carries more traffic than the Harbour Bridge."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: City nhiều hơn (555 so với 430)", "Đúng", "Sai: Smith có 1,225 xe", "Sai: hai cầu bằng nhau"],
           "Cột Midnight: City 555 > Smith 430. 1,225 là số của Smith lúc 8 giờ tối (nhầm cột).",
           ctx="At midnight, more cars cross the Smith Bridge than the City Bridge."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 1. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Harbour and River Bridges",
     "text": "The Harbour Bridge is [1] bridge. At peak morning rush hour, 12,500 vehicles cross the bridge, and this declines only slightly over the day. By 8 p.m., [2], usage drops by nearly half. The River Bridge has smaller volumes [3] a similar pattern.",
     "options": ["the busiest", "however", "but", "the most busiest", "because"],
     "items": [
        {"answer": 0, "why": "So sánh nhất của *busy* là **the busiest**. *the most busiest* thừa *most*."},
        {"answer": 1, "why": "**however** giữa hai dấu phẩy báo ý đối lập: ban ngày giảm nhẹ, tối giảm mạnh."},
        {"answer": 2, "why": "**but** nối hai ý trái chiều: ít xe hơn *nhưng* cùng xu hướng. *because* là nguyên nhân, không hợp nghĩa."},
     ]},
]

L = {
    "id": "T06",
    "pageTitle": "Task 1 Table T06 · Traffic on four bridges",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T06",
    "heading": "Cars per hour crossing four bridges in New Stratford",
    "topic": "Traffic on four bridges",
    "kind": "Bảng thay đổi · 5 mốc giờ trong ngày",
    "book": "Lessons for IELTS – Advanced Writing",
    "source": "Bài mẫu lấy từ sách: Lessons for IELTS – Advanced Writing, New Oriental Education & Technology Group IELTS Research Institute (có chỉnh sửa nhỏ).",
    "prompt": [
        "The table below shows the number of cars per hour crossing the four major bridges in New Stratford at 8 a.m., 12 noon, 4 p.m., 8 p.m., and midnight.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Number of cars per hour",
         "head": [["Bridges", "8 a.m.", "12 Noon", "4 p.m.", "8 p.m.", "Midnight"]],
         "rows": [
            ["Harbour Bridge", "12,500", "10,300", "11,750", "6,400", "2,550"],
            ["River Bridge", "8,300", "6,490", "8,500", "4,450", "1,250"],
            ["City Bridge", "6,225", "6,800", "6,150", "1,280", "555"],
            ["Smith Bridge", "2,350", "2,125", "3,330", "1,225", "430"],
         ]},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T06.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T06.json –", words, "từ")
