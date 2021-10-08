import requests
response = requests.get(
	url="http://api.open-notify.org/iss-now.json") # end-point for the API

print("Status code for the resoponse is : ")
print(response.status_code)  
# if the endpoint is valid, I will get 200 as the status of the respond 
# if the end-point is ivalid, I will get 404 as the status of the respond 

# if response.status_code == 404:
# 	raise Exception("Page Not found")
# elif response.status_code == 401:
# 	raise Exception("You are an unauthorized user") 

response.raise_for_status()
data = response.json() 			# The entire json format

iss_position = response.json()['iss_position']
print("The ISS position is : ",
	iss_position)

longitude = response.json()['iss_position']['longitude']
print("The logitude of ISS : ",longitude)

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude,latitude)

print("Latitude and Longitude : ")
print(iss_position)
