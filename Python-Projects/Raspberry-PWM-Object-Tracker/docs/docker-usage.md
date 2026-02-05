# Docker 使用說明

## 快速執行
```bash
# 執行陌生人偵測
docker run -it --rm -v /dev:/dev --privileged \
  -v /etc/localtime:/etc/localtime:ro \
  -e "LANG=C.UTF-8" \
  -p 9090:9090 \
  -v $(pwd):/app \
  -w /app/src \
  cv2-ocr-lcd-gpio-fr:cv3.3 python stranger.py
```
