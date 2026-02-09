# 🤖 مشروعي المحلي للذكاء الاصطناعي
## My Local AI Assistant Project

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/AbuSultancom/my-ai-assistant)
![GitHub forks](https://img.shields.io/github/forks/AbuSultancom/my-ai-assistant)

**مساعد ذكاء اصطناعي محلي باستخدام DeepSeek-R1 14B + Ollama + OpenClaw**

**Local AI Assistant using DeepSeek-R1 14B + Ollama + OpenClaw**

[English](#english) | [العربية](#العربية)

</div>

---

## 📋 فهرس المحتويات | Table of Contents

- [نبذة عني | About Me](#نبذة-عني)
- [مميزات المشروع | Features](#مميزات-المشروع)
- [المواصفات التقنية | Hardware](#المواصفات-تقنية)
- [التثبيت | Installation](#التثبيت)
- [الاستخدام | Usage](#الاستخدام)
- [لماذا هذا المشروع؟ | Why This Project?](#لماذا-هذا-المشروع)
- [التواصل | Contact](#التواصل)

---

# 🇸🇦 بالعربية

## نبذة عني <a name="نبذة-عني"></a>

أنا **عبد الحميد محمد حسن ال يحيئي**، طالب يمني عمري 18 سنة أدرس حالياً في الصين (تيانجين).

شغوف بالتقنية والذكاء الاصطناعي، وقد تعلمت كل شي بنفسي!

### 🎓 تعليمي
- **المدرسة**: مدارس الفاتح الدولية
- **التخصص**: علمي
- **المعدل**: 90%
- **التخرج**: 2023

### 🗣️ لغاتي
- العربية: لغة أم
- الإنجليزية: متقدم
- الصينية: متوسط

### 💻 مهاراتي التقنية
- DeepSeek-R1 14B (نشر محلي)
- Ollama (منصة الذكاء الاصطناعي)
- Linux و systemd
- OpenClaw (إطار العمل)
- برمجة بايثون

---

## مميزات المشروع <a name="مميزات-المشروع"></a>

```
✅ نشر نموذج ذكاء اصطناعي محلي (DeepSeek-R1 14B)
✅ دمج مع منصة Ollama
✅ ربط مع تطبيقات المراسلة (واتساب، تيليجرام)
✅ عمل 24/7 عبر systemd
✅ خصوصية كاملة
✅ بدون تكاليف شهرية
✅ إدارة ذاتية
```

---

## المواصفات التقنية <a name="المواصفات-تقنية"></a>

| المكون | المواصفة |
|--------|----------|
| **معالج الرسوميات** | NVIDIA RTX 4050 (6GB VRAM) |
| **الذاكرة** | 30GB RAM |
| **المعالج** | 16-Core CPU |
| **نظام التشغيل** | Linux |

---

## التثبيت <a name="التثبيت"></a>

### المتطلبات الأساسية:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y ollama wget curl

# تثبيت Ollama
curl -fsSL https://ollama.ai/install.sh | sh
```

### تنزيل النموذج:

```bash
# تحميل DeepSeek-R1 14B
ollama pull deepseek-r1:14b

# أو نسخة أخف
ollama pull deepseek-r1:7b
```

### تثبيت OpenClaw:

```bash
# نسخ المشروع
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# التثبيت
npm install -g openclaw
```

---

## الاستخدام <a name="الاستخدام"></a>

### بدء الخدمة:

```bash
# الطريقة الأولى: مباشرة
openclaw start

# الطريقة الثانية: عبر systemctl
sudo systemctl start openclaw
```

### إيقاف الخدمة:

```bash
sudo systemctl stop openclaw
```

---

## لماذا هذا المشروع؟ <a name="لماذا-هذا-المشروع"></a>

```
🔒 الخصوصية: جميع البيانات تبقى على جهازي
💰 التكلفة: لا توجد رسوم شهرية
🚀 السرعة: استجابات فورية
🎓 التعلم: تعلمت الكثير عن AI و Linux
```

---

## التواصل <a name="التواصل"></a>

**عبد الحميد محمد حسن ال يحيئي**

- 📧 البريد: alyhysycom1@gmail.com
- 📱 الهاتف: +8617822403412
- 🇨🇳 الموقع: تيانجين، الصين

---

---

# 🇺🇸 English

## About Me <a name="english"></a>

I am **Abdulhameed Mohammed Hasan Alyahaesi**, an 18-year-old Yemeni student currently studying in China (Tianjin).

Passionate about technology and AI, I learned everything by myself!

### 🎓 Education
- **School**: Al-Fateh International Schools
- **Track**: Scientific
- **GPA**: 90%
- **Graduated**: 2023

### 🗣️ Languages
- Arabic: Native
- English: Advanced
- Chinese: Intermediate

### 💻 Technical Skills
- DeepSeek-R1 14B (Local Deployment)
- Ollama (AI Platform)
- Linux & systemd
- OpenClaw (Framework)
- Python Programming

---

## Features <a name="features"></a>

```
✅ Local LLM Deployment (DeepSeek-R1 14B)
✅ Ollama Platform Integration
✅ Multi-platform Messaging (WhatsApp, Telegram)
✅ 24/7 Availability via systemd
✅ Complete Privacy
✅ No Monthly Costs
✅ Self-Managed
```

---

## Hardware <a name="hardware"></a>

| Component | Specification |
|-----------|---------------|
| **GPU** | NVIDIA RTX 4050 (6GB VRAM) |
| **RAM** | 30GB System Memory |
| **CPU** | 16-Core Processor |
| **OS** | Linux |

---

## Installation <a name="installation"></a>

### Prerequisites:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y ollama wget curl

# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
```

### Download Model:

```bash
# Download DeepSeek-R1 14B
ollama pull deepseek-r1:14b

# Or lighter version
ollama pull deepseek-r1:7b
```

### Install OpenClaw:

```bash
# Clone project
git clone https://github.com/openclaw/openclaw.git
cd openclaw

# Install
npm install -g openclaw
```

---

## Usage <a name="usage"></a>

### Start Service:

```bash
# Method 1: Direct
openclaw start

# Method 2: Via systemctl
sudo systemctl start openclaw
```

### Stop Service:

```bash
sudo systemctl stop openclaw
```

---

## Why This Project? <a name="why-this-project"></a>

```
🔒 Privacy: All data stays on my device
💰 Cost: No monthly fees
🚀 Speed: Instant responses
🎓 Learning: Learned so much about AI and Linux
```

---

## Contact <a name="contact"></a>

**Abdulhameed Mohammed Hasan Alyahaesi**

- 📧 Email: alyhysycom1@gmail.com
- 📱 Phone: +8617822403412
- 🇨🇳 Location: Tianjin, China

---

<div align="center">

**تم بناؤه بحب | Built with ❤️**

</div>
