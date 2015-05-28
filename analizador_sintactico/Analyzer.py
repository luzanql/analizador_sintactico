#!/usr/bin/python 

import nltk
import re
import os
from nltk.parse import stanford
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

class Analyzer:

	def __init__(self):
		pass


	def tagger(self, frase):
		#hacer el tag
		text = nltk.word_tokenize(frase)
		postag = nltk.pos_tag(text)

		#convertirlo al formato lips
		result = "("
		
		for index in range(len(postag)):
			result +=  "( " + postag[index][0] + " ( " + postag[index][1]+ " ) )"

		result += ")"

		#ejecutar bikel
		
		os.popen('tcsh parse 400 ../../dbparser/settings/collins.properties ../../wsj-02-21.obj.gz ' +result)


		

			
		
		return result
		

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
			cf.add_widget(tc,40,40) # (10,10) offsets
			cf.print_to_file('tree.ps')
			#cf.destroy()
			os.popen('convert tree.ps -resize 300% static/img/tree.png')
