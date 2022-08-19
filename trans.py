from PIL import Image 

def get_gray(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b 
    return gray

def get_pixel_color(pic_in,  pixels_x, pixels_y):
    img = Image.open(pic_in)
    w, h = img.size
    pixel_width=w/pixels_x
    pixel_height=h/pixels_y
    for j in range(pixels_y):
        print("    - [",end="")
        for i in range(pixels_x):
            rgb_s=img.getpixel((pixel_width/2+i*pixel_width, pixel_height/2+j*pixel_height))
            print(int(get_gray(*rgb_s)/10),end=",")
        print("]")

if __name__ == '__main__':
    pic_in = input("input image file:")
    pixels_num_x =int(input("input pixels_num_x:"))
    pixels_num_y =int(input("input pixels_num_y:"))
    get_pixel_color(pic_in,  pixels_num_x, pixels_num_y)