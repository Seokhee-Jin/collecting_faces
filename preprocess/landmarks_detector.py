import dlib
import cv2
import os

# cur_dir = os.path.split(os.path.realpath(__file__))[0]
# model_path = os.path.join(cur_dir, "preprocess",'shape_predictor_68_face_landmarks.dat')

class LandmarksDetector:
    print(os.getcwd())
    def __init__(self, predictor_model_path="/Users/jinseokhee/PycharmProjects/collecting_faces/preprocess/shape_predictor_68_face_landmarks.dat"):
        """
        :param predictor_model_path: path to shape_predictor_68_face_landmarks.dat file
        """
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(predictor_model_path)

    def get_landmarks(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        dets = self.detector(gray, 1)

        for detection in dets:
            try:
                face_landmarks = [(item.x, item.y) for item in self.shape_predictor(gray, detection).parts()]
                yield face_landmarks
            except:
                print("Exception in get_landmarks()!")

