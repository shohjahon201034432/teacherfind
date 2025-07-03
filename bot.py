from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from handlers import *
from database import init_db

async def start_handler(update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

async def message_handler(update, context: ContextTypes.DEFAULT_TYPE):
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
        await update.message.reply_text("Iltimos, to'g'ri variantni tanlang.")

def main():
    init_db()
    
    # ApplicationBuilder() o'rniga Application.builder() ishlatamiz
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    print("✅ Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()