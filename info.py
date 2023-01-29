import re
from os import environ

from dotenv import load_dotenv
load_dotenv()

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/34b8b3e4350b8a4818d5d.jpg https://telegra.ph/file/1993a54f372ea505868aa.jpg https://telegra.ph/file/1d6182871ed45170e8ba0.jpg https://telegra.ph/file/24a09af9c6e16e2633e36.jpg https://telegra.ph/file/23c899179b7aa6e50a50e.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

TUTORIAL_LINK = environ.get('TUTORIAL_LINK', False)
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
HIDE_BUTTON = "🙈 Hide Buttons 🙈"


KEYBOARD_BUTTON = list(i.strip() for i in environ.get("KEYBOARD_BUTTON").split(",")) if environ.get("KEYBOARD_BUTTON") else []
OPEN_MENU_BUTTON = environ.get('OPEN_MENU_BUTTON', "🙈 𝗛𝗜𝗗𝗘 𝗕𝗨𝗧𝗧𝗢𝗡𝗦 🙈")

OPEN_MENU_BUTTON2 = "🎬 𝖳𝖱𝖤𝖭𝖣𝖨𝖭𝖦 𝖭𝖮𝖶 🎬"
KEYBOARD_BUTTON2 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON2").split(",")) if environ.get("KEYBOARD_BUTTON2") else []

OPEN_MENU_BUTTON3 = environ.get('OPEN_MENU_BUTTON3', "💙 𝖬𝖴𝖲𝖳 𝖶𝖠𝖳𝖢𝖧 𝖬𝖮𝖵𝖨𝖤𝖲 💙")
KEYBOARD_BUTTON3 = ["Nerkonda Paarvai", "Asuran", "Thani Oruvan", "Dhuruvangal Pathinaaru", "Sathuranga Vettai", "Aayirathil Oruvan", "Vettaiyaadu Vilaiyaadu", "Samurai", "Anbe Sivam", "Mahanadhi", "Indian", "Mudhalvan", "Hey Ram", "Ratha Kanneer", "Aarilirunthu Arubathu Varai", "Nayagan (1987)", "Thalapathi", "Pasa Malar", "Soodhu Kavvum (2013)", "Madras", "Mozhi", "Papanasam", "Unnaipol Oruvan", "Thani Oruvan", "Kaakkaa Muttai", "Jigarthanda", "Uriyadi", "Joker", "Visaaranai", "Aaranya Kaandam", "Pudhu Pettai", "Anbe Sivam", "Kaakha Kaakha The Police", "Paruthiveeran", "Kattradhu Thamizh", "Moodar Koodam", "Ramana", "Market Street", "Chennai 600028", "Naan Kadavul", "Raam", "Irudhi Suttru", "Anjathe", "Poi Solla Porom", "Kalyana Samayal Saadham", "Abhiyum Naanum", "Pizza (2012)", "Aandavan Kattala", "Pariyerum Perumal", "Sardar", "Vikram", "Love Today (2022)"]

OPEN_MENU_BUTTON4 = environ.get('OPEN_MENU_BUTTON4', "🎞️ 𝖭𝖤𝖶 𝖯𝖱𝖤𝖣𝗏𝖣 𝖬𝖮𝖵𝖨𝖤𝖲 🎞️")
KEYBOARD_BUTTON4 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON2").split(",")) if environ.get("KEYBOARD_BUTTON2") else []

OPEN_MENU_BUTTON5 = environ.get('OPEN_MENU_BUTTON5', "")
KEYBOARD_BUTTON2 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON2").split(",")) if environ.get("KEYBOARD_BUTTON2") else []

OPEN_MENU_BUTTON5 = environ.get('OPEN_MENU_BUTTON5', "⚡ 𝖡𝖤𝖲𝖳 30 𝖳𝖠𝖬𝖨𝖫 𝖬𝖮𝖵𝖨𝖤𝖲 𝖨𝖭 2022 ⚡")
KEYBOARD_BUTTON5 = ["Gargi, Iravin Nizhal, Rocketry: The Nambi Effect, Veetla Vishesham, Nenjuku Needhi, Panni Kutty, Yaanai, Maamanithan, Vikram, Vaaitha, Don, Kathir, Manmatha Leelai, Selfie, Etharkkum Thunindhavan, Hey Sinamika, Valimai, FIR, Veeramae Vaagai Soodum, Sila Nerangalil Sila Manidhargal, Theal, Enna Solla Pogirai, Naai Sekar, Carbon, Nadhi, My Dear Bootham, Maayon, Vezham, Pattampoochi, Grandma"]

OPEN_MENU_BUTTON6 = environ.get('OPEN_MENU_BUTTON6', "⭐ 𝖳𝖮𝖯 50 𝖨𝖬𝖣𝖻 𝖱𝖠𝖳𝖨𝖭𝖦 𝖬𝖮𝖵𝖨𝖤𝖲 ⭐")
KEYBOARD_BUTTON6 = ["Nayakan", "Anbe Sivam", "Pariyerum Perumal", "Jai Bhim", "Soorarai Pottru", "Thevar Magan", "Kaithi", "96", "Visaaranai", "Thalapathi", "Asuran", "Sarpatta Parambarai", "Thani Oruvan", "Peranbu", "Vada Chennai", "Anniyan", "Raatchasan", "Sagara Sangamam", "Aaranya Kaandam", "Iruvar", "Kannathil Muthamittal", "Super Deluxe", "Aruvi", "Pudhu Pettai", "Kuruthipunal", "Mudhalvan", "Vikram", "Vikram Vedha", "Mahanadi", "Papanasam", "Mandela", "Michael Madana Kama Rajan", "Kadaisi Vivasayi", "Kaakkaa Muttai", "Soodhu Kavvum", "Dhuruvangal Pathinaaru", "Virumandi", "Jigarthanda", "Moondram Pirai", "Thillu Mullu", "Pithamagan", "Theeran Adhigaram Ondru", "Baasha", "Alaipayuthey", "Roja", "Apoorva Sagodharargal", "Kattradhu Thamizh", "Bombay", "Indian", "Padaiyappa"]

