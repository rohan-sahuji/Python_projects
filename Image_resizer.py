from PIL import Image

def resizer(image,wid,len):
    resized_img = image.resize((wid,len))
    #resized_img.save('Resized_test.jpg')
    resized_img.show()

image = input('Enter the image file name:')
img = Image.open(image)
print('Current size:', img.size)
width = int(input('Enter the new width:'))
length = int(input('Enter the new length:'))
resizer(img,width,length)