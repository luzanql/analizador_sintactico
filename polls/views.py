from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime
#import os
from polls.forms import TextoEntradaForm
# -*- encoding: utf-8 -*-
import sys


#sys.path.append('/home/andrea-lozada/Descargas/freeling-3.1/APIs/python')
#import freeling_python as freeling


def index(request):
    return render(request, 'index.html')

