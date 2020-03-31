from . import utils

from pytesseract import image_to_string
import pytesseract
from PIL import Image
from urllib.parse import urljoin

class web:
  kraj = 'Moravskoslezský kraj'

  def crawl(self):
    khs_url = 'http://www.khsova.cz/homepage/korona-statistika'

    html = utils.get_url(khs_url)
    img_url = urljoin(khs_url, html.select_one('.inner img:nth-of-type(2)')['src'])
    img = utils.get_img(img_url)

    first_row_offset = 110
    column_offset = 138
    row_spacing = 48.5
    number_height = 14
    target_color = img.getpixel((column_offset, first_row_offset))
    gray = (204, 204, 204, 255)
    white = (255, 255, 255, 255)
    okresy = [
      'Bruntál',
      'Frýdek-Místek',
      'Karviná',
      'Nový Jičín',
      'Opava',
      'Ostrava'
    ]

    cropped_imgs = []
    for row_index in range(0, 6):
      y = int(first_row_offset + row_spacing * row_index) - row_index
      px = img.getpixel((column_offset, y))
      x = column_offset
      while px == target_color:
        px = img.getpixel((x, y))
        x += 1
      x = x + 5
      cropped_imgs.append(
        img.crop((x, y, x+img.width, y+number_height)))

    results = []
    for index, cropped_img in enumerate(cropped_imgs):
      for x in range(0, cropped_img.width):
        for y in range(0, cropped_img.height):
          px = cropped_img.getpixel((x, y))
          if px == gray:
            cropped_img.putpixel((x, y), white)
      val = int(image_to_string(cropped_img))
      results.append(
        {'okres': okresy[index], 'kraj': self.kraj, 'hodnota': val})
    return results
