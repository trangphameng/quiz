"""T03 – Consumer spending in five countries, 2002 (IELTS Liz). Chạy: python3 gen/T03.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {illustrates|illustrate} {the proportion of|proportion} {consumer expenditure|expenditure} in Ireland, Italy, Spain, Sweden and Turkey on three types of consumer goods in 2002."},
    {"label": "Overview", "text": "Overall, the category of consumer goods that all countries spent most on was food, drinks and tobacco, which accounted for a {far higher|far} proportion than the other types of goods. The lowest spending could be seen in the category of leisure and education in all five countries. The {outlay|outlay} of Turkey was generally higher than that of the other four countries."},
    {"label": "Thân bài 1", "text": "{In terms of|interms} food, drinks and tobacco, Turkey spent the most at 32.14%. The expenditure of Ireland was also high (28.91%) {compared to|compared} Sweden, which spent the least (15.77%). Spain and Italy spent 18.80% and 16.36% {respectively|resp}. {On the other hand|otherhand}, the lowest expenditure was on leisure and education, which {accounted for|account} under 5% in all countries. Turkey spent most on these items at just 4.35% of its national expenditure, which was {around double|double} that of Spain (1.98%)."},
    {"label": "Thân bài 2", "text": "Clothing and footwear was the second category of consumer goods, and outlays for those items were {between|between} 9% in Italy and 5.40% in Sweden. The national spending in this area for the remaining countries {averaged around|averaged} 6.5%."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "illustrate", "word": "illustrate", "ipa": "/ˈɪləstreɪt/", "pos": "v", "vi": "minh hoạ, thể hiện"},
    {"key": "proportion", "word": "the proportion of", "ipa": "/ðə prəˈpɔːʃn əv/", "pos": "n phrase", "vi": "tỉ lệ (phần trăm) của"},
    {"key": "expenditure", "word": "consumer expenditure", "ipa": "/kənˈsjuːmə(r) ɪkˈspendɪtʃə(r)/", "pos": "n", "vi": "chi tiêu của người tiêu dùng"},
    {"key": "far", "word": "a far higher proportion", "ipa": "/ə fɑː ˈhaɪə(r)/", "pos": "phrase", "vi": "tỉ lệ cao hơn nhiều"},
    {"key": "outlay", "word": "outlay", "ipa": "/ˈaʊtleɪ/", "pos": "n", "vi": "khoản chi, mức chi"},
    {"key": "interms", "word": "in terms of", "ipa": "/ɪn tɜːmz əv/", "pos": "prep", "vi": "về mặt, xét về"},
    {"key": "compared", "word": "compared to", "ipa": "/kəmˈpeəd tə/", "pos": "prep", "vi": "so với"},
    {"key": "resp", "word": "respectively", "ipa": "/rɪˈspektɪvli/", "pos": "adv", "vi": "lần lượt là (đúng thứ tự đã nêu)"},
    {"key": "otherhand", "word": "on the other hand", "ipa": "/ɒn ði ˈʌðə hænd/", "pos": "phrase", "vi": "mặt khác, ngược lại"},
    {"key": "account", "word": "account for", "ipa": "/əˈkaʊnt fə(r)/", "pos": "v", "vi": "chiếm (bao nhiêu %)"},
    {"key": "double", "word": "around double that of", "ipa": "/əˈraʊnd ˈdʌbl ðæt əv/", "pos": "phrase", "vi": "khoảng gấp đôi mức của"},
    {"key": "between", "word": "between … and …", "ipa": "/bɪˈtwiːn/", "pos": "prep", "vi": "nằm trong khoảng từ … đến …"},
    {"key": "averaged", "word": "average around", "ipa": "/ˈævərɪdʒ əˈraʊnd/", "pos": "v", "vi": "trung bình khoảng"},
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
        mc("Đọc bảng", "Nước nào chi tỉ lệ cao nhất cho **Food/Drinks/Tobacco**?",
           ["Turkey", "Ireland", "Spain", "Italy"],
           "Turkey 32.14%, cao hơn Ireland (28.91%). Hai nước này đều cao, nên phải so từng chữ số."),
        mc("Đọc bảng", "Nước nào chi tỉ lệ cao nhất cho **Clothing/Footwear**?",
           ["Italy", "Turkey", "Spain", "Ireland"],
           "Italy 9.00%, các nước khác chỉ 5.40–6.63%. Turkey cao nhất ở hai cột còn lại, nhưng không phải ở cột này."),
        mc("Thì", "Bảng chỉ có một mốc là năm 2002. Bài viết nên dùng thì gì và động từ nào?",
           ["Quá khứ đơn: spent, accounted for", "Quá khứ đơn: increased, rose", "Hiện tại đơn: spends, accounts for", "Hiện tại hoàn thành: has spent"],
           "Năm 2002 đã qua nên dùng **quá khứ đơn**. Bảng tĩnh (1 mốc) không có thay đổi, nên không dùng *increased/rose*.", long=True),
        mc("Đơn vị", "Số **32.14%** ở hàng Turkey nghĩa là gì?",
           ["32.14% chi tiêu của người dân Turkey dành cho đồ ăn, uống, thuốc lá", "32.14% dân số Turkey hút thuốc", "Turkey chi 32.14 tỉ đô cho đồ ăn", "Chi tiêu cho đồ ăn ở Turkey tăng 32.14%"],
           "Đây là **tỉ lệ** trong tổng chi tiêu, không phải số tiền, không phải % dân số, cũng không phải mức tăng. Viết *32.14% of consumer spending*.", long=True),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Bảng có 15 con số, không thể nêu hết.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Cả 5 nước chi nhiều nhất cho đồ ăn/uống/thuốc lá, ít nhất cho giải trí/giáo dục", "Spain chi 6.51% cho quần áo", "Sweden chi 3.22% cho giải trí/giáo dục", "Italy chi 16.36% cho đồ ăn"],
           "Overview nêu quy luật chung của cả bảng. Các ý kia là số lẻ của một nước, để ở thân bài.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["Ireland chi 2.21% cho giải trí/giáo dục", "Turkey cao nhất về đồ ăn (32.14%)", "Italy cao nhất về quần áo (9.00%)", "Sweden thấp nhất về đồ ăn (15.77%)"],
           "Ba ý kia là cao nhất hoặc thấp nhất trong một cột. 2.21% của Ireland không nổi bật (không cao nhất, không thấp nhất).", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, food, drinks and tobacco took the largest share of spending in all five countries, while leisure and education took the smallest.",
            "Overall, Turkey spent 32.14% on food, drinks and tobacco.",
            "Overall, people in Turkey eat a lot, so they spend more on food.",
            "Overall, Ireland spent 28.91%, Italy 16.36%, Spain 18.80% and Sweden 15.77% on food."],
           "Overview tốt nêu quy luật chung, không có số. Các câu kia: có số liệu, đưa lý do ngoài bảng, hoặc liệt kê từng hàng.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu chia theo mục chi tiêu. Mỗi nhóm nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Overview"],
     "items": [
        {"label": "Đồ ăn/uống/thuốc lá: Turkey cao nhất, Sweden thấp nhất", "answer": 0,
         "why": "Bài mẫu viết về mục chi lớn nhất (và cả mục nhỏ nhất) ở **Thân bài 1**, so sánh nước cao nhất với nước thấp nhất."},
        {"label": "Quần áo/giày dép: từ 9% (Italy) đến 5.40% (Sweden)", "answer": 1,
         "why": "Mục quần áo được tách riêng ở **Thân bài 2**, dùng *between … and …* để nêu khoảng dao động."},
        {"label": "Mục nào cao nhất, mục nào thấp nhất ở cả 5 nước", "answer": 2,
         "why": "Đây là quy luật chung, không cần số, nên đặt ở **Overview**."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("So sánh", "Turkey 4.35%, Spain 1.98%. Cách nói nào đúng?",
           ["around double that of Spain", "twice more than Spain", "double than Spain", "two times higher as Spain"],
           "4.35 : 1.98 ≈ 2.2, nên **around double that of Spain**. *that of* thay cho *the spending of* để so đúng thứ với thứ. *twice more than* là dịch từ \"gấp đôi hơn\"."),
        mc("Chủ ngữ", "Câu nào đúng?",
           ["The figure for Sweden was 15.77%.", "Sweden was 15.77%.", "The figure of Sweden were 15.77%.", "Sweden's food is 15.77%."],
           "Chủ ngữ phải là **số liệu** (*the figure for*), không phải tên nước. *The figure* số ít nên đi với *was*. Bảng năm 2002 nên không dùng *is*.", long=True),
        mc("account for", "Câu nào đúng?",
           ["Leisure and education accounted for under 5% of spending.", "Leisure and education was accounted for under 5% of spending.", "Leisure and education accounted under 5% of spending.", "Leisure and education accounted with under 5% of spending."],
           "**account for** + % là chủ động, luôn có *for*. Không dùng bị động *was accounted for* khi muốn nói \"chiếm\".", long=True),
        mc("Bảng tĩnh", "Câu nào phù hợp với bảng chỉ có năm 2002?",
           ["Turkey spent 32.14% of its budget on food, drinks and tobacco.", "Turkey's spending on food increased to 32.14%.", "Turkey spends 32.14% on food in 2002.", "Turkey will spend 32.14% on food."],
           "Bảng 1 mốc: không có thay đổi, nên không dùng *increased*. Năm 2002 đã qua nên dùng quá khứ đơn **spent**.", long=True),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: Italy thấp nhất (16.36%)", "Sai: Spain thấp nhất (18.80%)", "Sai: Sweden cao nhất"],
           "Cột đồ ăn: Sweden 15.77% thấp hơn Italy (16.36%). Câu đúng.",
           ctx="Sweden spent the smallest proportion on food, drinks and tobacco."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: đứng thứ hai, luôn cao hơn giải trí/giáo dục", "Đúng", "Sai: đứng thứ nhất ở Italy", "Sai: bằng giải trí/giáo dục ở Sweden"],
           "Ở cả 5 nước, quần áo (5.40–9.00%) đều cao hơn giải trí/giáo dục (1.98–4.35%) và thấp hơn đồ ăn, nên là mục **thứ hai**. Italy: đồ ăn 16.36% vẫn cao hơn quần áo 9%.",
           ctx="Clothing and footwear was the third category of spending in all five countries."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: Italy cao nhất về quần áo (9.00%)", "Đúng", "Sai: Ireland cao nhất về đồ ăn", "Sai: Sweden cao nhất về giải trí (3.22%)"],
           "Turkey cao nhất ở đồ ăn (32.14%) và giải trí (4.35%), nhưng cột quần áo thì Italy cao nhất (9.00% so với 6.63%).",
           ctx="Turkey spent the highest proportion in every category."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 1. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Food, drinks and tobacco",
     "text": "In terms of food, drinks and tobacco, Turkey spent the most at 32.14%. The expenditure of Ireland was also high (28.91%) [1] Sweden, which spent the least (15.77%). Spain and Italy spent 18.80% and 16.36% [2]. [3], the lowest expenditure was on leisure and education, which accounted for under 5% in all countries.",
     "options": ["compared to", "respectively", "On the other hand", "compare with", "Because"],
     "items": [
        {"answer": 0, "why": "**compared to** + đối tượng so sánh. *compare with* thiếu *-d*, là động từ chứ không phải giới từ."},
        {"answer": 1, "why": "**respectively**: 18.80% đi với Spain, 16.36% đi với Italy, đúng thứ tự tên nước."},
        {"answer": 2, "why": "**On the other hand** chuyển sang ý đối lập (mục chi cao nhất -> mục chi thấp nhất). *Because* nêu lý do, không hợp."},
     ]},
]

L = {
    "id": "T03",
    "pageTitle": "Task 1 Table T03 · Consumer spending in five countries",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T03",
    "heading": "Consumer spending on different items in five countries (2002)",
    "topic": "Consumer spending in five countries",
    "kind": "Bảng tĩnh · 1 mốc năm (2002)",
    "book": "IELTS Liz (ieltsliz.com)",
    "source": "Đề: Cambridge IELTS (theo IELTS Liz). Bài mẫu: IELTS Liz, https://ieltsliz.com/ielts-table-band-9-model-answer/ (Model Answer 2, có chỉnh sửa nhỏ). Dùng cho mục đích học tập.",
    "prompt": [
        "The table below gives information about consumer spending on different items in five different countries in 2002.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Consumer spending on different items (2002)",
         "head": [["Country", "Food/Drinks/Tobacco", "Clothing/Footwear", "Leisure/Education"]],
         "rows": [
            ["Ireland", "28.91%", "6.43%", "2.21%"],
            ["Italy", "16.36%", "9.00%", "3.20%"],
            ["Spain", "18.80%", "6.51%", "1.98%"],
            ["Sweden", "15.77%", "5.40%", "3.22%"],
            ["Turkey", "32.14%", "6.63%", "4.35%"],
         ]},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T03.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T03.json –", words, "từ")
