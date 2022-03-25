from turtle import right
import imageio, os
import numpy as np
from PIL import Image

def average_pixel(pixels, dimensions):
    values = []
    print("Dimensions:", dimensions)
    for d in range(dimensions):
        avg = 0
        for pix in pixels:
            avg += int(pix[d])
        values.append(int(avg/len(pixels)))
    return tuple(values)


def corner_pixel(pixels, col, row, dimensions):
    if col == 0:
        if row == 0: #top left corner
            vertical_pixel = pixels[col+1][row]
            horizontal_pixel = pixels[col][row+1]
        else: #bottom left corner
            vertical_pixel = pixels[col+1][row]
            horizontal_pixel = pixels[col][row-1]
    else:
        if row == 0: #top right corner
            vertical_pixel = pixels[col-1][row]
            horizontal_pixel = pixels[col][row+1]
        else: # bottom right corner
            vertical_pixel = pixels[col-1][row]
            horizontal_pixel = pixels[col][row-1]
    values = average_pixel([vertical_pixel, horizontal_pixel], dimensions)
    return values


def horizontal_pixel(pixels, col, row, dimensions):
    if row == 0:
        side_pixel = pixels[col][row+1]
    else:
        side_pixel = pixels[col][row-1]
    left_pixel = pixels[col-1][row]
    right_pixel = pixels[col+1][row]
    values = average_pixel([side_pixel, left_pixel, right_pixel], dimensions)
    return values


def vertical_pixel(pixels, col, row, dimensions):
    if col == 0:
        side_pixel = pixels[col+1][row]
    else:
        side_pixel = pixels[col-1][row]
    top_pixel = pixels[col][row-1]
    bot_pixel = pixels[col][row+1]
    values = average_pixel([side_pixel, top_pixel, bot_pixel], dimensions)
    return values


def regular_pixel(pixels, col, row, dimensions):
    left_pixel = pixels[col-1][row]
    right_pixel = pixels[col+1][row]
    top_pixel = pixels[col][row-1]
    bot_pixel = pixels[col][row+1]
    values = average_pixel([left_pixel, right_pixel, top_pixel, bot_pixel], dimensions)
    return values



def resize_image(im, set_to):
    (width, height, dimensions) = im.shape
    size = (width, height)
    pixels = np.zeros((set_to, set_to, 4))
    for row in range(len(im)):
        for col in range(len(im[row])):
            if (row == 0 or row == height-1) and (col == 0 or col == width-1):
                print("Doing corner!")
                pixels[col][row] = corner_pixel(im, col, row, dimensions)
            elif (row == 0 or row == height-1) and (col != 0 and col != width-1):
                print("Doing horizontal pixel")
                print("COL, ROW: ", col, row)
                pixels[col][row] = horizontal_pixel(im, col, row, dimensions)
            elif (col == 0 or col == width-1) and (row != 0 and row != height-1):
                print("Doing vertical pixel")
                pixels[col][row] = vertical_pixel(im, col, row, dimensions)
            else:
                print("Doing regular pixel")
                pixels[col][row] = regular_pixel(im, col, row, dimensions)
    return pixels
    

def main():
    directory = "C:\\Users\\ltapi\\Desktop\\Projects\\LED_PROJECTS\\input"
    set_to = 16
    for f in os.listdir(directory):
        file_name = f
        f = os.path.join(directory, f)
        im = Image.open(f)
        print(im.mode)
        im = np.asarray(im)
        pixels = resize_image(im, set_to)
        im = Image.fromarray(pixels)
        im.save(f"output\\{file_name}")


if __name__ == '__main__':
    main()