OPEN_MENU_BUTTON7 = environ.get('OPEN_MENU_BUTTON7', "🎥 𝖫𝖠𝖳𝖤𝖲𝖳 𝖳𝖠𝖬𝖨𝖫 𝖶𝖤𝖡 𝖲𝖤𝖱𝖨𝖤𝖲 🎥")
KEYBOARD_BUTTON7 = ["Stockholm Requiem (2018)", "The Sandman"]

OPEN_MENU_BUTTON8 = environ.get('OPEN_MENU_BUTTON8', "❤️ 𝖪𝖠𝖭𝖠𝖠 𝖪𝖠𝖠𝖭𝖴𝖬 𝖪𝖠𝖠𝖫𝖠𝖭𝖦𝖠𝖫 2 ❤️")
BIGGBOSS = ["BIGG BOSS (Tamil) S06 - EP 1", "BIGG BOSS (Tamil) S06 - EP 2", "BIGG BOSS (Tamil) S06 - EP 3", "BIGG BOSS (Tamil) S06 - EP 4", "BIGG BOSS (Tamil) S06 - EP 5", "BIGG BOSS (Tamil) S06 - EP 6", "BIGG BOSS (Tamil) S06 - EP 7", "BIGG BOSS (Tamil) S06 - EP 8", "BIGG BOSS (Tamil) S06 - EP 9", "BIGG BOSS (Tamil) S06 - EP 10", "BIGG BOSS (Tamil) S06 - EP 11", "BIGG BOSS (Tamil) S06 - EP 12", "BIGG BOSS (Tamil) S06 - EP 13", "BIGG BOSS (Tamil) S06 - EP 14", "BIGG BOSS (Tamil) S06 - EP 15", "BIGG BOSS (Tamil) S06 - EP 16", "BIGG BOSS (Tamil) S06 - EP 17", "BIGG BOSS (Tamil) S06 - EP 18", "BIGG BOSS (Tamil) S06 - EP 19", "BIGG BOSS (Tamil) S06 - EP 20", "BIGG BOSS (Tamil) S06 - EP 21", "BIGG BOSS (Tamil) S06 - EP 22", "BIGG BOSS (Tamil) S06 - EP 23", "BIGG BOSS (Tamil) S06 - EP 24", "BIGG BOSS (Tamil) S06 - EP 25", "BIGG BOSS (Tamil) S06 - EP 26", "BIGG BOSS (Tamil) S06 - EP 27", "BIGG BOSS (Tamil) S06 - EP 28", "BIGG BOSS (Tamil) S06 - EP 29", "BIGG BOSS (Tamil) S06 - EP 30", "BIGG BOSS (Tamil) S06 - EP 31", "BIGG BOSS (Tamil) S06 - EP 32", "BIGG BOSS (Tamil) S06 - EP 33", "BIGG BOSS (Tamil) S06 - EP 34", "BIGG BOSS (Tamil) S06 - EP 35", "BIGG BOSS (Tamil) S06 - EP 36", "BIGG BOSS (Tamil) S06 - EP 37"]

OPEN_MENU_BUTTON9 = environ.get('OPEN_MENU_BUTTON9', "⚠️ 𝖮𝖳𝖳 𝖳𝖱𝖤𝖭𝖣𝖨𝖭𝖦 ⚠️")
KEYBOARD_BUTTON9 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON9").split(",")) if environ.get("KEYBOARD_BUTTON9") else []

OPEN_MENU_BUTTON10 = environ.get('OPEN_MENU_BUTTON10', "📬 𝖱𝖤𝖰𝖴𝖤𝖲𝖳𝖤𝖣 𝖬𝖮𝖵𝖨𝖤𝖲 📬")
KEYBOARD_BUTTON10 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON10").split(",")) if environ.get("KEYBOARD_BUTTON10") else []

