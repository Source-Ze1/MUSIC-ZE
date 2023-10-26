from AnonX import app
from strings.filters import command 
from pyrogram import Client,filters
from pyrogram.types import ForceReply,ChatPrivileges,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram.types import ChatPermissions, ChatPrivileges
import asyncio



@app.on_message(filters.command("رفع مشرف",""),filters.group)
async def UpAdmin(bot,msg):
	UserID = msg.reply_to_message.from_user.id
	ChatID = msg.chat.id
	
	Can_C = False
	Can_D = False
	Can_I = False
	Can_R = False
	Can_P = False
	Can_MV = False
	Can_PR = False
	
	R = await msg.chat.get_member(msg.from_user.id)
	
	if R.status == ChatMemberStatus.OWNER or R.status == ChatMemberStatus.ADMINISTRATOR:
		ask = await msg.chat.ask("⇜ تمام الحين ارسل صلاحيات المشرف \n\n1 ⇠ صلاحيه تغيير المعلومات\n2 ⇠ صلاحيه حذف الرسائل\n3 ⇠ صلاحيه دعوه مستخدمين\n4 ⇠ صلاحيه حظر وتقيد المستخدمين \n5 ⇠ صلاحيه تثبيت الرسائل \n6 ⇠ صلاحيه ادارة المكالمات\n7 ⇜ صلاحيه رفع مشرفين اخرين\n* ⇠ لرفع كل الصلاحيات ما عدا رفع المشرفين \n** ⇠ لرفع كل الصلاحيات مع رفع المشرفين \n\n⇜ يمديك تختار الارقام مع بعض  \n\nمثال: 136 \n༄",
		reply_markup=ForceReply(),filters=filters.text)
		TexT = ask.text
		
		if str("1") in TexT:
			Can_C = True
		if str("2") in TexT:
			Can_D = True
		if str("3") in TexT:
			Can_I = True
		if str("4") in TexT:
			Can_R = True
		if str("5") in TexT:
			Can_P = True
		if str("6") in TexT:
			Can_MV = True
		if str("7") in TexT:
			Can_PR = True
		if str("*") in TexT:
			Can_C = True
			Can_D = True
			Can_I = True
			Can_R = True
			Can_P = True
			Can_MV = True
		if str("**") in TexT:
			Can_C = True
			Can_D = True
			Can_I = True
			Can_R = True
			Can_P = True
			Can_MV = True
			Can_PR = True
		try:
			await bot.promote_chat_member(
			chat_id=ChatID,
			user_id=UserID,
			privileges=ChatPrivileges(
		    can_promote_members=Can_PR,
		    can_manage_video_chats=Can_MV,
		    can_pin_messages=Can_P,
		    can_invite_users=Can_I,
		    can_restrict_members=Can_R,
		    can_delete_messages=Can_D,
		    can_change_info=Can_C))
		except Exception as e:
			return await msg.reply(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
			
		if any(i in ask.text for i in ['1','2','3', '4', '5', '6','7','*','**']):
			return await msg.reply(f"**•「{msg.from_user.mention}」\nتم رفعته مشرف**",reply_markup=
			InlineKeyboardMarkup
			([[InlineKeyboardButton(
			msg.reply_to_message.from_user.first_name,
			user_id=
			msg.reply_to_message.from_user.id)]]))
		else:
			return await msg.reply("اتكلم بعدين و ارفع مشرف")
	
	else:
		return await msg.reply("هذا الامر للمشرفين فقط")


print("7")





@app.on_message(filters.command("رفع مشرف", "") & filters.channel)
def promote_c_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    
    Mody= ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_invite_users=True,
                    can_pin_messages=False,
                    is_anonymous=False
                )
    chat_id = message.chat.id
    client.promote_chat_member(chat_id, user_id, Mody)
    message.reply(f"تم رفع {user_id} ادمن بنجاح")
    




@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: {str(e)}"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)
