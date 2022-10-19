

from PIL import Image
img=Image.open("image.jpg")
from PIL import ImageDraw
I1=ImageDraw.Draw(img)
from PIL import ImageFont
font=ImageFont.truetype('calibri',25)
I1.text((331,142),"L1=104,7mm",fill=(255,255,255,255),font=font)