OPEN_MENU_BUTTON11 = environ.get('OPEN_MENU_BUTTON11', "📺 𝖧𝖮𝖳𝖲𝖳𝖠𝖱 📺")
KEYBOARD_BUTTON11 = ["Vikram, Theal, Bhuj, Netrikann, Baby, Teddy, Sultan , Eeswaran, Geetha Govindam, Dear Comrade, Bhoomi, Paramapadham Vilayattu, Sarileru Neekevvaru, Ispade Rajavum Idhaya Raniyum, Arjun Reddy, Bahubali 2, Mookuthi Amman, Saamy 2, Vada Chennai, Kaithi, Maari 2, Mister, Kolaigaran, Kali, Chekka Chivantha Vaanam, Adanga Maru, Vishwaroopam, Raja Rani, Nanban, Ragasiyam, OK Kanmani, Indri Netru Naalai, Majili, Hyper, DJ, MS Dhoni The Untold Story, Nani's Gang Leader, Pulimurugan, Venky Mama, Thuppaki, Bharath Ennum Naan, Maari, Velaikkaran, 118, Gentleman Sathya, Manathil Nindraval, Siruthai, 10 Endrathukulla, Sangathailavan, Banumathi, Ethir Neechal, Ramleela, Naan Local, Magadheera, Madras, Jigarthanda, Selvi, Vanga Mappilai Vanga, Nimir, Maan Karate, Vacha Kuri Thappathu, Middle Class Ambala, Sangili Bungili Kadhava Thorae, Veerabali, Ellam Eli Mayam, Nenjamellam Pala Vannam, Chennai 600028, Silukkuvarupatti Singam, Meagamann, Krishnarjuna Yudham, Anbudan Appavukku, Thiruppumunai, En Frienda Pola Yaaru Machan, Raja Rajathan, Vasuvum Saravananum Onna Padichavanga, Hello, Thoonga vanam, Kanne Kalaimaane, Manam, Devadas, Sagodharargal , Loafer, Aadu Puli, Mynaa, Kalavani, Kathai Thiraikathai Vasanam Iyakkam, Pisasu, Nedunchalai, Marina, Veppam, Pizza, Onaayum Aattukkuttiyum, Moodar Koodam, Saivam, Kadal, Kadhalil Sodhappuvadhu Yeppadi, Rangoon, Saravanan Irukka Bayamaen, Panjumittai, Ivan Avan, Jaanu, Seedan, Tamizhuku En Ondrai Azhuthavum, Sathuranga Vettai, Velainu Vandhutta Vellaikaaran, Bullet Raja, Chandi Veeran, Jeeva, Mundasupatti, Nee Naan Naam"]

OPEN_MENU_BUTTON12 = environ.get('OPEN_MENU_BUTTON12', "📺 𝖹𝖤𝖤 5 📺")
KEYBOARD_BUTTON12 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON12").split(",")) if environ.get("KEYBOARD_BUTTON12") else []

OPEN_MENU_BUTTON13 = environ.get('OPEN_MENU_BUTTON13', "📺 𝖲𝖮𝖭𝖸 𝖫𝖨𝖵 📺")
KEYBOARD_BUTTON13 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON13").split(",")) if environ.get("KEYBOARD_BUTTON13") else []

OPEN_MENU_BUTTON14 = environ.get('OPEN_MENU_BUTTON14', "📺 𝖵𝖮𝖮𝖳 📺")
KEYBOARD_BUTTON14 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON14").split(",")) if environ.get("KEYBOARD_BUTTON14") else []

OPEN_MENU_BUTTON15 = environ.get('OPEN_MENU_BUTTON15', "📺 𝖠𝖬𝖠𝖹𝖮𝖭 𝖯𝖱𝖨𝖬𝖤 📺")
KEYBOARD_BUTTON15 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON15").split(",")) if environ.get("KEYBOARD_BUTTON15") else []

OPEN_MENU_BUTTON16 = environ.get('OPEN_MENU_BUTTON16', "📺 𝖭𝖤𝖳𝖥𝖫𝖨𝖷 📺")
KEYBOARD_BUTTON16 = ["Aval, Anjaan, Aelay, Anaamika, Andhagaaram, Asuraguru, Baahubali: The Beginning, Bahubali: The Conclusion, Game Over, Goli Soda 2, Guru, Gundu, Jagat, Kannum Kannum Kollaiyadithal, Kalakalappu, K.D. Engira Karuppudurai, Kolaiyuthir Kaalam, Lens, Mandela, Merku Thodarchi Malai, Mehandi Circus, Miss India, Mersal, MR. Chandramouli, Naan Sivappu Manithan, Nibunan, Oh! Baby, Orange Mittai, Otha Seruppu Size 7, Pandigai, Petta, Power Paandi Pa Paandi, Psycho, RK Nagar, Sarkar, Sarvam Thaala Mayam, Settai, Seven, Saaho, Sigaram Thodu, Sethum Aayiram Pon , Spyder, Sometimes, Super Deluxe Movie, Taramani, Thaandavam, Theeya Velai Seiyyanum Kumaru, Uriyadi 2, Vanjagar Ulagam, Visaranai"]

OPEN_MENU_BUTTON17 = environ.get('OPEN_MENU_BUTTON17', "🎬 𝗔𝗖𝗧𝗥𝗘𝗦𝗦 𝗙𝗜𝗟𝗠𝗢𝗚𝗥𝗔𝗣𝗛𝗬 🎬")
KEYBOARD_BUTTON17 = list(i.strip() for i in environ.get("KEYBOARD_BUTTON17").split(",")) if environ.get("KEYBOARD_BUTTON17") else []

OPEN_MENU_BUTTON18 = "Vijay"
KEYBOARD_BUTTON18 = ["Naalaiya Theerpu", "Sendhoorapandi", "Rasigan", "Deva", "Rajavin Parvaiyile", "Vishnu", "Chandralekha", "Coimbatore Mappillai", "Poove Unakkaga", "Vasantha Vaasal", "Maanbumigu Maanavan", "Selva", "Kaalamellam Kaathiruppen", "Love Today", "Once More", "Nerrukku Ner", "Kadhalukku Mariyadhai", "Ninaithen Vandhai", "Priyamudan", "Nilaave Vaa", "Thulladha Manamum Thullum", "Endrendrum Kadhal", "Nenjinile", "Minsara Kanna", "Kannukkul Nilavu", "Kushi", "Priyamaanavale	", "Friends", "Badri", "Shahjahan	", "Thamizhan", "Youth	", "Bagavathi", "Vaseegara", "Pudhiya Geethai", "Thirumalai", "Udhaya", "Ghilli", "Madhuri", "Thirupaachi", "Sachein", "Sivakasi", "Aathi", "Pokkiri", "Azhagiya", "Tamil Magan", "Kuruvi", "Villu", "Vettaikaaran", "Sura", "Kaavalan", "Velayudham", "Nanban", "Thuppakki", "Thalaivaa", "Jilla", "Kaththi", "Puli", "Theri	", "Bairavaa", "Mersal", "Sarkar	", "Bigil 2019", "Master (2021)", "Beast (2022)"]

