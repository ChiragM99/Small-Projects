from PIL import Image, ImageFilter

img = Image.open('./images/')
filtered_img = img.filter(ImageFilter.BLUR)
img.convert('L')
img.rotate(90)
filtered_img.save("image.png", "png")

#resize
resize = filtered_img.resize((300, 300))
resize.save("resized.png", "png") 

#crop
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("cropped.png" "png")

# resize/compress img
img = Image.open('./images/image.png')
new_img = img.resize(400, 400)
new_img.save("thumb.png" "png")

img = Image.open('./images/blur.png')
img.thumbnail(400, 400)
img.save("thumb.png" "png")

