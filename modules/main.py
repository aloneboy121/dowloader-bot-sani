import os
import sys
import asyncio
import requests
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from vars import API_ID, API_HASH, BOT_TOKEN, OWNER, CREDIT, AUTH_USERS, TOTAL_USERS
from commands import register_commands_handlers
from text_handler import register_text_handlers
from html_handler import register_html_handlers
from features import register_feature_handlers
from upgrade import register_upgrade_handlers
from settings import register_settings_handlers
from broadcast import register_broadcast_handlers
from youtube_handler import register_youtube_handlers
from authorisation import register_authorisation_handlers
from drm_handler import register_drm_handlers

# Initialize the bot
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Keyboard for /start
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("✨ Commands", callback_data="cmd_command")],
    [InlineKeyboardButton("💎 Features", callback_data="feat_command"), InlineKeyboardButton("⚙️ Settings", callback_data="setttings")],
    [InlineKeyboardButton("💳 Plans", callback_data="upgrade_command")],
    [InlineKeyboardButton(text="📞 Contact", url=f"tg://openmessage?user_id={OWNER}"), InlineKeyboardButton(text="🛠️ Repo", url="https://github.com/nikhilsainiop/saini-txt-direct")],
])

# /start command
@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    user_id = m.chat.id
    if user_id not in TOTAL_USERS:
        TOTAL_USERS.append(user_id)
    user = await bot.get_me()
    mention = user.mention
    if m.chat.id in AUTH_USERS:
        caption = (
            f"𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 👋!\n\n"
            f"➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭\n\n"
            f"➠ For Guide Use button - **✨ Commands** 📖\n\n"
            f"➠ 𝐌𝐚𝐝𝐞 𝐁𝐲 : [{CREDIT}](tg://openmessage?user_id={OWNER}) 🦁"
        )
    else:
        caption = (
            f"𝐇𝐞𝐥𝐥𝐨 **{m.from_user.first_name}** 👋!\n\n"
            f"➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭\n\n"
            f"**You are currently using the free version.** 🆓\n"
            f"💬 Contact: [{CREDIT}](tg://openmessage?user_id={OWNER}) to Get The Subscription ! 🔓\n"
        )
    await bot.send_photo(
        chat_id=m.chat.id,
        photo="https://files.catbox.moe/18fp9e.jpg",
        caption=caption,
        reply_markup=keyboard
    )

# /id command
@bot.on_message(filters.command(["id"]))
async def id_command(client, message: Message):
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="Send to Owner", url=f"tg://openmessage?user_id={OWNER}")]])
    chat_id = message.chat.id
    text = f"<blockquote expandable><b>The ID of this chat id is:</b></blockquote>\n`{chat_id}`"
    
    if str(chat_id).startswith("-100"):
        await message.reply_text(text)
    else:
        await message.reply_text(text, reply_markup=keyboard)

# /info command
@bot.on_message(filters.private & filters.command(["info"]))
async def info(bot: Client, update: Message):
    text = (
        f"╭────────────────╮\n"
        f"│✨ **Your Telegram Info**✨ \n"
        f"├────────────────\n"
        f"├🔹**Name :** `{update.from_user.first_name} {update.from_user.last_name if update.from_user.last_name else 'None'}`\n"
        f"├🔹**User ID :** {('@' + update.from_user.username) if update.from_user.username else 'None'}\n"
        f"├🔹**TG ID :** `{update.from_user.id}`\n"
        f"├🔹**Profile :** {update.from_user.mention}\n"
        f"╰────────────────╯"
    )    
    await update.reply_text(text=text, disable_web_page_preview=True)

# /logs command
@bot.on_message(filters.command(["logs"]))
async def send_logs(client: Client, m: Message):
    try:
        with open("logs.txt", "rb") as file:
            sent = await m.reply_text("**📤 Sending you ....**")
            await m.reply_document(document=file)
            await sent.delete()
    except Exception as e:
        await m.reply_text(f"**Error sending logs:**\n<blockquote>{e}</blockquote>")

# /reset command
@bot.on_message(filters.command(["reset"]))
async def restart_handler(_, m: Message):
    if m.chat.id != OWNER:
        return
    await m.reply_text("𝐁𝐨𝐭 𝐢𝐬 𝐑𝐞𝐬𝐞𝐭𝐢𝐧𝐠...", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

# /stop command
@bot.on_message(filters.command("stop") & filters.private)
async def cancel_handler(client: Client, m: Message):
    if m.chat.id not in AUTH_USERS:
        await bot.send_message(
            m.chat.id, 
            f"<blockquote>__**Oopss! You are not a Premium member**__\n"
            f"__**Please Upgrade Your Plan**__\n"
            f"__**Send me your user id for authorization**__\n"
            f"__**Your User id** __- `{m.chat.id}`</blockquote>\n\n"
        )
    else:
        await m.reply_text("**⚡ No active process to cancel.**")

# Register all handlers
register_text_handlers(bot)
register_html_handlers(bot)
register_feature_handlers(bot)
register_settings_handlers(bot)
register_upgrade_handlers(bot)
register_commands_handlers(bot)
register_broadcast_handlers(bot)
register_youtube_handlers(bot)
register_authorisation_handlers(bot)
register_drm_handlers(bot)

# Startup functions
def notify_owner():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": OWNER, "text": "𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅"}
    requests.post(url, data=data)

def reset_and_set_commands():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setMyCommands"
    general_commands = [
        {"command": "start", "description": "✅ Check Alive the Bot"},
        {"command": "stop", "description": "🚫 Stop the ongoing process"},
        {"command": "id", "description": "🆔 Get Your ID"},
        {"command": "info", "description": "ℹ️ Check Your Information"},
        {"command": "logs", "description": "👁️ View Bot Activity"},
    ]
    owner_commands = general_commands + [
        {"command": "broadcast", "description": "📢 Broadcast to All Users"},
        {"command": "reset", "description": "✅ Reset the Bot"}
    ]
    requests.post(url, json={"commands": general_commands, "scope": {"type": "default"}, "language_code": "en"})
    requests.post(url, json={"commands": owner_commands, "scope": {"type": "chat", "chat_id": OWNER}, "language_code": "en"})

# Main async runner
async def main():
    reset_and_set_commands()
    notify_owner()
    await bot.start()
    print("Bot is now running...")
    await idle()  # Keeps bot alive
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
