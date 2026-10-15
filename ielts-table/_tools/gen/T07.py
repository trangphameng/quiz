"""T07 – International students in 2000 and 2005 (Lessons for IELTS – Writing, Model 1). Chạy: python3 gen/T07.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {illustrates|illustrate} the number of students from four different countries who attended {tertiary institutions|tertiary} in a western country in 2000 and 2005."},
    {"label": "Overview", "text": "{Overall|overall}, the number of international students {dropped slightly|slightly} over this five-year period and, {in particular|particular}, there was {a significant decrease|decrease} in student numbers from China, although China still {remained the largest group|largest}. There was {a fourfold rise|fourfold} in Brazilian student enrolments."},
    {"label": "Thân bài 1", "text": "In 2000, the number of students who came from China, at 35,000, was {more than twice|twice} the number of Indian students, at 15,000. Smaller numbers came from Japan and Brazil, at 6,000 and 2,000 {respectively|respectively}."},
    {"label": "Thân bài 2", "text": "In 2005, the proportion of students {changed considerably|considerably}. Chinese student numbers {decreased to|decreasedto} 22,000, but there was {a dramatic increase|dramatic} in the number of Brazilian students, which went from 2,000 to 8,000. Indian student numbers {stayed mostly unchanged|unchanged}, at around 16,000, and there was a small decrease in the number of Japanese students, from 6,000 in 2000 to 4,000 in 2005."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "illustrate", "word": "illustrate", "ipa": "/ˈɪləstreɪt/", "pos": "v", "vi": "minh hoạ, thể hiện"},
    {"key": "tertiary", "word": "tertiary institution", "ipa": "/ˈtɜːʃəri ˌɪnstɪˈtjuːʃn/", "pos": "n", "vi": "cơ sở giáo dục đại học, cao đẳng"},
    {"key": "overall", "word": "overall", "ipa": "/ˌəʊvərˈɔːl/", "pos": "adv", "vi": "nhìn chung"},
    {"key": "slightly", "word": "drop slightly", "ipa": "/drɒp ˈslaɪtli/", "pos": "phrase", "vi": "giảm nhẹ"},
    {"key": "particular", "word": "in particular", "ipa": "/ɪn pəˈtɪkjələ(r)/", "pos": "phrase", "vi": "đặc biệt là"},
    {"key": "decrease", "word": "a significant decrease", "ipa": "/ə sɪɡˈnɪfɪkənt ˈdiːkriːs/", "pos": "n phrase", "vi": "sự giảm đáng kể"},
    {"key": "largest", "word": "remain the largest group", "ipa": "/rɪˈmeɪn ðə ˈlɑːdʒɪst ɡruːp/", "pos": "phrase", "vi": "vẫn là nhóm đông nhất"},
    {"key": "fourfold", "word": "a fourfold rise", "ipa": "/ə ˈfɔːfəʊld raɪz/", "pos": "n phrase", "vi": "sự tăng gấp bốn lần"},
    {"key": "twice", "word": "more than twice", "ipa": "/mɔː ðən twaɪs/", "pos": "phrase", "vi": "hơn gấp đôi"},
    {"key": "respectively", "word": "respectively", "ipa": "/rɪˈspektɪvli/", "pos": "adv", "vi": "lần lượt (theo thứ tự đã nêu)"},
    {"key": "considerably", "word": "change considerably", "ipa": "/tʃeɪndʒ kənˈsɪdərəbli/", "pos": "phrase", "vi": "thay đổi đáng kể"},
    {"key": "decreasedto", "word": "decrease to", "ipa": "/dɪˈkriːs tə/", "pos": "phrase", "vi": "giảm xuống còn (+ số mới)"},
    {"key": "dramatic", "word": "a dramatic increase", "ipa": "/ə drəˈmætɪk ˈɪŋkriːs/", "pos": "n phrase", "vi": "sự tăng vọt"},
    {"key": "unchanged", "word": "stay unchanged", "ipa": "/steɪ ʌnˈtʃeɪndʒd/", "pos": "phrase", "vi": "giữ nguyên, không đổi"},
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
        mc("Đọc bảng", "Nước nào có nhiều sinh viên nhất ở **cả hai** năm?",
           ["China", "India", "Brazil", "Japan"],
           "China cao nhất cả năm 2000 (35,000) lẫn 2005 (22,000), dù giảm mạnh. India chỉ 15,000 và 16,000."),
        mc("So sánh", "Sinh viên Brazil năm 2005 so với năm 2000 thế nào?",
           ["Gấp 4 lần", "Gấp đôi", "Gấp 3 lần", "Tăng 4,000"],
           "2,000 -> 8,000: 8,000 = 4 x 2,000, nên **gấp 4 lần** (*a fourfold rise*). Thực tế tăng thêm 6,000, không phải 4,000."),
        mc("Thì", "Bảng có mấy mốc thời gian, và bài nên dùng thì nào?",
           ["2 mốc, quá khứ đơn", "2 mốc, hiện tại đơn", "1 mốc, quá khứ đơn", "2 mốc, tương lai đơn"],
           "Có 2 năm 2000 và 2005 (đều đã qua) -> bảng thay đổi, dùng **quá khứ đơn**: *dropped, decreased, went from… to…*."),
        mc("Đơn vị", "Số **35,000** ở hàng 2000, cột China nghĩa là gì?",
           ["35,000 sinh viên đến từ Trung Quốc", "35% sinh viên đến từ Trung Quốc", "35,000 sinh viên Trung Quốc tăng thêm", "35,000 sinh viên ở các nước khác"],
           "Bảng ghi **số người** (số tuyệt đối), không phải %. Đây là số sinh viên Trung Quốc năm 2000, không phải mức tăng.", long=True),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Không cần nêu hết mọi ô.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Tổng số giảm nhẹ; China giảm mạnh nhưng vẫn đông nhất", "India có 15,000 sinh viên năm 2000", "Japan có 4,000 sinh viên năm 2005", "Brazil có 2,000 sinh viên năm 2000"],
           "Overview nêu xu hướng chung và điểm nổi bật nhất. Các ý kia chỉ là số của một ô, để dành cho thân bài.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["Tổng năm 2005 là 50,000 người", "China vẫn là nhóm đông nhất", "Brazil tăng gấp 4 lần", "China giảm mạnh nhất"],
           "Ba ý kia là đặc điểm nổi bật (đông nhất, tăng mạnh nhất, giảm mạnh nhất). Con số tổng 50,000 bài mẫu không cần nêu, chỉ nói *dropped slightly*.", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, the total number of international students fell slightly, and although Chinese students decreased sharply, they remained the largest group.",
            "Overall, there were 35,000 Chinese students in 2000 and 22,000 in 2005.",
            "Overall, Chinese students probably chose other countries because fees became more expensive.",
            "Overall, China had 35,000, India had 15,000, Japan had 6,000 and Brazil had 2,000 students."],
           "Overview tốt nêu xu hướng chung, không số liệu. Các câu kia: có số liệu, đưa lý do ngoài bảng, hoặc liệt kê từng cột.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu chia thân bài theo năm. Mỗi nhóm số liệu nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Overview"],
     "items": [
        {"label": "Xếp hạng 4 nước năm 2000 (China gấp hơn đôi India)", "answer": 0,
         "why": "Thân bài 1 mô tả **năm đầu** 2000: China 35,000, India 15,000, Japan và Brazil ít hơn."},
        {"label": "China giảm, Brazil tăng mạnh, Japan giảm nhẹ đến 2005", "answer": 1,
         "why": "Thân bài 2 mô tả **thay đổi đến 2005**, kèm số cụ thể (22,000; 2,000 -> 8,000)."},
        {"label": "Tổng số sinh viên giảm nhẹ trong 5 năm", "answer": 2,
         "why": "Đây là xu hướng chung của cả bảng -> **Overview**, nói không cần số."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("Thay đổi", "Brazil: 2,000 -> 8,000. There was ___ in Brazilian student enrolments.",
           ["a fourfold rise", "a rise four times more", "a four times higher rise", "a rise of four"],
           "Tăng gấp 4 lần -> **a fourfold rise** (hoặc *rose fourfold*). *four times more / higher* là lỗi dịch từ \"tăng gấp 4 lần hơn\"; *a rise of four* nghĩa là chỉ tăng thêm 4 người."),
        mc("So sánh", "China 35,000, India 15,000. China's figure was ___ India's.",
           ["more than twice", "more than twice than", "twice more than", "more two times than"],
           "Gấp đôi: **twice + (as… as / the number of)**, không có *than* sau *twice*. *twice more than* là dịch từ \"gấp đôi hơn\"."),
        mc("Chủ ngữ", "Câu nào đúng?",
           ["The number of Chinese students was 35,000 in 2000.",
            "The number of Chinese students were 35,000 in 2000.",
            "China was 35,000 students in 2000.",
            "A number of Chinese students was 35,000 in 2000."],
           "**The number of** + động từ số ít (*was*). Một nước không thể \"là 35,000 sinh viên\". *A number of* nghĩa là \"nhiều\", không dùng để nêu số liệu.", long=True),
        mc("Mở bài", "Chọn câu mở bài tốt nhất.",
           ["The table illustrates how many students from four countries attended tertiary institutions in a western country in 2000 and 2005.",
            "The table below gives information about the country of origin of international students at tertiary institutions in a western country in 2000 and 2005.",
            "The graph illustrates how many students from four countries attended tertiary institutions in a western country in 2000 and 2005.",
            "The table illustrates how many students from four countries attend tertiary institutions in a western country in 2000 and 2005."],
           "Mở bài tốt viết lại đề bằng lời mình. Các câu kia: chép nguyên đề, gọi table là *graph*, hoặc dùng *attend* (hiện tại) cho năm đã qua.", long=True),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: India đông nhất năm 2005", "Sai: Brazil đông nhất năm 2005", "Sai: China chỉ có 16,000"],
           "Năm 2005: China 22,000 > India 16,000 > Brazil 8,000 > Japan 4,000. Câu đúng. 16,000 là số của India (nhầm cột).",
           ctx="Chinese students were still the largest group in 2005."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: gấp 4 lần (16,000 so với 4,000)", "Đúng", "Sai: Japan nhiều hơn India", "Sai: India chỉ có 15,000"],
           "Năm 2005: India 16,000 = 4 x Japan 4,000 -> *four times as many as*. 15,000 là số của India năm 2000 (nhầm năm).",
           ctx="In 2005, there were twice as many Indian students as Japanese students."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: năm 2005 Japan thấp nhất (4,000)", "Đúng", "Sai: năm 2000 India thấp nhất", "Sai: Brazil có 6,000 năm 2000"],
           "Brazil thấp nhất năm 2000 (2,000) nhưng năm 2005 đã lên 8,000, vượt Japan (4,000). 6,000 là số của Japan (nhầm cột).",
           ctx="Brazil had the smallest number of students in both years."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 2. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Changes by 2005",
     "text": "Chinese student numbers [1] 22,000, [2] there was a dramatic increase in the number of Brazilian students, which went from 2,000 to 8,000. Indian student numbers stayed mostly [3], at around 16,000.",
     "options": ["decreased to", "but", "unchanged", "decreased by", "because"],
     "items": [
        {"answer": 0, "why": "**decrease to** + số mới (còn 22,000). *decreased by 22,000* nghĩa là giảm mất 22,000, sai vì thực tế giảm 13,000."},
        {"answer": 1, "why": "**but** nối hai xu hướng trái chiều: China giảm, Brazil tăng. *because* là nguyên nhân, không hợp nghĩa."},
        {"answer": 2, "why": "**stay unchanged** = gần như không đổi (15,000 -> 16,000)."},
     ]},
]

L = {
    "id": "T07",
    "pageTitle": "Task 1 Table T07 · International students",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T07",
    "heading": "Country of origin of international students in 2000 and 2005",
    "topic": "International students",
    "kind": "Bảng thay đổi · 2000–2005",
    "book": "Lessons for IELTS – Writing",
    "source": "Bài mẫu lấy từ sách: Lessons for IELTS – Writing, New Oriental Education & Technology Group IELTS Research Institute (có chỉnh sửa nhỏ).",
    "prompt": [
        "The table below gives information about the country of origin of international students at tertiary institutions in a western country in 2000 and 2005.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Country of Origin of International Students in 2000 and 2005",
         "head": [["Year", "China", "India", "Japan", "Brazil", "Total"]],
         "rows": [
            ["2000", "35,000", "15,000", "6,000", "2,000", "58,000"],
            ["2005", "22,000", "16,000", "4,000", "8,000", "50,000"],
         ]},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T07.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T07.json –", words, "từ")
