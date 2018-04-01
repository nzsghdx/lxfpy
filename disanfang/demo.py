from PIL import Image

im=Image.open('test.jpg')
im2=Image.open('thumb.png')
print(im.format,im.size,im.mode)
print(im2.format,im2.size,im2.mode)
