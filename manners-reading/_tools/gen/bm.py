import json, os
from helpers import *

# ---- L01: patch existing lesson (paragraph links, credit, book) ----
p = os.path.join(OUT, 'L01.json')
d = json.load(open(p, encoding='utf-8'))
d['book'] = 'Basic Manners'
d['source'] = "Bài đọc phỏng theo Basic Manners – Ann Ingalls (The Child's World, 2013), tr. 4–9."
d['credit'] = "Tranh minh hoạ: Ronnie Rooney, trong Basic Manners (The Child's World, 2013). Dùng cho mục đích học tập."
for it in d['parts'][0]['items']:
    it['para'] = it['label'][-1]
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('patched L01')

# ---- L02 ----
lesson(2, 'BM', '10–13', 'Honest Words, Fair Play', 'Truth, Kindness and Fair Play', [
 "People {trust} friends who tell the truth. Imagine you ate the last piece of pie that your mum was saving for your dad. It might be {tempting} to blame the dog, but {owning up} is always the better choice. The same is true if you made a silly face at your baby sister and made her cry. Admitting what you did shows that you are honest, and {honesty} builds trust.",
 "However, being honest does not mean saying every thought that comes into your head. Some comments can hurt people's feelings, especially comments about how someone looks or smells. Nobody wants to be called \"stinky feet\", even if their feet really do smell! In situations like this, the kindest thing is to keep your thoughts to yourself.",
 "Games are another place where manners matter. Whether you win or lose, you should behave politely when the game is over. Winners should not {brag} or {show off}, and losers should not {sulk} or get angry. Throwing the cards across the room will not change the result; it will only make others unwilling to play with you next time.",
 "{A good sport} accepts that not everyone can win at the same time. Shaking hands or saying \"Good game!\" to the other players can be hard, especially after a close match, but it shows {maturity} and respect.",
 "Sadly, even famous players and coaches sometimes lose their temper. You may see your sports hero {throw a fit} or start a fight on TV. Remember that being talented is not the same as being a good {role model}.",
],[
 ("trust","trust","/trʌst/","động từ","tin tưởng"),
 ("tempting","tempting","/ˈtemptɪŋ/","tính từ","hấp dẫn, dễ khiến mình muốn làm"),
 ("owning up","own up","/əʊn ʌp/","cụm động từ","thú nhận, nhận lỗi"),
 ("honesty","honesty","/ˈɒnəsti/","danh từ","sự trung thực"),
 ("brag","brag","/bræɡ/","động từ","khoe khoang"),
 ("show off","show off","/ʃəʊ ɒf/","cụm động từ","khoe mẽ, thể hiện"),
 ("sulk","sulk","/sʌlk/","động từ","hờn dỗi"),
 ("a good sport","a good sport","/ɡʊd spɔːt/","cụm từ","người chơi đẹp, biết thắng thua"),
 ("maturity","maturity","/məˈtʃʊərəti/","danh từ","sự trưởng thành"),
 ("throw a fit","throw a fit","/θrəʊ ə fɪt/","cụm từ","nổi cơn tam bành"),
 ("role model","role model","/ˈrəʊl ˌmɒdl/","danh từ","tấm gương"),
],[
 which([
  ("A paragraph that explains how admitting a mistake builds trust", "A", "Đoạn A: *Admitting what you did… honesty builds trust.*"),
  ("A paragraph that gives an example of a comment that can hurt", "B", "Đoạn B nhắc ví dụ gọi người khác là *\"stinky feet\"*."),
  ("A paragraph that suggests something to say at the end of a match", "D", "Đoạn D: nói *\"Good game!\"* với đối thủ."),
  ("A paragraph that says some well-known people do not behave well", "E", "Đoạn E: *even famous players and coaches sometimes lose their temper.*"),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","What does the writer suggest you should do if you ate the pie?",["Admit that you ate it.","Blame the dog.","Buy another pie quietly.","Say nothing and hope nobody notices."],"Đoạn A: *owning up is always the better choice* (nhận lỗi là tốt nhất)."),
  tf("The writer believes you should always say exactly what you think.", False, "Sai. Đoạn B: trung thực **không có nghĩa** là nói mọi suy nghĩ ra miệng."),
  mc("Suy luận","Why shouldn't you call someone \"stinky feet\", even if it is true?",["It may hurt their feelings.","It is not a funny joke.","It is against school rules.","They might call you a name too."],"Đoạn B: lời nhận xét về ngoại hình, mùi cơ thể *can hurt people's feelings*."),
  mc("Chi tiết","According to paragraph C, what may happen if you throw the cards across the room?",["Other people may not want to play with you again.","You may win the next game.","The result of the game will change.","The teacher will give you more cards."],"*…it will only make others unwilling to play with you next time.*"),
  tf("The writer says that saying \"Good game!\" after a close match is always easy.", False, "Sai. Đoạn D: *can be hard, especially after a close match*."),
  mc("Ý chính","What is the main point of paragraph E?",["Being a famous player doesn't make someone a good example.","You should never watch sport on TV.","Coaches are usually better role models than players.","Talented people never lose their temper."],"*being talented is not the same as being a good role model.*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("bm-stinky","A girl holding her nose and saying Hey, stinky feet!","The girl may be telling the truth. So what is wrong with what she says?",["It is honest but unkind.","It is a lie.","It is too quiet.","It is a compliment."],"Có thể đúng sự thật, nhưng lời nói đó làm người khác tổn thương (đoạn B)."),
  pic("bm-stinky","A girl holding her nose and saying Hey, stinky feet!","According to the text, what would have been the kindest thing for the girl to do?",["Keep her thoughts to herself.","Say it more loudly.","Tell everyone else first.","Take a photo of his boots."],"Đoạn B: *the kindest thing is to keep your thoughts to yourself.*"),
  pic("bm-goodgame","Two football players from different teams giving a high five and saying Good game!","Which phrase from the text best describes these two players?",["good sports","role models who throw a fit","players who brag","losers who sulk"],"Hai đội đập tay và nói *Good game!*, đúng tinh thần **a good sport** (đoạn D)."),
 ]),
 gap("After the final", "Last Saturday, our team lost the final by one goal. [1] Our captain, Huy, walked over to the other team and shook their hands. [2] Later, the coach told us she was prouder of us that day than when we won. [3]", [
  "Some of us wanted to kick the ball away and go straight home.",
  "\"Good game,\" he said, even though he looked disappointed.",
  "She said that losing well is a skill, just like scoring goals.",
  "He told the winners that they had only been lucky.",
  "Then we all threw our water bottles at the referee.",
 ], [
  (0,"Sau khi thua, cảm xúc tự nhiên là muốn bỏ về; câu sau *Our captain…* đối lập với cảm xúc đó."),
  (1,"Huy bắt tay và nói *Good game* – đúng với hành động trước đó."),
  (2,"Giải thích lý do huấn luyện viên tự hào: thua đẹp cũng là một kỹ năng."),
 ]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…owning up is always the better choice* (A). What does **own up** mean?",["admit that you did something wrong","eat everything on your plate","get up early","blame someone else"],"**Own up** = thú nhận lỗi."),
  mc("Từ vựng","*…losers should not sulk or get angry* (C). If you **sulk**, you…",["stay quiet and unhappy because you didn't get what you wanted","laugh loudly at other people","practise harder for next time","congratulate the winner"],"**Sulk** = hờn dỗi, im lặng tỏ ra không vui."),
  mc("Từ vựng","*Winners should not brag* (C). Which word is closest in meaning to **brag**?",["boast","apologise","whisper","cheat"],"**Brag** = **boast** = khoe khoang."),
  mc("Từ vựng","*…your sports hero throw a fit* (E). What does **throw a fit** mean?",["suddenly become very angry and upset","throw a ball very far","get fit by training","fall over during a game"],"**Throw a fit** = nổi cơn tam bành, không phải ném gì."),
 ]),
])

