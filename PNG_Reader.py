import imageio
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
        root = Tk()
        root.withdraw()
        root.lift()

        file_path = filedialog.askopenfilename()
        im = imageio.imread(file_path)
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

    elif op == "0":
        raise SystemExit

if __name__ == "__main__":
    main()

