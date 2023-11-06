from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './imgs'
pathout = '/editedImgs'

for filename in os.listdir(path):
   img = Image.open(f"{path}/{filename}")

   #shapening, Black and White

   edit = img.filter(ImageFilter.SHARPEN).convert('L') #.rotate(90)


   #contrast enhancement

   factor = 1.5
   enhancer = ImageEnhance.Contrast(edit)
   edit = enhancer.enhance(factor)


   #resize image

   #for original image resize use this code =>  "edit = edit.resize((width, height))"
   
   
   #to create an additional resized image use code below => 

   sizes = [(300, 300)]
   for size in sizes:
      resized_edit = edit.copy()
      resized_edit.thumbnail(size)
      

   

   #ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.com/en/stable/

   clean_name = os.path.splitext(filename)[0]

   edit.save(f".{pathout}/{clean_name}_edited.jpg")

   resized_edit.save(f".{pathout}/{clean_name}_edited_{size[0]}x{size[1]}.jpg")
  
   