# ---- L03 ----
lesson(3, 'BM', '14–17', 'Kind Words, Open Doors', 'Small Words, Big Difference', [
 "When someone says \"Good job!\", the polite reply is simply \"Thank you.\" Accepting a {compliment} in this way shows that you are a {gracious} person, someone who is kind and pleasant to be around. In the same way, avoid {putting other people down} or pointing out their mistakes in front of others.",
 "Words are powerful. If something you said makes another person cry, don't pretend it didn't happen. Say \"I'm sorry\" and mean it. When someone thanks you, answer \"You're welcome.\" Once is enough: you don't want to {sound like a broken record}! In many parts of South America, people greet each other with a kiss on the cheek, sometimes on both cheeks, so politeness can look different around the world.",
 "Manners also matter when you are moving through busy places. Before getting into a {lift}, let the people inside get out first. On an {escalator}, wait for others to step on before you do. Pushing or {shoving} your way through never makes the journey faster for anyone.",
 "Doors are a good test of your manners. If someone is coming out as you are going in, let them go first. Hold the door open for older people and for parents with young children, who often {have their hands full} with bags, {pushchairs} and toys. If you go through a door first, don't let it {slam} in the face of the person behind you; hold it until they can take it.",
 "And when someone holds a door for you, don't just rush past. A quick \"Thank you!\" lets them know that their kindness was noticed.",
],[
 ("compliment","compliment","/ˈkɒmplɪmənt/","danh từ","lời khen"),
 ("gracious","gracious","/ˈɡreɪʃəs/","tính từ","tử tế, nhã nhặn"),
 ("putting other people down","put sb down","/pʊt daʊn/","cụm động từ","chê bai, hạ thấp ai"),
 ("sound like a broken record","sound like a broken record","/ˌbrəʊkən ˈrekɔːd/","cụm từ","nói đi nói lại như đĩa hỏng"),
 ("lift","lift","/lɪft/","danh từ","thang máy (Anh-Mỹ: elevator)"),
 ("escalator","escalator","/ˈeskəleɪtə(r)/","danh từ","thang cuốn"),
 ("shoving","shove","/ʃʌv/","động từ","xô đẩy"),
 ("have their hands full","have your hands full","/hændz fʊl/","cụm từ","tay bận đầy đồ; rất bận"),
 ("pushchairs","pushchair","/ˈpʊʃtʃeə(r)/","danh từ","xe đẩy em bé"),
 ("slam","slam","/slæm/","động từ","đóng sầm"),
],[
 headings(["Accepting praise politely","Saying sorry and thanks the right way","Getting in and out of crowded places","Helping people through doorways","Showing that you noticed a kindness","How to give a good compliment","Why lifts are dangerous"], [
  ("A",0,"Đoạn A: đáp lại *Good job!* bằng *Thank you* = nhận lời khen lịch sự."),
  ("B",1,"Đoạn B nói cách nói *I'm sorry* và *You're welcome*."),
  ("C",2,"Đoạn C: thang máy, thang cuốn, nơi đông người."),
  ("D",3,"Đoạn D: giữ cửa cho người già, cha mẹ có con nhỏ."),
  ("E",4,"Đoạn E: nói *Thank you* để người kia biết mình *noticed* lòng tốt."),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","According to paragraph A, what should you avoid doing?",["pointing out other people's mistakes in front of others","saying \"Thank you\" too quickly","accepting compliments","being kind and pleasant"],"*avoid putting other people down or pointing out their mistakes in front of others.*"),
  tf("The writer says you should repeat \"You're welcome\" several times to be extra polite.", False, "Sai. *Once is enough.*"),
  mc("Suy luận","Why does the writer mention South America?",["to show that polite greetings differ around the world","to explain how to say sorry","to say that kissing is rude","to describe a holiday"],"*politeness can look different around the world.*"),
  mc("Chi tiết","What should you do before getting into a lift?",["Let the people inside get out first.","Push the button many times.","Walk in as fast as you can.","Hold the door for everyone outside."],"Đoạn C: *let the people inside get out first.*"),
  tf("Parents with young children often find it hard to open doors.", True, "Đúng. Họ *have their hands full* với túi, xe đẩy, đồ chơi."),
  mc("Thông điệp","What is the writer's opinion about pushing in busy places?",["It doesn't help anyone get there faster.","It is fine if you are in a hurry.","It is only rude on escalators.","It is the best way to get a good place."],"*Pushing or shoving… never makes the journey faster for anyone.*"),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("bm-goodjob","A boy says Good job! to a girl decorating a cake; she says Thank you!","What does the girl's reply show about her?",["She is gracious.","She is bragging.","She is sulking.","She is putting him down."],"Đáp lại lời khen bằng *Thank you* thể hiện người **gracious** (đoạn A)."),
  pic("bm-door","A boy holds a door open for a mother with a pushchair and a baby","Which advice from paragraph D is the boy following?",["holding the door for a parent whose hands are full","letting the door slam behind him","waiting for people to get out of a lift","going through the door first"],"Người mẹ bế em bé và đẩy xe – đúng kiểu *have their hands full*."),
  pic("bm-door","A boy holds a door open for a mother with a pushchair and a baby","Why is the mother's \"Thank you!\" important, according to paragraph E?",["It shows that she noticed his kindness.","It tells him to close the door.","It means he must help her again.","It is the only English she knows."],"*A quick \"Thank you!\" lets them know that their kindness was noticed.*"),
 ]),
 gap("A small surprise", "At the shopping centre yesterday, I was walking behind an old man with a walking stick. [1] I hurried forward and held it open for him. [2] Then he did something that surprised me. [3]", [
  "When he reached the heavy glass door, he struggled to push it.",
  "He smiled and said, \"Thank you, young man. You've made my day.\"",
  "He held the next door open for a mother with a pushchair.",
  "I let the door slam behind me and ran inside.",
  "I was too busy looking at my phone to notice him.",
 ], [
  (0,"Câu sau *held **it** open*: **it** = cánh cửa nặng ở câu này."),
  (1,"Phản ứng tự nhiên khi được giúp: cảm ơn."),
  (2,"Điều bất ngờ: ông lại giữ cửa giúp người khác."),
 ]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*…you don't want to sound like a broken record!* (B). What does this mean?",["keep saying the same thing again and again","speak too quietly","sing badly","forget what to say"],"Đĩa hỏng cứ lặp một đoạn → nói đi nói lại."),
  mc("Từ vựng","*…parents… have their hands full* (D). Here, **have your hands full** means…",["be carrying a lot of things","be very rich","have dirty hands","be clapping"],"Ở đây là nghĩa đen: tay bận đầy đồ (túi, xe đẩy, đồ chơi)."),
  mc("Từ vựng","*…avoid putting other people down* (A). To **put someone down** is to…",["make them feel stupid or less important","help them sit down","write their name on a list","carry them carefully"],"**Put sb down** = chê bai, làm người khác thấy kém cỏi."),
 ]),
])

