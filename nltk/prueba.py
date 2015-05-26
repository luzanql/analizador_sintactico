import os
from nltk.parse import stanford
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

os.environ['STANFORD_PARSER'] = 'stanford-parser.jar'
os.environ['STANFORD_MODELS'] = 'stanford-parser-3.5.2-models.jar'

parser = stanford.StanfordParser(model_path="englishPCFG.ser.gz")
sentence = parser.raw_parse("Hello, My name is Melroy.")
print sentence

# GUI
for line in sentence:
	cf = CanvasFrame()
	tc = TreeWidget(cf.canvas(),line)
	cf.add_widget(tc,40,40) # (10,10) offsets
	cf.print_to_file('tree.ps')
	cf.destroy()
	os.popen('convert tree.ps tree.png')
