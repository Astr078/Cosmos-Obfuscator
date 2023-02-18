import base64
import lzma
import pystyle
from pystyle import *
import os
import sys
import platform
import base64
import sys
from time import sleep, time
from getpass import getpass
import py_compile
import random
import os
import secrets

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LR = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"



is_windows = True if platform.system() == "Windows" else False

def sun(text):
    os.system("")
    faded = ""
    red = 255
    green = 125
    blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
        if not red == 245:
            red -= 10
            if red < 245:
                red = 245
    return faded

def water(text):
    os.system("")
    faded = ""
    green = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def rose_to_green(text):
    os.system("")
    faded = ""
    red = 255
    blue = 255
    green = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if green < 255:
            green += 15
            if green > 255:
                green = 255
        if red > 0:
            red -= 15
            if red < 0:
                red = 0
        if blue > 0:
            blue -= 15
            if blue < 0:
                blue = 0
    return faded

def purple_pink(text):
    os.system("")
    faded = ""
    r = 189
    g = 50
    b = 202
    for line in text.splitlines():
        faded += (f"\033[38;2;{r};{g};{b}m{line}\033[0m\n")
        if r < 255:
            r += 20
        if g < 155:
            g += 20
        if b > 100:
            b -= 20
    return faded

def cyan(text):
    os.system("")
    faded = ""
    blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{blue};0;255m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return faded
# citations = ["Every star has its own destiny.",
#              "Only a look can create the universe."]
# rdmcitation = random.choice(citations)
text = f"""

         ▄▄·       .▄▄ · • ▌ ▄ ·.       .▄▄ · 
        ▐█ ▌▪▪     ▐█ ▀. ·██ ▐███▪▪     ▐█ ▀. . 
       .██ ▄▄ ▄█▀▄ ▄▀▀▀█▄▐█ ▌▐▌▐█· ▄█▀▄ ▄▀▀▀█▄ .
        ▐███▌▐█▌.▐▌▐█▄▪▐███ ██▌▐█▌▐█▌.▐▌▐█▄▪▐█
        ·▀▀▀  ▀█▄▀▪ ▀▀▀▀ ▀▀  █▪▀▀▀ ▀█▄▀▪ ▀▀▀▀ v1.0

╔═════════╩═════════════════════════════════╩═════════╗
║            Every star has its own destiny.          ║
║               https://discord.io/Astr0              ║
║          Created By Brigade Anti-420 !!#7274        ║
╚═════════════════════════════════════════════════════╝

"""




