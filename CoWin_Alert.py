#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# importing the requests library
import requests
import sys
import time
import argparse
import yaml
import subprocess
	
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

def searchyPin() :
	print("Input PIN Code : ")
	pincode = input()
	return pincode

def searchByState() :
	print("Select State : ")
	states_data = getAllStates()
	print("Input State ID : ")
	state_id = input()
	print("District in Selected state : ")
	districts_data = getAllDistricts(state_id)
	print("Input District ID : ")
	district_id = input()

	return state_id,district_id

def getAgeLimit() :
	print("Enter Age Limit : ")
	ageLimit = int(input())
	print(ageLimit)
	return ageLimit

def getVaccineType() :
	print("Enter Vaccine Type")
	print("1 : COVAXIN")
	print("2 : COVISHIELD")
	print("3 : Any")
	print("Enter your input : ")
	vaccineType = int(input())
	print(vaccineType)
	return vaccineType

def getDate() :
	print("Enter Date in DD-MM-YYYY format :")
	date = input()
	return date

def GetMeVaccineCenterForPin(pincode, ageLimit, vaccineType,date) :

	# api-endpoint
	URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
	  
	# location given here
	location = "delhi technological university"
	  
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {'pincode':pincode,'date':date}
	  
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)

	#print(URL+'?pincode='+pincode+'&date='+date)
	print('Checking Availibility for pincode : '+pincode+' On : '+date)
	url = URL+'?pincode='+pincode+'&date='+date
	  
	try:  
		# extracting data in json format
		data = r.json()
	except :
		print("Request blocked. We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner.")
		return False

	#print(data['centers'])

	
	for center in data['centers'] :
		#print(str(center['state_id']) + ' : '+ str(center['state_name']))

		for session in center['sessions'] :
			# Check if avilable
			if session['available_capacity'] > 0 :
				# Check if suitabel for my Age
				if session['min_age_limit'] <= ageLimit :
					if int(vaccineType) == 3 :
						print(center['name'])
						print(" Time From : "+str(center['from']+ " To : "+str(center['to'])))
						print("Availability : "+str(session['available_capacity']))
						print("==="*5)
						return True

					if (int(vaccineType) == 1) & (session['vaccine'].upper() == "COVAXIN"):
						print(center['name'])
						print(" Time From : "+str(center['from']+ " To : "+str(center['to'])))
						print("Availability : "+str(session['available_capacity']))
						print("==="*5)
						return True

					if (int(vaccineType) == 2) & (session['vaccine'].upper() == "COVISHIELD"):
						print(center['name'])
						print(" Time From : "+str(center['from']+ " To : "+str(center['to'])))
						print("Availability : "+str(session['available_capacity']))
						print("==="*5)
						return True
				#else :
					#print("Age Limit condition failed")
			
			#else :
				#print("Not available")

	return False

	
	#return data['states']

