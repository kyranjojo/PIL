from PIL import Image
thumb_size = (600,600)
img = Image.open('img/pic.jpg')
img.thumbnail(thumb_size)
img.size
img.show()