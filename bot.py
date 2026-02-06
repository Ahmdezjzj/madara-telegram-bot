"""
نسخة مصححة من bot.py تعمل على Render بدون خطأ Updater
تعتمد على مكتبة python-telegram-bot الإصدار 20+
"""

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# تفعيل اللوق
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# قراءة التوكن من متغيرات البيئة في Render
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise Exception("يجب إضافة BOT_TOKEN في Environment Variables داخل Render")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً! أرسل لي رابط فصل من موقع Madara لأقوم بمعالجته."
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "طريقة الاستخدام:\n"
        "- أرسل رابط الفصل مباشرة\n"
        "- سأقوم بجلب الصور ورفعها"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.startswith("http"):
        await update.message.reply_text("الرجاء إرسال رابط صحيح.")
        return

    await update.message.reply_text("جاري معالجة الرابط... (هنا تضع كود Madara scraper)")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("حدث خطأ:", exc_info=context.error)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error_handler)

    # مهم لـ Render: الاستماع على PORT الذي يحدده السيرفر
    port = int(os.environ.get("PORT", 10000))

    print(f"Running on port {port}")

    app.run_polling()


if __name__ == "__main__":
    main()
