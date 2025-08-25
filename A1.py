import cv2 as cv
import random

path = input("Enter the Image Path: ")

image = cv.imread(path)

# Phase 1
# print("Enter your choice: ")
def image_processing_basic(image, path):
    gray = None
    while True:
        op = input("\n\n1: Display Raw Image\n2: Grayscale Image Conversion\n3: Display Grayscale Image\n4: Save Raw Image\n5: Save Grayscale Image\nEnter your choice: ")
        if image is not None:
            if op == '1':
                cv.imshow("Raw Image", image)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif op == '2':
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                cv.imshow("Grayscale Image Conversion Successful", gray)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif op == '3':
                if gray is None:
                    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                cv.imshow("Grayscale Image", gray)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif op == '4':
                title = input("Enter Name: ")
                cv.imwrite(F"{title}.png", image)
            elif op == '5':
                if gray is None:
                    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                title = input("Enter Name: ")
                cv.imwrite(F"{title}.png", gray)
            elif op == '6':
                print("Exiting Application")
                return
            else:
                print("Wrong choice\nTry again!\n**************************\n")
        else:
            print("File could not be opened!")

# Phase 2
def image_processing_advanced(image, path):
    while True:
        print("\n***Image Flipping and Cropping***\n")
        op = input("1: Flip Menu\n2: Crop Menu\n3: Back to previous Menu\nEnter Your choice: ")
        if op == '1':
            flip(image)
        elif op == '2':
            cropped(image)
        elif op == '3':
            print("Exiting System")
            return
        else:
            print("Wrong Choice\nTry Again!")
# Helper function for advanced Image processing
def flip(image):
    while True:
        op = input("Flip Menu:\n1: Flip Horizontally\n2: Flip Vertically\n3: Flip Both ways\n4: Exit to previous menu\nEnter choice: ")
        if op == '1':
            flip_horizontal = cv.flip(image, 1)
            cv.imshow("Image flipped horizontally", flip_horizontal)
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif op == '2':
            flip_vertical = cv.flip(image, 0)
            cv.imshow("Image flipped vertically", flip_vertical)
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif op == '3':
            flip_both = cv.flip(image, -1)
            cv.imshow("Image flipped Both Direction", flip_both)
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif op == '4':
            print("Exiting to previous menu")
            return
        else:
            print("Wrong Choice\nTry Again!")

def cropped(image):
    h, w, _= image.shape
    mid_h = h//2
    mid_w = w//2
    while True:
        op = input("Crop Menu\n1: Crop top left\n2: Crop top right\n3: Crop bottom left\n4: Crop bottom right\n5: Enter custom dimensions\n6: Exit to previous menu\nEnter your choice: ")
        if op == '1':
            crop = image[0:mid_h, 0:mid_w]
            crop = cv.resizeWindow(crop, mid_h, mid_w)
            display("Top-left", crop)
        elif op == '2':
            crop = image[0:mid_h, mid_w: w]
            display("Top-right", crop)
        elif op == '3':
            crop = image[mid_h:h, 0:mid_w]
            display("Bottom-left", crop)
        elif op == '4':
            crop = image[mid_h: h, mid_w:w]
            display("Bottom-right", crop)
        elif op == '5':
            start_h = int(input("Enter starting point: "))
            end_h = int(input("Enter ending point: "))
            start_w = int(input("Enter starting width: "))
            end_w = int(input("Enter ending width: "))
            crop = image[start_h:end_h, start_w: end_w]
            display("Custom-crop", crop)
        elif op == '6':
            print("Exiting to previous menu")
            return
        else:
            print("Wrong Choice\nTry again!")


def display(title,image):
    if image is not None:
        cv.imshow(title, image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Image could not be opened")
    return





def main(image, path):
    print("\t********\n\tWelcome to Image Processing\n\t********\n")
    while True:
        op = input("\n1: Simple Image Processing\n2: Advanced Image Processing\n3: Exit System\nEnter your choice: ")
        if op == '1':
            image_processing_basic(image, path)
        elif op == '2':
            image_processing_advanced(image, path)
        elif op == '3':
            print("\n*********\nThanks for using our program\n")
            return
        else:
            print("\nWrong Input\nTry Again.\n**************\n")

main(image, path)

# image_processing_basic(image, path)
