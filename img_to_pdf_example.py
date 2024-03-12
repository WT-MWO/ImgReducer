from src.imagehandler import ImageHandler
from src.img_to_pdf import Img_to_pdf

# INPUT
jpg_folder_path = "C:\\Users\\mwo\\test"
pdf_name = 'test.pdf'

# Reduce size of images
imghandler = ImageHandler(jpg_folder_path)
imghandler.get_images()
imghandler.size_reduce()
# Saving reduced images
imghandler.save_reduced_image(as_copy=False, quality=25)
# Combine images to one pdf file
img_to_pdf = Img_to_pdf(path=jpg_folder_path, pdf_name=pdf_name)
img_to_pdf.save()
