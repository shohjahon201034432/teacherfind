import logging
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from handlers import *
from database import init_db

# Logging ni yoqamiz
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_handler(update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Start handler called")
    await start(update, context)

async def message_handler(update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Message received: {update.message.text}")
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
    logger.info("Bot ishga tushmoqda...")
    
    # Database ni ishga tushiramiz
    try:
        init_db()
        logger.info("Database muvaffaqiyatli ishga tushdi")
    except Exception as e:
        logger.error(f"Database xatosi: {e}")
        return
    
    # Bot token ni tekshiramiz
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN topilmadi!")
        return
    
    logger.info(f"Bot token: {BOT_TOKEN[:10]}...")
    
    # Application yaratamiz
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Handler'larni qo'shamiz
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    logger.info("✅ Bot ishga tushdi!")
    print("✅ Bot ishga tushdi!")
    
    # Polling ni boshlash
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()