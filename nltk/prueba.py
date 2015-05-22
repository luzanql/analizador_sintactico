import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = 'stanford-parser.jar'
os.environ['STANFORD_MODELS'] = 'stanford-parser-3.5.2-models.jar'

parser = stanford.StanfordParser(model_path="englishPCFG.ser.gz")
sentence = parser.raw_parse("Hello, My name is Melroy.")
print sentence

# GUI
for line in sentence:
	line.draw()
"""
for line in sentences:
	#print line
	for sentence in line:
		print sentence
		sentence.draw()
"""
