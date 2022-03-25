import imageio, os
import numpy as np

def corner_pixel(pixels, col, row, size):
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
    r_av = (vertical_pixel[0] + horizontal_pixel[0])/2
    g_av = (vertical_pixel[1] + horizontal_pixel[1])/2
    b_av = (vertical_pixel[2] + horizontal_pixel[2])/2
    return (r_av, g_av, b_av)


def horizontal_pixel(pixels, col, row, size):
    if row == 0:
        side_pixel = pixels[col][row+1]
    else:
        side_pixel = pixels[col][row-1]
    left_pixel = pixels[col-1][row]
    right_pixel = pixels[col+1][row]
    r_av = (side_pixel[0] + left_pixel[0] + right_pixel[0])/3
    g_av = (side_pixel[1] + left_pixel[1] + right_pixel[1])/3
    b_av = (side_pixel[2] + left_pixel[2] + right_pixel[2])/3
    return (r_av, g_av, b_av)
    


def vertical_pixel(pixels, col, row, size):
    if col == 0:
        side_pixel = pixels[col+1][row]
    else:
        side_pixel = pixels[col-1][row]
    top_pixel = pixels[col][row-1]
    bot_pixel = pixels[col][row+1]
    r_av = (side_pixel[0] + top_pixel[0] + bot_pixel[0])/4
    g_av = (side_pixel[1] + top_pixel[1] + bot_pixel[1])/4
    b_av = (side_pixel[2] + top_pixel[2] + bot_pixel[2])/4
    return (r_av, g_av, b_av)

def regular_pixel(pixels, col, row, size):
    left_pixel = pixels[col-1][row]
    right_pixel = pixels[col+1][row]
    top_pixel = pixels[col][row-1]
    bot_pixel = pixels[col][row+1]
    r_av = (left_pixel[0] + right_pixel[0] + top_pixel[0] + bot_pixel[0])/4
    g_av = (left_pixel[1] + right_pixel[1] + top_pixel[1] + bot_pixel[1])/4
    b_av = (left_pixel[2] + right_pixel[2] + top_pixel[2] + bot_pixel[2])/4
    return (r_av, g_av, b_av)



def resize_image(f, set_to):
    im = imageio.imread(f)
    width, height, dimensions = im.shape
    size = (width, height)
    if width != set_to and height != set_to:
        pixels = np.zeros((16, 16, 3))
        for row in range(len(im)):
            for col in range(len(row)):
                if (row == 0 or row == height) and (col == 0 or col == width):
                    pixels[col][row] = corner_pixel(im, col, row, size)
                elif (row == 0 or row == height) and (col != 0 and col != width):
                    pixels[col][row] = horizontal_pixel(im, col, row, size)
                elif (col == 0 or col == width) and (row != 0 and row != height):
                    pixels[col][row] = vertical_pixel(im, col, row, size)

def main():
    directory = "C:\\Users\\ltapi\\Desktop\\Universidad\\Fun\\LED_PROJECTS\\input"
    set_to = 16
    for f in os.listdir(directory):
        f = os.path.join(directory, f)
        resize_image(f, set_to)




if __name__ == '__main__':
    main()