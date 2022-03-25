import imageio, os
import numpy as np
from PIL import Image
from tkinter import filedialog, Tk

def main():
    print("----------------------------")
    print("\n 1. Run input images")
    print(" 0. EXIT\n")
    op = input("Select option: ")
    print(op)
    print(type(op))
    if op == "1":
        directory = "C:\\Users\\ltapi\\Desktop\\Projects\\LED_PROJECTS\\input"
        for f in os.listdir(directory):
            file_name = f
            f = os.path.join(directory, f)
            f = format_image(f, file_name)
            #order_pixels(f)
    elif op == "0":
        raise SystemExit


def format_image(f, file_name):
    im = Image.open(f)
    print(im.size)
    im = im.resize((16, 16))
    print(im.mode)
    im = im.rotate(90)
    dimensions = 4
    if "RGB" in im.mode:
        if im.mode =="RGB":
            dimensions = 3
        im = np.asarray(im)
        try_this(im, dimensions, file_name)
        return im
        
        
def try_this(image, d, file_name):
    for i in range(16):
        if i % 2 == 0:
            new = np.zeros((16, d), dtype="uint8")
            for l in range(16):
                new[l] = image[i][l]
            print(new)
            for l in range(16):
                image[i][l] = new[15-l]
    im = Image.fromarray(image)
    im = im.rotate(270)
    im.save(f"output\\{file_name}")


    return image
def invert_lines(pixels, d):
    for i in range(16):
        if i % 2 == 1:
            print(pixels[i])
            for x in range(16):
                new = np.zeros((16, d), dtype="uint8")
                
                new[x] = pixels[x, i]
            new = np.flip(new)
            for x in range(16):
                pixels[x, i] = new[x]

def switch_pixels(pixels):
    new = pixels
    print("NEWWWW: ", new)
    for i in range(len(pixels)):
        pixels[i] = new[len(pixels)-i-1]
    return pixels



def order_pixels(image):
    for i in range(16):
        if i % 2 == 0:
            print("HAPPENSSSSS")
            temp_pixs = [[0, 0, 0, 0]] * 16
            for c in range(16):
                temp_pixs[c] = image[c][i]
            print(temp_pixs)
            for z in range(16):
                image[z, i] = temp_pixs[15-z]
    
    
if __name__ == "__main__":
    main()
