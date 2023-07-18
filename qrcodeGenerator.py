# BASIC

import qrcode


text = "kinglseyokoronkwo.hashnode.com"

# qrc_encoded = qrcode.make(text)
# qrc_encoded.save("qrce.png")

#ADVANCED




qrcoded = qrcode.QRCode(version=1,box_size=6,border=4,error_correction= qrcode.constants.ERROR_CORRECT_M)
qrcoded.add_data(text)
qrcoded.make(fit=True)
qrcImage = qrcoded.make_image(fill_color='red',back_color='blue')
qrcImage.save("vaersion1.box6.png")