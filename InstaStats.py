import json
import urllib.request, urllib.parse
import subprocess
from bs4 import BeautifulSoup
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

req      = urllib.request.Request('http://www.instagram.com/sj___156')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')
html     = urllib.request.urlopen(req).read()
response = BeautifulSoup(html, 'html.parser')
jsonObject = response.select("body > script:nth-of-type(1)")[0].text.replace('window._sharedData =','').replace(';','')
data      = json.loads(jsonObject)
following = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']
followed  = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
posts     = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
username  = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['owner']['username']

# check value populated 
print(followed)

# set display to be variable of inky_display
inky_display = InkyPHAT("red")
# set the border to be white around the display
inky_display.set_border(inky_display.WHITE)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
# set font try to experiment with different font
font = ImageFont.truetype(FredokaOne, 22)

line1 = 'Insta followers:'
line2 = str(followed)
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
