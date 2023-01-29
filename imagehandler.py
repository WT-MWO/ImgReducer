import os
from PIL import Image
import time


class ImageHandler:
    """This class allows for multiple images modifications such as:
    - saving with reduced size (optimized)
    - resizing images with given size
    - rotating images in one of directions
    - renaming files without size modification with possibility to add img creation date
    This code used PIL (Python Imaging Library) licensed with open source HPND License.
    """

    def __init__(self, path) -> None:
        self.path = path
        self.resized_img_dict = {}  # Holds modified images
        self.imgsize = {}
        self.imgmode = {}
        self.image_list = []  # Hold "raw" images to be modified
        pass

    def is_image(self):
        """Defines if file is a image according to given
        extensions: jpg, png, gif"""
        is_image = True
        for file in os.listdir(self.path):
            img_extensions = [".jpg", ".png", ".gif"]
            ext = os.path.splitext(file)[1]
            if ext.lower() not in img_extensions:
                is_image = False
            return is_image

    def get_images(self):
        """Gets all images from given path, adds to list: image_list"""
        for file in os.listdir(self.path):
            if self.is_image():
                img = Image.open(os.path.join(self.path, file))
                self.image_list.append(img)

    def size_reduce(self, quality=60):
        # Needs rework, quality not used
        """Resizes images with PIL, image name and data is stored in dict"""
        for img in self.image_list:
            resized_img = img.resize(img.size, Image.Resampling.LANCZOS)
            self.resized_img_dict[resized_img.tobytes()] = img.filename
            self.imgsize[img.filename] = img.size
            self.imgmode[img.filename] = img.mode

    def save_reduced_image(
        self,
        as_copy=True,
        prefix="",
        suffix="",
        optimized=True,
        quality=60,
        format="jpg",
    ):
        """Saves resized images with given names and addins, image data is
        restored from dictionaries"""
        for img, name in self.resized_img_dict.items():
            if as_copy:
                suffix = "-Copy"
            head, tail = os.path.split(name)
            raw_name = tail.split(".")
            img_name = head + "\\" + prefix + raw_name[0] + suffix + "." + format
            image = Image.frombytes(
                mode=self.imgmode[name], data=img, size=self.imgsize[name]
            )
            image.save(img_name, optimize=optimized, quality=quality)

    def image_resize(self, size=(800, 800), as_copy=True, optimized=True, quality=60):
        """Resizing images based on given size, size must be
            given as a tuple (width, height),
        as_copy - adds "-Copy" as suffix,
        quality - percents"""
        for file in os.listdir(self.path):
            if self.is_image():
                if as_copy:
                    suffix = "-Copy"
                else:
                    suffix = ""
                img = Image.open(os.path.join(self.path, file))
                # img = img_org.copy()
                img.thumbnail(size, Image.Resampling.LANCZOS)
                ext = os.path.splitext(file)[1]
                name = os.path.splitext(file)[0]
                img.save(
                    self.path + "\\" + name + suffix + ext,
                    optimize=optimized,
                    quality=quality,
                )

    def image_rotate(self, angle=90):
        """Rotates by given angle counterclockwise"""
        for img in self.image_list:
            rotated_img = img.rotate(angle, expand=1)
            rotated_img.save(img.filename)

    def get_file_datetime(self, path_name_file="", ymd_date=True):
        """Gets a creation datetime data of the file"""
        # This function need rework, useless if statement
        creation_date = os.path.getctime(path_name_file)
        cd_time_obj = time.gmtime(creation_date)
        if ymd_date:
            date_str = "-" + time.strftime(r"%Y-%m-%d", cd_time_obj)
        else:
            date_str = "-" + time.strftime(r"%Y-%m-%d, %H:%M:%S", cd_time_obj)
        return date_str

    def image_rename(
        self, name="Image", add_number=True, start_from=0, add_date_year=False
    ):
        """Rename image without size modification, modifies only name.
        This is supposed to be called after save_reduced_image operations."""
        n = start_from
        for file in os.listdir(self.path):
            ext = os.path.splitext(file)[1]
            filepath = self.path + "\\" + file
            if add_date_year:
                creation_date = self.get_file_datetime(
                    path_name_file=filepath,
                )
            else:
                creation_date = ""
            os.rename(
                filepath,
                self.path + "\\" + name + "_" + str(n) + str(creation_date) + ext,
            )
            if add_number:
                n += 1
