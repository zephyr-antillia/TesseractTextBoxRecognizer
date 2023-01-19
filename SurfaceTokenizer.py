#
# SurfaceTokenizer.py
# 2023/01/10
# to-arai

from janome.tokenizer import Tokenizer


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

  # 2023/01/10
  def get_nouns(self, sentence):
    if type(sentence) == list:
      sentence = ' '.join(sentence)
    words = []
    for token in self.tokenizer.tokenize(sentence):
      part_of_speech = token.part_of_speech.split(',')[0]
      if part_of_speech == u'名詞':
        word = token.surface
        if len(word)>0:
          words.append(word)
    return words