def GetMeVaccineCenterForStateDistrict(state_id, district_id, ageLimit, vaccineType,date) :

	# api-endpoint
	URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
	  
	# location given here
	location = "delhi technological university"
	  
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {'district_id':district_id,'date':date}
	  
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)

	#print(URL+'?district_id='+district_id+'&date='+date)
	print("Checking Availibility for district_id : "+district_id+' On : '+date)
	url = URL+'?district_id='+district_id+'&date='+date

	try:  
		# extracting data in json format
		data = r.json()
	except :
		print("Request blocked. We can't connect to the server for this app or website at this time. There might be too much traffic or a configuration error. Try again later, or contact the app or website owner.")
		return False

	#print(data)
	#print(data['centers'])

	
	for center in data['centers'] :
		#print(str(center['state_id']) + ' : '+ str(center['state_name']))

		for session in center['sessions'] :
			# Check if date is correct
			if session['date'] == date :
				# Check if avilable
				if int(session['available_capacity']) > 0 :
					# Check if suitabel for my Age
					if session['min_age_limit'] <= ageLimit :
						if int(vaccineType) == 3 :
							print(center['name'])
							print("Fee : "+str(center['fee_type']))
							print("Date : "+str(session['date']))
							print(" Time From : "+str(center['from']+ " To : "+str(center['to'])))
							print("Availability : "+str(session['available_capacity']))
							print("Vaccine : "+str(session['vaccine'].upper()))
							print("==="*5)
							return True
						else :
							print("vaccineType failed")

						if (int(vaccineType) == 1) & (session['vaccine'].upper() == "COVAXIN"):
							print(center['name'])
							print("Fee : "+str(center['fee_type']))
							print("Date : "+str(session['date']))
							print(" Time From : "+str(center['from']+ " To : "+str(center['to'])))
							print("Availability : "+str(session['available_capacity']))
							print("Vaccine : "+str(session['vaccine'].upper()))
							print("==="*5)
							return True

						if (int(vaccineType) == 2) & (session['vaccine'].upper() == "COVISHIELD"):
							print(center['name'])
							print("Fee : "+str(center['fee_type']))
							print("Date : "+str(session['date']))
							print(" Time From : "+str(center['from']+ " To : "+str(center['to'])))
							print("Availability : "+str(session['available_capacity']))
							print("Vaccine : "+str(session['vaccine'].upper()))
							print("==="*5)
							return True
					#else :
						#print("Age Limit condition failed")
				#else :
					#print("Not available")

	return False

def morph(msg) :
	return ("%s\n%s\n%s" % ("~"*80, ("~~ %s" % (msg)), "~"*79))	
def main():
	
	ap = argparse.ArgumentParser(description='''Co-Win Appointment Booking App''', allow_abbrev=False, add_help = False)
	gp = ap.add_argument_group(morph("Help"))
	gp.add_argument('-h','--help', action='help', default=argparse.SUPPRESS, help='Show this messahe and exit')
	gp = ap.add_argument_group(morph("Configure Filter"))
	gp.add_argument('-f','--filter', type=str, default='config.yaml', help='Filter Config YAML file')
	gp = ap.add_argument_group(morph("Get State and Dictrict ID"))
	gp.add_argument('-i', action='store_true',help='Dump State ID and District ID')
	gp.add_argument('-r', action='store_true',help='Ring the Alert')

	args = ap.parse_args()
	#print(args.filter)

	if args.r :
		audio_file = "./bell.wav"
		return_code = subprocess.call(["afplay", audio_file])
		exit()

	if args.i :
		print("Printing State and District IDs")
		states = getAllStates()
		print("Input State ID : ")
		state_id = input()
		districts = getAllDistricts(state_id)
		print("Above are District IDs for State ID "+str(state_id))
		exit()

	with open(args.filter) as f:
	    config = yaml.safe_load(f)
	#print(str(config))

	found = False
	count = 0

	while not found :

		time.sleep(8)
		count = count+1
		print("==============================")
		print("Checking Count : "+str(count))
		
		if 'pincodesearch' in config :
			for pinsearch in config['pincodesearch']:
				result = GetMeVaccineCenterForPin(str(pinsearch['pincode']), pinsearch['age'], pinsearch['vaccine'],pinsearch['date'])
				if result :
					found = True
					print(f"Hit Found on : pincode {pinsearch['pincode']} age {pinsearch['age']} vaccine {pinsearch['vaccine']} on date {pinsearch['date']} ")

		if 'stateSearch' in config :
			for state in config['stateSearch']:
				result = GetMeVaccineCenterForStateDistrict(state['state_id'], str(state['district_id']), state['age'], state['vaccine'],state['date'])
				if result :
					found = True
					print(f"Hit Found on : State {state['state_id']} District {state['district_id']} vaccine {state['vaccine']} on date {state['date']} ")

		print("==============================")
		
	
	audio_file = "./bell.wav"

	return_code = subprocess.call(["afplay", audio_file])




if __name__=="__main__":
    main()
