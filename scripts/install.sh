#!/bin/bash
echo "🚀 Starting Installation of Local AI Assistant..."
sudo apt update && sudo apt install -y curl git
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
# Pull the optimized model
ollama pull deepseek-r1:14b
echo "✅ Base system installed successfully."
