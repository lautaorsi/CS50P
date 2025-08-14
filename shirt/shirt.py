from PIL import Image
from PIL import ImageOps

import sys

def main():
    try:
         over = sys.argv[1]
         newphoto = sys.argv[2]
    except IndexError:
         sys.exit('Too few command-line arguments')

    try:
         x = sys.argv[3]
    except IndexError:
         if ".png" not in sys.argv[2] and ".jpg" not in sys.argv[2] and ".pneg" not in sys.argv[2]:
               sys.exit('Invalid output')
         else:
               a = sys.argv[1].split('.')
               b = sys.argv[2].split('.')
               if a[1] == b[1]:
                    try:
                        photo(over)
                    except FileNotFoundError:
                        sys.exit('File does not exist')
               else:
                        sys.exit('Input and output have different extensions')
    else:
        sys.exit('Too many command-line arguments')


def photo(under):
    image = Image.open(under ,'r')
    over = Image.open('shirt.png', 'r')
    nimage = ImageOps.fit(image, (600,600))
    shirt = ImageOps.fit(over, (600,600))
    nimage.paste(shirt,shirt)
    nimage.save(sys.argv[2])









if __name__ == "__main__":
    main()
