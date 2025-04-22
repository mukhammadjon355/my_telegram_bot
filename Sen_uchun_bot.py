import time
import random
import telebot
from datetime import datetime, timedelta
from telebot import types

# Telegram bot token va chat ID
API_TOKEN = '8104233817:AAEeDts-GUirezF3mb7aP35CPdTihqvSI-o'
CHAT_ID = '7611420735'
bot = telebot.TeleBot(API_TOKEN)

# Visol kuni
target_date = datetime(2025, 11, 17)

# Kontentlar
iliq_sozlar = [
    "Sen juda go'zalsan.",
    "Sen mening baxtim.",
    "Men seni sevaman.",
    "Sen har doim meni quvontirasan.",
    "Sening ko'zlaring dunyoni yoritadi.",
    "Sen bilan bo'lgan har daqiqa baxtdir.",
    "Sening borlig'ing hayotimga rang bag'ishlaydi.",
    "Har tong seni o'ylab uyg'onaman.",
    "Har kunim sen bilan go'zal.",
    "Yuragim faqat sen uchun uradi.",
    "Sening ko'zlaringning yarmi dunyo.",
    "Sen bilan bo'lgan har bir daqiqa — baxt.",
    "Sen nafaqat tashqi go'zalsan, balki ichki go'zalliging ham ajoyib.",
    "Dunyo sening atrofingda aylanadi.",
    "Sening tabassuming barcha muammolarni unuttiradi.",
    "Sen bilan dunyo yanada yorqinroq.",
    "Har bir kulginga mehrimni yo'llayman.",
    "Sen bilan birga, dunyo yorqin.",
    "Har kuni sen bilan, har kunim yangi baxtga to'ladi.",
    "Har bir qadam sen bilan yurish — hayotimning eng yaxshi qismidir.",
    "Sen mening eng yaxshi, eng yaqin do'stim."
]

topshiriqlar = [
    "Bugun tabassum qildingmi?",
    "Oynaga qarab qanchalik go'zal ekaningni ko'rganmisan?",
    "Bugun qalbingni iliqlikka to'ldir.",
    "Bugun o'zingni sev.",
    "Bugun ijobiylikni boshqalar bilan bo'lish.",
    "Bugun kichik bir orzuni yozib qo'y.",
    "Sen tabassum qilganingda, butun olam chiroyli bo'ladi.",
    "Har kuningda minnatdor bo‘l.",
    "Hayotingda kichik baxtlarni ko‘rishni unutma.",
    "Biror kishiga mehr ko‘rsat, hatto kichkina bir so‘z bilan.",
    "Unutmadingmi Hamma narsa niyatdan va orzudan boshlanishini.",
    "Orzu qilishdan toxtab qolma Gozalim.",
    "Muxammadjonga Sevishingni ayt.",
    "Oynaga qarab Naqadar G'zal ekaningni ayt.",
    "Muxammadjon sendan Xabar kutayotgandur balki.",
    "Nima bo'lsa ham gap qaytarma.",
    "Arab tilida hech bo'lmasa bronta harf organ.",
    "Dunyo seni atrofingda aylansin.",
]

sherlar = [
    "Senga atalgan bu yurak, bir umr sen bilan,\nSen bo‘lmasang, hayotim bo‘lar puch, begona bilan.",
    "Yulduzlar ostida seni o‘ylab yotdim,\nTun jim, yuragim esa senga to‘ldi, sevgilim.",
    "Go‘zallikning timsoli sen, so‘z yetmaydi ta’rifga,\nKo‘zlaringda yashirin bir olam, yuragimni olib ketgan dunyoga.",
    "Sen kelgan kunimdan boshlab,\nDunyo nurli, hayotim baxtli.",
    "Senga yozilgan bu satrlar,\nYuragimdagi cheksiz mehrlar.",
    "Yulduzlar yorqin, kechayu kunduz,\nSen bilan men, baxtga yetar edik.",
    "Hayot yo'llari uzun, shirin,\nSen bilan borishim, hech qachon yolg'iz.",
    "Seni sevaman, seni his qilaman,\nHar safar ko'rganimda, yuragimni titrataman.",
    "Qo'lni uzat, sevgilim, tutib yuramiz,\nBizni hech narsa ajratolmaydi, sevinch bilan yo'limiz.",
    "Yillardan so'ng ham, sevgimiz kuchli,\nSen bilan har bir kunim o'zgacha, ajoyib."
]