OPEN_MENU_BUTTON19 = "Kamal Hasan"
KEYBOARD_BUTTON19 = ["Kalathur Kannamma", "Paarthaal Pasi Theerum", "Paadha Kaanikkai", "Kannum Karalum (Missing)", "Vanambadi", "Anandha Jodhi", "Maanavan", "Annai Velankanni", "Kurathi Magan", "Arangetram", "Sollathaan Ninaikkiren", "Paruva Kaalam", "Gumasthavin Magal", "Naan Avanillai", "Kanyakumari", "Anbu Thangai", "Vishnu Vijayam", "Aval Oru Thodar Kathai", "Panathukkaga", "Cinema Paithiyam", "Pattampoochi", "Aayirathil Oruthi", "Then Sindhudhe Vaanam", "Melnaattu Marumagal", "Thangathile Vairam", "Pattikkaattu Raja", "Njan Ninne Premikkunnu", "Maalai Sooda Vaa", "Apoorva Raagangal", "Thiruvonam", "Mattoru Seetha", "Raasaleela", "Andharangam", "Agni Pushpam", "Appooppan", "Samasya", "Manmadha Leelai", "Anthuleni Katha", "Swimming Pool", "Aruthu", "Satyam", "Oru Oodhappu Kan Simittugiradhu", "Unarchigal", "Kuttavum Shikshayum", "Kumaara Vijayam", "Idhaya Malar", "Ponni", "Nee Ente Lahari", "Moondru Mudichu", "Mogam Muppadhu Varusham", "Lalitha", "Uyarndhavargal", "Siva Thandavum", "Aasheervaadam", "Avargal", "Madhura Swapanam", "Aaina", "Sreedevi", "Unnai Suttrum Ulagam", "Kabita", "Ashtamangalyam", "Nirakudam", "Ormakal Marikkumo", "16 Vayathinile", "Aadu Puli Attam", "Aanandham Paramaanandham", "Naam Pirandha Mann", "Kokila", "Satyavan Savithri", "Aadhya Paadam", "Madanolsavam", "Kaathirunna Nimisham", "Anumodhanam", "Avalude Ravukal", "Nizhal Nijamagiradhu", "Aval Viswasthayayirunnu", "Maro Charitra", "Ilamai Oonjal Aadukirathu", "Amara Prema", "Sattam En Kaiyil", "Padakuthira", "Vayasu Pilichindi", "Vayanadan Thamban", "Sakka Podu Podu Raja", "Sigappu Rojakkal", "Manidharil Ithanai Nirangala", "Aval Appadithan", "Thappida Thala", "Thappu Thalangal", "Yaetta", "Sommokadidi Sokokadidi", "Sigappukkal Mookkuthi", "Neeya?", "Allaudinaum Arputha Vilakkum", "Thaayillamal Naan Illai", "Ninaithale Inikkum", "Andamaina Anubhavam", "Idi Katha Kaadu", "Kalyanaraman", "Nool Veli", "Guppedu Manasu", "Mangala Vaathiyam", "Neela Malargal", "Azhiyatha Kolangal", "Pasi", "Ullasa Paravaigal", "Natchathiram", "Guru", "Varumayin Niram Sivappu", "Maria", "My Darling", "Saranam Ayyappa", "Aakali Rajyam", "Meendum Kokila", "Prema Pitchi ", "Ram Lakshman", "Raja Paarvai", "Thillu Mullu", "Kadal Meengal", "Ek Duuje Ke Liye", "Savaal", "Sankarlal", "Amavasya Chandrudu", "Tik Tik Tik", "Ellam Inba Mayyam", "Vazhvey Maayam", "Andagaadu", "Anthiveyilile Ponnu", "Neethi Devan Mayakkam", "Moondram Pirai", "Maattuvin Chattangale", "Simla Special", "Sanam Teri Kasam", "Sakalakala Vallavan", "Ezham Rathri", "Rani Theni", "Yeh To Kamaal Ho Gaya", "Pagadai Panirendu", "Agni Sakshi", "Zara Si Zindagi", "Uruvangal Maralam", "Sattam", "Sagara Sangamam", "Sadma", "Poikkal Kudhirai", "Benkiyalli Aralida Hoovu", "Thoongathey Thambi Thoongathey", "Yeh Desh", "Ek Nai Paheli", "Yaadgar", "Raaj Tilak", "Enakkul Oruvan", "Karishmaa", "Oru Kaidhiyin Diary", "Kaakki Sattai", "Andha Oru Nimidam", "Uyarndha Ullam", "Saagar", "Geraftaar", "Mangamma Sapatham", "Japanil Kalyanaraman", "Dekha Pyar Tumhara", "Swati Mutyam", "Naanum Oru Thozhilali", "Vikram", "Manakanakku", "Oka Radha Iddaru Krishnulu", "Punnagai Mannan", "Kadhal Parisu", "Vrutham", "Kadamai Kanniyam Kattupaadu", "Per Sollum Pillai", "Nayakan", "Pushpaka Vimana", "Sathya", "Daisy", "Soora Samhaaram", "Unnal Mudiyum Thambi", "Apoorva Sagodharargal", "Chanakyan", "Vetri Vizha", "Indrudu Chandrudu", "Michael Madana Kama Rajan", "Gunaa", "Singaravelan", "Thevar Magan", "Maharasan", "Kalaignan", "Mahanadhi", "Magalir Mattum", "Nammavar", "Sathi Leelavathi", "Subha Sankalpam", "Kuruthipunal", "Indian", "Avvai Shanmughi", "Chachi 420", "Kaathala Kaathala", "Hey Ram", "Thenali", "Aalavandhan", "Paarthale Paravasam", "Pammal K. Sambandam ", "Panchatanthiram", "Anbe Sivam", "Nala Damayanthi", "Virumaandi", "Vasool Raja MBBS", "Mumbai Xpress", "Rama Shama Bhama", "Vettaiyaadu Vilaiyaadu", "Dasavathaaram", "Unnaipol Oruvan", "Eenadu (Telugu of 212)", "Four Friends", "Manmadan Ambu", "Vishwaroopam", "Uttama Villain", "Papanasam", "Thoongaa Vanam", "Meen Kuzhambum Mann Paanaiyum", "Vishwaroopam 2", "Vikram"]

