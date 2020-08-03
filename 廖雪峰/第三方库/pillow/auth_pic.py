from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

weight = 60 * 4
height = 60

def back_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def text_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def randChar():
    return chr(random.randint(65, 90))

image = Image.new('RGB', (weight, height), (255, 255, 255))
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(weight):
    for y in range(height):
        draw.point((x, y), fill = back_color())

for i in range(4):
    draw.text((60 * i + 10, 10), randChar(), font = font, fill = text_color())

image = image.filter(ImageFilter.BLUR)
image.save(r'C:\Users\New\Desktop\python\第三方库\pillow\验证码.jpg', 'jpeg')
