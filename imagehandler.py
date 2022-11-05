import os
from PIL import Image, ImageOps

# Docelowo stworzyc gui z inputem original path -> destination path, picture size, antialias y/n, format png/jpg
# Docelowo wybór zdjęć w gui powinien się odbywać na zasadzie zbioru wybranych zdjęć, nie z zawartości 

#funkcje do zaimplementowania
#[x]redukcja wagi z nadpisaniem pod tą samą nazwą
#[x]jak wyżej, ale z kopią
#[x]możliwość zapisania pod formatem .png
#[x]możliwość dodania prefixu/suffixu z zachowaniem starej nazwy
#[]możliwość dodania prefixu/suffixu ze zmianą nazwy
#[]możliwość zmiany rozdzielczości/wymiarów zdjecia
#[x]możliwość podania samej ścieżki bez koniecznośći podawania rozszerzenia i czy sa tam tylko zdjecia, ma rozpoznac sam
#[]możliwość dodania rotate


class ImageHandler:
    def __init__(self, path) -> None:
        self.path = path
        self.resized_img_dict = {} #holds modified images
        self.imgsize = {}
        self.imgmode = {}
        self.image_list = [] #hold "raw" images to be modified
        pass

    def get_images(self):
        for file in os.listdir(self.path):
            img_extensions = [".jpg", ".png", ".gif"] #needs to be tested for all except jpg
            ext = os.path.splitext(file)[1]
            if ext.lower() not in img_extensions:
                continue
            img = Image.open(os.path.join(self.path,file))
            self.image_list.append(img)
    
    def size_reduce(self, optimized = True, quality=60):
        for img in self.image_list:
            resized_img = img.resize(img.size, Image.Resampling.LANCZOS)
            self.resized_img_dict[resized_img.tobytes()] = img.filename
            self.imgsize[img.filename] = img.size
            self.imgmode[img.filename] = img.mode

    def save_image(self, as_copy = True, prefix="", suffix="", optimized = True, quality=60, format = "jpg"):
        for img, name in self.resized_img_dict.items():
            if as_copy:
                if suffix == "":
                    suffix = "-Copy"
            img_name = prefix + os.path.splitext(name)[0] + suffix + '.' + format
            image = Image.frombytes(mode= self.imgmode[name], data = img, size=self.imgsize[name],)
            image.save(img_name, optimize=optimized, quality=quality)

    def image_rename(self, new_name = "Image"):
        pass

    def image_resize(self):
        pass

    def image_rotate(self):
        pass