OPEN_MENU_BUTTON20 = "Rajinikanth"
KEYBOARD_BUTTON20 = ["Soon"]

OPEN_MENU_BUTTON21 = "Ajith"
KEYBOARD_BUTTON21 = ["Amaravathi", "Prema Pusthakam (Telugu)", "Rajavin Parvaiyile", "Paasamalargal", "Pavithra", "Aasai", "Vaanmathi", "Minor Mappillai", "Kalluri Vaasal", "Kadhal Kottai", "Nesam", "Raasi", "Pagaivan", "Ullasam", "Rettai Jadai Vayasu", "Kadhal Mannan", "Aval Varuvala", "Anantha Poongatre", "Amarkalam", "Nee Varuvai Ena", "Unnidathil Ennai Koduthen", "Uyirodu Uyiraga", "Mugavaree", "Kandukonden Kandukondain", "Unnai Kodu Ennai Tharuven", "Citizen", "Dheena", "Poovellam Un Vaasam", "Asoka", "Thodarum", "Unnai Thedi", "Vaalee", "Red", "Ennai Thalatta Varuvala", "Raja", "Anjaneya", "Villain", "Jana", "Attagasam", "Ji", "Paramasivan", "Varalaru", "Thirupathi", "Kireedam", "Billa", "Aalwar", "Aaegan", "Asal", "Mankatha", "English Vinglish", "Yennai Arindhaal", "Arambam", "Veeram", "Vedalam", "Vivegam", "Billa 2", "Viswasam (2019)", "Nerkonda Paarvai", "Valimai"]

OPEN_MENU_BUTTON22 = "Dhanush"
KEYBOARD_BUTTON22 = ["Thulluvadho Ilamai 2002", "Kadhal Kondein", "Pudhukottaiyilirundhu Saravanan", "Sullan", "Thiruda Thirudi", "Devathaiyai Kanden", "Adhu Oru Kana Kaalam", "Dreams", "Thiruvilayadal Arambam", "Parattai Engira Azhagu Sundaram", "Polladhavan", "Yaaradi Nee Mohini", "Padikathavan", "Mappillai", "Seedan", "Kutty", "Aadukalam", "Uthama Puthiran", "Venghai", "Mayakkam Enna", "3", "Ambikapathy", "Maryan", "Naiyaandi", "Velaiilla Pattadhari 2", "Shamitabh", "Anegan", "Maari", "Thanga Magan", "Vai Raja Vai", "Thodari", "Kodi", "Pa Paandi", "Velaiilla Pattadhari 2", "Enai Nokki Paayum Thotta", "Vada Chennai", "Maari 2", "Asuran", "Pattas", "Jagame Thanthiram", "Atrangi Re", "Karnan", "The Gray Man"]

OPEN_MENU_BUTTON23 = "Suriya"
KEYBOARD_BUTTON23 = ["Nerukku Ner 1997", "Kaadhale Nimmadhi 1998", "Sandhippoma 1998", "Periyanna 1999", "Poovellaam Kettuppaar 1999", "Uyirile Kalanthathu 2000", "Friends 2001", "Nandha 2001", "Mounam Pesiyadhe 2002", "Unnai Ninaithu 2002", "Shree 2002", "Kaakha..Kaakha: The Police 2003", "Pithamagan 2003", "Ayitha Ezhuthu 2004", "Peralagan 2004", "Mayaavi 2005", "Ghajini 2005", "Aaru 2005", "June R 2005", "Sillunu Oru Kaadhal 2006", "Vel 2007", "Kuselan 2008", "Vaaranam Aayiram 2008", "Ayan 2009", "Aadhavan 2009", "Singam 2010", "Rakhta Charitra 2 2010", "Manmadhan Ambu 2010", "Ko 2011", "Avan Ivan 2011", "7 Aum Arivu 2011", "Maattrraan 2012", "Chennaiyil Oru Naal 2013", "Singam 2 2013", "Ninaithathu Yaaro 2014", "Anjaan 2014", "Massu Engira Masilamani 2015", "Pasanga 2 2015", "24 2016", "Singam 3 2017", "The Ghazi Attack 2017", "Kootathil Oruthan 2017", "Thaanaa Serndha Koottam 2018", "Kadaikutty Singam 2018", "NGK 2019", "Kaappaan 2019", "Soorarai Pottru 2020", "Navarasa 2021", "Jai Bhim 2021", "Etharkkum Thunindhavan"]

