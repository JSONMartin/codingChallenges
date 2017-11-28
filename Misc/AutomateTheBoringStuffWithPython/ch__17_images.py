import sys, os
from PIL import ImageColor, Image

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

processCatImage()
createNewImage()
