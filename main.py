import os
from square.client import Client


client = Client(
    access_token=os.getenv("ACCESS_TOKEN"),
    environment='sandbox',
)

result = api_locations.list_locations()
# Call the success method to see if the call succeeded
if result.is_success():
	# The body property is a list of locations
    locations = result.body['locations']
	# Iterate over the list
    for location in locations:
    	# Each location is represented as a dictionary
        for key, value in location.items():
        	print(f"{key} : {value}")
        print("\n")
# Call the error method to see if the call failed
elif result.is_error():
    print('Error calling LocationsApi.listlocations')
    errors = result.errors
    # An error is returned as a list of errors
    for error in errors:
    	# Each error is represented as a dictionary
        for key, value in error.items():
            print(f"{key} : {value}")
        print("\n")