OPEN_MENU_BUTTON24 = "Chiyaan Vikram"
KEYBOARD_BUTTON24 = ["En Kadhal Kanmani", "Thanthu Vitten Ennai", "Pudhiya Mannargal", "Ullaasam", "Meera", "Vinnukum Mannukum", "Dhill", "Kasi", "Kaaval Geetham", "Sethu", "Gemini", "Samurai", "King", "Dhool", "Pithamagan", "Arul", "Kadhal Sadugudu", "Sammy", "Anniyan", "Majaa", "Raavanan", "Deiva Thirumagal", "Bheema", "Kanthaswamy", "David", "Rajapattai", "Thandavam", "I", "10 Endrathukulla", "Iru Mugan 2016", "Sketch 2018", "Saamy 2 2018", "Kadaram Kondan 2019", "Mahaan"]

OPEN_MENU_BUTTON25 = "Vijay Sethupathi"
KEYBOARD_BUTTON25 = ["Ghilli 2004", "M. Kumaran S/O Mahalakshmi 2004", "Dishyum 2006", "Pudhu Pettai 2006", "Lee 2007", "Anjathe 2008", "Vennila Kabadi Kuzhu 2009", "Naan Mahaan Alla 2010", "Bale Pandiya 2010", "Thenmerku Paruvakaatru 2010", "Sundarapandian 2012", "Pizza 2012", "Naduvula Konjam Pakkatha Kaanom 2012", "Soodhu Kavvum 2013", "Idharkuthane Aasaipattai Balakumara 2013", "Rummy 2014", "Pannaiyarum Padminiyum 2014", "Kathai Thiraikathai Vasanam Iyakkam 2014", "Thirudan Police 2014", "Vanmam 2014", "Purampokku Engira Podhuvudamai 2015", "Orange Mittai 2015", "Naanum Rowdy Thaan 2015", "Sethupathi 2016", "Kadhalum Kadandhu Pogum 2016", "Iraivi 2016", "Dharma Durai 2016", "Aandavan Kattalai 2016", "Rekka 2016", "Kavan 2017", "Vikram Vedha 2017", "Kootathil Oruthan 2017", "Puriyaatha Puthir 2017", "Kathanayagan 2017", "Karuppan 2017", "Oru Nalla Naal Paathu Solren 2018", "Traffic Ramasamy 2018", "Junga 2018", "Imaikkaa Nodigal 2018", "Chekka Chivantha Vaanam 2018", "96 2018", "Seethakaathi 2018", "Petta 2019", "Super Deluxe 2019", "Sindhubaadh 2019", "Sye Raa Narasimha Reddy 2019", "Sangathamizhan 2019", "Action 2019", "Oh My Kadavule 2020", "Ka Pae Ranasingam 2020", "Dhira 2020", "Master 2021", "Uppena 2021", "Kutty Story 2021", "Navarasa 2021", "Laabam 2021", "Sangathamilan", "Anabelle Sethupathi", "Mugizh 2021", "Kaathuvaakula Rendu Kaadhal", "Vikram 2022"]

NORMAL_MENU_BUTTON = environ.get('NORMAL_MENU_BUTTON', "")
NORMAL_KEYBOARD_BUTTON = list(i.strip() for i in environ.get("NORMAL_KEYBOARD_BUTTON").split(",")) if environ.get("NORMAL_KEYBOARD_BUTTON") else []

OPEN_MENU_BUTTON26 = "Siva Karthikeyan"
KEYBOARD_BUTTON26 = ["Marina", "3 Moonu", "Manam Kothi Paravai", "Kedi Billa Killadi Ranga", "Ethir Neechal", "Varuthapadatha Valibar Sangam", "Maan Karate", "Kaaki Sattai", "Rajni Murugan", "Remo", "Velaikkaran", "Seemaraja", "Kanaa", "Hero", "Namma Veettu Pillai", "Doctor (2021)", "DON (2022)"]

OPEN_MENU_BUTTON27 = "Karthi"
KEYBOARD_BUTTON27 = ["Paruthiveeran 2007", "Ayirathil Oruvan 2010", "Paiyaa 2010", "Naan Mahan Alla 2010", "Siruthai 2011", "Madras 2014", "Saguni 2012", "Alex Pandian 2013", "All in All Azhagu Raja 2013", "Biriyani 2013", "Komban 2015", "Thozha 2016", "Kaashmora 2016", "Kaatru Veliyidai 2017", "Theeran 2017", "Kadaikutty Singam 2018", "Dev 2019", "Thambi 2019", "Kaithi 2019", "Sulthan 2021"]

OPEN_MENU_BUTTON28 = "Simbu"
KEYBOARD_BUTTON28 = ["Mythili Ennai Kaathali", "Oru Thayin Sabhatham", "Uravai Kaatha kili", "En Thangai Kalyani", "Kadhal Azhivathillai", "Dum", "Kovil", "Alai", "Kuththu", "Manmadhan", "Thotti Jaya", "Vallavan", "Saravana", "Kaalai", "Silambattam", "Vinnaithaandi Varuvaayaa", "Vaanam", "Osthe", "Inga Enna Solluthu", "Podaa Podi", "Vaalu", "Idhu Namma Aalu", "Achcham Yenbadhu", "Anbanavan Asaradhavan", "Chekka Chivantha Vaanam", "90ML", "Vantha Rajavathaan Varuven", "Kaatrin Mozhi", "Eeswaran", "Maanaadu"]

