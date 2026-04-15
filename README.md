# Belajar DeepSeek Tool Use AI 🚀

Project ini adalah panduan praktis untuk mempelajari cara menggunakan **Function Calling (Tools)** dengan **DeepSeek AI** menggunakan Python dan SDK OpenAI.

## 🌟 Fitur Utama
- **DeepSeek Integration**: Implementasi pemanggilan fungsi menggunakan endpoint DeepSeek yang kompatibel dengan OpenAI.
- **Stock Price Tool**: Contoh fungsi dunia nyata untuk mengambil data harga saham secara dinamis.
- **Web Documentation**: Dokumentasi interaktif berbasis web dengan fitur **Light/Dark Mode**.
- **Automated Handling**: Penanganan otomatis terhadap permintaan `tool_calls` dari AI.

## 📂 Struktur Project
```text
belajar_tools_ai/
├── docs/               # Web Dokumentasi (HTML/CSS/JS)
├── deepseek_tools.py   # Script Utama Python
├── requirements.txt    # Daftar dependensi
└── README.md           # File ini
```

## 🛠️ Instalasi

1. **Clone repository ini** (atau buat foldernya secara lokal).
2. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Setel API Key DeepSeek**:
   Dapatkan API Key dari [DeepSeek Platform](https://platform.deepseek.com/).
   ```bash
   # Windows (PowerShell)
   $env:DEEPSEEK_API_KEY = "sk-your-key-here"

   # Linux / Mac
   export DEEPSEEK_API_KEY="sk-your-key-here"
   ```

## 🚀 Cara Penggunaan

Jalankan script utama untuk melihat AI berinteraksi dengan tool:
```bash
python deepseek_tools.py
```

## 🌐 Dokumentasi Web
Project ini dilengkapi dengan web dokumentasi modern. Buka file berikut di browser Anda:
`docs/index.html`

Fitur Web:
- **Responsive Layout**: Nyaman dibuka di HP maupun Desktop.
- **Theming**: Toggle Mode Terang & Gelap.
- **Learning Path**: Panduan metode belajar yang terstruktur.

## 📚 Metode Belajar
1. **Analisis Schema**: Pelajari bagaimana deskripsi tool memengaruhi keputusan AI.
2. **Modifikasi Tool**: Coba tambahkan fungsi baru seperti `get_crypto_price`.
3. **Debug Logic**: Perhatikan bagaimana pesan `role: tool` dikirim kembali ke AI.

---
Dibuat untuk keperluan belajar integrasi DeepSeek dan Tool Use.
