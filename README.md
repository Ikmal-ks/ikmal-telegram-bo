# 🤖 Ikmal AI Bot

Bot Telegram cerdas yang dibuat dengan nama pribadi **Ikmal**, memiliki fitur lengkap berbasis AI:

- 💬 ChatGPT (teks)
- 🖼️ Gambar AI dari teks
- 🎭 Stiker AI dari prompt
- 🔊 Teks ke Suara (TTS)
- 🎥 Simulasi Video AI
- 👤 Branding pribadi dengan foto avatar

---

## 🚀 Fitur Bot

| Perintah       | Fungsi                              |
|----------------|-------------------------------------|
| `/start`       | Menyapa pengguna dengan avatar Ikmal |
| `/ask <teks>`  | Menjawab pertanyaan via ChatGPT     |
| `/img <prompt>`| Membuat gambar dari teks (DALL·E)   |
| `/sticker`     | Kirim stiker dari prompt            |
| `/tts <teks>`  | Mengubah teks menjadi suara         |
| `/vid <prompt>`| Simulasi video AI (dummy response)  |

---

## 🛠️ Setup Environment

Buat file `.env` (jika tidak pakai Railway):

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
OWNER_NAME=Ikmal