OPEN_MENU_BUTTON29 = "Jeeva"
KEYBOARD_BUTTON29 = ["Aasai Aasaiyai 2003", "Thithikudhe 2003", "Raam 2005", "Dishyum 2006", "Keerthi Chakra 2006", "E 2006", "Pori 2007", "Kattradhu Thamizh 2007", "Thenavattu 2008", "Siva Manasula Sakthi 2009", "Kacheri Arambam 2010", "Boss Engira Baskaran 2010", "Singam Puli 2011", "Ko 2011", "Rowthiram 2011", "Vanthaan Vendraan 2011", "Nanban 2012", "Mugamoodi 2012", "Yeto Vellipoyindhi Manasu 2012", "Neethaane En Ponvasantham 2012", "David 2013", "North 24 Kaatham 2013", "Endrendrum Punnagai 2013", "Jilla 2014", "Yaan 2014", "Size Zero 2015", "Pokkiri Raja 2016", "Thirunaal 2016", "Kadavul Irukaan Kumaru 2016", "Kavalai Vendam 2016", "Sangili Bungili Kadhava Thorae 2017", "Kalakalappu 2 2018", "Tamizh Padam 2.0 2018", "Kee 2019", "Gorilla 2019", "Seeru 2020", "Gypsy 2020", "Kalathil Sandhippom"]

OPEN_MENU_BUTTON30 = "Atharvaa"
KEYBOARD_BUTTON30 = []

OPEN_MENU_BUTTON31 = "Jayam Ravi"
KEYBOARD_BUTTON31 = ["Jayam 2003", "M. Kumaran Son of Mahalakshmi 2004", "Daas 2005", "Mazhai 2005", "Idhaya Thirudan 2005", "Unnakum Ennakum 2006", "Deepavali 2007", "Santhosh Subramaniyam 2008", "Dhaam Dhoom 2008", "Peraanmai 2009", "Thillalangadi 2010", "Ko 2011", "Engeyum Kadhal 2011", "Aadhi Bhagavan 2013", "Ninaithathu Yaaro 2014", "Nimirndhu Nil 2014", "Janda Pai Kapiraju 2015", "Romeo Juliet 2015", "Sakalakala Vallavan 2015", "Thani Oruvan 2015", "Boologam 2015", "Miruthan 2016", "Bogan 2017", "Vanamagan 2017", "Tik Tik Tik 2018", "Adanga Maru 2018", "Comali 2019", "Bhoomi 2021"]

OPEN_MENU_BUTTON32 = "Vijay Antony"
KEYBOARD_BUTTON32 = ["Naan 2012", "Salim 2014", "India Pakistan 2015", "Pichaikkaran 2016", "Nambiar 2016", "Saithan 2016", "Yaman 2017", "Mupparimanam 2017", "Annadurai 2017", "Kaali 2018", "Traffic Ramasamy 2018", "Thimiru Pudichavan 2018", "Kolaigaran 2019", "Kodiyil Oruvan 2021"]

OPEN_MENU_BUTTON33 = "Allu Arjun"
KEYBOARD_BUTTON33 = ["Gangotri 2003", "Arya 2004", "Bunny 2005", "Happy 2006", "Desamuduru 2007", "Shankardada Zindabad 2007", "Parugu 2008", "Arya 2009", "Varudu 2010", "Velam 2010", "Badrinath 2011", "Julayi 2012", "Iddarammayilatho 2013", "Yevadu 2014", "Race Gurram 2014", "S/O Satyamurthy 2015", "Rudhramadevi 2015", "Sarrainodu 2016", "Duvvada Jagannadham 2017", "Naa Peru Surya Naa Illu India 2018", "Ala Vaikunthapurramuloo 2020", "Pushpa: The Rise - Part 1 2021"]

OPEN_MENU_BUTTON34 = "Santhanam"
KEYBOARD_BUTTON34 = ["Kadhal Azhivathillai 2002", "Manmadhan 2004", "Sachien 2005", "Oru Kalluriyin Kathai 2005", "February 14 2005", "Sillunu Oru Kaadhal 2006", "Vallavan 2006", "Rendu 2006", "Parattai Engira Azhagu Sundaram 2007", "Kireedam 2007", "Azhagiya Tamizh Magan 2007", "Billa 2007", "Santhosh Subramaniyam 2008", "Arai Enn 305-il Kadavul 2008", "Kuselan 2008", "Silambattam 2008", "Siva Manasula Sakthi 2009", "Maasilamani 2009", "Kanden Kadhalai 2009", "Theeradha Vilaiyattu Pillai 2010", "Thillalangadi 2010", "Boss Engira Baskaran 2010", "Enthiran 2010", "Chikku Bukku 2010", "Siruthai 2011", "Singam Puli 2011", "Kandaen 2011", "Deiva Thirumagal 2011", "Vanthaan Vendraan 2011", "Velayudham 2011", "Osthi 2011", "Muppozhudhum Un Karpanaigal 2012", "Oru Kal Oru Kannadi 2012", "Leelai 2012", "Kalakalappu 2012", "Ishtam 2012", "Saguni 2012", "Eega 2012", "Thaandavam 2012", "Neethaane En Ponvasantham 2012", "Kanna Laddu Thinna Aasaiya 2013", "Alex Pandian 2013", "Settai 2013", "Singam 2 2013", "Pattathu Yaanai 2013", "Thalaivaa 2013", "Raja Rani 2013", "Ya Ya 2013", "Vanakkam Chennai 2013", "All in All Azhagu Raja 2013", "Endrendrum Punnagai 2013", "Veeram 2014", "Salala Mobiles 2014", "Inga Enna Solluthu 2014", "Idhu Kathirvelan Kadhal 2014", "Thalaivan 2014", "Vallavanukku Pullum Aayudham 2014", "Aranmanai 2014", "Lingaa 2014", "I 2015", "Aambala 2015", "Nannbenda 2015", "Vasuvum Saravananum Onna Padichavanga 2015", "Vaalu 2015", "Dhilluku Dhuddu 2016", "Nambiar 2016", "Sakka Podu Podu Raja 2017", "Dhilluku Dhuddu 2 2019", "A1 2019", "Dagaalty 2020", "Biscoth 2020", "Paris Jeyaraj 2021", "Dikkiloona 2021", "Sabhaapathy 2021"]

