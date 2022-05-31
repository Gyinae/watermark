from PIL import Image, ImageFont, ImageDraw

#Import image and create an image object
image = Image.open("image/1.jpg")
width, height = image.size

#creating a watermark for the image
draw = ImageDraw.Draw(image)
text = "Twitter: @_gyinae__"

# choosing a font image and dimensions for text
font = ImageFont.truetype('arial.ttf', 36)
text_width, text_height = draw.textsize(text, font)

#choosing the positioning of the text
margin = 10
x_cor = width - text_width - margin
y_cor = height - text_height - margin

#Placing the watermark at the bottom right corner
draw.text((x_cor,y_cor), text, font=font)
image.show()

# Save watermark
image.save("image/watermark.jpg")