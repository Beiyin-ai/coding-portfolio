# ===========================================
# MNIST Multi-Model Inference Docker Image
# ===========================================
# CPU-Only Version - Optimized for deployment
# ===========================================

FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MODEL_DIR=/app/models \
    HF_HOME=/app/.cache/huggingface \
    TRANSFORMERS_CACHE=/app/.cache/huggingface \
    CUDA_VISIBLE_DEVICES=""

WORKDIR /app

# Install system dependencies (including curl for healthcheck)
# Note: libgl1-mesa-glx renamed to libgl1 in newer Debian
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download HuggingFace models to avoid runtime download
# This significantly speeds up container startup
RUN python -c "from transformers import ViTImageProcessor, ViTForImageClassification, pipeline; \
    print('Downloading google/vit-base-patch16-224...'); \
    ViTImageProcessor.from_pretrained('google/vit-base-patch16-224'); \
    ViTForImageClassification.from_pretrained('google/vit-base-patch16-224', num_labels=10, ignore_mismatched_sizes=True); \
    pipeline('image-classification', model='google/vit-base-patch16-224'); \
    print('Downloading farleyknight-org-username/vit-base-mnist...'); \
    ViTImageProcessor.from_pretrained('farleyknight-org-username/vit-base-mnist'); \
    ViTForImageClassification.from_pretrained('farleyknight-org-username/vit-base-mnist'); \
    print('All models downloaded successfully.')"

# Copy application code
COPY app.py .

# Create models directory
RUN mkdir -p /app/models

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
