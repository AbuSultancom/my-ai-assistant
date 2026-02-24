# 🔌 API Reference

The Local AI Assistant exposes several endpoints via the OpenClaw and Ollama integration.

## 1. Chat Completion (Ollama compatible)
- **Endpoint:** `POST /api/chat`
- **Description:** Sends a message to the DeepSeek-R1 14B model.

## 2. Status Probe
- **Endpoint:** `GET /api/status`
- **Description:** Returns the health status of the Gateway and the Model.

## 3. Webhook Integration
- **Platform:** WhatsApp / Telegram
- **Logic:** Asynchronous message handling via OpenClaw relay.
