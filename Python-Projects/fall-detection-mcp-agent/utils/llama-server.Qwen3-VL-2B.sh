#!/bin/bash

firefox 'localhost:8880' &

llama-server \
  --model  ~/model/unsloth/Qwen3-VL-2B-Instruct-Q4_K_M.gguf \
  --mmproj ~/model/unsloth/Qwen3-VL-2B-mmproj-F16.gguf \
  -ngl 99 \
  -c  8192 \
  --flash-attn on \
  --temp 0.9 \
  --top-p 0.9 \
  --min-p 0.05 \
  --repeat-penalty 1.1 \
  --host 0.0.0.0 \
  --port 8880

## 上傳： p3.png
## 輸入： 請詳細描述這張圖

## -ngl 99  就是  --n-gpu-layers 99
## -c 8192  就是  --ctx-size 8192

## https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-GGUF
## https://huggingface.co/unsloth/Qwen3-VL-2B-Instruct-GGUF/tree/main
