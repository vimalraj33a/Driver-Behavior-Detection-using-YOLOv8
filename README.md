# Driver-Behavior-Detection-using-YOLOv8
This project uses a custom-trained YOLOv8 object detection model to classify and detect different driver behaviors from images, videos, or live webcam input.  The goal is to improve road safety by identifying distracted driving patterns in real time.
Here’s a **professional GitHub README.md** for your project — clean, structured, and ready to impress recruiters 👇
You can copy-paste directly into your repo.

---

 🚗 Driver Behavior Detection using YOLOv8

A real-time **Driver Monitoring System (DMS)** built using **YOLOv8 and Computer Vision** to detect driver activities and identify unsafe behaviors such as texting, drinking, or phone usage.

---

Project Overview

This project uses a **custom-trained YOLOv8 object detection model** to classify and detect different driver behaviors from images, videos, or live webcam input.

The goal is to improve **road safety** by identifying distracted driving patterns in real time.

---

 Features

* 🔍 Real-time driver behavior detection
* 🎥 Works with webcam, images, and videos
* ⚡ GPU-accelerated training and inference
* 📦 Custom dataset training support
* 🧠 Detects multiple driver actions simultaneously

---

Classes Detected

| Class ID | Behavior             |
| -------- | -------------------- |
| 0        | Drinking             |
| 1        | Hair and Make-up     |
| 2        | Operating the Radio  |
| 3        | Safe Driving         |
| 4        | Talking on Phone     |
| 5        | Talking with Someone |
| 6        | Texting Phone        |
| 7        | Turning              |

---

🛠 Tech Stack

* **YOLOv8 (Ultralytics)**
* **Python**
* **OpenCV**
* **PyTorch (CUDA Enabled)**
* **VS Code**

---

📂 Project Structure

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
├── runs/
├── venv/
├── train.py
├── detect.py
├── requirements.txt
├── yolov8n.pt
└── README.md
```
📊 Results

* Real-time detection with bounding boxes and labels
* High-speed inference using GPU
* Accurate classification of driver behaviors


