from imagehandler import ImageHandler

#paste you folder path 
dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics"

imghandler = ImageHandler(dir)


imghandler.get_images()

##place for modification functions
imghandler.size_reduce()

##saving images, as copy add prefix etc.
#imghandler.save_reduced_image(as_copy = False, quality=40)

##resizing images to given size, but keeping the ratio
#imghandler.image_resize(size=(1920,1080), as_copy=True)

##rotates image conterclockwise
#imghandler.image_rotate(angle=-90)

##run this to rename in order, possibly add date
#imghandler.image_rename(name="IMG", start_from=0, add_date_year=False)