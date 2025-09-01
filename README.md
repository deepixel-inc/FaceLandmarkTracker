# FaceLandmarkTracker

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-Proprietary-red)
![Commercial](https://img.shields.io/badge/Commercial%20License-Required-orange)
[![Get License](https://img.shields.io/badge/Get%20License-Contact%20Us-yellow)](#license)

`FaceLandmarkTracker` is a high-performance face landmark detection and tracking library built on **OpenCV** and **DeepCore (Deepixels proprietary library)**. It leverages TensorFlow Lite models for real-time face detection, landmark extraction, and head pose estimation. A Python wrapper is included for easy integration.

---

## Features

* Real-time face landmark tracking
* Face bounding box extraction
* Head pose estimation
* Visibility confidence per keypoint
* Debug visualization of landmarks
* Easy Python integration

---

## Installation

Install via pip using the provided `.whl` file:

```bash
pip install FaceLandmarkTracker-<version>-py3-none-any.whl
```

> ⚠️ **Note:** This library is **proprietary and paid**. You must have a valid license to use it.

---

## Python Usage

```python
import cv2
from deeppy import FaceLandmarkTracker

def run_face_tracker():
    dp_face = FaceLandmarkTracker()
    dp_face.init("head_lite.tflite", "face_v7_7_lite.tflite")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        dp_face.run(frame, 0.1, False)
        print("Keypoints:", dp_face.get_keypoints())
        print("Rect:", dp_face.get_rect())
        print("Pose:", dp_face.get_pose())

        frame = dp_face.display_debug(frame)
        cv2.imshow("FaceLandmarkTracker", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_face_tracker()
```

---

## API Reference

### Initialization

```python
bool init()
```
* Returns `True` if models loaded successfully


### Tracking

```python
run(image_src, fThresh, isStill)
```

* `image_src` – input image (numpy array)
* `fThresh` – confidence threshold
* `isStill` – whether image is static

### Get Results

```python
keypoints = get_keypoints()
rect = get_rect()
visibility = get_visibility()
pose = get_pose()
```

### Visualization

```python
image_out = display_debug(image_src)
```

* Draws landmarks, bounding boxes, and pose axes on the image

---

## Landmark Indexing

`FaceLandmarkTracker` outputs an array of **106 keypoints** corresponding to facial landmarks.
Each landmark has a fixed index, which you can use to identify facial regions such as eyes, nose, lips, and jawline.

Below is an illustration showing the **landmark indexing scheme**:

<img width="512" height="512" alt="result" src="https://github.com/user-attachments/assets/05862c02-4a6d-4654-a8b9-c96652170ec2" />
*(Example: numbers correspond to keypoint indices returned by `get_keypoints()`)*


## License

This library is **proprietary and requires a paid license**. You may **not use, distribute, or modify** it without a valid license.

### How to Get a License

* Contact us via email: [sales@deepixels.com](mailto:sales@deepixels.com)
* Provide your organization name and intended use case
* We will provide license terms and pricing

> ![Get License](https://img.shields.io/badge/Get%20License-Contact%20Us-yellow)

---
