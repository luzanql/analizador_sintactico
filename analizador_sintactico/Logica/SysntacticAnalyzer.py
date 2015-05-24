import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = 'stanford-parser.jar'
os.environ['STANFORD_MODELS'] = 'stanford-parser-3.5.2-models.jar'

class AnalizadorSintactico:
	
	def __init(self):
		self.parser = stanford.StanfordParser(model_path="englishPCFG.ser.gz")

	def parse_sentence(self, input):
		sentence = self.parser.raw_parse(input)
		return sentence[0]

	def dibujar(self, tree):
		tree.draw()

