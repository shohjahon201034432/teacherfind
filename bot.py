from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from config import BOT_TOKEN
from handlers import *
from database import init_db

async def message_handler(update, context):
    text = update.message.text
    if text == "I'm a Teacher":
        await register_teacher(update, context)
    elif text == "I'm a Student":
        await choose_subject(update, context)
    elif text in subjects:
        await show_teachers(update, context)
    elif "|" in text:
        await save_teacher(update, context)
    else:
        await update.message.reply_text("Iltimos, to‘g‘ri variantni tanlang.")

def main():
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
