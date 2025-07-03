from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from config import BOT_TOKEN
from handlers import start, register_teacher, choose_subject, show_teachers, save_teacher, subjects
from database import init_db
from telegram import Update

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler))

    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
