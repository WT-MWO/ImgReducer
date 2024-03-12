from PIL import Image
import os


class Img_to_pdf():
    """This class allows for merging multiple images from given directory to one pdf file.
    This code used PIL (Python Imaging Library) licensed with open source HPND License.
    """
    def __init__(self, path, pdf_name) -> None:
        self.path = path
        self.pdf_name = pdf_name
        self.pic_format = '.jpg'

    def save(self):
        list_of_jpg = []
        for x in os.listdir(self.path):
            if x.endswith(self.pic_format):
                # print(x)
                list_of_jpg.append(x)
        images = [
            Image.open(self.path + '\\' + f).convert("L")
            for f in list_of_jpg
        ]
        pdf_path = self.path + '\\' + self.pdf_name
        images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:], optimize=True
        )
