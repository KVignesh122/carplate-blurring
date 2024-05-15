from os.path import basename, splitext
import os
import cv2
import argparse
from detector import create_detector


def parse_args():
    parser = argparse.ArgumentParser(description="Blur carplates in images")
    parser.add_argument('image_path', type=str, help='Path to the input image')
    return parser.parse_args()


def main():
    args = parse_args()
    image_path = args.image_path
    directory_path = os.path.dirname(image_path)
    
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        print("\n< ERROR: Unable to read image file. >")
        return

    # Create and destroy HarCascade XML file
    harcascade = create_detector()
    plate_detector = cv2.CascadeClassifier(harcascade)
    os.remove(harcascade)

    min_area = 500
    plates = plate_detector.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            plate_img = image[y:y + h, x:x + w]
            blurred_plate = cv2.GaussianBlur(plate_img, (31, 31), 50)
            image[y:y + h, x:x + w] = blurred_plate

    save_path = os.path.join(directory_path, f'{splitext(basename(image_path))[0]}_blurred.jpg')
    cv2.imwrite(save_path, image)
    return


if __name__ == '__main__':
    main()
