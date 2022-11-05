#import PIL
import os
import glob
from PIL import Image
import io

# Skrypt powinien mieć możliwość zapisywania pod inną nazwą z numeracją lub możliwość zapisywania pod starą nazwą w nowym folderze, w formacie png lub jpeg.
# Docelowo stworzyc gui z inputem original path -> destination path, picture size, antialias y/n, format png/jpg
# Docelowo wybór zdjęć w gui powinien się odbywać na zasadzie zbioru wybranych zdjęć, nie z zawartości 

#funkcje do zaimplementowania
#[x]redukcja wagi z nadpisaniem pod tą samą nazwą
#[x]jak wyżej, ale z kopią
#[x]możliwość zapisania pod formatem .png
#[x]możliwość dodania prefixu/suffixu z zachowaniem starej nazwy
#[]możliwość dodania prefixu/suffixu ze zmianą nazwy
#[]możliwość zmiany rozdzielczości/wymiarów zdjecia
#[]możliwość podania samej ścieżki bez koniecznośći podawania rozszerzenia
#[]możliwość dodania rotate
#[]możliwość wklejenia path bez przejmowania sie jaki format zdjec jest w folderze i czy sa tam tylko zdjecia, ma rozpoznac sam

dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics\*.jpg"
dir2 = r"D:\DATA\m.wolinski\Downloads\drive-download-20220926T095835Z-001\drive-download-20220926T095835Z-001\*.jpg"

class ImageHandler:
    def __init__(self, path) -> None:
        self.path = path
        self.resized_img_dict = {}
        self.imgsize = {}
        self.imgmode = {}
        pass
    
    def size_reduce(self, optimized = True, quality=60):
        image_list = []
        for file in glob.glob(self.path):
            img = Image.open(file)
            image_list.append(img)
        for img in image_list:
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
            #image = Image.open(io.BytesIO(img))
            image.save(img_name, optimize=optimized, quality=quality)


imghandler = ImageHandler(dir)
imghandler.size_reduce()
imghandler.save_image(as_copy = False)