def obfuscate_code(input_file, output_file):
    with open(input_file, "rb") as f:
        code = f.read()
    compressed_code = lzma.compress(code)
    obfuscated_code = base64.urlsafe_b64encode(compressed_code).decode("utf-8").replace('\n', '')
    padding = "=" * ((4 - len(obfuscated_code) % 4) % 4)
    obfuscated_code = obfuscated_code.replace("\n", "").replace(" ", "")
    obfuscated_code = obfuscated_code + padding
    # Obfuscate code using Cosmos
    random_strings = []
    for i in range(2):
        random_string = secrets.token_urlsafe(random.randint(2,10))
        random_strings.append(random_string)

    myname = ""
    for r in random_strings:
        myname += f'''import base64;import lzma;data=base64.urlsafe_b64decode('{r}');code=lzma.decompress(data);exec(code.decode('utf-8'));'''

    hidden1 = random.randint(1000, 2000)
    mynameexp1 = myname * hidden1
    hidden2 = random.randint(5000, 6000)
    mynameexp2 = myname * hidden2
    hidden3 = random.randint(28000, 30000)
    mynameexp3 = myname * hidden3
    confusing ='''
import random

class Cosmos:

    def generate_coordinates(self, x_coordinates):
        y_coordinates = []
        for x in x_coordinates:
            y = (x * random.uniform(random.uniform(73645, 99999), 99999) - random.uniform(random.uniform(73645, 99999), 99999)) * random.uniform(random.uniform(73645, 99999), 99999)
            y = y + (random.uniform(random.uniform(73645, 99999), 99999) / random.uniform(random.uniform(73645, 99999), 99999))
            y = y * random.uniform(random.uniform(73645, 99999), 99999)
            y_coordinates.append(y)
  
    def generate_data(n_points):
        x = UnicodeDecodeError(5555, 10999, 99999, n_points)
        y = UnboundLocalError.sin(x) + UnicodeEncodeError.random.uniform(scale=0.1, size=n_points)
        return x, y

    def save_data(x, y, filename):
        data = KeyboardInterrupt.random.uniform({"x": x, "y": y})
        data.to_csv(filename, index=False)
'''
    # Write obfuscated code to file
    # sans_ext = os.path.splitext(os.path.basename(filename))[0]
    # size2 = os.path.getsize(f"{sans_ext}-cosmosOBF.py")
    # size2_in_kb = round(size2 / 1024, 2)
    with open(output_file, "w") as f:
        f.write(
            f"__obfuscator__ = 'Cosmos'\n___version__= '1.0'\n__Creators__ = ('Brigade Anti420#7274, Astr078')\n__github__ = 'https://github.com/Astr078'\n__server__ = 'https://discord.io/Astr0'\n\n{confusing}\nif __name__ == '__main__':\n '''{myname}''';a='''import base64;import lzma;data=base64.urlsafe_b64decode('frfrfre');code=lzma.decompress(data);exec(code.decode('utf-8'))''';'''{mynameexp1}''';'''{myname}''';i='''import base64;import lzma;data=base64.urlsafe_b64decode('{obfuscated_code}');code=lzma.decompress(data);exec(code.decode('utf-8'))''';'''{mynameexp1}''';exec(i);'''{mynameexp1}''';'''{mynameexp3}'''")
    # obfuscated_pyc = os.path.splitext(f'{filename}')[0] + ".pyc"
    # ask = input(LIGHT_PURPLE + ' [' + white + '?' + LIGHT_PURPLE +
    #           '] ' + white + 'Do you want to compile the obfuscated code into a .pyc file? (y/n) ')
    # if ask == "y":
    # py_compile.compile(output_file, cfile=obfuscated_pyc)
    # with open(obfuscated_pyc, 'r+b') as f:
    #     f.seek(0, 2)  # Go to the end of the file
    #     addtt = r'''import base64;import lzma;data=base64.b64decode('');code=lzma.decompress(data);exec(code.decode('utf-8'));'''
    #     nal4 = random.randint(20000, 21000)
    #     mynameexp = addtt * nal4
    #     f.write(b'\nCompiled With Cosmos Obfuscator !')  # Write some text
    # else:
    #     print('')
    #     return obfuscated_code
    
if __name__ == "__main__":
    white = Col.white
    dblue = Col.blue
    centerban = Center.XCenter(text)
    rdmcolor= [water, cyan, sun, purple_pink, rose_to_green]
    rdm = random.choice(rdmcolor)
    print(rdm(centerban))
    filename = input(LIGHT_PURPLE + ' [' + white + '?' + LIGHT_PURPLE +'] ' + white + "Drag the file you want to obfuscate: ")
    if os.path.isfile(filename):
        sans_ext = os.path.splitext(os.path.basename(filename))[0]
        now = time()
        # ask2 = input(LIGHT_PURPLE + ' [' + white + '?' + LIGHT_PURPLE +
        #       '] ' + white + 'Do you want to compile in py ? (y/n)')
        # if ask2 == ('y'):
        now = round(time() - now, 2)        
        obfuscate_code(filename, f"{sans_ext}-cosmosOBF.py")
        # else :
        #     print('')
        if os.path.isfile(f"{sans_ext}-cosmosOBF.py"):
            size = os.path.getsize(filename)
            size_in_kb = round(size / 1024, 2)
            size2 = os.path.getsize(f"{sans_ext}-cosmosOBF.py")
            size2_in_kb = round(size2 / 1024, 2)
            print(LIGHT_PURPLE + ' [' + white + '>' + LIGHT_PURPLE +
              '] ' + white + f"The size of your original file is {size_in_kb} ko.")
            print(LIGHT_PURPLE + ' [' + white + '>' + LIGHT_PURPLE +
              '] ' + white + f"The size of your obfuscated file is {size2_in_kb} ko.")
        else:
            print(LIGHT_PURPLE + ' [' + white + '!' + LIGHT_PURPLE +
              '] ' + white + f"Failed to get the size of your new file.")

        print(LIGHT_PURPLE + ' [' + white + '>' + LIGHT_PURPLE +
              '] ' + white + f"File succesfully obfuscated in "+ LIGHT_PURPLE +f"{now}"+ white +"s with python "f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} \n")
        input(LIGHT_PURPLE + ' [' + white + '>' + LIGHT_PURPLE +
              '] ' + white + "You can now close this window")

    else:
        print(LIGHT_PURPLE + ' [' + white + '!' + LIGHT_PURPLE +
              '] ' + white + f"\n{filename} n'est pas un fichier valide.")
