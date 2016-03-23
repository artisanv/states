#!/usr/bin/env python

import csv
import os 
import sys

sys.path.append("..")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') # in notes is django_states.settings

from main.models import State , StateCapital , City
import django
django.setup()

dir_path = os.path.dirname (os.path.abspath(__file__)) # finding directory path
# print '%s/states.csv' %dir_path

states_csv = os.path.join(dir_path,'cities.csv') #best way .. pythonic way :P

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
	new_city, created = City.objects.get_or_create(name=row['city']) #created is a boolean for the function called , must include

	# print new_city
	# print created

	#new_state = State()

	# class attribiutes here refer to the model ( left)
    # names inside row[] are refered to the names from the csv file
	#new_state.abbreviation = row['state']
	


	# new_state,created = State.objects.get_or_create(abbreviation=row['state'])
	# new_city.state = new_state

	new_city.state ,created = State.objects.get_or_create(abbreviation = row['state'])
	

	
	
	#statecapital, created = StateCapital.objects.get_or_create(name=row['capital'])
	#statecapital.state =new_city
	new_city.county = row['county']
	new_city.latitude = row['latitude']
	new_city.longtitude = row['longitude']
	new_city.zip_code = row['zip_code']
	


	try:
		new_city.save()
	except Exception, e:
		print e
		print row 
	



# from main.models import State

# states = State.objects.all()

# for state in states:
# 	print state.name

