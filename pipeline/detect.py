from ultralytics import YOLO
from emit import emit_person_event
import cv2

model = YOLO("yolov8n.pt")

CAMERA_ZONES = {
    "cam1": "skincare",
    "cam2": "makeup",
    "cam3": "entrance",
    "cam4": "stockroom",
    "cam5": "checkout"
}


def process_video(video_path, camera_id):

    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        frame_count += 1

        if frame_count % 30 != 0:
            continue

        results = model(frame, verbose=False)

        people = 0

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                if class_id == 0:
                    people += 1

        print(
            f"{camera_id} | Frame {frame_count}: "
            f"{people} people detected"
        )

        if people > 0:

            emit_person_event(
                store_id="purplle_001",
                camera_id=camera_id,
                frame_number=frame_count,
                people_count=people,
                zone=CAMERA_ZONES[camera_id]
            )

    cap.release()

    print(f"Finished {camera_id}")


if __name__ == "__main__":

    videos = [
        ("../data/CAM 1.mp4", "cam1"),
        ("../data/CAM 2.mp4", "cam2"),
        ("../data/CAM 3.mp4", "cam3"),
        ("../data/CAM 4.mp4", "cam4"),
        ("../data/CAM 5.mp4", "cam5")
    ]

    for video_path, camera_id in videos:

        print(f"\nProcessing {camera_id}")

        process_video(video_path, camera_id)