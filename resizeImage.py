# install pillow
from PIL import Image
    
    
image = Image.open('qrcode.png')
print("Current Size: ",image.size)