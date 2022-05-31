#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
image = Image.open('image/1.jpg')
width, height = image.size

draw = ImageDraw.Draw(image)
text = "sample watermark"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
image.show()

#Save watermarked image
image.save('image/watermark.jpg')