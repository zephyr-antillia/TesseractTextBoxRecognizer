# SurfaceTokenizer.py

from janome.tokenizer import Tokenizer
#import matplotlib
from matplotlib.pyplot import imshow

class SurfaceTokenizer:
  def __init__(self):
    self.tokenizer = Tokenizer()

  def get_token_surface(self, sentence):
    if type(sentence) == list:
      sentence = ' '.join(sentence)
    words = []
    for token in self.tokenizer.tokenize(sentence):
      word = token.surface
      word = word.replace(" ", "")
      word = word.replace("\n", "")
      if len(word)>0:
        words.append(word)
    return words