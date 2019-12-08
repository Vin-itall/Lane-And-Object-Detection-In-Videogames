import time
import ImageGrab
import cv2
import numpy as np
from imageai.Detection import ObjectDetection

detector = ObjectDetection()

model_path = "Model/yolo.h5"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
print('Model Loaded')

def objectDetector(image):
    returned_image,detection = detector.detectObjectsFromImage(input_type="array",input_image=image,output_type="array")
    return returned_image

for i in range(5):
    time.sleep(1)
    print(i)
while(True):
    grabscreen = np.array(ImageGrab.grab(bbox=(50,50,800,600)))
    try:
        pimg = objectDetector(grabscreen)
        cv2.imshow('Capture',cv2.cvtColor(pimg, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    except TypeError:
        pass