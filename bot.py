from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")  # قراءة التوكن من متغيرات البيئة

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("مرحبًا! أنا بوت الذكاء الصناعي بتاعك، جاهز للدردشة 😊")

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = f"انت قولت: {user_message}"
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
