#!/usr/bin/env python

import csv
import os 
import sys

sys.path.append("..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') # in notes is django_states.settings

from main.models import State , StateCapital
import django
django.setup()

dir_path = os.path.dirname (os.path.abspath(__file__)) # finding directory path
# print '%s/states.csv' %dir_path

states_csv = os.path.join(dir_path,'states.csv') #best way .. pythonic way :P

csv_file = open(states_csv,'r') # r = read mode

print csv_file

reader = csv.DictReader(csv_file)

for row in reader :
	# print row['abbrev']
	# print row['state']
	# print row['capital']
	# print row['latitude']
	# print row['longitude']
	# print row['population']
	new_state, created = State.objects.get_or_create(name=row['state']) #created is a boolean for the function called , must include

	print new_state
	print created

	#new_state = State()

	# class attribiutes here refer to the model ( left)
    # names inside row[] are refered to the names from the csv file
	new_state.abbreviation = row['abbrev']
	new_state.name = row['state']

	new_state.save()
	
	statecapital, created = StateCapital.objects.get_or_create(name=row['capital'])
	statecapital.state =new_state
	statecapital.capital = row['capital']
	statecapital.latitude = row['latitude']
	statecapital.longtitude = row['longitude']
	statecapital.population = row['population']
	statecapital.save()



# from main.models import State

# states = State.objects.all()

# for state in states:
# 	print state.name

