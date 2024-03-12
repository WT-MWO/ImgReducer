from src.imagehandler import ImageHandler
from src.img_to_pdf import Img_to_pdf

# INPUT
jpg_folder_path = "C:\\Users\\mwo\\test"
pdf_name = 'test.pdf'


# CODE
imghandler = ImageHandler(jpg_folder_path)
imghandler.get_images()
# Place for modification functions
imghandler.size_reduce()
# Saving images, as copy add prefix etc.
imghandler.save_reduced_image(as_copy=False, quality=25)

img_to_pdf = Img_to_pdf(path=jpg_folder_path, pdf_name=pdf_name)
img_to_pdf.save()
