import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# ======= KONFIGURASI ========
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '7381621550:AAFsRzM3-2E8XcWF5NneosFAQAMVD8bLACs')
OPENAI_KEY = os.getenv('OPENAI_API_KEY', 'sk-...MFEA')
openai.api_key = OPENAI_KEY

# Path to your personal photo (place 'my_photo.jpg' in project root)
MY_PHOTO_PATH = 'my_photo.jpg'

# ======= HANDLERS ========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Halo! Saya *Ikmal AI Bot* 🤖\n\n"
        "Perintah yang tersedia:\n"
        "/ask <pertanyaan> - Tanya ke ikmal\n"
        "/img <prompt> - Buat gambar \n"
        "/sticker <prompt> - Buat stiker \n"
        "/tts <teks> - Ubah teks jadi suara\n"
        "/vid <prompt> - Generate video (simulasi)\n"
        "/me - Kirim foto saya\n"
    )
    await update.message.reply_markdown(text)

# ChatGPT text response
async def ask_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = ' '.join(context.args)
    if not prompt:
        return await update.message.reply_text("Gunakan: /ask siapa presiden Indonesia?")
    await update.message.reply_text("Sedang berpikir...")
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    text = resp.choices[0].message.content
    await update.message.reply_text(text)

# Image generation
async def img_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = ' '.join(context.args)
    if not prompt:
        return await update.message.reply_text("Gunakan: /img kucing memakai jas astronaut")
    await update.message.reply_text("Membuat gambar...")
    resp = openai.Image.create(prompt=prompt, n=1, size="512x512")
    url = resp['data'][0]['url']
    await update.message.reply_photo(photo=url)

# Sticker generation (convert generated image to sticker)
async def sticker_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = ' '.join(context.args)
    if not prompt:
        return await update.message.reply_text("Gunakan: /sticker kartun lucu")
    await update.message.reply_text("Membuat stiker...")
    resp = openai.Image.create(prompt=prompt, n=1, size="512x512")
    url = resp['data'][0]['url']
    # Download then send as sticker
    import requests, tempfile
    r = requests.get(url)
    tf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    tf.write(r.content)
    tf.flush()
    await update.message.reply_sticker(sticker=open(tf.name, 'rb'))
    os.unlink(tf.name)

# Text-to-speech
async def tts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    if not text:
        return await update.message.reply_text("Gunakan: /tts selamat pagi semuanya")
    await update.message.reply_text("Menghasilkan suara...")
    # Simple TTS via OpenAI voice endpoint (contoh simulasi)
    resp = openai.Audio.create(
        model="tts-1", text=text, voice="alloy"
    )
    audio_url = resp['data'][0]['url']
    await update.message.reply_audio(audio=audio_url)

# Video generation (simulasi)
async def vid_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fitur video AI sedang dalam pengembangan.")

# Kirim foto pribadi
async def me_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.isfile(MY_PHOTO_PATH):
        await update.message.reply_photo(photo=InputFile(MY_PHOTO_PATH))
    else:
        await update.message.reply_text("Foto pribadi tidak ditemukan di server.")

# Setup bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask_handler))
    app.add_handler(CommandHandler("img", img_handler))
    app.add_handler(CommandHandler("sticker", sticker_handler))
    app.add_handler(CommandHandler("tts", tts_handler))
    app.add_handler(CommandHandler("vid", vid_handler))
    app.add_handler(CommandHandler("me", me_handler))
    print("Bot Ikmal is running...")
    app.run_polling()
