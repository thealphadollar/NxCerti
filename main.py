from PIL import Image, ImageFont, ImageDraw
import csv


"""
ONLY BELOW CONFIG TO BE MODIFIED
"""
CSV_FILE = "names.csv"  # path to the csv file containing names at index 0 without heading
FONT_SIZE = 100  # font size
COLOR = (34, 53, 104)  # font color
TEXT_MIDDLE_POS = (1200, 650)  # coordinates to begin writing text 
FONT = ImageFont.truetype("fonts/JosefinSans-Bold.ttf", size = FONT_SIZE)  # font to be used
"""
CONFIG ENDS
"""


NAMES = []

temp_template = Image.open("template.png")
template = Image.new('RGB', temp_template.size, (255, 255, 255))
template.paste(temp_template, mask=temp_template.split()[3])
raw_template = ImageDraw.Draw(template)

with open(CSV_FILE, "r") as name_file:
    data = csv.reader(name_file)
    for row in data:
        NAMES.append(row[0])

"""
first argument: position
second argument: text to put
third argument:  color
fourth argument: font to be used
"""
for name in NAMES:
    name_width, name_height = raw_template.textsize(name, font=FONT)
    name_pos = (TEXT_MIDDLE_POS[0]-(name_width/2), TEXT_MIDDLE_POS[1]-(name_height/2))
    raw_template.text(name_pos, name, COLOR, FONT)
    template.save("KWoC18-"+name+".pdf", "PDF", resolution=100.0)