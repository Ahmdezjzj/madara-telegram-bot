import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from madara import MadaraUploader

TOKEN = os.getenv("BOT_TOKEN")
SITE_URL = os.getenv("SITE_URL")
WP_USER = os.getenv("WP_USER")
WP_PASS = os.getenv("WP_PASS")

uploader = MadaraUploader(SITE_URL, WP_USER, WP_PASS)

async def start(update: Update, context):
    await update.message.reply_text("أرسل رابط المانهوا لأرفعها للموقع 📥")

async def handle(update: Update, context):
    url = update.message.text

    await update.message.reply_text("جاري جلب المانهوا... ⏳")

    try:
        result = uploader.upload_manga(url)

        await update.message.reply_text(
            f"✅ تم الرفع بنجاح\n\n"
            f"📘 الاسم: {result['title']}\n"
            f"📚 الفصول: {result['chapters']}\n"
            f"🔗 {result['link']}"
        )

    except Exception as e:
        await update.message.reply_text(f"❌ خطأ:\n{e}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
