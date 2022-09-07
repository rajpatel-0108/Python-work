from PIL import Image
import os

# im = Image.open("unsplash/saves/1.jpeg")
# im.show()
# print(os.path.getsize("unsplash/saves/2.jpg"))

# images = [file for file in files if file.endswith(('jpeg', 'png', 'jpg'))]
# print(images)
# for image in images:
#     img = Image.open("unsplash/"+image)
#     img.thumbnail((600,600))
#     img.save("resized_"+image, optimize=True, quality=40)



files = os.listdir("foodiesfeed")
print(files)

def resize(im, new_width):
    width, height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width,new_height))
    return resized_image

extensions = ['jpeg', 'png', 'jpg']
for file in files:
    ext = file.split(".")[-1]
    if ext in extensions:
        im = Image.open("foodiesfeed/"+file)
        im_resized = resize(im,300)
        im.save("resized_"+file, optimize=True, quality=60)

