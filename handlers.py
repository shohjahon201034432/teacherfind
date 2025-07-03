from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from database import add_teacher, get_teachers_by_subject

subjects = ['English', 'Math', 'IT', 'Driving', 'Physics', 'Arabic']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["I'm a Teacher"], ["I'm a Student"]]
    await update.message.reply_text("Welcome to UstozTop Bot!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

async def register_teacher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your details in this format:\n\nFull Name | Subject | About You | Telegram @username | Phone")

async def save_teacher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        parts = update.message.text.split('|')
        fullname, subject, desc, tg, phone = [p.strip() for p in parts]
        add_teacher(user_id, fullname, subject, desc, tg, phone)
        await update.message.reply_text("✅ Registered successfully!")
    except Exception as e:
        await update.message.reply_text("❌ Error in format. Use: Name | Subject | Info | @username | phone")

async def choose_subject(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[s] for s in subjects]
    await update.message.reply_text("Choose a subject:", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

async def show_teachers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subject = update.message.text
    teachers = get_teachers_by_subject(subject)
    if not teachers:
        await update.message.reply_text("❌ No teachers found for this subject.")
        return

    for t in teachers:
        name, about, tg, phone = t
        await update.message.reply_text(
            f"👨‍🏫 {name}\n📘 {about}\n📱 {tg}\n📞 {phone}"
        )