OPEN_MENU_BUTTON35 = "Yogi Babu"
KEYBOARD_BUTTON35 = ["Thulli Thirintha Kaalam 1998", "Pandavar Bhoomi 2001", "Iyarkai 2003", "Jananam 2004", "Maanja Velu 2010", "Thadaiyara Thaakka 2012", "Yennai Arindhaal 2015", "Bruce Lee - The Fighter 2015", "Kuttram 23 2017", "Chekka Chivantha Vaanam 2018", "Thadam 2019", "Mafia: Chapter 1 2020", "Yanai 2022"]

OPEN_MENU_BUTTON36 = "Arun Vijay"
KEYBOARD_BUTTON36 = ["Thulli Thirintha Kaalam 1998", "Pandavar Bhoomi 2001", "Iyarkai 2003", "Jananam 2004", "Maanja Velu 2010", "Thadaiyara Thaakka 2012", "Yennai Arindhaal 2015", "Bruce Lee - The Fighter 2015", "Kuttram 23 2017", "Chekka Chivantha Vaanam 2018", "Thadam 2019", "Mafia: Chapter 1 2020", "Yanai 2022"]

OPEN_MENU_BUTTON37 = "SJ Suryah"
KEYBOARD_BUTTON37 = ["Aasai 1995", "Kushi 2000", "New 2004", "Ah Aah: Anbe Aaruyire 2005", "Kalvanin Kadhali 2005", "Thirumagan 2007", "Vyabari 2007", "Nanban 2012", "Pizza II: Villa 2013", "Isai 2015", "Vai Raja Vai 2015", "Yatchan 2015", "144 2015", "Iraivi 2016", "Remo 2016", "Spyder 2017", "Mersal 2017", "Monster 2019", "Nenjam Marappathillai 2021", "Maanaadu 2021"]

OPEN_MENU_BUTTON38 = "Dhruv Vikram"
KEYBOARD_BUTTON38 = ["Adithya Varma 2019", "Varma 2020", "Mahaan 2022"]

OPEN_MENU_BUTTON39 = "Vikram Prabhu"
KEYBOARD_BUTTON39 = ["Kumki 2012", "Ivan Veramaathiri 2013", "Arima Nambi 2014", "Sigaram Thodu 2014", "Vellaikaara Durai 2014", "Idhu Enna Maayam 2015", "Wagah 2016", "Veera Sivaji 2016", "Sathriyan 2017", "Neruppu Da 2017", "Pakka 2018", "60 Vayadu Maaniram 2018", "Thuppakki Munai 2018", "Vaanam Kottattum 2020", "Asura Guru 2020", "Pulikkuthi Pandi 2021"]

OPEN_MENU_BUTTON40 = "Arulnithi"
KEYBOARD_BUTTON40 = ["D Block", "Vamsam 2010", "Udhayan 2011", "Mouna Guru 2011", "Thagaraaru 2013", "Oru Kanniyum Moonu Kalavaanikalum 2014", "Demonte Colony 2015", "Naalu Policeum Nalla Irundha Oorum 2015", "Aaradhu Sinam 2016", "Brindavanam 2017", "Iravukku Aayiram Kangal 2018", "K-13 2019", "Kalathil Sandhippom 2021"]

OPEN_MENU_BUTTON41 = "Shiva"
KEYBOARD_BUTTON41 = ["Chennai 600028 2007", "Saroja 2008", "Thamizh Padam 2010", "Va: Quarter Cutting 2010", "Ko 2011", "Kalakalappu 2012", "Thillu Mullu 2013", "Ya Ya 2013", "aVanakkam Chennai 2013", "Masala Padam 2015", "144 2015", "Adra Machan Visilu 2016", "Chennai 600028 II: Second Innings 2016", "Kalakalappu 2 2018", "Tamizh Padam 2.0 2018", "LOL: Enga Siri Paappom 2021"]

OPEN_MENU_BUTTON42 = "Madhavan"
KEYBOARD_BUTTON42 = ["Alaipayuthey 2000", "Minnale 2001", "Rehnaa Hai Terre Dil Mein 2001", "Paarthale Paravasam 2001", "Dum Dum Dum 2001", "Kannathil Muthamittal 2002", "Run 2002", "Anbe Sivam 2003", "Jay Jay 2003", "Laysa Laysa 2003", "Nala Damayanthi 2003", "Priyamana Thozhi 2003", "Aethiree 2004", "Ayitha Ezhuthu 2004", "Priyasakhi 2005", "Thambi 2005", "Rang De Basanti 2006", "Rendu 2006", "Aarya 2007", "Guru 2007", "13B: Fear Has a New Address 2009", "3 Idiots 2009", "Om Shanti 2010", "Teen Patti 2010", "Manmadhan Ambu 2010", "Tanu Weds Manu 2011", "Vettai 2012", "Tanu Weds Manu Returns 2015", "Saala Khadoos 2016", "Magalir Mattum 2017", "Vikram Vedha 2017", "Nishabdham", "Maara", "Decoupled", "Rocketry The Nambi Effect (2022)"]
