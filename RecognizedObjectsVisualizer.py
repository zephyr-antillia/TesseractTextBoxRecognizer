# Copyright 2023 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# RecognizedObjectVisualizer.py
import os

from PIL import Image, ImageDraw, ImageFont
#import traceback2 as traceback
import traceback

TEXT_HORIZONTAL = 0
TEXT_VERTICAL   = 1

class RecognizedObjectsVisualizer:

  def __init__(self, font_name= "BIZ-UDMinchoM.ttc"):
    self.font_name  = font_name
 

  def get_font(self, height, width):
    fsize = 14
    direction = TEXT_VERTICAL
    try:
      #if height % 2 == 1:
      #  height += 1
      fsize = width

      if height < width:
        fsize = height
        direction = TEXT_HORIZONTAL
      font = ImageFont.truetype(self.font_name, fsize) 
    except IOError:
      print("Failed to font_name {} size {} ".format(self.font_name, fsize))
     
      try:
       font = ImageFont.truetype(self.font_name, 20)
      except IOError:
       font = ImageFont.truetype('arial.ttf', 20)
    
    return (font, direction)


  def visualize(self, boxies, image_file, output_dir, draw_boundingbox):
    org = Image.open(image_file)
    w, h = org.size
    img = Image.new("RGB", (w,  h), (255, 255, 255))
 
    draw = ImageDraw.Draw(img)
    for box in boxies:
      text = box.content
      pos  = box.position
        
      min_x = pos[0][0]
      min_y = pos[0][1]
      max_x = pos[1][0]
      max_y = pos[1][1]
      if draw_boundingbox:
        draw.rectangle(pos, fill=None, outline="red", width=1)
 
      #draw.rectangle([(min_x, min_y), (max_x, max_y)], fill=None, outline="red", width=1)
      h = max_y - min_y
      w = max_x - min_x
      (font, direction) = self.get_font(h, w)
      if direction == TEXT_HORIZONTAL:
        draw.text((min_x, min_y), text, fill='black', font=font)
      else:
        #print("VERT {}".format(texts[i]))
        y = min_y
        for ch in text:
          draw.text((min_x, y), ch, fill="black", font=font)
          print(ch)
          y += w

    basename = os.path.basename(image_file)
    
    output_file = os.path.join(output_dir, basename)
    print("--- output_file {}".format(output_file))

    img.save(output_file) #, "PNG") 

