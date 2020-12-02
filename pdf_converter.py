from PIL import Image
import PIL
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
import os


def convert_file_to_images(path_to_file):
    return convert_from_path(path_to_file)


def save_pil_images(save_path, images):
    print(len(images))
    for i in range(0, len(images)):
        image = images[i]
        image_save_path = os.path.join(save_path, str(i) + ".jpg")
        print(image_save_path)
        image.save(image_save_path)


if __name__ == "__main__":
    cwd = os.getcwd()
    path_to_pdf = os.path.join(cwd, 'SRD-OGL_V5.1.pdf')
    images = convert_file_to_images(path_to_pdf)
    output_path = os.path.join(cwd, 'output')
    save_pil_images(output_path, images)