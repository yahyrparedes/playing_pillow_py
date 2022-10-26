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
        rotate: Rote image in any angle 
        """
        # angle = 45
        # new_image = image.rotate(angle, expand=True )  # rote the image in angle indicate

        """
        transpose: Rotate in angle constant
        # Image.ROTATE_90
        # Image.ROTATE_180
        # Image.ROTATE_270
        """
        angle = Image.ROTATE_180
        new_image = image.transpose(angle)  # rote the image in angle indicate

        """
        show: Display image
        """
        new_image.show()

        """
        save: Save image
        """
        new_image.save(f'images/liger_zero_schneider_{angle}.jpg')



    except FileNotFoundError as error:
        print('Image not found!')


if __name__ == '__main__':
    work_whit_images()
