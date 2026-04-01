<div align="center">

<h1>🚗 Driver Behavior Detection using YOLOv8</h1>

<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-CUDA%20Enabled-orange?style=for-the-badge&logo=pytorch&logoColor=white"/>
</p>

<p>
  A real-time <strong>Driver Monitoring System (DMS)</strong> built with <strong>YOLOv8 + Computer Vision</strong> to detect driver activities and flag unsafe driving behaviors such as texting, phone usage, or drinking — in real time.
</p>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Classes Detected](#-classes-detected)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Results](#-results)
- [License](#-license)

---

## 🧠 Overview

This project uses a **custom-trained YOLOv8 object detection model** to classify and detect different driver behaviors from images, videos, or live webcam input.

The goal is to improve **road safety** by identifying distracted driving patterns in real time using deep learning and computer vision techniques.

---

## ✨ Features

- 🔍 **Real-time detection** — Live webcam-based driver behavior recognition
- 🎥 **Multi-source support** — Works with webcam feed, image files, and video files
- ⚡ **GPU-accelerated** — CUDA-enabled training and inference for high speed
- 📦 **Custom dataset training** — Supports custom annotated datasets via `data.yaml`
- 🧠 **Multi-class detection** — Identifies multiple driver actions simultaneously
- 📊 **Bounding box visualization** — Annotated output with class labels and confidence scores

---

## 🏷️ Classes Detected

| Class ID | Behavior             |
|:--------:|----------------------|
| 0        | 🥤 Drinking           |
| 1        | 💄 Hair and Make-up   |
| 2        | 📻 Operating the Radio |
| 3        | ✅ Safe Driving        |
| 4        | 📱 Talking on Phone    |
| 5        | 🗣️ Talking with Someone |
| 6        | 💬 Texting Phone       |
| 7        | 🔄 Turning             |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics) | Object detection model |
| Python 3.8+ | Core programming language |
| OpenCV | Video/image processing |
| PyTorch (CUDA) | Deep learning backend |
| VS Code | Development environment |

---

## 📂 Project Structure

```
driver_behavior_yolov8/
│
├── dataset/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   └── data.yaml
│
├── runs/                  # Training outputs (weights, metrics)
├── venv/                  # Virtual environment
├── train.py               # Model training script
├── detect.py              # Inference script (image/video/webcam)
├── requirements.txt       # Python dependencies
├── yolov8n.pt             # Pretrained YOLOv8 base model
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/driver_behavior_yolov8.git
cd driver_behavior_yolov8
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare Your Dataset

Organize your dataset as shown in the project structure and configure `dataset/data.yaml`:

```yaml
path: ./dataset
train: train/images
val: valid/images
test: test/images

nc: 8
names:
  - Drinking
  - Hair and Make-up
  - Operating the Radio
  - Safe Driving
  - Talking on Phone
  - Talking with Someone
  - Texting Phone
  - Turning
```

### 4. Train the Model

```bash
python train.py
```

### 5. Run Detection

```bash
# On an image
python detect.py --source path/to/image.jpg

# On a video
python detect.py --source path/to/video.mp4

# On live webcam
python detect.py --source 0
```

---

## 📊 Results

- ✅ Real-time detection with bounding boxes and class labels
- ⚡ High-speed inference using GPU acceleration
- 🎯 Accurate classification across 8 driver behavior categories
- 📈 Training metrics (loss, mAP) saved under `runs/`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ using YOLOv8 and Python | Made for Road Safety</sub>
</div>
