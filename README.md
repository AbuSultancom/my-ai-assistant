# 🤖 My Local AI Assistant

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/AbuSultancom/my-ai-assistant)
![GitHub forks](https://img.shields.io/github/forks/AbuSultancom/my-ai-assistant)

**Local AI Assistant using DeepSeek-R1 14B + Ollama + OpenClaw**

[English](#english) | [العربية](#العربية)

</div>

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Hardware](#hardware)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 About <a name="about"></a>

Built a fully functional local AI assistant system that runs **DeepSeek-R1 14B** model without any cloud dependency. Integrated with **OpenClaw** for messaging platforms (WhatsApp, Telegram).

### لماذا هذا المشروع؟

- 🔒 **الخصوصية**: جميع البيانات تبقى محلية
- 💰 **التكلفة**: لا توجد رسوم شهرية
- 🚀 **السرعة**: استجابات فورية
- 🎓 **التعلم**: تعلمت الكثير عن AI و Linux

---

## ✨ Features <a name="features"></a>

```
✅ Local LLM Deployment (DeepSeek-R1 14B)
✅ Ollama Platform Integration
✅ Multi-platform Messaging (WhatsApp, Telegram)
✅ 24/7 Availability via systemd
✅ Privacy-First Architecture
✅ Cost-Effective AI Solution
✅ Self-Hosted & Self-Managed
```

---

## 💻 Hardware <a name="hardware"></a>

| Component | Specification |
|-----------|---------------|
| **GPU** | NVIDIA RTX 4050 (6GB VRAM) |
| **RAM** | 30GB System Memory |
| **CPU** | 16-Core Processor |
| **OS** | Linux (Ubuntu/Debian) |

---

## 🛠️ Installation <a name="installation"></a>

### المتطلبات الأساسية:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y ollama wget curl

# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
```

### تنزيل النموذج:

```bash
# Download DeepSeek-R1 14B
ollama pull deepseek-r1:14b

# أو نسخة أخف إذا احتجت
ollama pull deepseek-r1:7b
```

### تثبيت OpenClaw:

```bash
# Clone OpenClaw
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# التثبيت
npm install -g openclaw
```

### إعداد systemd service:

```bash
# نسخ ملف الخدمة
sudo cp openclaw.service /etc/systemd/system/

# تفعيل الخدمة
sudo systemctl enable openclaw
sudo systemctl start openclaw
```

---

## 📖 Usage <a name="usage"></a>

### بدء الخدمة:

```bash
# طريقة 1: مباشرة
openclaw start

# طريقة 2: عبر systemctl
sudo systemctl start openclaw
```

### إيقاف الخدمة:

```bash
sudo systemctl stop openclaw
```

### التحقق من الحالة:

```bash
sudo systemctl status openclaw
```

---

## 🤝 Contributing <a name="contributing"></a>

المساهمة مرحب بها!

---

## 📄 License <a name="license"></a>

MIT License - feel free to use and modify!

---

## 📞 Contact <a name="contact"></a>

**Abdulhameed Mohammed Hasan Alyahaesi**

- 📧 Email: alyhysycom1@gmail.com
- 📱 Phone: +8617822403412
- 🇨🇳 Location: Tianjin, China

---

<div align="center">

**Built with ❤️ and ☕**

</div>

---

## <a name="العربية"></a>🇸🇦 بالعربية

### حول المشروع

هذا مشروع لنظام مساعد ذكي يعمل محلياً باستخدام:
- **DeepSeek-R1 14B**: نموذج ذكاء اصطناعي كبير
- **Ollama**: منصة لتشغيل النماذج المحلية
- **OpenClaw**: إطار عمل للتواصل مع تطبيقات المراسلة

### المميزات

- ✅ خصوصية كاملة (البيانات لا تخرج من جهازك)
- ✅ تكلفة صفر (لا رسوم شهرية)
- ✅ سرعة عالية
- ✅ تعلمت كل شي بنفسي!

### التواصل

- 📧 alyhysycom1@gmail.com
- 📱 +8617822403412
