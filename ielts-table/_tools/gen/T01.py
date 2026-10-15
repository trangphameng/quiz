"""T01 – Fairtrade coffee and bananas (Cambridge IELTS 10, Test 2). Chạy: python3 gen/T01.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The tables show how Fairtrade coffee and banana sales changed in five countries in 2004 {compared to|compared} 1999."},
    {"label": "Overview", "text": "Overall, coffee sales rose in all five countries, most {dramatically|dramatically} in the UK. Banana sales also rose in {all but two|allbut} countries, and were highest in the UK in both years."},
    {"label": "Thân bài 1", "text": "In 1999, the highest coffee sales, 3 million euros (3m), were reported in Switzerland, and this figure {doubled|double} in 2004. {The figure for|figure} the UK was originally 50% lower than that for Switzerland (1.5m), while sales in Denmark were slightly higher (1.8m). However, while {the former|former} rose dramatically to 20m, {the latter|latter} {remained relatively stable|stable}. There was {little difference|little} between the figures for Belgium (1m) and Sweden (0.8m), and both experienced noticeable increases, to 1.7m and 1m, {respectively|resp}."},
    {"label": "Thân bài 2", "text": "The UK had the highest banana sales in both years, with sales rising over {threefold|threefold} from 15 million euros to 47m. Swiss sales were originally almost {twice as high as|twice} those of Denmark (1m and 0.6m, respectively), and both {surged|surge}, reaching 5.5m and 4m. There was little difference between the figures for Sweden and Belgium (2m and 1.8m, respectively), and both roughly {halved|halve}, to around 1m in 2004."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "compared", "word": "compared to", "ipa": "/kəmˈpeəd tə/", "pos": "prep", "vi": "so với"},
    {"key": "dramatically", "word": "dramatically", "ipa": "/drəˈmætɪkli/", "pos": "adv", "vi": "(tăng/giảm) mạnh, đột biến"},
    {"key": "allbut", "word": "all but two", "ipa": "/ɔːl bʌt tuː/", "pos": "phrase", "vi": "tất cả, trừ hai (nước)"},
    {"key": "double", "word": "double", "ipa": "/ˈdʌbl/", "pos": "v", "vi": "tăng gấp đôi"},
    {"key": "figure", "word": "the figure for", "ipa": "/ðə ˈfɪɡə fə/", "pos": "n phrase", "vi": "số liệu của (một nước, một nhóm)"},
    {"key": "former", "word": "the former", "ipa": "/ðə ˈfɔːmə(r)/", "pos": "pron", "vi": "cái được nhắc trước (trong hai cái)"},
    {"key": "latter", "word": "the latter", "ipa": "/ðə ˈlætə(r)/", "pos": "pron", "vi": "cái được nhắc sau (trong hai cái)"},
    {"key": "stable", "word": "remain relatively stable", "ipa": "/rɪˈmeɪn ˈrelətɪvli ˈsteɪbl/", "pos": "v phrase", "vi": "giữ tương đối ổn định"},
    {"key": "little", "word": "little difference between", "ipa": "/ˈlɪtl ˈdɪfrəns bɪˈtwiːn/", "pos": "n phrase", "vi": "chênh lệch rất ít giữa"},
    {"key": "resp", "word": "respectively", "ipa": "/rɪˈspektɪvli/", "pos": "adv", "vi": "lần lượt là (đúng thứ tự đã nêu)"},
    {"key": "threefold", "word": "threefold", "ipa": "/ˈθriːfəʊld/", "pos": "adv", "vi": "gấp ba lần"},
    {"key": "twice", "word": "twice as high as", "ipa": "/twaɪs əz haɪ əz/", "pos": "phrase", "vi": "cao gấp đôi"},
    {"key": "surge", "word": "surge", "ipa": "/sɜːdʒ/", "pos": "v", "vi": "tăng vọt"},
    {"key": "halve", "word": "halve", "ipa": "/hɑːv/", "pos": "v", "vi": "giảm (còn) một nửa"},
]

def mc(tag, q, options, why, ctx=None, long=False):
    d = {"type": "mc", "tag": tag, "q": q, "options": options, "why": why}
    if ctx: d["ctx"] = ctx
    if long: d["long"] = True
    return d

CHECK = "Câu này có đúng với bảng không?"
parts = [
    {"type": "questions", "before": True, "title": "Part 1 · Đọc bảng",
     "instr": "Nhìn hai bảng (cà phê và chuối) rồi trả lời. Chưa cần xem bài mẫu.",
     "questions": [
        mc("Đọc bảng", "Năm 2004, nước nào bán **cà phê** Fairtrade nhiều nhất?",
           ["UK", "Switzerland", "Denmark", "Belgium"],
           "Năm 2004 UK đạt 20 triệu euro, hơn gấp ba Switzerland (6). Switzerland chỉ cao nhất ở năm 1999 (3), nên phải nhìn đúng cột năm."),
        mc("Đọc bảng", "Doanh số **chuối** giảm ở những nước nào?",
           ["Belgium và Sweden", "Denmark và Sweden", "Belgium và Switzerland", "Không nước nào giảm"],
           "Belgium 1.8 -> 1 và Sweden 2 -> 0.9. Ba nước còn lại đều tăng, Denmark tăng từ 0.6 lên 4."),
        mc("Thì", "Bảng có 2 mốc đã qua (1999 và 2004). Bài viết nên dùng thì nào?",
           ["Quá khứ đơn (rose, fell)", "Hiện tại đơn (rises, falls)", "Hiện tại hoàn thành (has risen)", "Tương lai (will rise)"],
           "Số liệu thuộc các năm đã qua nên dùng **quá khứ đơn**. Hiện tại hoàn thành không đi với mốc năm cụ thể như *in 2004*."),
        mc("Đơn vị", "Số **20** ở hàng UK (cà phê, 2004) nghĩa là gì?",
           ["20 triệu euro tiền bán hàng", "20% thị phần cà phê", "20 triệu kg cà phê", "20 nghìn euro tiền bán hàng"],
           "Tiêu đề cột ghi *millions of euros*: đây là giá trị bán, không phải khối lượng hay phần trăm. Viết *20 million euros* hoặc *20m*."),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Bảng có nhiều số, không thể nêu hết.",
     "questions": [
        mc("Ý chính", "Nếu chỉ được nêu **một** chi tiết về cà phê, con chọn chi tiết nào?",
           ["UK tăng từ 1.5 lên 20 triệu euro", "Sweden tăng từ 0.8 lên 1 triệu euro", "Denmark tăng từ 1.8 lên 2 triệu euro", "Belgium tăng từ 1 lên 1.7 triệu euro"],
           "Ưu tiên chi tiết nổi bật nhất: thay đổi lớn nhất hoặc số cao nhất. UK tăng hơn 13 lần, các nước khác chỉ tăng nhẹ.", long=True),
        mc("Ý chính", "Ý nào **ít đáng** đưa vào overview nhất?",
           ["Denmark bán cà phê nhiều hơn Belgium năm 1999", "Doanh số cà phê tăng ở cả 5 nước", "UK dẫn đầu về chuối ở cả hai năm", "Doanh số chuối giảm ở 2 nước"],
           "Overview chỉ nêu xu hướng lớn của cả bảng. So sánh hai nước có số nhỏ (1.8 và 1) là chi tiết, nếu cần thì để vào thân bài.", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, coffee sales rose in all five countries, while banana sales increased in three, with the UK leading for both products by 2004.",
            "Overall, UK coffee sales rose from 1.5 to 20 million euros, and banana sales rose from 15 to 47 million euros.",
            "Overall, people in the UK seem to care more about fair trade than people in other countries.",
            "Overall, coffee sales were highest in Switzerland, and banana sales rose in all five countries."],
           "Overview tốt nêu 2 xu hướng chung, không có số. Các câu kia: có số liệu, nêu ý kiến ngoài bảng, hoặc sai (năm 2004 UK cao nhất về cà phê, chuối giảm ở 2 nước).", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài này viết Thân bài 1 về cà phê, Thân bài 2 về chuối. Mỗi nhóm số liệu dưới đây nên nằm ở đâu?",
     "options": ["Thân bài 1 (cà phê)", "Thân bài 2 (chuối)", "Overview", "Không cần nêu"],
     "items": [
        {"label": "Switzerland và Denmark: cùng tăng mạnh (1 -> 5.5 và 0.6 -> 4)", "answer": 1,
         "why": "Đây là số liệu **chuối**, nên vào Thân bài 2. Hai nước cùng xu hướng tăng vọt nên gộp chung một câu."},
        {"label": "Belgium và Sweden: số nhỏ, cùng tăng nhẹ (1 -> 1.7 và 0.8 -> 1)", "answer": 0,
         "why": "Đây là số liệu **cà phê**, nên vào Thân bài 1. Hai nước có số gần nhau, cùng tăng nhẹ nên gộp chung."},
        {"label": "Cà phê tăng ở cả 5 nước, chuối tăng ở 3/5 nước", "answer": 2,
         "why": "Đây là xu hướng chung của cả hai bảng, không có số cụ thể, nên đặt ở **Overview**."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("So sánh", "Chuối ở UK tăng từ 15 lên 47 triệu euro. Cách nói nào đúng?",
           ["rose more than threefold", "rose three times more than", "tripled more", "increased by three times as"],
           "47 : 15 ≈ 3.1, nên **rose more than threefold** (hoặc *more than tripled*). *three times more than* là dịch từ \"tăng hơn ba lần\" và cần thêm vế so sánh."),
        mc("Chủ ngữ", "Câu nào đúng?",
           ["The figure for Denmark remained relatively stable.", "Denmark remained relatively stable.", "The figure of Denmark were relatively stable.", "Denmark's coffee was relatively stable."],
           "Chủ ngữ phải là **số liệu** (*the figure for*, *sales in*), không phải tên nước. *The figure* số ít nên đi với *was/remained*.", long=True),
        mc("respectively", "Trong câu này, *respectively* cho biết điều gì?",
           ["Belgium lên 1.7m, Sweden lên 1m", "Belgium lên 1m, Sweden lên 1.7m", "Cả hai nước đều lên 1.7m", "Hai nước tăng tổng cộng 2.7m"],
           "**respectively** = lần lượt: số thứ nhất đi với nước nhắc trước, số thứ hai đi với nước nhắc sau. Viết sai thứ tự là sai số liệu.",
           ctx="Belgium and Sweden both experienced increases, to 1.7m and 1m, respectively."),
        mc("Mở bài", "Chọn câu mở bài tốt nhất.",
           ["The tables compare sales of Fairtrade coffee and bananas in five European countries in 1999 and 2004.",
            "The tables below give information about sales of Fairtrade-labelled coffee and bananas in 1999 and 2004 in five European countries.",
            "The charts show sales of Fairtrade coffee and bananas in five European countries in 1999 and 2004.",
            "The tables will show how sales of Fairtrade coffee and bananas change in five European countries."],
           "Mở bài tốt viết lại đề bằng lời mình (*compare*), đúng thì. Các câu kia: chép nguyên đề, gọi bảng là *charts*, hoặc sai thì.", long=True),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: Denmark cao gấp ba Switzerland", "Sai: hai nước bằng nhau (6m)", "Sai: Switzerland chỉ cao gấp đôi Denmark"],
           "Năm 2004 cà phê: Switzerland 6, Denmark 2. 6 = 3 x 2 nên câu đúng.",
           ctx="In 2004, Switzerland's coffee sales were three times as high as Denmark's."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: Sweden giảm mạnh, từ 2m xuống 0.9m", "Đúng", "Sai: Sweden tăng từ 0.9m lên 2m", "Sai: Sweden giữ nguyên 2m"],
           "Chuối ở Sweden: 2 -> 0.9, giảm hơn một nửa chứ không phải giảm nhẹ. Số 1.8 là của Belgium năm 1999 (nhầm hàng).",
           ctx="Sweden's banana sales fell slightly, from 2m to 1.8m."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: tăng hơn 13 lần, từ 1.5m lên 20m", "Đúng", "Sai: UK giảm", "Sai: tăng đúng gấp ba"],
           "Cà phê ở UK: 1.5 -> 20, tăng hơn 13 lần. *doubled* chỉ đúng với Switzerland (3 -> 6).",
           ctx="UK coffee sales doubled between 1999 and 2004."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 2. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Bananas",
     "text": "Swiss sales were originally almost [1] those of Denmark (1m and 0.6m, respectively), and both [2], reaching 5.5m and 4m. There was little difference between the figures for Sweden and Belgium (2m and 1.8m, respectively), and both roughly [3], to around 1m in 2004.",
     "options": ["surged", "twice higher than", "halved", "twice as high as", "decreased half"],
     "items": [
        {"answer": 3, "why": "**twice as high as** = cao gấp đôi. Không nói *twice higher than* (dịch từ \"cao hơn gấp đôi\")."},
        {"answer": 0, "why": "**surge** = tăng vọt, hợp với 1 -> 5.5m và 0.6 -> 4m. Sau *both* cần động từ quá khứ."},
        {"answer": 2, "why": "**halve** = giảm một nửa (2m -> 0.9m, 1.8m -> 1m). *decreased half* là dịch từng chữ \"giảm một nửa\", sai ngữ pháp."},
     ]},
]

L = {
    "id": "T01",
    "pageTitle": "Task 1 Table T01 · Fairtrade coffee and bananas",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T01",
    "heading": "Sales of Fairtrade coffee and bananas (1999 & 2004)",
    "topic": "Fairtrade coffee and bananas",
    "kind": "2 bảng · thay đổi 1999 -> 2004",
    "book": "Cambridge IELTS 10",
    "source": "Đề: Cambridge IELTS 10, Test 2. Bài mẫu band 7: E. Tahassoni (tahassoni.com), có chỉnh sửa nhỏ. Dùng cho mục đích học tập.",
    "prompt": [
        "The tables below give information about sales of Fairtrade-labelled coffee and bananas in 1999 and 2004 in five European countries.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Coffee – sales (millions of euros)", "head": [["Coffee", "1999", "2004"]],
         "rows": [["UK", "1.5", "20"], ["Switzerland", "3", "6"], ["Denmark", "1.8", "2"], ["Belgium", "1", "1.7"], ["Sweden", "0.8", "1"]]},
        {"caption": "Bananas – sales (millions of euros)", "head": [["Bananas", "1999", "2004"]],
         "rows": [["UK", "15", "47"], ["Switzerland", "1", "5.5"], ["Denmark", "0.6", "4"], ["Belgium", "1.8", "1"], ["Sweden", "2", "0.9"]]},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T01.json –", words, "từ")