# ---- L04 ----
lesson(4, 'BM', '18–21', "At a Friend's Table", 'How to Be a Great Guest', [
 "Every family has its own way of doing things, and their habits may be quite different from what you {are used to}. This is natural, because people come from different countries and {cultures}. Your family might always eat spaghetti on Sundays, while your friend's family might prefer fried rice, pickled beetroot or strudel.",
 "So what should you do if you are {invited} to dinner and the food on the table is completely new to you? The answer is simple: give it a try. You might {discover} a new favourite. Even dishes that sound strange, like fried frog legs or pickled pig's feet, could turn out to be delicious! {Pulling a face} or asking for something else would be unkind to the people who cooked for you.",
 "{Customs} vary around the world. In Japan, for instance, children often {bow} when they arrive at someone's house for dinner. Noticing and respecting these differences is part of being a good guest.",
 "One final piece of advice: don't be a {slob}. Clean up after yourself. If you have been finger painting at school, wash your hands instead of wearing the paint home. And after eating at a friend's house, offer to carry your dishes to the sink.",
 "Good manners make everyone feel comfortable. They help us make friends and even {solve} problems. Keep practising them, and you may become the best-liked kid in town.",
],[
 ("are used to","be used to","/bi ˈjuːst tə/","cụm từ","quen với"),
 ("cultures","culture","/ˈkʌltʃə(r)/","danh từ","văn hoá"),
 ("invited","invite","/ɪnˈvaɪt/","động từ","mời"),
 ("discover","discover","/dɪˈskʌvə(r)/","động từ","khám phá, phát hiện"),
 ("pulling a face","pull a face","/pʊl ə feɪs/","cụm từ","nhăn mặt"),
 ("customs","custom","/ˈkʌstəm/","danh từ","phong tục"),
 ("bow","bow","/baʊ/","động từ","cúi chào"),
 ("slob","slob","/slɒb/","danh từ","người bừa bộn, luộm thuộm"),
 ("solve","solve","/sɒlv/","động từ","giải quyết"),
],[
 which([
  ("A paragraph that says each family's habits can be different", "A", "Đoạn A: *Every family has its own way of doing things.*"),
  ("A paragraph that explains what to do if you don't recognise the food", "B", "Đoạn B: *give it a try*."),
  ("A paragraph that gives an example of a greeting custom in another country", "C", "Đoạn C: trẻ em Nhật cúi chào."),
  ("A paragraph that describes habits of a tidy person", "D", "Đoạn D: rửa tay, mang bát đĩa ra bồn rửa."),
  ("A paragraph that mentions manners helping to solve problems", "E", "Đoạn E: *help us make friends and even solve problems.*"),
 ]),
 questions("Part 2 · Reading comprehension", "Chọn đáp án đúng hoặc True / False.", [
  mc("Chi tiết","According to paragraph A, why do families have different habits?",["People come from different countries and cultures.","Some families don't like spaghetti.","Children choose the food at home.","Shops sell different food every day."],"*…because people come from different countries and cultures.*"),
  tf("The writer suggests asking for a different meal if you don't like the look of the food.", False, "Sai. Đoạn B: hỏi món khác là *unkind*."),
  mc("Suy luận","Why does the writer mention frog legs and pig's feet?",["as examples of food that sounds strange but may taste good","to show what Japanese children eat","because they are the writer's favourite dishes","to warn readers not to eat them"],"*…dishes that sound strange… could turn out to be delicious!*"),
  mc("Từ vựng","In paragraph C, bowing in Japan is an example of…",["a custom","a slob","a favourite dish","a problem"],"*Customs vary around the world. In Japan, for instance…*"),
  tf("The writer says good manners can help people get on with each other.", True, "Đúng. Đoạn E: *help us make friends and even solve problems.*"),
  mc("Thông điệp","What is the main purpose of the text?",["to give advice on being a polite guest and respecting differences","to teach readers how to cook new dishes","to compare food in Japan and South America","to explain how to finger paint"],"Cả bài là lời khuyên khi làm khách và tôn trọng sự khác biệt."),
 ]),
 questions("Part 3 · Picture tasks", "Quan sát tranh minh hoạ trong sách và trả lời.", [
  pic("bm-dinner","Two girls at a table, each holding a meatball on a fork","The girls are trying food at a friend's house. Which advice are they following?",["Give new food a try.","Ask for a different dish.","Clean up after yourself.","Bow when you arrive."],"Họ đang nếm thử món ăn – đúng lời khuyên *give it a try* (đoạn B)."),
  pic("bm-dishes","A boy carrying his plate to a woman standing by the kitchen sink","What is the boy doing?",["carrying his dishes to the sink after the meal","asking for more food","washing his hands after painting","bowing to his friend's mother"],"Đúng lời khuyên cuối đoạn D."),
  pic("bm-dishes","A boy carrying his plate to a woman standing by the kitchen sink","Which word from the text is the OPPOSITE of how the boy is behaving?",["a slob","a guest","polite","comfortable"],"**Slob** = người bừa bộn, không dọn dẹp – ngược với cậu bé."),
 ]),
 gap("Dinner at Mai's house", "When I stayed with my friend Mai's family, they served a fish soup I had never tasted before. [1] I took a small spoonful and, to my surprise, I loved it. [2] After dinner, I helped carry the bowls to the kitchen. [3]", [
  "At first, I was a little worried because it smelled very strong.",
  "Mai's grandmother laughed and gave me a second bowl.",
  "Her mum said I was one of the most polite guests they'd ever had.",
  "I told them that my mum's soup was much better.",
  "Then I ordered a pizza on my phone.",
 ], [
  (0,"Lo lắng ban đầu → câu sau *to my surprise, I loved it* tạo đối lập."),
  (1,"Thích món ăn → bà cho thêm bát nữa."),
  (2,"Giúp dọn bát → mẹ Mai khen là khách lịch sự."),
 ]),
 questions("Part 5 · Words in context", "Đoán nghĩa của từ/cụm từ dựa vào ngữ cảnh.", [
  mc("Từ vựng","*Pulling a face… would be unkind* (B). **Pull a face** means…",["make an expression that shows you don't like something","pull someone's cheek","draw a picture of a face","smile politely"],"**Pull a face** = nhăn mặt tỏ ý không thích."),
  mc("Từ vựng","*…different from what you are used to* (A). **Be used to something** means…",["be familiar with it","not like it at all","use it every day at school","be afraid of it"],"**Be used to** = quen với."),
  mc("Từ vựng","*…don't be a slob. Clean up after yourself.* (D). A **slob** is a person who…",["is lazy and untidy","cooks very well","is always on time","is very shy"],"Câu sau *Clean up after yourself* giúp đoán nghĩa: người bừa bộn."),
 ]),
])
