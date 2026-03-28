#!/bin/bash
img_path=${1:-p2.png}

img64=$(base64 -w0 "$img_path")

echo $img64 | head -c180

tmpFile=$(mktemp)

cat > "$tmpFile" << myEOF
{
  "messages":[
    {
      "role":"user",
      "content":[
          { "type":"text", "text":"圖片中有多少人" },
          { "type":"image_url","image_url":{"url": "data:image/png;base64,$img64" }}
      ]
    }
  ]
}
myEOF

response=$(curl  \
   -s http://localhost:8880/v1/chat/completions \
   -H "Content-Type: application/json" \
   -d @"$tmpFile" | jq -r '.choices[0].message.content' )

ls -l "$tmpFile"
rm "$tmpFile"

echo $response