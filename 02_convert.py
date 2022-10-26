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
        convert: Convert images between different pixel representations “L”, “RGB” and “CMYK.”
        """
        new_image = image.convert('L')  # convert to gray scale

        """
        show: Display image
        """
        new_image.show()

        """
        save: Save image
        """
        new_image.save('images/liger_zero_schneider_gray.jpg')



    except FileNotFoundError as error:
        print('Image not found!')


if __name__ == '__main__':
    work_whit_images()