hikoyalar = [
    "Bir kun Muxabbatxon tongda uyg‘ondi. Har tongda u yuragini iliq so‘zlar bilan to‘ldirib, hayotga mehr bilan qarardi.",
    "Bir bor edi, bir yoqimli qiz, uning ismi Muxabbatxon edi. Har kuni biror yangi narsa o‘rganar, orzular sari yurardi.",
    "U kechqurun yulduzlarga qarab: 'Sen bilan birga bo'lishim orzu emas, taqdirdir', derdi Muxammadjon haqida o‘ylab.",
    "Yomg‘irli bir kun edi. Ammo Muxabbatxon yuragida quyosh porlardi — sababi yuragida Muxammadjonning muhabbati bor edi.",
    "Bir kun bir qiz, qalbidagi muhabbat bilan barcha g'amlarni yengdi. Chunki u sevgan inson — Muxammadjon bor edi.",
    "Bir kuni bir kichkina bola bor edi, u juda mehribon edi. Har kuni, u o'zingizni yaxshi his qilishni tavsiya etardi.",
    "Bir zamonlar shaharda bir qo'shni bor edi, u hamma bilan yaxshi munosabatda bo'lardi. Ularning hayotlari ko'plab sirlar bilan to'ldirilgan edi.",
    "Bir vaqtlar bir qiz bor edi, uning ismi Muxabbatxon edi. Har kuni u o'zining kichkina qishlog'ida baxtli hayot kechirdi.",
    "Bir kuni bir o'qituvchi talabalariga sevgini qanday anglashni o'rgatardi. Ularning har biri o'z dunyosida mehr bilan yashardi.",
    "O'rmonning chekkasida bir kishi yashar edi, uning dilida tabassum bor edi. Har kuni o'zi bilan yaxshi o'ylab, yaxshi xabarlar tarqatardi."
]

hayrli_tun_sozlar = ["Shirinim", "Asalim", "Muxabbatim"]

# Visol sanasigacha qolgan kunlarni hisoblash
def days_until_visol():
    today = datetime.now()
    remaining = target_date - today
    return remaining.days

# 08:00 xabari
def morning_message():
    iliq = random.choice(iliq_sozlar)
    topsh = random.choice(topshiriqlar)
    kunlar = days_until_visol()
    msg = (
        f"Salom Muxabbatim!\n\n"
        f"{iliq}\n\n"
        f"Bugungi topshiriq:\n{topsh}\n\n"
        f"Visol kuniga {kunlar} kun qoldi.\nInshaAllah!"
    )
    bot.send_message(CHAT_ID, msg)

# 12:00 sher
def lunch_poem():
    sher = random.choice(sherlar)
    bot.send_message(CHAT_ID, f"Bugungi she'r:\n\n{sher}")

# 18:00 hikoya
def evening_story():
    hiko = random.choice(hikoyalar)
    bot.send_message(CHAT_ID, f"Bugungi hikoya:\n\n{hiko}")

# 21:00 Hayrli tun
def night_message():
    sozni_boshi = random.choice(hayrli_tun_sozlar)
    bot.send_message(CHAT_ID, f"{sozni_boshi} Muxabbatim, yaxshi dam ol! Hayrli tun.")
    
    # Tugmalar yaratish
def create_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Qancha kun qoldi?")
    item2 = types.KeyboardButton("Bugungi topshiriq")
    markup.add(item1, item2)
    return markup

# /start komanda uchun javob
@bot.message_handler(commands=["start"])
def handle_start(message):
    markup = create_buttons()
    bot.send_message(message.chat.id, "Bot ishga tushdi. Har kuni sizni quvontiradi!", reply_markup=markup)

# Tugma orqali foydalanuvchidan javob olish
@bot.message_handler(func=lambda message: message.text == "Qancha kun qoldi?")
def handle_days(message):
    remaining_days = days_until_visol()
    bot.send_message(message.chat.id, f"Visol kuniga {remaining_days} kun qoldi.")

# Bot boshlanishi
def start_bot():
    @bot.message_handler(commands=["start"])
    def handle_start(message):
        bot.send_message(message.chat.id, "Bot ishga tushdi. Har kuni sizni quvontiradi!")

# Kundalik xabarlar
def schedule_messages():
    sent_flags = {"08:00": False, "12:00": False, "18:00": False, "21:00": False}
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == "08:00" and not sent_flags["08:00"]:
            morning_message()
            sent_flags["08:00"] = True
        elif now == "12:00" and not sent_flags["12:00"]:
            lunch_poem()
            sent_flags["12:00"] = True
        elif now == "18:00" and not sent_flags["18:00"]:
            evening_story()
            sent_flags["18:00"] = True

        elif now == "21:00" and not sent_flags["21:00"]:
            night_message()
            sent_flags["21:00"] = True

        if now == "00:00":
            for key in sent_flags:
                sent_flags[key] = False
        time.sleep(30)

# Botni ishga tushurish
start_bot()
schedule_messages()