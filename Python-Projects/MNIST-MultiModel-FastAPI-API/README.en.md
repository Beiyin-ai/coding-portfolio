# MNIST Multi-Model Inference FastAPI API

A multi-model inference API service for handwritten digit recognition (MNIST), built with FastAPI framework. Supports simultaneous inference with multiple deep learning models through a unified API interface.

## ✨ Features

- **Multi-model Support**: Load and run multiple model architectures simultaneously
- **Real-time Inference**: Accept image uploads and return multi-model inference results
- **Best Model Selection**: Automatically select results from the highest confidence model
- **Health Monitoring**: Service health check endpoints
- **CORS Support**: Cross-origin request support for frontend integration

## 🤖 Supported Model Types

1. **Custom Models** (PyTorch-based)
   - SimpleNN: Simple fully connected neural network
   - SimpleCNN: Convolutional neural network
   - ViT_Custom: Custom Vision Transformer

2. **HuggingFace Models** (transformers-based)
   - ViT_HF_4060: Fine-tuned ViT model
   - ViT_HF_BestTuned: Best fine-tuned version
   - ViT_ImageNet: Pretrained ImageNet model
   - ViT_3rd_MNIST: Third-party pretrained MNIST model

## 🚀 Quick Start

### Environment Setup

```bash
# Clone project
git clone <your-repo-url>
cd MNIST-MultiModel-FastAPI-API

# Install dependencies
pip install -r requirements.txt

# Set model path (optional)
export MODEL_DIR="./models"
```

### Start Service

```bash
python app.py
```

Service will start at `http://localhost:8000`.

## 📡 API Endpoints

### 1. Root - Service Information
```
GET /
```
Returns API basic information and loaded model list.

### 2. Health Check
```
GET /health
```
Checks service status, device information, and model count.

### 3. Model List
```
GET /models
```
Returns names of all available models.

### 4. Inference Endpoint
```
POST /predict
Content-Type: multipart/form-data
```
Upload image for inference.

**Example Request (curl):**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@test_image.png"
```

**Response Format:**
```json
{
  "success": true,
  "results": {
    "SimpleNN": {
      "model_name": "SimpleNN",
      "prediction": 7,
      "confidence": 0.95,
      "probabilities": [0.01, 0.02, ..., 0.95]
    }
  },
  "best_model": "SimpleNN",
  "best_prediction": 7
}
```

## 🏗️ Project Architecture

```
app.py                    # Main application
├── Model Definitions
│   ├── SimpleNN          # Simple neural network
│   ├── SimpleCNN         # Convolutional neural network
│   └── ViT_MNIST         # Vision Transformer
├── FastAPI Application
│   ├── Startup Events    # Model loading
│   ├── CORS Settings     # Cross-origin support
│   └── API Endpoints     # RESTful interfaces
└── Data Preprocessing
    └── MNIST Processing  # Image normalization
```

## 🔧 Tech Stack

- **Backend Framework**: FastAPI (async support)
- **Deep Learning**: PyTorch, HuggingFace Transformers
- **Image Processing**: OpenCV, Pillow
- **API Documentation**: Auto-generated Swagger UI

## 📊 Model Performance Comparison

| Model | Accuracy | Inference Speed | Features |
|-------|----------|-----------------|----------|
| SimpleNN | ~95% | Fastest | Lightweight, suitable for fast inference |
| SimpleCNN | ~98% | Fast | Balanced performance and speed |
| ViT_Custom | ~99% | Medium | Highest accuracy |
| ViT_HF | ~99.2% | Slower | Pretraining advantage |

## 📁 Directory Structure

```
MNIST-MultiModel-FastAPI-API/
├── app.py              # Main program
├── requirements.txt    # Dependencies
├── README.md          # Chinese documentation
├── README.en.md       # English documentation
├── models/            # Model weight files
│   ├── simple_nn_mnist.pth
│   ├── simple_cnn_mnist.pth
│   └── ...
├── docs/              # Documentation
│   ├── ARCHITECTURE.md
│   └── API_DOCS.md
└── tests/             # Test files
    └── test_api.py
```

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License
