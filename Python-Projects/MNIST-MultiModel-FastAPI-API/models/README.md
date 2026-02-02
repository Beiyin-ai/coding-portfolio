# 模型檔案說明

請將訓練好的模型權重檔案 (.pth) 放置於此目錄。

## 必要模型檔案

根據 app.py 中的設定，需要以下模型檔案：

### 自定義模型
1. `simple_nn_mnist.pth` - SimpleNN 模型權重
2. `simple_cnn_mnist.pth` - SimpleCNN 模型權重  
3. `myvit_mnist.pth` - 自定義 ViT 模型權重

### HuggingFace 微調模型
4. `myvit_mnist_hf_4060.pth` - ViT HF 4060 權重
5. `myvit_mnist_hf_best_tuned.pth` - ViT HF 最佳微調權重

## 檔案命名規則

模型檔案應符合以下命名規則，以便 app.py 自動載入：

```
{模型名稱}_{資料集}.pth
```

範例：
- `simple_nn_mnist.pth`
- `myvit_mnist_hf_4060.pth`

## 模型訓練

如需重新訓練模型，請參考以下指令：

```bash
# 訓練 SimpleNN
python train_simplenn.py

# 訓練 SimpleCNN  
python train_simplecnn.py

# 訓練 ViT
python train_vit.py
```

## 注意事項

1. 模型權重檔案通常較大，建議使用 `.gitignore` 排除
2. 確保模型架構與權重檔案匹配
3. 可根據需要新增其他模型檔案
