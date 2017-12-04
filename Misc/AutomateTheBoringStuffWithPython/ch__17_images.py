import sys, os
from PIL import ImageColor, Image, ImageDraw, ImageFont

red = ImageColor.getcolor('red', 'RGBA')
black = ImageColor.getcolor('black', 'RGBA')
cornFlowerBlue = ImageColor.getcolor('CornflowerBlue', 'RGBA')


os.chdir('/Users/jmartin/code/codingChallenges/Misc/AutomateTheBoringStuffWithPython')

def processCatImage():
    catImage = Image.open('zophie.png')

    attributes = {
        'size': catImage.size,
        'mode': catImage.mode,
        'filename': catImage.filename
    }

    width, height = attributes['size']

    print(attributes)
    print(f"Width:{width} Height:{height}")

    print("Saving JPG version...")
    catImage.save("zophie.jpg")

def createNewImage():
    image = Image.new('RGBA', (100, 200), 'purple')
    image.save('purpleImage.png')
    print("Saving purple image")

def drawing():
    WIDTH, SIZE = 200, 200
    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)

    for i in range(0, WIDTH, WIDTH // 10):
        draw.line([0, i, WIDTH, i],'black')
        draw.line([i, 0, i, WIDTH],'black')

    for i in range(10, 160, 40):
      draw.ellipse([40 + i, 40 + i, 80 + i, 80 * i], 'pink', 'purple')

    im.save('drawing.png')

processCatImage()
createNewImage()
drawing()