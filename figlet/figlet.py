import random
import sys
from pyfiglet import Figlet
figlet = Figlet()
lf = figlet.getFonts()
rf = random.choice(lf)
if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in lf :
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=rf)
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")