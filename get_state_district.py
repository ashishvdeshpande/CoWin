#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# importing the requests library
import requests
import sys
	
def getAllStates() :
	  
	# api-endpoint
	URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
	  
	# location given here
	location = "delhi technological university"
	  
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {}
	  
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)
	  
	# extracting data in json format
	data = r.json()

	#print(data['states'])

	for state in data['states'] :
		print(str(state['state_id']) + ' : '+ str(state['state_name']))

	return data['states']

def getAllDistricts(state_id) :
	  
	# api-endpoint
	URL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(state_id)
	  
	# location given here
	location = "delhi technological university"
	  
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {}
	  
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)
	  
	# extracting data in json format
	data = r.json()

	#print(data['districts'])

	for district in data['districts'] :
		print(str(district['district_id']) + ' : '+ str(district['district_name']))

	return data['districts']
	
def main():
	states = getAllStates()
	print("Input State ID : ")
	state_id = input()
	districts = getAllDistricts(state_id)
	print("Input District ID : ")
	district_id = input()

	'''
	print(states)
	prints(districts)
	print("State Id for : "+str(states[int(state_id)])+" is "+state_id)
	print("District Id for : "+str(districts[int(district_id)])+" is "+district_id)
	'''

	
if __name__=="__main__":
    main()
