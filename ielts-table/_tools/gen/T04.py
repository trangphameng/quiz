"""T04 – UK income spent on four items by adults and children, 1998 (IELTS Liz). Chạy: python3 gen/T04.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {illustrates|illustrate} the percentage of income that was spent on food, electronic equipment, music and videos by both adults and children, {divided by gender|divided}, in the UK in 1998."},
    {"label": "Overview", "text": "Overall, adults spent less of their whole income on the four items {compared to|compared} children. Adult spending was {mainly|mainly} on food, with women spending {nearly three times as much as|three} men on that item, and little was spent on other items. For children, {a large proportion of|proportion} their money was spent on music, and spending on other items was also {significant|significant}, with the least spent on food."},
    {"label": "Thân bài 1", "text": "For adults, 25% of their money {went on|wenton} food, with women using {up to|upto} 39% of their income on it, compared to only 14% for men. Expenditure on electronic equipment {accounted for|account} 10% of men's income but only 1% for women. {No more than|nomore} 5% was spent on all other items by both genders."},
    {"label": "Thân bài 2", "text": "{In terms of|interms} children, expenditure on music was 39%, with girls spending 40% (two {percentage points|points} more than boys). Spending on electronic equipment was 23% overall, {although|although} girls only used 5% of their money on this. For videos, both genders used around 18% of their income. However, food accounted for only about 10% of spending in total and by each gender."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "illustrate", "word": "illustrate", "ipa": "/ˈɪləstreɪt/", "pos": "v", "vi": "minh hoạ, thể hiện"},
    {"key": "divided", "word": "divided by gender", "ipa": "/dɪˈvaɪdɪd baɪ ˈdʒendə(r)/", "pos": "phrase", "vi": "chia theo giới tính"},
    {"key": "compared", "word": "compared to", "ipa": "/kəmˈpeəd tə/", "pos": "prep", "vi": "so với"},
    {"key": "mainly", "word": "mainly", "ipa": "/ˈmeɪnli/", "pos": "adv", "vi": "chủ yếu"},
    {"key": "three", "word": "nearly three times as much as", "ipa": "/ˈnɪəli θriː taɪmz əz mʌtʃ əz/", "pos": "phrase", "vi": "gần gấp ba lần"},
    {"key": "proportion", "word": "a large proportion of", "ipa": "/ə lɑːdʒ prəˈpɔːʃn əv/", "pos": "n phrase", "vi": "một phần lớn của"},
    {"key": "significant", "word": "significant", "ipa": "/sɪɡˈnɪfɪkənt/", "pos": "adj", "vi": "đáng kể"},
    {"key": "wenton", "word": "(money) go on", "ipa": "/ɡəʊ ɒn/", "pos": "phrasal v", "vi": "(tiền) được tiêu vào"},
    {"key": "upto", "word": "up to", "ipa": "/ʌp tuː/", "pos": "prep", "vi": "lên tới"},
    {"key": "account", "word": "account for", "ipa": "/əˈkaʊnt fə(r)/", "pos": "v", "vi": "chiếm (bao nhiêu %)"},
    {"key": "nomore", "word": "no more than", "ipa": "/nəʊ mɔː ðən/", "pos": "phrase", "vi": "không quá"},
    {"key": "interms", "word": "in terms of", "ipa": "/ɪn tɜːmz əv/", "pos": "prep", "vi": "về mặt, xét về"},
    {"key": "points", "word": "percentage point", "ipa": "/pəˈsentɪdʒ pɔɪnt/", "pos": "n", "vi": "điểm phần trăm (40% − 38% = 2 điểm %)"},
    {"key": "although", "word": "although", "ipa": "/ɔːlˈðəʊ/", "pos": "conj", "vi": "mặc dù"},
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
        mc("Đọc bảng", "Nhóm nào dành tỉ lệ thu nhập cao nhất cho **food**?",
           ["women", "adults", "girls", "men"],
           "Cột food: women 39% là cao nhất. Girls có 40% nhưng đó là cột **music** (nhầm cột); food của girls chỉ 11%."),
        mc("Đọc bảng", "Trẻ em (children) chi nhiều nhất cho mục nào?",
           ["music", "electronic equipment", "videos", "food"],
           "Hàng children: music 39%, cao hơn electronic equipment (23%), videos (12%), food (10%)."),
        mc("Thì", "Bảng chỉ có năm 1998. Bài viết nên dùng thì nào?",
           ["Quá khứ đơn (spent, accounted for)", "Hiện tại đơn (spend, account for)", "Hiện tại hoàn thành (have spent)", "Tương lai (will spend)"],
           "Năm 1998 đã qua nên dùng **quá khứ đơn**. Bảng chỉ có 1 mốc, nên không viết *increased/decreased*.", long=True),
        mc("Đơn vị", "Số **39%** ở hàng women, cột food nghĩa là gì?",
           ["Phụ nữ dành 39% thu nhập cho thực phẩm", "39% phụ nữ có mua thực phẩm", "Phụ nữ chiếm 39% tổng chi thực phẩm ở UK", "Chi tiêu thực phẩm của phụ nữ tăng 39%"],
           "Tiêu đề bảng: *proportion of income … spent on*. Đây là phần trăm **thu nhập** của nhóm đó, không phải % số người hay mức tăng.", long=True),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Bảng có 24 con số, không thể nêu hết.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Người lớn chi chủ yếu cho thực phẩm, trẻ em chi nhiều nhất cho âm nhạc", "Men chi 5% cho âm nhạc", "Boys chi 9% cho thực phẩm", "Adults chi 1% cho videos"],
           "Overview so sánh hai nhóm lớn (người lớn và trẻ em) theo mục chi nổi bật nhất. Các ý kia là số lẻ, để ở thân bài.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["Men chi 2% cho videos", "Women chi 39% cho thực phẩm", "Girls chi 40% cho âm nhạc", "Children chi ít nhất cho thực phẩm (10%)"],
           "Ba ý kia là cao nhất hoặc thấp nhất. 2% cho videos của men không nổi bật, có thể gộp vào câu \"các mục khác dưới 5%\".", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, adults spent most of their income on food, whereas children spent the largest share on music.",
            "Overall, women spent 39% on food and men spent 14%.",
            "Overall, children spend too much money on music, which is a waste.",
            "Overall, boys spent 9% on food, 18% on electronics, 38% on music and 18% on videos."],
           "Overview tốt nêu xu hướng chính của hai nhóm, không có số. Các câu kia: có số liệu, nêu ý kiến cá nhân, hoặc liệt kê một hàng.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu chia theo người lớn và trẻ em. Mỗi nhóm nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Overview"],
     "items": [
        {"label": "Men và women: thực phẩm, thiết bị điện tử", "answer": 0,
         "why": "Số liệu của **người lớn** (men, women) vào Thân bài 1, so sánh nam và nữ."},
        {"label": "Boys và girls: âm nhạc, thiết bị điện tử, videos", "answer": 1,
         "why": "Số liệu của **trẻ em** (boys, girls) vào Thân bài 2. Chia theo nhóm người giúp so sánh giới tính trong cùng đoạn."},
        {"label": "Trẻ em dành phần thu nhập cho 4 mục lớn hơn người lớn", "answer": 2,
         "why": "Đây là so sánh chung giữa hai nhóm, không cần số, nên đặt ở **Overview**."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("So sánh", "Women 39%, men 14% cho thực phẩm. Cách nói nào đúng?",
           ["nearly three times as much as men", "three times higher as men", "triple than men", "three times much as men"],
           "39 : 14 ≈ 2.8, nên **nearly three times as much as**. Cấu trúc: *số lần + as much/many + as*. Nói \"gấp đôi\" là chưa đúng số liệu."),
        mc("Phần trăm", "Girls 40%, boys 38% cho âm nhạc. Cách nói nào chính xác?",
           ["two percentage points more than boys", "two percents more than boys", "two percentage more than boys", "more two percent than boys"],
           "Hiệu giữa hai tỉ lệ (40% − 38%) gọi là **percentage points**. *percent* không thêm *s*; *percentage* cần danh từ đi sau."),
        mc("Chủ ngữ", "Câu nào đúng?",
           ["The proportion of income spent on videos by women was 0.5%.", "The proportion of income spent on videos by women were 0.5%.", "Women was 0.5% on videos.", "Videos of women is 0.5%."],
           "Chủ ngữ là **the proportion** (số ít) nên đi với *was*. *women* chỉ nằm trong cụm bổ nghĩa, không quyết định động từ.", long=True),
        mc("Mở bài", "Chọn câu mở bài tốt nhất.",
           ["The table compares the percentage of their income that adults and children in the UK spent on four common items in 1998.",
            "The proportion of income adults and children spent on 4 common items in the UK in 1998.",
            "The chart shows the proportion of income adults and children spent on four items in the UK in 1998.",
            "The table shows how much income adults and children spend on four items in the UK in 1998."],
           "Mở bài tốt viết lại đề bằng lời mình (*compares the percentage of their income*), đúng thì. Các câu kia: chép nguyên tiêu đề, gọi bảng là *chart*, hoặc sai thì (*spend*).", long=True),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: boys chi nhiều hơn (38% so với 40%)", "Sai: hai nhóm bằng nhau", "Sai: girls chi 17% cho âm nhạc"],
           "Cột music: girls 40% > boys 38%. Câu đúng. 17% là videos của girls (nhầm cột).",
           ctx="Girls spent a larger proportion of their income on music than boys."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: gấp 10 lần (10% so với 1%)", "Đúng", "Sai: women chi nhiều hơn", "Sai: hai nhóm bằng nhau (5%)"],
           "Electronic equipment: men 10%, women 1%, tức gấp 10 lần chứ không phải gấp đôi. 5% là số của adults (nhầm hàng).",
           ctx="Men spent twice as much of their income on electronic equipment as women."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: thực phẩm mới thấp nhất (10%)", "Đúng", "Sai: âm nhạc thấp nhất", "Sai: thiết bị điện tử thấp nhất (5%)"],
           "Hàng children: food 10% < videos 12%. 5% cho thiết bị điện tử là số của girls (nhầm hàng).",
           ctx="Children spent the least on videos."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 1. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Adults",
     "text": "For adults, 25% of their money [1] food, with women using up to 39% of their income on it, [2] only 14% for men. Expenditure on electronic equipment [3] 10% of men's income but only 1% for women.",
     "options": ["went on", "compared to", "accounted for", "was accounted for", "spent for"],
     "items": [
        {"answer": 0, "why": "**money went on** + thứ được mua = tiền được tiêu vào. *spent for* sai giới từ (spend money **on**)."},
        {"answer": 1, "why": "**compared to** + số liệu so sánh, đứng sau dấu phẩy."},
        {"answer": 2, "why": "**accounted for** + % = chiếm, chủ động. Không dùng bị động *was accounted for*."},
     ]},
]

L = {
    "id": "T04",
    "pageTitle": "Task 1 Table T04 · Income spent by adults and children",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T04",
    "heading": "Proportion of income spent on four items in the UK (1998)",
    "topic": "Income spent by adults and children",
    "kind": "Bảng tĩnh · 1 mốc năm (1998)",
    "book": "IELTS Liz (ieltsliz.com)",
    "source": "Đề và bài mẫu: IELTS Liz, https://ieltsliz.com/ielts-table-spending-on-items/ (có chỉnh sửa nhỏ). Dùng cho mục đích học tập.",
    "prompt": [
        "The table below shows the proportion of income adults and children spent on 4 common items in the UK in 1998.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "The proportion of income adults and children spent on 4 common items in the UK in 1998",
         "head": [["", "food", "electronic equipment", "music", "videos"]],
         "rows": [
            ["adults", "25%", "5%", "5%", "1%"],
            ["men", "14%", "10%", "5%", "2%"],
            ["women", "39%", "1%", "5%", "0.5%"],
            ["children", "10%", "23%", "39%", "12%"],
            ["boys", "9%", "18%", "38%", "18%"],
            ["girls", "11%", "5%", "40%", "17%"],
         ]},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T04.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T04.json –", words, "từ")
