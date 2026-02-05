# Docker 快速使用

## 快速指令
```bash
# 可以用來偵測狗狗
docker run -it --rm -v /dev:/dev --privileged \
  -v /etc/localtime:/etc/localtime:ro \
  -e "LANG=C.UTF-8" \
  -p 9090:9090 \
  -v ~:/z \
  -w /z/Raspberry-PWM-Object-Tracker/src/ \
  cv2-ocr-lcd-gpio-fr:cv3.3 ./search_xx_rec.py -o 12
```
