from src.imagehandler import ImageHandler

# Paste you folder path
dir = r"test"

imghandler = ImageHandler(dir)


imghandler.get_images()

# Place for modification functions
imghandler.size_reduce()

# Saving images, as copy add prefix etc.
imghandler.save_reduced_image(as_copy=False, quality=25)

# Resizing images to given size, but keeping the ratio
# imghandler.image_resize(size=(1920,1080), as_copy=True)

# Rotates image conterclockwise
# imghandler.image_rotate(angle=-90)

# Run this to rename in order, possibly add date
# imghandler.image_rename(name="IMG", start_from=0, add_date_year=False)
