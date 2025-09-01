import cv2 as cv
import random



# Phase 1
# Image basic processing
def image_processing_basic(image, path):
    gray = None
    while True:
        op = input("\n\n1: Display Raw Image\n2: Grayscale Image Conversion\n3: Display Grayscale Image\n4: Save Raw Image\n5: Save Grayscale Image\n6: Exit to previous menu\nEnter your choice: ")
        if image is not None:
            if op == '1':
                display("Raw Image", image)
                # cv.imshow("Raw, Image", image)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
            elif op == '2':
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                display("Grayscale Image Conversion Succeessful")
                # cv.imshow("Grayscale Image Conversion Successful", gray)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
            elif op == '3':
                if gray is None:
                    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                display("Grayscale Image", image)
                # cv.imshow("Grayscale Image", gray)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
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
# ***********************************************************************************************************************************
# Phase 2
# Image transformation
def image_processing_advanced(image, path):
    while True:
        print("\n***Image Flipping and Cropping***\n")
        op = input("1: Flip Menu\n2: Crop Menu\n3: Rotate Image\n4: Resize Menu\n5: Back to previous Menu\nEnter Your choice: ")
        if op == '1':
            flip(image)
        elif op == '2':
            cropped(image)
        elif op == '3':
            rotate(image)
        elif op == '4':
            resized_function(image)
        elif op == '5':
            print("Exitig system")
            return
        else:
            print("Wrong Choice\nTry Again!")
# Helper function for advanced Image processing
    # Flip image
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

    # crop image
def cropped(image):
    h, w, _= image.shape
    mid_h = h//2
    mid_w = w//2
    while True:
        op = input("Crop Menu\n1: Crop top left\n2: Crop top right\n3: Crop bottom left\n4: Crop bottom right\n5: Enter custom dimensions\n6: Exit to previous menu\nEnter your choice: ")
        if op == '1':
            new_image = image[0:mid_h, 0:mid_w]
            # crop = cv.resizeWindow(crop, mid_h, mid_w)
            resize_window_only(new_image, mid_w - 0 ,mid_h - 0 )
        elif op == '2':
            new_image = image[0:mid_h, mid_w: w]
            resize_window_only(new_image, mid_w - w, mid_h - 0)
            # display("Top-right", crop)
        elif op == '3':
            new_image = image[mid_h:h, 0:mid_w]
            resize_window_only(new_image, mid_w - 0, h - mid_h)
            # display("Bottom-left", crop)
        elif op == '4':
            new_image = image[mid_h: h, mid_w:w]
            resize_window_only(new_image, w - mid_w, h - mid_h)
            # display("Bottom-right", crop)
        elif op == '5':
            start_h = int(input("Enter starting height: "))
            end_h = int(input("Enter ending height: "))
            start_w = int(input("Enter starting width: "))
            end_w = int(input("Enter ending width: "))
            new_image = image[start_h:end_h, start_w: end_w]
            resize_window_only(new_image, end_w - start_w, end_h - start_h)
            # display("Custom-crop", crop)
        elif op == '6':
            print("Exiting to previous menu")
            return
        else:
            print("Wrong Choice\nTry again!")

    # helper function to practice DRY
def display(title,image):
    if image is not None:
        cv.imshow(title, image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Image could not be opened")
        return


def resize_window_only(image, w, h):
    cv.namedWindow("Cropped Window", cv.WINDOW_NORMAL)
    cv.resizeWindow("Cropped Window",w, h )
    display("Cropped Window", image)



    # Rotate
def rotate(image):
    h, w, _ = image.shape
    center = (w//2, h//2)
    angle = int(input("Enter the rotation angle: "))
    scale = float(input("Enter the scale while rotation: "))
    size_change = input("Do you want to interchange the dimensions(y/n): ")
    Matrix = cv.getRotationMatrix2D(center, angle, scale)
    if size_change.lower() == 'y':
        # Matrix = cv.getRotationMatrix2D(center, angle, scale)
        rotated_image = cv.warpAffine(image, Matrix, (w,h))
        display("Rotated Image with original dimensions", rotated_image)
    else:
        rotated_image = cv.warpAffine(image, Matrix, (h,w))
        display("Rotated Image with interchanged dimensions",rotated_image)

def resized_function(image):
    while True:
        op = input("1: Window Resize\n2: Image resize\n3: Back to previous menu\nEnter your choice: ")
        if op == '1':
            w = int(input("Enter Width: "))
            h = int(input("Enter Height: "))
            cv.namedWindow("Resized Window", cv.WINDOW_NORMAL)
            cv.resizeWindow("Resized Window",w, h )
            display("Resized Window", image)
        elif op == '2':
            w = int(input("Enter Width: "))
            h = int(input("Enter Height: "))
            resized_image = cv.resize(image, (w,h))
            display("Resized Image", resized_image)
        elif op == '3':
            print("Returning to previous menu")
            return
        else:
            print("Wrong Input\nTry Again.")

# ***********************************************************************************************************************************
# Phase 3






# ***********************************************************************************************************************************


def main():
    print("\t********\n\tWelcome to Image Processing\n\t********\n")
    while True:
        path = input("Enter the Image Path: ")
        image = cv.imread(path)
        if image is None:
            print("Something went wrong")
            continue
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

main()

# image_processing_basic(image, path)
# E:\f21 pro\IMG_20220721_124444.jpg
