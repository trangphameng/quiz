"""T08 – New cars sold in the USA, 2000 and 2005 (Lessons for IELTS – Writing, Model 3). Chạy: python3 gen/T08.py"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {illustrates|illustrate} the number of new cars sold in the USA in 2000 and 2005 and the four major countries that they {came from|camefrom}."},
    {"label": "Overview", "text": "{In general|general}, there was {a slight decrease|slight} in the number of cars sold over the period and, {in particular|particular}, in the number of American cars."},
    {"label": "Thân bài 1", "text": "In 2000, {the largest number of|largest} cars sold in the USA was {locally produced|locally} American cars, at 4.2 million. 2.2 million Japanese cars were sold, and {smaller numbers|smaller} from South Korea and Germany, at 1.1 million and 0.2 million {respectively|respectively}."},
    {"label": "Thân bài 2", "text": "In 2005, this {changed significantly|significantly}. The number of American cars {dropped considerably|dropped}, to 2.6 million, and there was {a significant rise|rise} in the number of Japanese cars sold, to 3.4 million. Sales of South Korean cars {stayed unchanged|unchanged}, at 1.1 million, and there was {a small increase|increase} in German cars, to 0.3 million in 2005."},
]
words = 145  # theo sách

vocab = [
    {"key": "illustrate", "word": "illustrate", "ipa": "/ˈɪləstreɪt/", "pos": "v", "vi": "minh hoạ, thể hiện"},
    {"key": "camefrom", "word": "come from", "ipa": "/kʌm frəm/", "pos": "phrase", "vi": "đến từ, có xuất xứ từ"},
    {"key": "general", "word": "in general", "ipa": "/ɪn ˈdʒenrəl/", "pos": "phrase", "vi": "nhìn chung"},
    {"key": "slight", "word": "a slight decrease", "ipa": "/ə slaɪt ˈdiːkriːs/", "pos": "n phrase", "vi": "sự giảm nhẹ"},
    {"key": "particular", "word": "in particular", "ipa": "/ɪn pəˈtɪkjələ(r)/", "pos": "phrase", "vi": "đặc biệt là"},
    {"key": "largest", "word": "the largest number of", "ipa": "/ðə ˈlɑːdʒɪst ˈnʌmbə(r) əv/", "pos": "phrase", "vi": "số lượng lớn nhất"},
    {"key": "locally", "word": "locally produced", "ipa": "/ˈləʊkəli prəˈdjuːst/", "pos": "adj", "vi": "sản xuất trong nước"},
    {"key": "smaller", "word": "smaller numbers", "ipa": "/ˈsmɔːlə(r) ˈnʌmbəz/", "pos": "n phrase", "vi": "số lượng ít hơn"},
    {"key": "respectively", "word": "respectively", "ipa": "/rɪˈspektɪvli/", "pos": "adv", "vi": "lần lượt (theo thứ tự đã nêu)"},
    {"key": "significantly", "word": "change significantly", "ipa": "/tʃeɪndʒ sɪɡˈnɪfɪkəntli/", "pos": "phrase", "vi": "thay đổi đáng kể"},
    {"key": "dropped", "word": "drop considerably", "ipa": "/drɒp kənˈsɪdərəbli/", "pos": "phrase", "vi": "giảm mạnh"},
    {"key": "rise", "word": "a significant rise", "ipa": "/ə sɪɡˈnɪfɪkənt raɪz/", "pos": "n phrase", "vi": "sự tăng đáng kể"},
    {"key": "unchanged", "word": "stay unchanged", "ipa": "/steɪ ʌnˈtʃeɪndʒd/", "pos": "phrase", "vi": "giữ nguyên, không đổi"},
    {"key": "increase", "word": "a small increase", "ipa": "/ə smɔːl ˈɪŋkriːs/", "pos": "n phrase", "vi": "sự tăng nhẹ"},
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
        mc("Đọc bảng", "Năm **2005**, xe của nước nào bán chạy nhất ở Mỹ?",
           ["Japan", "USA", "South Korea", "Germany"],
           "Năm 2005: Japan 3.4 triệu > USA 2.6 triệu. USA chỉ đứng đầu năm 2000 (4.2 triệu), đừng nhầm năm."),
        mc("Đọc bảng", "Số xe Mỹ giảm bao nhiêu từ 2000 đến 2005?",
           ["1.6 triệu", "2.6 triệu", "1.2 triệu", "0.3 triệu"],
           "4.2 - 2.6 = **1.6 triệu**. 2.6 là số năm 2005 (số còn lại), 1.2 triệu là mức tăng của Japan (3.4 - 2.2)."),
        mc("Đơn vị", "**0.2 million** (Germany, 2000) là bao nhiêu xe?",
           ["200,000 xe", "2 triệu xe", "20,000 xe", "2,000 xe"],
           "1 million = 1,000,000, nên 0.2 million = **200,000**. Đọc kỹ đơn vị *million* trước khi so sánh."),
        mc("Thì", "Bảng có mấy mốc thời gian, và bài nên dùng thì nào?",
           ["2 mốc, quá khứ đơn", "2 mốc, hiện tại đơn", "1 mốc, quá khứ đơn", "2 mốc, tương lai đơn"],
           "Có 2 năm 2000 và 2005, đều đã qua -> bảng thay đổi, dùng **quá khứ đơn**: *dropped, stayed, there was*."),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Không cần nêu hết mọi ô.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Tổng số xe giảm nhẹ, chủ yếu do xe Mỹ giảm", "Xe Đức bán được 0.2 triệu năm 2000", "Xe Hàn bán được 1.1 triệu năm 2005", "Xe Nhật bán được 2.2 triệu năm 2000"],
           "Overview nêu xu hướng chung của cả bảng. Các ý kia chỉ là số của một ô, để dành cho thân bài.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["Tổng năm 2005 là 7.4 triệu xe", "Xe Nhật vượt xe Mỹ năm 2005", "Xe Mỹ giảm mạnh nhất", "Xe Hàn không thay đổi"],
           "Ba ý kia là thay đổi nổi bật. Con số tổng 7.4 triệu bài mẫu không nêu, chỉ nói *a slight decrease*.", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, slightly fewer new cars were sold in 2005, with American cars falling sharply while Japanese cars became the best-sellers.",
            "Overall, 4.2 million American cars were sold in 2000, but only 2.6 million in 2005.",
            "Overall, Americans preferred Japanese cars because they were cheaper and more reliable.",
            "Overall, USA had 4.2 million, Japan 2.2 million, Germany 0.2 million and South Korea 1.1 million."],
           "Overview tốt nêu xu hướng chung và thay đổi lớn nhất, không số liệu. Các câu kia: có số, đưa lý do ngoài bảng, hoặc liệt kê một hàng.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu chia thân bài theo năm. Mỗi nhóm số liệu nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Overview"],
     "items": [
        {"label": "Xếp hạng 4 nước năm 2000 (xe Mỹ đứng đầu)", "answer": 0,
         "why": "Thân bài 1 mô tả **năm 2000**: Mỹ 4.2 triệu, Nhật 2.2 triệu, Hàn và Đức ít hơn."},
        {"label": "Xe Mỹ giảm, xe Nhật tăng và vượt lên năm 2005", "answer": 1,
         "why": "Thân bài 2 mô tả **thay đổi đến 2005**, kèm số (2.6 triệu, 3.4 triệu)."},
        {"label": "Tổng số xe bán ra giảm nhẹ", "answer": 2,
         "why": "Đây là xu hướng chung của cả bảng -> **Overview**, nói không cần số."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("Tỉ lệ", "Năm 2000, xe Mỹ là 4.2 trên tổng 7.7 triệu. American cars accounted for ___ of all sales.",
           ["more than half", "almost a quarter", "about a third", "nearly three quarters"],
           "4.2 : 7.7 ≈ 55% -> **more than half**. *a quarter* = 25%, *a third* ≈ 33%, *three quarters* = 75%."),
        mc("So sánh", "Năm 2000: Mỹ 4.2 triệu, Nhật 2.2 triệu. Almost ___ American cars were sold as Japanese cars.",
           ["twice as many", "twice more", "double than", "two times as much"],
           "*cars* đếm được -> **twice as many … as**. *twice more* là dịch từ \"gấp đôi hơn\"; *much* chỉ dùng cho danh từ không đếm được."),
        mc("Chủ ngữ", "Câu nào đúng?",
           ["The figure for Japanese cars rose to 3.4 million in 2005.",
            "Japan was 3.4 million in 2005.",
            "Japanese cars was rose to 3.4 million in 2005.",
            "The number of Japanese cars were 3.4 million in 2005."],
           "Chủ ngữ phải là số liệu: **the figure for…** / *the number of… was*. Một nước không thể \"là 3.4 triệu\"; *was rose* sai cấu trúc; *the number of* đi với động từ số ít.", long=True),
        mc("Từ nối", "American car sales fell, ___ Japanese car sales rose.",
           ["whereas", "because", "so", "during"],
           "**whereas** (= *while*) nối hai xu hướng trái ngược. *because / so* chỉ nguyên nhân, kết quả; *during* là giới từ, không nối hai mệnh đề."),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: xe Mỹ vẫn nhiều hơn", "Sai: hai nước bằng nhau", "Sai: xe Nhật chỉ có 2.2 triệu"],
           "Năm 2005: Japan 3.4 triệu > USA 2.6 triệu. Câu đúng. 2.2 triệu là số của Japan năm 2000 (nhầm năm).",
           ctx="By 2005, Japanese cars had overtaken American cars in the USA."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: chỉ tăng từ 0.2 lên 0.3 triệu", "Đúng", "Sai: giảm từ 0.3 xuống 0.2 triệu", "Sai: giữ nguyên 1.1 triệu"],
           "Germany 0.2 -> 0.3 triệu: tăng thêm một nửa, không phải gấp đôi (gấp đôi phải là 0.4). 1.1 triệu là số của South Korea (nhầm cột).",
           ctx="Sales of German cars doubled between 2000 and 2005."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: tổng giảm nhẹ (7.7 -> 7.4 triệu)", "Đúng", "Sai: tổng giữ nguyên", "Sai: tổng giảm mạnh"],
           "Cột Total: 7.7 -> 7.4 triệu, giảm 0.3 triệu -> **giảm nhẹ** (*a slight decrease*), không phải tăng.",
           ctx="The total number of new cars sold rose slightly from 2000 to 2005."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 2. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Changes by 2005",
     "text": "The number of American cars dropped considerably, [1] 2.6 million, and there was a significant rise in the number of Japanese cars sold, to 3.4 million. Sales of South Korean cars stayed [2], at 1.1 million, and there was [3] in German cars, to 0.3 million in 2005.",
     "options": ["to", "unchanged", "a small increase", "by", "a small increasing"],
     "items": [
        {"answer": 0, "why": "**drop to** + số mới (còn 2.6 triệu). *by 2.6 million* nghĩa là giảm mất 2.6 triệu, sai vì thực tế giảm 1.6 triệu."},
        {"answer": 1, "why": "**stay unchanged**: Hàn Quốc 1.1 triệu ở cả hai năm."},
        {"answer": 2, "why": "Sau *there was a…* cần danh từ: **a small increase**. *increasing* là V-ing, không đi sau *a small*."},
     ]},
]

L = {
    "id": "T08",
    "pageTitle": "Task 1 Table T08 · New cars sold in the USA",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T08",
    "heading": "Country of origin of new cars sold in the USA in 2000 and 2005",
    "topic": "New cars sold in the USA",
    "kind": "Bảng thay đổi · 2000–2005",
    "book": "Lessons for IELTS – Writing",
    "source": "Bài mẫu lấy từ sách: Lessons for IELTS – Writing, New Oriental Education & Technology Group IELTS Research Institute (có chỉnh sửa nhỏ).",
    "prompt": [
        "The table below shows the country of origin of new cars sold in the USA in 2000 and 2005.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Country of Origin of New Cars Sold in the USA in 2000 and 2005 (million cars)",
         "head": [["Year", "USA", "Japan", "Germany", "South Korea", "Total"]],
         "rows": [
            ["2000", "4.2", "2.2", "0.2", "1.1", "7.7"],
            ["2005", "2.6", "3.4", "0.3", "1.1", "7.4"],
         ]},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T08.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T08.json –", words, "từ")
