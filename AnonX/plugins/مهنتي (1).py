#✘ ITALY MUSIC @I6ALY ✘
import random
from AnonX import app 
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@app.on_message(filters.command(['مهنتي'], prefixes=""))
def get_user_info(_, message):
    url = f"https://t.me/{message.from_user.username}"
    age = random.randint(15, 40)
    jobs = ["مدرس 👨‍🏫", "طبيب 👨‍⚕", "مهندس 👷‍♂", "خيال 🏇", "سباح 🏊", "مطور 👨‍💻"]
    job = random.choice(jobs)
    statuses = ["متزوج 👨‍👩‍👧‍👦", "اعذب 🧍‍♂", "مرتبط 👩‍❤️‍💋‍👨", "نرجسي 💆‍♂", "ملهم 🧝‍♂"]
    status = random.choice(statuses)
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"اسـمـك :  {message.from_user.first_name}", url=url)],
            [InlineKeyboardButton(f"عـمـرك :  {age}", callback_data=f"age_{age}")],
            [InlineKeyboardButton(f"مـهـنـتـك :  {job}", callback_data=f"job_{job}")],
            [InlineKeyboardButton(f"حـالـتـك :  {status}", callback_data=f"status_{status}")]
        ]
    )
    app.send_photo(
        chat_id=message.chat.id,
        photo=url,
        reply_markup=inline_keyboard,
        reply_to_message_id=message.message_id
    )
    
print("OKAY ITALY MUSIC CODE WORKING NOW⚡")
