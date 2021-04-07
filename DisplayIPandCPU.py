from inky import InkyPHAT
import subprocess

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 22)

def get_IP():
    IP = subprocess.check_output(["hostname", "-I"]).split()[0]
    #print(IP)
    IP2 = 'IP' + str(IP)
    IP3 = (IP2[4:-1])
    return IP3

def get_cpu_temp():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'

def get_cpu_temp2():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu2 = tmp.read()
    tmp.close()
    return cpu2

line1 = 'IP: ' + get_IP()
line2 = 'CPU: ' + get_cpu_temp()

line_padding = 6

w1, h1 = font.getsize(line1)
x = (inky_display.WIDTH / 2) - (w1 / 2)
y = (inky_display.HEIGHT / 2) - h1 - (line_padding / 2)
draw.text((x, y), line1, inky_display.RED, font)

w2, h2 = font.getsize(line2)
x = (inky_display.WIDTH / 2) - (w2 / 2)
y = (inky_display.HEIGHT / 2) + (line_padding / 2)
draw.text((x, y), line2, inky_display.BLACK, font)

inky_display.set_image(img)
inky_display.show()
