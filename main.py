from PIL import Image, ImageFont, ImageDraw
import csv
import os

"""
ONLY BELOW CONFIG TO BE MODIFIED
"""
TEMPLATE_PATH = "template.png"  # path to the base template image
TO_SAVE_PATH = "certificates/"  # folder to save the certificates to
CSV_FILE = "names.csv"  # path to the csv file containing names at index 0 without heading
HAS_HEADING = False  # True if csv file has heading row, False otherwise
INDEX = 0  # index at which the names are stored for certificate
FONT_SIZE = 100  # font size
VERIFY_FONT_SIZE = 35 # font size for the verification text
COLOR = (34, 53, 104)  # font color
TEXT_MIDDLE_POS = (1200, 650)  # coordinates to begin writing text 
FONT = ImageFont.truetype("fonts/JosefinSans-Bold.ttf", size = FONT_SIZE)  # font to be used for name
VERIFY_FONT = ImageFont.truetype("fonts/JosefinSans-Italic.ttf", size=VERIFY_FONT_SIZE)  # font to be used for verification text
"""
CONFIG ENDS
"""


NAMES = []

temp_template = Image.open(TEMPLATE_PATH)

with open(CSV_FILE, "r") as name_file:
    data = csv.reader(name_file)
    if HAS_HEADING:
        next(data, None)
    for row in data:
        NAMES.append(row[INDEX])

if not os.path.exists(TO_SAVE_PATH):
    os.makedirs(TO_SAVE_PATH)

"""
first argument: position
second argument: text to put
third argument:  color
fourth argument: font to be used
"""
for name in NAMES:
    template = Image.new('RGB', temp_template.size, (255, 255, 255))
    template.paste(temp_template, mask=temp_template.split()[3])
    raw_template = ImageDraw.Draw(template)
    name_width, name_height = raw_template.textsize(name, font=FONT)
    name_pos = (TEXT_MIDDLE_POS[0]-(name_width/2), TEXT_MIDDLE_POS[1]-(name_height/2))
    verify_text = "Verify at https://kossiitkgp.org/public-files/KWoC/2018-Certificates/" + name.replace(" ", "%20",10) + ".pdf"
    verify_width, verify_height = raw_template.textsize(verify_text, font=VERIFY_FONT)
    verify_pos = (TEXT_MIDDLE_POS[0]-(verify_width/2), TEXT_MIDDLE_POS[1]+(name_height) - (verify_height/4))
    raw_template.text(name_pos, name, COLOR, FONT)
    raw_template.text(verify_pos, verify_text, COLOR, VERIFY_FONT)
    template.save(TO_SAVE_PATH+"KWoC18-"+name+".pdf", "PDF", resolution=100.0)