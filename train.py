import torch
from ultralytics import YOLO
from pathlib import Path

def train_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    data_yaml = Path("dataset/data.yaml").resolve()
    print("Using dataset:", data_yaml)

    model = YOLO("yolov8n.pt")

    model.train(
        data=str(data_yaml),
        epochs=50,
        imgsz=640,
        batch=8,
        device=device,
        project="runs",
        name="driver_behavior"
    )

if __name__ == "__main__":
    train_model()
