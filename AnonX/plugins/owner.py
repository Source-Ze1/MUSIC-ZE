#كود تافه ملوش لازمة اسرقه واذكر المصدر @z0hary 
from AnonX import app 
from strings.filters import command
from pyrogram import Client, filters,idle,enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus


@mody.on_message(filters.command(["المالك"],""))
async def creator(c,msg):
    x = []
    async for m in mody.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       lol = await mody.get_users(int(x[0]))
       if lol.photo:
         async for photo in mody.get_chat_photos(x[0],limit=1):
          await msg.reply_photo(photo.file_id,caption=f"ΌᎳΝᎬᎡ | - {lol.mention} 🕷",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(lol.first_name, url=f"https://t.me/{lol.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await msg.reply_text(f"ΌᎳΝᎬᎡ | - {lol.mention} 🕷", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(lol.first_name, url=f"https://t.me/{lol.username}")],]))
    else:
        await msg.reply_text("الاك محذوف يقلب")
        
        
