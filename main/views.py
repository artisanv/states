from django.shortcuts import render
from django.http import HttpResponse
from main.models import State, City
from main.models import State, StateCapital
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from main.forms import CitySearchForm
from django.template import ReqestContext
from django.shortcuts import render,render_to_response
from main.forms import CitySearchForm, CreateCityForm
# Create your views here.

def city_create(request):
	request_context = ReqestContext(request)
	context={}

	if request.method=='POST' :
		form = CreateCityForm(request.POST)
		context['form']=form

		if form.is_valid():
			form.save()

			return render_to_response("city_create.html",context,context_instance =request_context)
		else:

			context['valid'] = form.errors
			return render_to_response("city_create.html",context,context_instance =request_context)








def city_search(request):
	request_context = ReqestContext(request)

	context={}

	if request.method == 'POST'
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state form.cleaned_data['state']

			context ['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

			return render_to_response('city_search.html',context,context_instance=request_context)
		else:
			context['valid'] =forms.errors

			return render_to_response('city_search.html',context,context_instance=request_context)

	else:
		form = CitySearchForm()
		context['form'] = form
		return render_to_response('city_search.html',context,context_instance=request_context)
		




class StateListView (ListView):
	model = State
	template_name ='states_list.html'
	context_object_name = 'states'

def state_detail(request,pk):

	context ={}
	state = state.objects.all(pk=pk)
	context ['state'] = state
	return render(request,'state_detail.html',context)

class StateDetailView (DetailView):
	model =state
	template_name = 'state_detail.html'
	context_object_name ='state'
	return render(request)






def template_view (request):
	context ={}

	states = State.objects.all()

	context['states'] = states

	return render(request,'state_list.html',context)



def get_search (request):

	get_var = request.Get.get ('q',None)

	print request.Get
	print request.POST


	text_string =''

	text_string += 'Search Term : %s <br>' % get_var

	text_string += """
	<form action  = "/get_search method ="GET">

	Search Cities :
	<input type ='text' name ='q'>

	</form>
	"""

	if get_var != None:
		cities = city.objects.filter(name__icontains=get_var)
		for city in cities:
			text_string+= '%s <br>' % city.name


def state_detail (request, name):
	state = State.objects.get(name=name)
	cities = state.city_set.all()


	text_string ='<h3> %s </h3>' % state.name

	for city in cities:
		try:
			text_string += '%s </br>'% city.name
		except Exception , e :
			print e
	return HttpResponse(text_string)


def state_list(request):

	context ={}

	
	states = State.objects.all()
	state_list = []

	context['states']= states

	# for state in states:

	# 	try :
	# 		state_list.append("<a href='/state_detail/%s'> %s -- %s </a> <br>" %(state.name,state.name, state.statecapital.name)) ##why statecapital not StateCapital ??
	# 	except Exception , e:
	# 		print e
	# return HttpResponse(state_list)	
	return render(request,'state_list.html',context)


	