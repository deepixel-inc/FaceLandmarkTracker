# FaceLandmarkTracker
[![Deepixel](https://img.shields.io/badge/Deepixel-Visit%20Website-blue?style=flat-square)](https://deepixel.xyz)
[![Get License](https://img.shields.io/badge/Get%20License-Contact%20Us-yellow)](#license)

`FaceLandmarkTracker` is a high-performance face landmark detection and tracking library built on **OpenCV** and **DeepCore (Deepixels proprietary library)**. It leverages TensorFlow Lite models for real-time face detection, landmark extraction, and head pose estimation. A Python wrapper is included for easy integration.

`FaceLandmarkTracker` outputs an array of **106 keypoints** corresponding to facial landmarks.
Each landmark has a fixed index, which you can use to identify facial regions such as eyes, nose, lips, and jawline.

Below is an illustration showing the **landmark indexing scheme**:

<img width="512" height="512" alt="result" src="https://github.com/user-attachments/assets/05862c02-4a6d-4654-a8b9-c96652170ec2" />

*(Example: numbers correspond to keypoint indices returned by `get_keypoints()`)*

---

## Features

* Real-time face landmark tracking
* Face bounding box extraction
* Head pose estimation
* Visibility confidence per keypoint
* Debug visualization of landmarks
* Easy Python integration
* Works on CPU only — no GPU required
* Supported Python versions: 3.9, 3.10, 3.11, 3.12

---

## Installation

Install via pip using the provided `.whl` file:

```bash
pip install deeppy-2.19.459-cp310-cp310-win_amd64.whl
```

> ⚠️ **Note:** This library requires an **active internet connection** to validate your license at runtime.

---


## Performance

`FaceLandmarkTracker` is optimized for real-time performance on CPU. Typical inference speeds:

| Environment                                | Resolution  | FPS  |
| ------------------------------------------ | ----------- | ----------|
| Noteboook CPU (Intel i7 11th Gen)          |  640x480    |   200     |
| Desktop CPU (Intel i7 11th Gen)            |  640x480    |   330     | 

* No GPU required — runs efficiently on modern CPUs
* Real-time performance with webcam streams
* Benchmarks may vary depending on CPU model and input resolution

> ⚠️ **Note:** Performance may be slightly lower when displaying debug visualization.

---

## Python Usage
1. Example Python code for capturing and processing a live camera stream.

```python
import cv2
from deeppy import FaceLandmarkTracker

def run_face_tracker_camera():
    dp_face = FaceLandmarkTracker()
    dp_face.init()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        dp_face.run(frame, 0.2, False)
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
    run_face_tracker_camera()
```


2. Example Python code for processing from images.

```python
import cv2
from deeppy import FaceLandmarkTracker

def run_face_tracker_image(image_paths):
    dp_face = FaceLandmarkTracker()
    dp_face.init()

    for path in image_paths:
        frame = cv2.imread(path)
        if frame is None:
            print("Failed to load image.")
            return
    
        dp_face.run(frame, 0.2, True)
        print("Keypoints:", dp_face.get_keypoints())
        print("Rect:", dp_face.get_rect())
        print("Pose:", dp_face.get_pose())

        frame = dp_face.display_debug(frame)
        cv2.imshow("FaceLandmarkTracker", frame)

        if cv2.waitKey(0) & 0xFF == 27:  # ESC key
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_paths = ["example.jpg","example2.jpg"]
    run_face_tracker_image(image_paths)
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
* `fThresh` – confidence threshold, the common value is around 0.2
* `isStill` – whether image is static

### Get Results

```python
keypoints = get_keypoints()
rect = get_rect()
visibility = get_visibility()
pose = get_pose()
```

* `get_keypoints()` – returns 106 x 2 array of facial landmarks
* `get_rect()` – returns bounding box `[x, y, width, height]` where x,y is the top left corner of the bounding box.
* `get_visibility()` – visibility confidence per landmark
* `get_pose()` – estimated head pose `[pitch, yaw, roll]`

### Visualization

```python
image_out = display_debug(image_src)
```

* Draws landmarks, bounding boxes, and pose axes on the image

---




## License

This library is **proprietary and requires a paid license**. You may **not use, distribute, or modify** it without a valid license.  
An active internet connection is required at runtime for license validation.  


### How to Get a License

* Contact us via email: [support@deepixels.xyz](mailto:support@deepixels.xyz)


