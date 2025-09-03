
from deeppy import FaceLandmarkTracker
import cv2

# Initailize tracking class
dp_face = FaceLandmarkTracker()

# Load license
license_path = "dp_face_2025.lic"
dp_face.init(license_path)

# Load frame from camera and process
def camera_example():
    cap = cv2.VideoCapture(0)

    while(1):
        ret, image = cap.read()
        if not ret:
            break
        dp_face.run(image,0.1,False)
        
        print(dp_face.get_keypoints())
        print("Rect : ", dp_face.get_rect())
        print("Pose : ", dp_face.get_pose())
        image = dp_face.display_debug(image)

        cv2.imshow("reslt", image)
        if cv2.waitKey(1) == 27:
            break

# Load frame from video and process
def video_example(video_path):
    cap = cv2.VideoCapture(video_path)

    while(1):
        ret, image = cap.read()
        if not ret:
            break
        dp_face.run(image,0.1,False)
        
        print(dp_face.get_keypoints())
        print("Rect : ", dp_face.get_rect())
        print("Pose : ", dp_face.get_pose())
        image = dp_face.display_debug(image)

        cv2.imshow("reslt", image)
        if cv2.waitKey(1) == 27:
            break

# Load frame from images and process
def image_example(image_paths):

    for path in image_paths:
        image = cv2.imread(path)
        if image is None:
            break
        dp_face.run(image,0.1,False)
        
        print(dp_face.get_keypoints())
        print("Rect : ", dp_face.get_rect())
        print("Pose : ", dp_face.get_pose())
        image = dp_face.display_debug(image)

        cv2.imshow("result", image)
        if cv2.waitKey(0) == 27:
            break

# Main Process
if __name__ == "__main__":
    image_paths = [r"rsc/thispersondoesnotexist.jpg"]
    image_example(image_paths)
