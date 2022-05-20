

from telethon import TelegramClient, events
from telethon.sync import TelegramClient, events

api_id = 7790829
api_hash = "b462be4430bda3a2b4a1e48093877d19"
phone_number = "+91639279xxxx"

client = TelegramClient("kk", api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
	chat_id = event.chat_id
	msg = event.raw_text
	msg = msg.lower()
	if msg == "hello":
		await event.reply("Hello there")
	if msg == "hi" or msg == "ello":
		await event.reply("Hello")
	if msg == "hello there":
		await event.reply("General Kenobi")
	if msg == "aur batao":
		await event.reply("aur tum batao")
	trashlist = ['.','~',',','\'','"','/','!','@','#','&','-','(',')','^','%','|','<','>','*','+','[',']','{','}','`','=',':','/']
	if (msg[0] in trashlist) and (msg[-1] in trashlist):
		await event.reply(file='D://Telebot/anim/spam.mp4')
	if msg=="bye":
		await event.reply("Bye!")
	if msg=="lol":
		await event.reply(file='D://Telebot/anim/lol.mp4')
	if msg=="wtf":
		await event.reply(file='D://Telebot/anim/wtf.mp4')
	if 'cru_name' in msg:
	    await event.reply(file='D://Telebot/anim/shoot.mp4')
	if 'sh_name' in msg:
		await event.reply(file='D://Telebot/anim/shoot.mp4')
	if 'crushname' in msg:
		await event.reply(file='D://Telebot/anim/shoot.mp4')

	if chat_id == -1001494152996:
		trashlist = ['.','~',',','\'','"','/','!','@','#','&','-','(',')','^','%','|','<','>','*','+','[',']','{','}','`','=',':','/']
		if (msg[0] in trashlist) and (msg[-1] in trashlist):
			await event.reply(file='D://Telebot/anim/spam.mp4')
		if msg=="bye":
			await event.reply("Bye!")
		if msg=="lol":
			await event.reply(file='D://Telebot/anim/lol.mp4')
		if msg=="wtf":
			await event.reply(file='D://Telebot/anim/wtf.mp4')
		if 'cru' in msg:
			await event.reply(file='D://Telebot/anim/shoot.mp4')
		if 'sh' in msg:
			await event.reply(file='D://Telebot/anim/shoot.mp4')
		if 'crush' in msg:
			await event.reply(file='D://Telebot/anim/shoot.mp4')


client.start()
client.run_until_disconnected()
