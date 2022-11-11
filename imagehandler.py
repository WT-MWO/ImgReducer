import os
from PIL import Image, ImageOps
import time
# Docelowo stworzyc gui z inputem original path -> destination path, picture size, antialias y/n, format png/jpg
# Docelowo wybór zdjęć w gui powinien się odbywać na zasadzie zbioru wybranych zdjęć, nie z zawartości 

#funkcje do zaimplementowania
#[x]redukcja wagi z nadpisaniem pod tą samą nazwą
#[x]jak wyżej, ale z kopią
#[x]możliwość zapisania pod formatem .png
#[x]możliwość dodania prefixu/suffixu z zachowaniem starej nazwy
#[x]możliwość dodania  zmiany nazwy z numeracja
#[]możliwość zmiany rozdzielczości/wymiarów zdjecia
#[x]możliwość podania samej ścieżki bez koniecznośći podawania rozszerzenia i czy sa tam tylko zdjecia, ma rozpoznac sam
#[]możliwość dodania rotate#
#[x]dopisywanie daty do tytułu - data oryg zdjecia, data biezaca

class ImageHandler:
    def __init__(self, path) -> None:
        self.path = path
        self.resized_img_dict = {} #holds modified images
        self.imgsize = {}
        self.imgmode = {}
        self.image_list = [] #hold "raw" images to be modified
        pass

    def is_image(self):
        is_image = True
        for file in os.listdir(self.path):
            img_extensions = [".jpg", ".png", ".gif"]
            ext = os.path.splitext(file)[1]
            if ext.lower() not in img_extensions:
               is_image = False
            return is_image

    def get_images(self):
        for file in os.listdir(self.path):
            if self.is_image():
                img = Image.open(os.path.join(self.path,file))
                self.image_list.append(img)
    
    def size_reduce(self, optimized = True, quality=60):
        for img in self.image_list:
            resized_img = img.resize(img.size, Image.Resampling.LANCZOS)
            self.resized_img_dict[resized_img.tobytes()] = img.filename
            self.imgsize[img.filename] = img.size
            self.imgmode[img.filename] = img.mode

    def save_reduced_image(self, as_copy = True, prefix="", suffix="", optimized = True, quality=60, format = "jpg"):
        for img, name in self.resized_img_dict.items():
            if as_copy:
                if suffix == "":
                    suffix = "-Copy"
            img_name = prefix + os.path.splitext(name)[0] + suffix + '.' + format
            image = Image.frombytes(mode= self.imgmode[name], data = img, size=self.imgsize[name],)
            image.save(img_name, optimize=optimized, quality=quality)
#split image handler into imagereducer class and imagemodifierclass
#add image save function which will be used in resize rotate etc.

    def image_resize(self, size = (800, 800), as_copy = True, optimized = True, quality=60):
        for file in os.listdir(self.path):
            if self.is_image():
                if as_copy:
                    img = Image.open(os.path.join(self.path,file))
                    #img = img_org.copy()
                    img.thumbnail(size, Image.Resampling.LANCZOS)
                    ext = os.path.splitext(file)[1]
                    name = os.path.splitext(file)[0]
                    img.save(self.path + "\\" + name + '-Copy' + ext, optimize = optimized, quality = quality)


    def image_rotate(self):
        pass

class FileModifier():
    def __init__(self, path) -> None:
        self.path = path

    def get_file_datetime(self, path_name_file = "", ymd_date = True):
    #return string
        creation_date = os.path.getctime(path_name_file)
        cd_time_obj = time.gmtime(creation_date)
        if ymd_date: 
            date_str = "-" + time.strftime(r"%Y-%m-%d", cd_time_obj)
        else:
            date_str = "-" + time.strftime(r"%Y-%m-%d, %H:%M:%S", cd_time_obj)
        return date_str

    def image_rename(self, name = "Image", add_number = True, start_from = 0, add_date_year = False):
    #this is supposed to be called after save_image, operation is executed only on filenames in dir
        n = start_from
        for file in os.listdir(self.path):
            ext = os.path.splitext(file)[1]
            filepath = self.path + "\\" + file
            if add_date_year:
                creation_date = self.get_file_datetime(path_name_file = filepath,)
            else:
                creation_date = ""
            os.rename(filepath, self.path + "\\" + name + '_' + str(n) + str(creation_date) + ext)
            if add_number:
                n += 1

