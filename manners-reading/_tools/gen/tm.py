from helpers import *

# ---- L21 ----
lesson(21, 'TM', '4–7', 'Welcome to the Table', 'A Warm Welcome', [
 "When guests come to your house, {greet} them at the door. Take their coats and hang them up on {hangers}; don't throw them in a big pile on the floor.",
 "Shake hands with your guests and hug your relatives, even Aunt Edna with her bad breath and {false teeth}! A warm welcome makes everyone feel at home from the very first minute.",
 "At the dinner table, {be a pal}. Pull out a chair for a lady or an older guest and hold it {steady} while she sits down and moves closer to the table.",
 "Then find your own seat and sit up straight. Put your napkin on your {lap}, and keep your elbows off the table. You don't want to look like a {barbarian} at a {feast}!",
 "Rules about hands are different around the world. In France, for example, it is considered rude to keep your hands under the table. Both hands should stay {visible}, resting near your plate, for the whole meal.",
],[
 ("greet","greet","/ɡriːt/","động từ","chào đón"),
 ("hangers","hanger","/ˈhæŋə(r)/","danh từ","móc treo quần áo"),
 ("false teeth","false teeth","/ˌfɔːls ˈtiːθ/","danh từ","răng giả"),
 ("be a pal","be a pal","/pæl/","cụm từ","tử tế như một người bạn"),
 ("steady","steady","/ˈstedi/","tính từ","vững, không lung lay"),
 ("lap","lap","/læp/","danh từ","lòng (phần đùi khi ngồi)"),
 ("barbarian","barbarian","/bɑːˈbeəriən/","danh từ","người man rợ, thiếu văn minh"),
 ("feast","feast","/fiːst/","danh từ","bữa tiệc lớn"),
 ("visible","visible","/ˈvɪzəbl/","tính từ","có thể nhìn thấy"),
],[
 headings(["At the front door","A warm welcome for everyone","Helping someone sit down","How to sit at the table","A French custom"], [
  ("A",0,"Đoạn A: chào khách ở cửa, treo áo khoác."),
  ("B",1,"Đoạn B: bắt tay, ôm họ hàng."),
  ("C",2,"Đoạn C: kéo ghế, giữ ghế cho khách ngồi."),
  ("D",3,"Đoạn D: ngồi thẳng, khăn ăn trên đùi, không chống khuỷu tay."),
  ("E",4,"Đoạn E: phong tục ở Pháp."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","What should you do with your guests' coats?",["Hang them up.","Put them on the floor.","Wear them.","Leave them in the car."],"*hang them up on hangers.*"),
  tf("The writer suggests hugging your relatives only if you like them.", False, "Sai. *even Aunt Edna with her bad breath and false teeth!*"),
  mc("Suy luận","Why does the writer mention Aunt Edna's bad breath?",["to show that you should be welcoming even when it isn't easy","to give advice about cleaning your teeth","to explain why some relatives stay at home","to describe what she had for lunch"],"Dù không dễ chịu vẫn nên đón tiếp nồng hậu."),
  mc("Chi tiết","According to (C), how can you help someone sit down?",["Pull out their chair and hold it steady.","Bring them a cushion.","Push them towards the table.","Show them where the bathroom is."],"*Pull out a chair… and hold it steady.*"),
  tf("The writer says it is fine to rest your elbows on the table.", False, "Sai. *keep your elbows off the table.*"),
  mc("Chi tiết","In France, where should your hands be during a meal?",["above the table","under the table","on your lap","in your pockets"],"*Both hands should stay visible, resting near your plate.*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("tm-greet","A smiling girl holds up a coat beside a pile of clothes and says: Hi Aunt Edna! to an elderly woman with glasses","Who is the elderly woman most likely to be?",["one of the girl's relatives","the girl's teacher","a shop assistant","a stranger in the street"],"*Hi Aunt Edna!* → họ hàng (dì/bà)."),
  pic("tm-greet","A smiling girl holds up a coat beside a pile of clothes and says: Hi Aunt Edna! to an elderly woman with glasses","According to (A), what should the girl do with the coats?",["Hang them on hangers.","Leave them in a pile on the floor.","Put them on herself.","Give them to the dog."],"*don't throw them in a big pile on the floor.*"),
  pic("tm-elbows","A bored-looking boy sits at a dining table with his elbow on the table and his chin in his hand, while a dog lies under his chair","Which rule is the boy breaking?",["Keep your elbows off the table.","Greet guests at the door.","Hang coats on hangers.","Hug your relatives."],"Đoạn D: *keep your elbows off the table.*"),
 ]),
 gapmix("Grandad's birthday dinner", "Last Sunday, we had a big dinner for Grandad's birthday. [1] When everyone came to the table, I pulled out Grandma's chair for her. [2] During the meal, I sat up straight with my napkin on my lap. [3]", [
  ("I stood at the front door to welcome the guests and hang up their coats.","Khách đến → chào và treo áo."),
  ("She smiled and said I was a real gentleman.","Phản ứng của bà khi được kéo ghế."),
  ("At the end, Grandad said my table manners were better than his!","Kết: được ông khen."),
 ], [
  "Nobody came because Grandad had forgotten to invite them.",
  "Then I put my elbows on the table and fell asleep.",
 ], [0,4,1,3,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*At the dinner table, be a pal* (C). To **be a pal** means to…",["be friendly and helpful","be quiet","be the first to eat","be a guest"],"**Pal** = bạn → cư xử tử tế, giúp đỡ."),
  mc("Từ vựng","*…look like a barbarian at a feast!* (D). A **barbarian** is someone who…",["is wild and has no manners","is a famous chef","always eats slowly","organises parties"],"**Barbarian** = người man rợ."),
  mc("Từ vựng","*Both hands should stay visible* (E). **Visible** means…",["able to be seen","hidden","clean","warm"],"**Visible** = nhìn thấy được."),
 ]),
])

# ---- L22 ----
lesson(22, 'TM', '8–11', 'Waiting and Cutlery', 'Forks, Knives and Patience', [
 "Before you start eating, wait until everyone has been {served}. In many homes, the polite signal to begin is when the hosts pick up their forks.",
 "Don't {reach across} the table for food. Instead, ask someone to pass it to you, and when dishes go round, pass them to your left. Take only as much as you think you can eat. Don't {pile} a mountain of mashed potato on your plate!",
 "Customs are not the same everywhere. In Afghanistan, it is polite for guests to eat first, and they are expected to eat the most! So if you ever visit, don't be shy about your {appetite}.",
 "At a {formal} dinner, you may see several knives and forks, and some may even be placed above your plate. Don't panic! Start with the {cutlery} on the outside (Americans call it silverware) and work your way in. And never use your knife as a {toothpick}!",
 "Your bread plate sits to the left of your dinner plate. Choose a piece of bread or a roll, {tear off} a small piece and butter just that piece. Don't try to rip the whole roll apart with your teeth, or {crumbs} might fly across the table!",
],[
 ("served","serve","/sɜːv/","động từ","dọn (món) cho, phục vụ"),
 ("reach across","reach across","/riːtʃ əˈkrɒs/","cụm động từ","với tay qua"),
 ("pile","pile","/paɪl/","động từ","chất đống"),
 ("appetite","appetite","/ˈæpɪtaɪt/","danh từ","sự thèm ăn"),
 ("formal","formal","/ˈfɔːml/","tính từ","trang trọng"),
 ("cutlery","cutlery","/ˈkʌtləri/","danh từ","dao, dĩa, thìa"),
 ("toothpick","toothpick","/ˈtuːθpɪk/","danh từ","tăm"),
 ("tear off","tear off","/teər ˈɒf/","cụm động từ","xé ra"),
 ("crumbs","crumb","/krʌm/","danh từ","vụn bánh"),
],[
 which([
  ("A paragraph that explains which knives and forks to use first", "D", "Đoạn D: *Start with the cutlery on the outside.*"),
  ("A paragraph that describes the signal to start eating", "A", "Đoạn A: chủ nhà cầm dĩa lên."),
  ("A paragraph that warns you not to take too much food", "B", "Đoạn B: *Don't pile a mountain of mashed potato.*"),
  ("A paragraph that explains how to eat bread politely", "E", "Đoạn E: xé miếng nhỏ, phết bơ."),
  ("A paragraph about a country where guests are expected to eat a lot", "C", "Đoạn C: Afghanistan."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","When is it polite to start eating?",["when everyone has been served and the hosts begin","as soon as your food arrives","when you feel hungry","after the first person finishes"],"*wait until everyone has been served… the hosts pick up their forks.*"),
  tf("The writer says you should pass dishes to your right.", False, "Sai. *pass them to your left.*"),
  mc("Chi tiết","What should you do if a dish is too far away from you?",["Ask someone to pass it.","Stand up and reach for it.","Wait until the end of the meal.","Go without it."],"*ask someone to pass it to you.*"),
  tf("In Afghanistan, guests are expected to eat less than their hosts.", False, "Sai. *they are expected to eat the most!*"),
  mc("Chi tiết","If there are several forks, which one should you use first?",["the one on the outside","the one closest to the plate","the biggest one","the one above the plate"],"*Start with the cutlery on the outside.*"),
  mc("Suy luận","Why does the writer warn about crumbs in (E)?",["Biting into a whole roll can make a mess.","Crumbs are bad for your teeth.","Bread should never be eaten at dinner.","Butter makes crumbs fly."],"*Don't try to rip the whole roll apart with your teeth, or crumbs might fly.*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("tm-reach","A boy leans over the table and stretches his arm across a girl's plate to grab food from a basket","What is the boy doing wrong?",["reaching across the table","using the wrong fork","eating with his fingers","talking with his mouth full"],"Đoạn B: *Don't reach across the table.*"),
  pic("tm-reach","A boy leans over the table and stretches his arm across a girl's plate to grab food from a basket","What should the boy have done instead?",["asked someone to pass the food","waited until the next day","taken the whole basket","eaten the girl's food"],"*ask someone to pass it to you.*"),
  pic("tm-forks","A boy at a table holds up a fork in each hand and looks confused by all the knives and forks around his plate","Which paragraph would help this boy most?",["Paragraph D","Paragraph A","Paragraph C","Paragraph E"],"Đoạn D: dùng dao dĩa từ ngoài vào trong."),
 ]),
 gapmix("My first fancy dinner", "Last month, my aunt took me to a smart restaurant to celebrate her birthday. [1] I had no idea which one to use. [2] Then the waiter brought a basket of warm bread rolls. [3]", [
  ("When I sat down, I saw three forks and two knives next to my plate.","Cần chỗ cho *which one* → nhiều dao dĩa."),
  ("Luckily, my aunt whispered, \"Start from the outside and work your way in.\"","Cô chỉ cách dùng."),
  ("I tore off a small piece and buttered it, just like everyone else.","Ăn bánh mì đúng cách (đoạn E)."),
 ], [
  "There was only a spoon on the table, so I ate everything with it.",
  "The restaurant was closed, so we went home.",
 ], [4,0,3,1,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*Don't reach across the table* (B). To **reach across** means to…",["stretch your arm over something to get it","walk around","sit down","pass something to the left"],"**Reach across** = với tay qua."),
  mc("Từ vựng","*Don't pile a mountain of mashed potato on your plate!* (B). Here, **a mountain of** means…",["a very large amount of","a small amount of","a picture of","a hot plate of"],"Nghĩa bóng: rất nhiều."),
  mc("Từ vựng","*…never use your knife as a toothpick!* (D). A **toothpick** is…",["a small stick for cleaning between your teeth","a kind of toothbrush","a sharp knife","a dentist"],"**Toothpick** = cây tăm."),
 ]),
])

# ---- L23 ----
lesson(23, 'TM', '12–15', 'Mouthfuls and Fingers', 'Slurps, Crumbs and Germs', [
 "It is not polite to talk or {chomp} with your mouth full, and don't {stuff} too much food in at once. You can do all of that at a hot-dog eating {contest}, but not at Grandma's table! Lift the food from your plate to your mouth; don't drop your face into your bowl. Leave that move for the dog!",
 "If you need to leave the table to go to the toilet, put your napkin on your chair and say, \"Please excuse me.\" And if you ever eat in China, don't finish everything on your plate. Your host may think you are rude, but leaving a little shows that you are a good guest.",
 "Don't {slurp} your food or lick your fingers; nobody wants to listen to that! Never stick your finger in the cake {icing}, however good it looks, and don't {double-dip} your crisp in the dip. Nobody wants your {germs}!",
 "Only eat with your fingers when the food is meant to be eaten that way. Don't grab your pork chop like a {caveman}, but it's fine to pick up a taco. It also depends on where you are: in fancy restaurants, even chips are eaten with a fork.",
 "Sometimes the rules are {turned upside down}. In Japan, slurping your noodle soup is a good thing, and the louder, the better! It tells the cook that you really enjoyed the meal.",
],[
 ("chomp","chomp","/tʃɒmp/","động từ","nhai nhóp nhép"),
 ("stuff","stuff","/stʌf/","động từ","nhồi, tống (đồ ăn)"),
 ("contest","contest","/ˈkɒntest/","danh từ","cuộc thi"),
 ("slurp","slurp","/slɜːp/","động từ","húp xì xụp"),
 ("icing","icing","/ˈaɪsɪŋ/","danh từ","lớp kem phủ bánh"),
 ("double-dip","double-dip","/ˌdʌbl ˈdɪp/","động từ","chấm lại lần hai (sau khi đã cắn)"),
 ("germs","germ","/dʒɜːm/","danh từ","vi trùng"),
 ("caveman","caveman","/ˈkeɪvmæn/","danh từ","người tiền sử"),
 ("turned upside down","turn sth upside down","/ˌʌpsaɪd ˈdaʊn/","cụm từ","đảo lộn hoàn toàn"),
],[
 headings(["Mouths full and faces down","Leaving the table – and leaving some food","Sounds and germs to avoid","When fingers are allowed","A custom that breaks the rule"], [
  ("A",0,"Đoạn A: không nói khi miệng đầy, không cúi mặt vào bát."),
  ("B",1,"Đoạn B: xin phép rời bàn; ở Trung Quốc để lại chút thức ăn."),
  ("C",2,"Đoạn C: không húp, không liếm tay, không chấm lại – vi trùng."),
  ("D",3,"Đoạn D: món nào được ăn bằng tay."),
  ("E",4,"Đoạn E: ở Nhật, húp to lại là lịch sự."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","Where does the writer say stuffing your mouth might be OK?",["at a hot-dog eating contest","at Grandma's table","at a fancy restaurant","in China"],"*You can do all of that at a hot-dog eating contest.*"),
  tf("Before you leave the table, you should put your napkin on your chair.", True, "Đúng. *put your napkin on your chair and say, \"Please excuse me.\"*"),
  mc("Chi tiết","Why should you leave a little food on your plate in China?",["Finishing everything may seem rude to your host.","Food is very expensive there.","The dog eats the leftovers.","It shows that you are full of energy."],"*Your host may think you are rude…*"),
  mc("Chi tiết","Why is double-dipping a bad idea?",["It spreads germs.","It wastes crisps.","It makes the dip too salty.","It is too noisy."],"*Nobody wants your germs!*"),
  tf("According to (D), you should always eat with a knife and fork.", False, "Sai. *it's fine to pick up a taco.*"),
  mc("Ý chính","What is the main point of (E)?",["Something rude in one place can be polite in another.","Japanese food is always noisy.","You should never eat noodle soup.","Cooks prefer quiet guests."],"Húp to: bất lịch sự ở nơi khác nhưng lịch sự ở Nhật."),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("tm-bowl","An elderly woman eats soup with a spoon while a girl and a dog beside her lean down into their bowls","Which paragraph gives advice for the girl in this picture?",["Paragraph A","Paragraph C","Paragraph D","Paragraph E"],"Đoạn A: *don't drop your face into your bowl.*"),
  pic("tm-bowl","An elderly woman eats soup with a spoon while a girl and a dog beside her lean down into their bowls","Which sentence from the text is a joke about the animal in this picture?",["Leave that move for the dog!","Nobody wants your germs!","Please excuse me.","The louder, the better!"],"Chú chó cúi mặt vào bát → *Leave that move for the dog!*"),
  pic("tm-dip","Two girls share a bowl of crisps and dip; one dips a crisp into the bowl while the other watches","What should the girl NOT do after biting her crisp?",["dip it into the bowl again","eat the rest of it","hold it with her fingers","offer the bowl to her friend"],"Đoạn C: *don't double-dip your crisp.*"),
 ]),
 gapmix("Noodles in Tokyo", "Last summer my family went on holiday to Japan. [1] Everyone around us was slurping loudly. [2] So I tried it too, and the cook gave me a big smile. [3]", [
  ("On the first evening, we went to a small restaurant that served noodle soup.","Bối cảnh: quán mì."),
  ("At first, I was shocked, because at home slurping is bad manners.","Phản ứng ban đầu với tiếng húp."),
  ("I learnt that good manners can be very different in different countries.","Bài học rút ra."),
 ], [
  "The waiter asked us to be quiet because slurping was rude.",
  "We ate pizza with knives and forks at our hotel.",
 ], [3,0,1,4,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…talk or chomp with your mouth full* (A). To **chomp** means to…",["chew noisily","whisper","swallow quickly","smile"],"**Chomp** = nhai nhóp nhép."),
  mc("Từ vựng","*Don't grab your pork chop like a caveman* (D). This means don't eat it…",["in a wild way with your hands","too slowly","with chopsticks","in the kitchen"],"**Caveman** → ăn bốc thô lỗ."),
  mc("Từ vựng","*…don't double-dip your crisp* (C). To **double-dip** is to…",["put food you have bitten back into a shared dip","buy two bags of crisps","dip with both hands","share your crisps"],"Chấm lại lần hai sau khi đã cắn."),
 ]),
])

# ---- L24 ----
lesson(24, 'TM', '16–21', 'No Thanks and Thank You', 'Kind Words at the Table', [
 "Not everyone likes the same food, so it's useful to know how to {refuse} politely. If a dish is new to you, try a tiny bite first; you might like it more than you expect. But if you really don't {fancy} fish eggs or frog's legs, simply say, \"No, thank you.\" Never say, \"That smells {rotten}!\" You could hurt your host's feelings.",
 "Remember that cooking dinner for guests takes a lot of {effort}. Think about that before you say anything {unkind} about the food.",
 "When the meal is over, say something nice to the cook and the host, and thank them for the delicious food. If you didn't enjoy it, you can still find something kind to say, like, \"The flowers on the table are so pretty!\"",
 "Wait to be {excused} before you leave the table. Until then, stay in your seat, listen to the conversation and {join in} if you like. And, of course, thank your host for inviting you.",
 "Now you know which fork to use and which way to pass the pasta. Keep practising, and soon you will {impress} everyone with your table manners. You might even be invited back! Before long, your manners will be {finger-licking good}.",
],[
 ("refuse","refuse","/rɪˈfjuːz/","động từ","từ chối"),
 ("fancy","fancy","/ˈfænsi/","động từ","thích, muốn (ăn)"),
 ("rotten","rotten","/ˈrɒtn/","tính từ","thối, hỏng"),
 ("effort","effort","/ˈefət/","danh từ","công sức"),
 ("unkind","unkind","/ˌʌnˈkaɪnd/","tính từ","không tử tế"),
 ("excused","excuse","/ɪkˈskjuːz/","động từ","cho phép (rời đi)"),
 ("join in","join in","/dʒɔɪn ˈɪn/","cụm động từ","tham gia"),
 ("impress","impress","/ɪmˈpres/","động từ","gây ấn tượng"),
 ("finger-licking good","finger-licking good","/ˈfɪŋɡə lɪkɪŋ/","cụm từ","ngon đến mút tay"),
],[
 which([
  ("A paragraph that gives an example of a kind comment that isn't about the food", "C", "Đoạn C: khen hoa trên bàn."),
  ("A paragraph that suggests tasting something before deciding", "A", "Đoạn A: *try a tiny bite first.*"),
  ("A paragraph that encourages you to keep practising", "E", "Đoạn E: *Keep practising.*"),
  ("A paragraph that reminds you how hard cooking can be", "B", "Đoạn B: *takes a lot of effort.*"),
  ("A paragraph that explains when you may leave the table", "D", "Đoạn D: *Wait to be excused.*"),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","What does the writer suggest if a food is new to you?",["Try a tiny bite first.","Refuse it straight away.","Smell it carefully.","Ask for something else."],"*try a tiny bite first.*"),
  tf("Saying \"That smells rotten!\" is a polite way to refuse food.", False, "Sai. *Never say… You could hurt your host's feelings.*"),
  mc("Chi tiết","Why should you avoid saying unkind things about the food?",["The host has made a big effort to cook it.","The food might be cold.","The other guests will eat it.","It may come from a restaurant."],"*cooking dinner for guests takes a lot of effort.*"),
  mc("Suy luận","Why might a guest mention the flowers after a meal?",["to say something kind without lying about the food","because they want to take the flowers home","because the flowers can be eaten","to change the subject to gardening"],"Không thích món ăn vẫn có thể khen điều khác, thật lòng mà tế nhị."),
  tf("According to (D), you may leave the table as soon as you finish eating.", False, "Sai. *Wait to be excused before you leave the table.*"),
  mc("Chi tiết","According to (E), what might happen if you have great table manners?",["You might be invited back.","You might have to cook next time.","You will sit at a different table.","You will win a prize."],"*You might even be invited back!*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("tm-refuse","A boy holds his nose and pulls a face at a plate of food while a woman serves something from a bowl","How does the boy feel about the food?",["He doesn't like it.","He loves it.","He is very hungry.","He wants to cook it himself."],"Bịt mũi, nhăn mặt → không thích."),
  pic("tm-refuse","A boy holds his nose and pulls a face at a plate of food while a woman serves something from a bowl","What would be the most polite thing for the boy to say?",["\"No, thank you.\"","\"That smells rotten!\"","\"Yuck! Take it away!\"","\"I'll bring a sandwich next time.\""],"Đoạn A: *simply say, \"No, thank you.\"*"),
  pic("tm-flowers","A smiling girl at a table points to a vase of flowers while the host stands beside her holding a plate","Which paragraph matches this picture best?",["Paragraph C","Paragraph A","Paragraph D","Paragraph E"],"Đoạn C: *The flowers on the table are so pretty!*"),
 ]),
 gapmix("Dinner at Lucy's", "Last night I had dinner at my friend Lucy's house. [1] I had never tried it before, and it looked a bit strange. [2] After dinner, I waited until Lucy's mum said we could leave the table. [3]", [
  ("Her dad served a spicy fish curry.","Cần món ăn được nhắc (*it*)."),
  ("I took a small bite, and to my surprise, it was delicious!","Thử một miếng nhỏ (đoạn A)."),
  ("Before I went home, I thanked them both for inviting me.","Kết: cảm ơn chủ nhà."),
 ], [
  "Her dad had ordered the same pizza that I eat every week.",
  "Then I ran out of the room before dessert.",
 ], [0,4,3,1,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…if you really don't fancy fish eggs* (A). If you don't **fancy** something, you…",["don't want it","can't afford it","don't recognise it","are allergic to it"],"**Fancy** = muốn, thích."),
  mc("Từ vựng","*Wait to be excused* (D). To **be excused** is to…",["be given permission to leave","be told off","be invited","be served first"],"**Be excused** = được phép rời đi."),
  mc("Từ vựng","*…your manners will be finger-licking good* (E). Why is this phrase funny here?",["It is usually used about tasty food, not manners.","You should lick your fingers.","The food will be sticky.","Manners are a kind of food."],"**Finger-licking good** thường nói về đồ ăn ngon; tác giả dùng đùa cho phép lịch sự."),
 ]),
])
