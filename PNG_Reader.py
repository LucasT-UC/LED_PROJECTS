import imageio, os
import numpy as np
from tkinter import filedialog, Tk

def main():
    print("----------------------------")
    print("\n 1. Select PNG (16x16)")
    print(" 0. EXIT\n")
    op = input("Select option: ")
    print(op)
    print(type(op))
    if op == "1":
        directory = "C:\Users\ltapi\Desktop\Universidad\Fun\LED_PROJECTS\input"
        for f in os.listdir(directory):
            f = os.path.join(directory, f)
            send_image(f)
    elif op == "0":
        raise SystemExit


def send_image(f):
    im = imageio.imread(f)
    dimensions = im.size//256
    pixels = np.zeros((16, 16, 3))
    if dimensions == 3 or dimensions == 4:
        for y in range(len(im)):
            for x in range(len(im[y])):
                pixels[y][x][0] = im[x][y][0]
                pixels[y][x][1] = im[x][y][1]
                pixels[y][x][2] = im[x][y][2]
        print(pixels)
    else:
        print(f"Can't read a png with {dimensions} data values")
    
if __name__ == "__main__":
    main()
