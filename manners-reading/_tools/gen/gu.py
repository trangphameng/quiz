from helpers import *

# ---- L13 ----
lesson(13, 'GU', '4–7', 'Getting Ready to Be a Guest', "You're Invited!", [
 "Imagine finding an {invitation} in your letterbox: you have been invited to a party! What should you do first? Read the day and time carefully and check your calendar. If you are free, {reply} as soon as you can so that your friend knows you will be there. Never just turn up without answering.",
 "Being a guest means going to someone's party or simply visiting their home. It sounds like fun, and it usually is. But are you going to be a good guest? Good manners are the key. They show your {host}, the person who invited you, that you are really pleased to be there.",
 "Before a party, ask if you can bring something. Perhaps your friend needs a ball for a game, or maybe you could bring a pizza to {pass around}. Many guests also bring a small present to say thank you; flowers or chocolates make perfect {host gifts}.",
 "Being on time matters too. If you arrive late, you may {hold everyone up} and {spoil} the fun for the other guests. If possible, ask whether you can come a little early to help {set up}.",
 "There are plenty of jobs for early helpers. You could {fan} out the napkins on the table, put out the funny party hats or make tiny sandwiches. Your host will {appreciate} your help, and the party will be ready in no time.",
],[
 ("invitation","invitation","/ˌɪnvɪˈteɪʃn/","danh từ","lời mời, thiệp mời"),
 ("reply","reply","/rɪˈplaɪ/","động từ","trả lời, hồi đáp"),
 ("host","host","/həʊst/","danh từ","chủ nhà, người mời"),
 ("pass around","pass around","/pɑːs əˈraʊnd/","cụm động từ","chuyền tay mời mọi người"),
 ("host gifts","host gift","/ˈhəʊst ɡɪft/","danh từ","quà tặng chủ nhà"),
 ("hold everyone up","hold sb up","/həʊld ʌp/","cụm động từ","làm ai bị chậm trễ"),
 ("spoil","spoil","/spɔɪl/","động từ","làm hỏng, làm mất vui"),
 ("set up","set up","/set ʌp/","cụm động từ","chuẩn bị, sắp xếp"),
 ("fan","fan (out)","/fæn/","động từ","xếp xoè hình quạt"),
 ("appreciate","appreciate","/əˈpriːʃieɪt/","động từ","trân trọng, cảm kích"),
],[
 headings(["Answering an invitation","What a good guest is","Things you could bring","Don't be late","Jobs for early arrivals"], [
  ("A",0,"Đoạn A: đọc thiệp mời, xem lịch và **reply**."),
  ("B",1,"Đoạn B giải thích thế nào là khách và vì sao cần phép lịch sự."),
  ("C",2,"Đoạn C: mang bóng, pizza, hoa hoặc sô-cô-la."),
  ("D",3,"Đoạn D: đến muộn sẽ *hold everyone up*."),
  ("E",4,"Đoạn E liệt kê việc có thể làm khi đến sớm."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","What should you do first when you receive an invitation?",["Check the day, the time and your calendar.","Buy a present for the host.","Phone all your other friends.","Start making sandwiches."],"*Read the day and time carefully and check your calendar.*"),
  tf("The writer says it is fine to go to a party without replying to the invitation.", False, "Sai. *Never just turn up without answering.*"),
  mc("Chi tiết","According to (B), what do good manners show your host?",["that you are happy to be their guest","that you are richer than the other guests","that you want to leave early","that you are a good cook"],"*…that you are really pleased to be there.*"),
  mc("Chi tiết","Which of these does the writer mention as a good present for a host?",["chocolates","a football","a pizza","a party hat"],"*flowers or chocolates make perfect host gifts.* Pizza và bóng là đồ mang đến cho bữa tiệc, không phải quà."),
  tf("According to (D), arriving late can affect the other guests.", True, "Đúng. *you may hold everyone up and spoil the fun for the other guests.*"),
  mc("Suy luận","Why might a host be glad if a guest arrives a little early?",["The guest can help get things ready.","The guest can eat more food.","The host can go out for a while.","The party can finish sooner."],"*ask whether you can come a little early to help set up.*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("gu-invite","A smiling boy runs away from a letterbox holding a letter, while a small dog jumps beside him","Which paragraph does this picture match best?",["Paragraph A","Paragraph C","Paragraph D","Paragraph E"],"Cậu bé vừa lấy thư mời ở hộp thư → đoạn A."),
  pic("gu-invite","A smiling boy runs away from a letterbox holding a letter, while a small dog jumps beside him","According to the text, what should the boy do next?",["Check the date and reply to the invitation.","Throw the letter away.","Go straight to the party without telling anyone.","Buy a new party hat."],"Đoạn A: xem ngày giờ rồi **reply**."),
  pic("gu-popcorn","A boy and a girl prepare a party table with paper hats; the girl holds a bowl of popcorn and says: I will put out the popcorn.","What are the children in this picture doing?",["helping to set up before a party","tidying up after a party","playing a ball game","replying to an invitation"],"Bày mũ giấy, bỏng ngô lên bàn → giúp chuẩn bị (đoạn E)."),
 ]),
 gapmix("Leo's birthday party", "Last month my friend Leo invited me to his birthday party. [1] On the day, I arrived half an hour early. [2] When the other guests came, everything was ready. [3]", [
  ("I replied the same evening to say I would come.","Nhận lời mời → trả lời ngay (đúng như đoạn A)."),
  ("Leo's mum gave me a job: putting the party hats on the table.","Đến sớm → được giao việc chuẩn bị."),
  ("Leo's mum said I was the most helpful guest she had ever had.","Mọi thứ sẵn sàng → mẹ Leo khen. Đây là câu kết hợp lý."),
 ], [
  "Leo was cross because I had arrived so late.",
  "Nobody was there because the party had already finished.",
 ], [3,0,1,4,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…you may hold everyone up* (D). To **hold someone up** means to…",["make them late","lift them into the air","help them stand","phone them"],"**Hold sb up** = làm ai chậm trễ."),
  mc("Từ vựng","*…a pizza to pass around* (C). If you **pass** food **around**, you…",["offer it to each person in turn","throw it away","eat it all yourself","keep it for later"],"**Pass around** = chuyền cho từng người."),
  mc("Từ vựng","*Your host will appreciate your help* (E). **Appreciate** means…",["be thankful for","not notice","refuse","pay for"],"**Appreciate** = trân trọng, biết ơn."),
 ]),
])

# ---- L14 ----
lesson(14, 'GU', '8–11', 'Arriving the Right Way', 'At the Front Door', [
 "The moment you step through a friend's front door, your manners are on show. First, take off your hat, even if your hair is {sticking up} in every direction underneath. It is a small but important sign of {respect}.",
 "Next, take off your shoes and leave them neatly on the {doormat}. This is especially important on snowy or rainy days. Nobody wants {muddy} footprints or {slushy} puddles all over their clean floors.",
 "In Japan, taking off your shoes is a firm tradition. People remove them just inside the front door, and the host usually leaves a pair of {slippers} there for each guest to wear around the house.",
 "Good guests also avoid surprises. Always phone before you {drop in on} a friend or {relative}. Never just appear on someone's {doorstep} with a suitcase! Your friend may already have other plans, and an unexpected visitor can be stressful.",
 "When you are invited to stay, tell your friend what time you will arrive and when you will be going home. Then stick to it. A good guest does not {outstay their welcome} by staying as long as they please.",
],[
 ("sticking up","stick up","/stɪk ʌp/","cụm động từ","dựng đứng, chĩa lên"),
 ("respect","respect","/rɪˈspekt/","danh từ","sự tôn trọng"),
 ("doormat","doormat","/ˈdɔːmæt/","danh từ","thảm chùi chân"),
 ("muddy","muddy","/ˈmʌdi/","tính từ","lấm bùn"),
 ("slushy","slushy","/ˈslʌʃi/","tính từ","lầy nhầy (tuyết tan)"),
 ("slippers","slippers","/ˈslɪpəz/","danh từ","dép đi trong nhà"),
 ("drop in on","drop in on","/drɒp ˈɪn ɒn/","cụm động từ","ghé thăm (không hẹn trước)"),
 ("relative","relative","/ˈrelətɪv/","danh từ","họ hàng"),
 ("doorstep","doorstep","/ˈdɔːstep/","danh từ","bậc cửa, trước cửa nhà"),
 ("outstay their welcome","outstay your welcome","/ˌaʊtˈsteɪ/","cụm từ","ở lâu quá mức chủ nhà mong muốn"),
],[
 which([
  ("A paragraph that says your hair is no excuse to break a rule", "A", "Đoạn A: *even if your hair is sticking up…*"),
  ("A paragraph that explains why the weather makes one rule more important", "B", "Đoạn B: *especially important on snowy or rainy days.*"),
  ("A paragraph that describes a custom in another country", "C", "Đoạn C: phong tục ở Nhật Bản."),
  ("A paragraph that warns against arriving with a suitcase without warning", "D", "Đoạn D: *Never just appear… with a suitcase!*"),
  ("A paragraph that advises you to say when you will leave", "E", "Đoạn E: *when you will be going home.*"),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Suy luận","Why does the writer mention hair in (A)?",["to show you should take off your hat even if your hair looks messy","to suggest you should brush your hair before a visit","to explain why hats are fashionable","to say that messy hair is rude"],"*take off your hat, even if your hair is sticking up…*"),
  tf("The writer suggests keeping your shoes on when it is raining.", False, "Sai. Bỏ giày ra *especially important on snowy or rainy days.*"),
  mc("Chi tiết","What do hosts in Japan often leave by the front door?",["slippers for their guests","umbrellas","a doormat with each guest's name","a box of chocolates"],"*the host usually leaves a pair of slippers there for each guest.*"),
  mc("Chi tiết","According to (D), why should you phone before visiting?",["Your friend may already have other plans.","Phone calls are cheaper than visits.","Your friend may want to meet you at the station.","It is the law in many countries."],"*Your friend may already have other plans.*"),
  tf("A surprise visit can cause stress for the person you are visiting.", True, "Đúng. *an unexpected visitor can be stressful.*"),
  mc("Ý chính","What is the main message of the whole text?",["Think about your host's home and plans when you visit.","Always take your own slippers when you visit friends.","Visiting friends is too complicated.","Japanese homes are cleaner than other homes."],"Cả bài: giữ sạch nhà chủ, gọi trước, hẹn giờ về → nghĩ cho chủ nhà."),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("gu-boots","A child in a woolly hat and scarf sits by a red front door pulling off wet boots next to a doormat, while a cat watches","Which piece of advice is the child following?",["taking off wet boots by the door","phoning before a visit","wearing slippers in the garden","bringing a suitcase"],"Đoạn B: cởi giày, để ở thảm cạnh cửa."),
  pic("gu-boots","A child in a woolly hat and scarf sits by a red front door pulling off wet boots next to a doormat, while a cat watches","Why is this rule especially important in the picture?",["The weather is cold and wet.","The cat is hungry.","The door is locked.","The child is late."],"Mũ len, khăn, vũng nước → trời tuyết/mưa: *especially important on snowy or rainy days.*"),
  pic("gu-phone","A girl talks on the phone while looking at a calendar; a dog sleeps on the floor","What is the girl most likely doing?",["arranging a time to visit someone","ordering a pizza","doing her homework","complaining about her dog"],"Gọi điện + xem lịch → hẹn trước giờ đến (đoạn D–E)."),
 ]),
 gapmix("A surprise for Grandma", "Last winter my cousin Tom decided to visit Grandma without telling her. [1] When he knocked on the door, nobody answered. [2] Now Tom always phones before he visits. [3]", [
  ("He thought it would be a lovely surprise.","Giải thích vì sao Tom không báo trước."),
  ("Grandma had gone to stay with her sister for the weekend.","Không ai mở cửa → bà đi vắng (*may already have other plans*)."),
  ("That way, Grandma has time to get ready, and she always bakes his favourite cake.","Lợi ích của việc gọi trước."),
 ], [
  "Grandma was so happy that she had cleaned the whole house for him.",
  "He took off his boots and put on his slippers in the garden.",
 ], [0,3,4,2,1]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…even if your hair is sticking up* (A). Hair that is **sticking up** is…",["pointing upwards in a messy way","very long and straight","hidden under a hat","freshly washed"],"**Stick up** = dựng đứng lên."),
  mc("Từ vựng","*Always phone before you drop in on a friend* (D). To **drop in on** someone means to…",["visit them, often without a fixed plan","fall over at their house","leave them a message","invite them to your home"],"**Drop in on** = ghé thăm."),
  mc("Từ vựng","*A good guest does not outstay their welcome* (E). To **outstay your welcome** means to…",["stay longer than your host wants","arrive too early","forget to say hello","leave without saying goodbye"],"**Out-** (vượt quá) + **stay** → ở lâu hơn chủ nhà mong muốn."),
 ]),
])

# ---- L15 ----
lesson(15, 'GU', '12–15', 'In Someone Else\'s Home', 'Their House, Their Rules', [
 "When you visit a friend, stay with them. Don't {wander off} around the house on your own, opening doors to see what is behind them.",
 "If you use the bathroom, do not open the cupboards or look in the drawers. It is not nice to be {nosy}. Staying for a {sleepover} and forgot your toothpaste? Simply ask your host if you can use some of theirs, rather than searching for it.",
 "Every family has its own {house rules}, and they may be different from the rules in your home. Perhaps shoes are not allowed upstairs, or nobody eats in the living room. If you are not sure, just ask. Following the rules shows respect for the whole family.",
 "Always {tidy up} after yourself. Put toys away after you play with them, and leave the bathroom {as clean as a whistle}. Accidents happen, of course. If you break something, say how sorry you are and offer to fix it or {replace} it.",
 "At a sleepover, remember that other people want to sleep. Late at night, {whisper} and walk quietly. Don't {stomp} around like a dinosaur, or you might wake the whole house up!",
],[
 ("wander off","wander off","/ˈwɒndər ɒf/","cụm động từ","đi lang thang ra chỗ khác"),
 ("nosy","nosy","/ˈnəʊzi/","tính từ","tò mò, tọc mạch"),
 ("sleepover","sleepover","/ˈsliːpəʊvə(r)/","danh từ","ngủ lại nhà bạn"),
 ("house rules","house rules","/ˈhaʊs ruːlz/","danh từ","nội quy trong nhà"),
 ("tidy up","tidy up","/ˈtaɪdi ʌp/","cụm động từ","dọn dẹp"),
 ("as clean as a whistle","as clean as a whistle","/ˈwɪsl/","thành ngữ","sạch bong"),
 ("replace","replace","/rɪˈpleɪs/","động từ","thay thế (mua cái mới)"),
 ("whisper","whisper","/ˈwɪspə(r)/","động từ","nói thì thầm"),
 ("stomp","stomp","/stɒmp/","động từ","dậm chân thình thịch"),
],[
 headings(["Stay close to your friend","No snooping in the bathroom","Every home has its own rules","Clean-ups and accidents","Quiet nights"], [
  ("A",0,"Đoạn A: ở cạnh bạn, không đi lang thang."),
  ("B",1,"Đoạn B: không lục tủ trong phòng tắm (*nosy*)."),
  ("C",2,"Đoạn C: mỗi nhà có **house rules** riêng."),
  ("D",3,"Đoạn D: dọn dẹp, làm vỡ đồ thì xin lỗi và đền."),
  ("E",4,"Đoạn E: ban đêm nói nhỏ, đi nhẹ."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","What does the writer say you should NOT do when visiting a friend?",["explore the house on your own","play with your friend","use the bathroom","ask questions"],"*Don't wander off around the house on your own.*"),
  tf("If you forget your toothpaste, you should look for some in the bathroom drawers.", False, "Sai. *ask your host… rather than searching for it.*"),
  mc("Chi tiết","According to (C), what should you do if you don't know a family's rules?",["Ask.","Follow your own family's rules.","Wait until someone tells you off.","Go home early."],"*If you are not sure, just ask.*"),
  mc("Chi tiết","Which example of a house rule is given in (C)?",["Nobody eats in the living room.","Everyone must go to bed at eight.","Guests must bring slippers.","Pets are not allowed indoors."],"*…or nobody eats in the living room.*"),
  tf("The writer says you should offer to fix or replace something you break.", True, "Đúng. *offer to fix it or replace it.*"),
  mc("Suy luận","Why does the writer compare a noisy guest to a dinosaur in (E)?",["to describe heavy, noisy footsteps in a funny way","because dinosaurs are popular at sleepovers","to suggest guests should play dinosaur games","because the host has a toy dinosaur"],"Hình ảnh khủng long → bước chân nặng nề, ồn ào; cách nói hài hước."),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("gu-snoop","A girl opens a bathroom mirror cabinet and bottles fall out all around her head","What is the girl doing wrong?",["looking inside her host's bathroom cabinet","stomping around at night","leaving toys on the floor","forgetting to say thank you"],"Đoạn B: *do not open the cupboards or look in the drawers.*"),
  pic("gu-snoop","A girl opens a bathroom mirror cabinet and bottles fall out all around her head","Which word from the text best describes the girl's behaviour?",["nosy","tidy","patient","quiet"],"Lục tủ nhà người khác = **nosy**."),
  pic("gu-stomp","A child in spotty pyjamas and big dinosaur slippers bangs two cymbals together while a dog watches","Which paragraph gives advice for the child in this picture?",["Paragraph E","Paragraph A","Paragraph C","Paragraph D"],"Mặc đồ ngủ, dép khủng long, đánh chũm chọe → đoạn E: *Don't stomp around like a dinosaur.*"),
 ]),
 gapmix("My first sleepover", "Last Saturday I stayed at my friend Ava's house for the first time. [1] Before dinner, Ava's dad told me that nobody was allowed to eat upstairs. [2] Later that night, we wanted to giggle and tell stories, but everyone else was asleep. [3]", [
  ("I was excited but also a bit nervous because I didn't know her family well.","Lần đầu ngủ lại → vừa háo hức vừa lo."),
  ("That was different from my house, but I followed the rule without complaining.","Phản ứng với **house rule** vừa được nêu."),
  ("So we whispered under the blankets until we fell asleep.","Mọi người đã ngủ → thì thầm."),
 ], [
  "Ava's dad had broken his favourite mug that morning.",
  "We ran up and down the stairs shouting until two o'clock in the morning.",
 ], [4,0,1,3,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…leave the bathroom as clean as a whistle* (D). **As clean as a whistle** means…",["completely clean","quite dirty","full of water","very noisy"],"Thành ngữ: sạch bong."),
  mc("Từ vựng","*Don't wander off around the house* (A). To **wander off** is to…",["walk away from the group without a clear purpose","fall asleep","run a race","help with the cooking"],"**Wander off** = đi lang thang ra chỗ khác."),
  mc("Từ vựng","*Don't stomp around like a dinosaur* (E). To **stomp** is to…",["walk with heavy, noisy steps","walk on tiptoe","dance gracefully","crawl slowly"],"**Stomp** = dậm chân thình thịch."),
 ]),
])

# ---- L16 ----
lesson(16, 'GU', '16–21', 'Meals, Chats and Goodbyes', 'A Perfect Visit', [
 "If you are lucky, your friend's family may ask you to stay for a meal. Always wait to be {offered} food; never {help yourself} from the kitchen. When the meal is over, tell your host how delicious it was, carry your plate to the kitchen and offer to help with the {washing-up}. It is a great way of saying \"Thank you\". In Turkey, asking for a second helping is even a {compliment} to the cook!",
 "Talk to your friend's family too. Be polite, answer their questions and remember the {magic words}: \"Please\", \"Thank you\" and \"Excuse me\".",
 "Be friendly, but try not to {get in the way}. Everyone needs a bit of space. If your host starts {yawning}, it is probably time to go home, not time to describe every comic in your {collection}!",
 "When it is time to leave, thank your host. Once you are home, send a {thank-you note} saying how much fun you had.",
 "Finally, {return the favour}. Invite your friend to your house some time, and this time you can be the host. After all, good guests often make great hosts!",
],[
 ("offered","offer","/ˈɒfə(r)/","động từ","mời"),
 ("help yourself","help yourself","/help jɔːˈself/","cụm từ","tự lấy (đồ ăn)"),
 ("washing-up","washing-up","/ˌwɒʃɪŋ ˈʌp/","danh từ","việc rửa bát"),
 ("compliment","compliment","/ˈkɒmplɪmənt/","danh từ","lời khen"),
 ("magic words","magic words","/ˌmædʒɪk ˈwɜːdz/","danh từ","những từ 'thần kỳ' (lời lịch sự)"),
 ("get in the way","get in the way","/ɡet ɪn ðə ˈweɪ/","cụm từ","làm vướng, cản trở"),
 ("yawning","yawn","/jɔːn/","động từ","ngáp"),
 ("collection","collection","/kəˈlekʃn/","danh từ","bộ sưu tập"),
 ("thank-you note","thank-you note","/ˈθæŋk juː nəʊt/","danh từ","thiệp/thư cảm ơn"),
 ("return the favour","return the favour","/rɪˌtɜːn ðə ˈfeɪvə(r)/","cụm từ","đáp lại lòng tốt"),
],[
 which([
  ("A paragraph that mentions a country where asking for more food is polite", "A", "Đoạn A: Thổ Nhĩ Kỳ – xin thêm là lời khen."),
  ("A paragraph that lists some useful polite expressions", "B", "Đoạn B: *Please, Thank you, Excuse me.*"),
  ("A paragraph that describes a sign that a visit should end", "C", "Đoạn C: chủ nhà ngáp → nên về."),
  ("A paragraph about something to do after you get home", "D", "Đoạn D: *Once you are home, send a thank-you note.*"),
  ("A paragraph that suggests swapping roles with your friend", "E", "Đoạn E: lần này bạn làm chủ nhà."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","According to (A), what should you do if you are hungry at a friend's house?",["wait until the family offers you food","take a snack from the kitchen","go home for lunch","order a pizza"],"*Always wait to be offered food; never help yourself.*"),
  tf("The writer suggests offering to help with the washing-up after a meal.", True, "Đúng. *offer to help with the washing-up.*"),
  mc("Chi tiết","In Turkey, why is asking for more food a good thing?",["It shows the cook that the food was very good.","It means the guest is very hungry.","It is a way of saying goodbye.","It stops food from being wasted."],"*asking for a second helping is even a compliment to the cook.*"),
  tf("The writer thinks you should show your host your whole comic collection.", False, "Sai. *not time to describe every comic in your collection!*"),
  mc("Chi tiết","What should you write in a thank-you note?",["how much fun you had","what you didn't like","when you want to come back","a list of your comics"],"*saying how much fun you had.*"),
  mc("Thông điệp","What does the last sentence of the text suggest?",["Being a guest teaches you how to be a good host.","Hosts are better people than guests.","You should never invite friends home.","Good guests never visit twice."],"*good guests often make great hosts!*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("gu-dishes","A girl stands beside a woman washing dishes in a sink full of bubbles and asks: May I help you with the dishes?","Which part of a visit does this picture show?",["after a meal","arriving at the front door","a sleepover at night","getting an invitation"],"Rửa bát → sau bữa ăn (đoạn A)."),
  pic("gu-yawn","Two boys sit at a table; one yawns while the other says: I should go home. I will see you tomorrow.","Why does the boy in red decide to go home?",["His friend is yawning and looks tired.","His friend asked him to leave.","It has started to rain.","He forgot his toothpaste."],"Đoạn C: *If your host starts yawning, it is probably time to go home.*"),
  pic("gu-note","A girl sits at a table writing a thank-you card","Which paragraph matches this picture?",["Paragraph D","Paragraph B","Paragraph C","Paragraph E"],"Viết thiệp cảm ơn → đoạn D."),
 ]),
 gapmix("Dinner at Sam's", "On Friday I had dinner at my friend Sam's house. [1] After dinner, Sam's mum started clearing the table. [2] At nine o'clock, Sam began to yawn. [3]", [
  ("His dad made a huge pot of spaghetti, and I told him it was the best I'd ever tasted.","Bữa tối + lời khen món ăn."),
  ("I jumped up, carried my plate to the kitchen and offered to dry the dishes.","Mẹ Sam dọn bàn → mình giúp."),
  ("I realised it was time to go, so I thanked everyone and said goodbye.","Sam ngáp → đến lúc về."),
 ], [
  "Sam's dad served us eggs and toast for breakfast.",
  "So we went to the cinema to watch a film about dinosaurs.",
 ], [3,0,1,4,2]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…never help yourself from the kitchen* (A). To **help yourself** means to…",["take something without waiting to be offered","ask for help","do your homework alone","clean the kitchen"],"**Help yourself** = tự lấy."),
  mc("Từ vựng","*…try not to get in the way* (C). If you **get in the way**, you…",["stop others from doing what they want or need to do","get lost","arrive late","find the right path"],"**Get in the way** = gây vướng víu."),
  mc("Từ vựng","*Finally, return the favour* (E). To **return the favour** means to…",["do something kind for someone who was kind to you","take a present back to the shop","ask for help again","go back home"],"**Return the favour** = đáp lại lòng tốt."),
 ]),
])
