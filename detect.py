from ultralytics import YOLO
import cv2
from pathlib import Path

# ✅ Correct model path
model_path = Path("runs/detect/runs/driver_behavior7/weights/best.pt").resolve()
print("Loading model from:", model_path)

model = YOLO(str(model_path))

cap = cv2.VideoCapture(0)  # webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.4)
    annotated_frame = results[0].plot()

    cv2.imshow("Driver Behavior Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
