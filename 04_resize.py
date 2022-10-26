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
        resize: 
        """
        width, height = image.size  # obtain image size

        # now go resize ten times
        n_width = width // 10  # int
        n_height = height // 10  # int

        new_image = image.resize((n_width, n_height))  # new size for image

        """
        show: Display image
        """
        new_image.show()

        """
        save: Save image
        """
        new_image.save(f'images/liger_zero_schneider_{n_width}x{n_height}.jpg')



    except FileNotFoundError as error:
        print('Image not found!')


if __name__ == '__main__':
    work_whit_images()
