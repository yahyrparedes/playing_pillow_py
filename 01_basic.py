from PIL import Image


## work images
def work_whit_images():
    # Remember use try and except

    try:
        """
        open: Load image in memory
        """
        image = Image.open('images/liger_zero_schneider.jpeg')

        """
        size: Get dimens for images
        """
        width, height = image.size  # tupla (w, h)
        print(f'Image width is {width}')  # ancho
        print(f'Image height is {height}')  # alto

        """
        mode: Get mode ("1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr")
        jpg = RGB (red green blue)
        png = RGBA (red green blue alpha)
        """
        mode = image.mode  # str
        print(f'Image mode is {mode}')

        """
        format: Display format (JPG-PNG-JPEG-)
        """
        format = image.format
        print(f'Image format is {format}')

        """
        show: Display image
        """
        image.show()

    except FileNotFoundError as error:
        print('Image not found!')


def show_dimens_image():
    image = Image.open('images/liger_zero_schneider.jpeg')
    return image.size


if __name__ == '__main__':
    work_whit_images()
