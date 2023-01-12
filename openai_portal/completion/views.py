from django.shortcuts import render
from django.http import HttpResponse
import openai
import os
import logging

openai.api_key = os.getenv('openai_key')


# Create your views here.
def completion(request):
	# define options for form <select> elements
	engine_options = ['text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001']
	engine_help = '''Engines determine how the text generation is handled. Here's an overview of available models:
	- text-davinci-003: most advanced, slowest
	- text-curie-001: advanced, slower
	- text-babbage-001: simple, faster
	- text-ada-001: simplest, fastest
	'''
	num_generations = ['1', '2', '3']
	context = {'engine_options': engine_options, 'num_generations': num_generations, 'engine_help': engine_help}
	if request.method == 'GET':
		return render(request, 'completion/completion.html', context)
	if request.method == 'POST':
		gpt_response = openai.Completion.create(engine=request.POST.get('engine-option'), prompt=request.POST.get('query'), max_tokens=1024, n=int(request.POST.get('num-generations')))
		context['output'] = gpt_response.choices
		logging.warn(context['output'])
		context['query'] = request.POST.get('query')
		return render(request, 'completion/completion.html', context)