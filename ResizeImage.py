from PIL import Image
from resizeimage import resizeimage
import os


def initial_image_folder():
    '''
    Set the initial photo for your image
    :return: String Folder Location
    '''
    return 'GivenImages'
def output_image_folder():
    '''
    Set the output for your updated photos
    :return: String Folder Location
    '''
    return 'OutputImages'

def create_input_folder():
    '''
    Creates folder for input images
    '''
    os.mkdir(initial_image_folder())

def create_output_folder():
    '''
    Creates folder for output
    '''
    os.mkdir(output_image_folder())

def image_demensions(height, width):
    return [round(height*.15),round(width*.15)]


def main():

    #Test if folders exist
    if not os.path.exists(output_image_folder()):
        create_output_folder()
    if not os.path.exists(initial_image_folder()):
        create_input_folder()

    #iterate through initial image folder
    for file in os.listdir(initial_image_folder()):

        #Creates file names
        file_name_input =  initial_image_folder()+'\\' + file
        file_name_output = output_image_folder()+'\\' + file

        #Checks file extension
        if file.endswith(".jpg") or file.endswith(".png"):
            with open(file_name_input,'r+b') as f:
                with Image.open(f) as image:
                    #Adjustes image and saves the image
                    updated_image = resizeimage.resize_thumbnail(image,image_demensions(image.height, image.width), Image.ANTIALIAS)
                    updated_image.save(file_name_output, image.format)

main()