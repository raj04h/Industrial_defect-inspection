import cv2
from ultralytics import YOLO

# Load your model
model = YOLO("yolo26m-seg.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not open webcam")
    exit()

print("Webcam opened successfully")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Failed to read frame")
        break

    # YOLO segmentation inference
    results = model.predict(
        source=frame,
        imgsz=640,
        conf=0.25,
        verbose=False
    )

    # Draw boxes + segmentation masks
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO26m-Seg Webcam", annotated_frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()