from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime
#import os
#from .forms import TextoEntradaForm
# -*- encoding: utf-8 -*-
import sys
from analizador_sintactico.Analyzer import Analyzer


#sys.path.append('/home/andrea-lozada/Descargas/freeling-3.1/APIs/python')
#import freeling_python as freeling


def index(request):
	if request.method == 'POST':
		if 'texto' in request.POST and request.POST['texto']:
			
			entrada_texto = request.POST['texto']
			analizador = Analyzer()
			analizador.execute(entrada_texto)
			return render(request, 'index.html',{'texto_entrada': entrada_texto, 'results':1})

		else:
			return HttpResponse('Please submit a search term.')
	elif request.method == 'GET':
		return render(request, 'index.html')
	else:
		raise Http404()
    


