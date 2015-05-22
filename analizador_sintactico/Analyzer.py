#!/usr/bin/python 

import os
from nltk.parse import stanford
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

class Analyzer:

	def __init__(self):
		pass

	def execute(self, frase):

		os.environ['STANFORD_PARSER'] = 'nltk/stanford-parser.jar'
		os.environ['STANFORD_MODELS'] = 'nltk/stanford-parser-3.5.2-models.jar'

		parser = stanford.StanfordParser(model_path="nltk/englishPCFG.ser.gz")
		sentence = parser.raw_parse(frase)
		print sentence

		# GUI
		for line in sentence:
			cf = CanvasFrame()
			tc = TreeWidget(cf.canvas(),line)
			cf.add_widget(tc,10,10) # (10,10) offsets
			cf.print_to_file('tree.ps')
			cf.destroy()
			os.popen('convert tree.ps tree.png')
