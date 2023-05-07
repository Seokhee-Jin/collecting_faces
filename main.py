from ffhq_dataset.gen_aligned_image import FaceAlign
import cv2

if __name__ == "__main__":
    a = FaceAlign()
    b = cv2.imread("/Users/jinseokhee/Pictures/instagram/343973427_270575548657408_8881576880503537909_n.jpg")
    c = a.get_crop_image(b)
    cv2.imwrite("./test.jpg", c)

#