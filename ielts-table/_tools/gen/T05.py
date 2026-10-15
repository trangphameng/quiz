"""T05 – Fruit prices by season (Lessons for IELTS Advanced Writing). Chạy: python3 gen/T05.py"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

sample = [
    {"label": "Mở bài", "text": "The table {depicts|depict} average fruit prices over the year in one country in the Southern hemisphere. Four different fruits are used as {exemplars|exemplar}."},
    {"label": "Overview", "text": "Overall, locally grown fruit {varies in price and availability|varies} according to the seasons, whereas imported fruit is more {consistently priced|consistently}."},
    {"label": "Thân bài 1", "text": "The price of locally grown apples varies from {a peak of|peak} $4.50 per kilo in summer to {a low of|low} $2.25 in winter, and they are {available all year round|yearround}. {In contrast|contrast}, locally grown oranges are {not on sale|onsale} in autumn, and their cheapest season is spring, at $3.90 {on average|average} per kilo. Summer is the most expensive time to buy local oranges."},
    {"label": "Thân bài 2", "text": "However, imported oranges and bananas are available all year and are consistently priced at around $5 and $3 per kilo {respectively|respectively}. Strawberries are the most expensive fruit and are {at their cheapest|cheapest} in summer, at $6 a kilo. They are most expensive in autumn ($8 per kilo) and are {not available|notavail} in winter at all."},
]
words = sum(len(re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", p["text"]).split()) for p in sample)

vocab = [
    {"key": "depict", "word": "depict", "ipa": "/dɪˈpɪkt/", "pos": "v", "vi": "thể hiện, mô tả"},
    {"key": "exemplar", "word": "exemplar", "ipa": "/ɪɡˈzemplɑː(r)/", "pos": "n", "vi": "ví dụ tiêu biểu"},
    {"key": "varies", "word": "vary in price and availability", "ipa": "/ˈveəri ɪn praɪs ənd əˌveɪləˈbɪləti/", "pos": "phrase", "vi": "thay đổi về giá và việc có hàng"},
    {"key": "consistently", "word": "consistently priced", "ipa": "/kənˈsɪstəntli praɪst/", "pos": "phrase", "vi": "có giá ổn định"},
    {"key": "peak", "word": "a peak of", "ipa": "/ə piːk əv/", "pos": "n phrase", "vi": "mức cao nhất là"},
    {"key": "low", "word": "a low of", "ipa": "/ə ləʊ əv/", "pos": "n phrase", "vi": "mức thấp nhất là"},
    {"key": "yearround", "word": "available all year round", "ipa": "/əˈveɪləbl ɔːl jɪə raʊnd/", "pos": "phrase", "vi": "có bán quanh năm"},
    {"key": "contrast", "word": "in contrast", "ipa": "/ɪn ˈkɒntrɑːst/", "pos": "phrase", "vi": "ngược lại"},
    {"key": "onsale", "word": "(not) on sale", "ipa": "/ɒn seɪl/", "pos": "phrase", "vi": "(không) được bày bán"},
    {"key": "average", "word": "on average", "ipa": "/ɒn ˈævərɪdʒ/", "pos": "phrase", "vi": "tính trung bình"},
    {"key": "respectively", "word": "respectively", "ipa": "/rɪˈspektɪvli/", "pos": "adv", "vi": "lần lượt (theo đúng thứ tự)"},
    {"key": "cheapest", "word": "at their cheapest", "ipa": "/ət ðeə ˈtʃiːpɪst/", "pos": "phrase", "vi": "ở mức rẻ nhất"},
    {"key": "notavail", "word": "not available", "ipa": "/nɒt əˈveɪləbl/", "pos": "adj", "vi": "không có (bán)"},
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
        mc("Đọc bảng", "Giá **cao nhất** trong cả bảng là của loại quả nào, vào mùa nào?",
           ["Dâu tây, mùa thu (April)", "Dâu tây, mùa hè (January)", "Cam nhập khẩu, mùa thu (April)", "Cam nội địa, mùa hè (January)"],
           "Dâu tây tháng 4 giá $8.00, cao nhất bảng. $6.00 là giá dâu tháng 1 (mức rẻ nhất của dâu); cam nhập khẩu cao nhất chỉ $5.50.", long=True),
        mc("So sánh", "Táo nội địa tháng 1 ($4.50) so với tháng 7 ($2.25) thì sao?",
           ["Đắt gấp đôi", "Đắt gấp ba", "Đắt hơn khoảng $1", "Rẻ bằng một nửa"],
           "4.50 = 2 x 2.25 nên tháng 1 đắt **gấp đôi** tháng 7. Chênh lệch là $2.25, không phải $1."),
        mc("Thì", "Bảng không ghi năm, chỉ có các tháng và mùa. Bài nên dùng thì nào?",
           ["Hiện tại đơn (varies, are)", "Quá khứ đơn (varied, were)", "Tương lai (will vary)", "Hiện tại tiếp diễn (is varying)"],
           "Không có năm cụ thể thì bảng mô tả một thực tế chung, dùng **hiện tại đơn**. Bài mẫu viết *varies*, *are not on sale*.", long=True),
        mc("Đơn vị", "Số **$4.50** ở hàng Apples (L), cột January nghĩa là gì?",
           ["Giá trung bình 1 kg táo nội địa vào tháng 1", "Giá 1 quả táo nội địa vào tháng 1", "Tổng tiền bán táo nội địa trong tháng 1", "Giá táo tăng thêm $4.50 trong tháng 1"],
           "Đề ghi *average price in dollars per kilogram*: giá **trung bình mỗi kg**, không phải giá 1 quả hay tổng doanh thu.", long=True),
     ]},
    {"type": "questions", "before": True, "title": "Part 2 · Đặc điểm chính",
     "instr": "Chọn ý đáng viết. Bảng có 20 ô, không thể nêu hết.",
     "questions": [
        mc("Ý chính", "Ý nào nên đưa vào **overview**?",
           ["Quả nội địa đổi giá và có lúc không có hàng; quả nhập khẩu giá ổn định", "Cam nhập khẩu giá $5.50 vào tháng 4", "Táo nội địa giá $4.25 vào tháng 10", "Chuối giá $2.99 vào tháng 1"],
           "Overview nêu xu hướng chung: nhóm **nội địa** (L) thay đổi theo mùa, nhóm **nhập khẩu** (I) ổn định. Các ý kia là một con số lẻ.", long=True),
        mc("Ý chính", "Chi tiết nào **ít quan trọng nhất**?",
           ["Táo nội địa giá $4.25 vào tháng 10", "Dâu tây đắt nhất và không có bán mùa đông", "Chuối giữ nguyên giá $2.99 cả năm", "Táo nội địa rẻ nhất vào mùa đông ($2.25)"],
           "Ba ý kia là cao nhất, thấp nhất hoặc điểm đặc biệt. $4.25 tháng 10 không nổi bật, bài mẫu cũng bỏ qua.", long=True),
        mc("Overview", "Chọn overview tốt nhất.",
           ["Overall, locally grown fruit varies in price and availability according to the seasons, whereas imported fruit is more consistently priced.",
            "Overall, strawberries cost $8 in April and $6 in January.",
            "Overall, people should buy imported fruit because it is better.",
            "Overall, apples cost $4.50, $3.75, $2.25 and $4.25 in the four months."],
           "Overview tốt so sánh hai nhóm (nội địa và nhập khẩu), không có số. Các câu kia: có số liệu, nêu ý kiến ngoài bảng, hoặc liệt kê một hàng.", long=True),
     ]},
    {"type": "match", "before": True, "plain": True, "pick": "Chọn đoạn",
     "title": "Part 3 · Nhóm số liệu",
     "instr": "Bài mẫu không viết theo thứ tự từng hàng mà nhóm lại. Mỗi nhóm nên vào đoạn nào?",
     "options": ["Thân bài 1", "Thân bài 2", "Overview"],
     "items": [
        {"label": "Táo nội địa và cam nội địa (giá đổi theo mùa)", "answer": 0,
         "why": "Hai loại quả **nội địa** đổi giá rõ theo mùa, được tả trong Thân bài 1."},
        {"label": "Cam nhập khẩu, chuối và dâu tây", "answer": 1,
         "why": "Thân bài 2 gom hai loại **nhập khẩu** giá ổn định, rồi tới dâu tây là quả đắt nhất."},
        {"label": "Quả nội địa thay đổi theo mùa, quả nhập khẩu ổn định", "answer": 2,
         "why": "Đây là so sánh chung giữa hai nhóm, không cần số, nên đặt ở **Overview**."},
     ]},
    {"type": "questions", "title": "Part 4 · Ngôn ngữ số liệu",
     "instr": "Bài mẫu đã mở. Chọn cách viết đúng.",
     "questions": [
        mc("Khoảng giá", "Táo nội địa: cao nhất $4.50 (hè), thấp nhất $2.25 (đông). Giá táo varies ...",
           ["from a peak of $4.50 in summer to a low of $2.25 in winter",
            "between a peak of $4.50 in summer to a low of $2.25 in winter",
            "from a peak at $4.50 in summer until a low at $2.25 in winter",
            "from the highest $4.50 in summer to the lowest $2.25 in winter"],
           "Cấu trúc **from + to** hoặc **between + and**, không trộn *between* với *to*. *a peak* / *a low* đi với **of** + số.", long=True),
        mc("So sánh", "Táo tháng 1 ($4.50) so với tháng 7 ($2.25). Apples are ... in January ... in July.",
           ["twice as expensive ... as", "twice more expensive ... than", "two times expensive ... than", "double expensive ... as"],
           "**twice as + tính từ + as**. *twice more than* là lỗi dịch từ \"gấp đôi hơn\"; *double* không đứng trước tính từ như vậy.", long=True),
        mc("respectively", "Cam nhập khẩu khoảng $5, chuối khoảng $3. Câu nào đúng?",
           ["Imported oranges and bananas cost around $5 and $3 per kilo respectively.",
            "Imported oranges and bananas cost around $3 and $5 per kilo respectively.",
            "Respectively, imported oranges and bananas cost around $5 and $3 per kilo.",
            "Imported oranges and bananas cost respectively around $5 and $3 per kilo respectively."],
           "**respectively** đặt cuối câu; thứ tự số phải khớp thứ tự danh từ (cam -> $5, chuối -> $3). Câu đảo thành $3 và $5 là sai số liệu.", long=True),
        mc("Từ nối", "Apples are available all year round. ___, local oranges are not on sale in autumn.",
           ["In contrast", "Because", "Moreover", "As a result"],
           "Hai ý trái ngược (có quanh năm / không có mùa thu) nên dùng **In contrast**. *Moreover* là thêm ý cùng chiều, *As a result* là kết quả."),
     ]},
    {"type": "questions", "title": "Part 5 · Đúng với bảng không?",
     "instr": "Đọc câu, so lại với bảng. Sai một con số là mất điểm Task Achievement.",
     "questions": [
        mc("Kiểm tra số liệu", CHECK,
           ["Đúng", "Sai: chuối rẻ nhất vào mùa đông", "Sai: chuối đắt nhất vào mùa hè", "Sai: chuối không có bán mùa đông"],
           "Hàng Bananas (I): $2.99 ở cả bốn cột. Câu đúng.",
           ctx="Imported bananas are the same price all year round."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: rẻ nhất vào mùa xuân ($3.90)", "Đúng", "Sai: rẻ nhất vào mùa hè ($4.95)", "Sai: rẻ nhất vào mùa đông ($2.25)"],
           "Cam nội địa: mùa đông $4.30, mùa xuân $3.90, nên mùa xuân rẻ nhất. $2.25 là giá táo (nhầm hàng).",
           ctx="Locally grown oranges are cheapest in winter."),
        mc("Kiểm tra số liệu", CHECK,
           ["Sai: $8 so với $6, chỉ đắt hơn $2", "Đúng", "Sai: dâu tây rẻ nhất vào mùa thu", "Sai: dâu tây không có bán mùa thu"],
           "Dâu tây mùa thu $8.00, mùa hè $6.00. Gấp đôi phải là $12. Mùa dâu không có bán là **mùa đông**, không phải mùa thu.",
           ctx="Strawberries are twice as expensive in autumn as in summer."),
     ]},
    {"type": "gap", "title": "Part 6 · Hoàn thành bài mẫu",
     "instr": "Đoạn trích từ Thân bài 2. Chọn cụm cho mỗi chỗ trống. Có 2 cụm thừa.",
     "textTitle": "Imported fruit and strawberries",
     "text": "However, imported oranges and bananas are available all year and are [1] priced at around $5 and $3 per kilo [2]. Strawberries are the most expensive fruit and are [3] in summer, at $6 a kilo.",
     "options": ["consistently", "respectively", "at their cheapest", "consistent", "more cheaper"],
     "items": [
        {"answer": 0, "why": "Trước phân từ *priced* cần **trạng từ** -> *consistently*. *consistent* là tính từ."},
        {"answer": 1, "why": "**respectively** cuối câu: cam $5, chuối $3, đúng thứ tự."},
        {"answer": 2, "why": "**at their cheapest** = ở mức rẻ nhất. *more cheaper* sai vì *cheaper* đã là so sánh hơn."},
     ]},
]

L = {
    "id": "T05",
    "pageTitle": "Task 1 Table T05 · Fruit prices by season",
    "eyebrow": "IELTS Writing Task 1 · Table · Đề T05",
    "heading": "Average fruit prices in four months in a Southern hemisphere country",
    "topic": "Fruit prices by season",
    "kind": "Bảng thay đổi · 4 mùa trong năm (không ghi năm)",
    "book": "Lessons for IELTS – Advanced Writing",
    "source": "Bài mẫu lấy từ sách: Lessons for IELTS – Advanced Writing, New Oriental Education & Technology Group IELTS Research Institute (có chỉnh sửa nhỏ).",
    "prompt": [
        "The table below shows the average price in dollars per kilogram of apples, oranges, bananas, and strawberries in January, April, July, and October in a Southern hemisphere country.",
        "Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "Write at least 150 words.",
    ],
    "tables": [
        {"caption": "Average price in dollars per kilogram",
         "head": [["Fruit", "January (Summer)", "April (Autumn)", "July (Winter)", "October (Spring)"]],
         "rows": [
            ["Apples (L)", "$4.50", "$3.75", "$2.25", "$4.25"],
            ["Oranges (L)", "$4.95", "NA", "$4.30", "$3.90"],
            ["Oranges (I)", "$5.00", "$5.50", "$5.25", "$5.00"],
            ["Bananas (I)", "$2.99", "$2.99", "$2.99", "$2.99"],
            ["Strawberries (L)", "$6.00", "$8.00", "NA", "$6.50"],
         ],
         "note": "L = locally grown · I = imported · NA = not available"},
    ],
    "words": words,
    "sample": sample,
    "vocab": vocab,
    "parts": parts,
}
json.dump(L, open(os.path.join(HERE, "..", "lessons", "T05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("T05.json –", words, "từ")
