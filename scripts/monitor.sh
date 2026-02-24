#!/bin/bash
echo "📊 Monitoring System Resources..."
watch -n 1 "nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu --format=csv"
