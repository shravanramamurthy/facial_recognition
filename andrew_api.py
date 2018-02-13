import requests
import json
import pprint


def getStudentId(andrew_id):
	# setup parameters

	# send requests
	url = "https://apis.scottylabs.org/directory/v1/andrewID/" + andrew_id

	response = requests.get(url)
	data = ""
	if (response.status_code == 200):
		data = response.json()
	else:
		return None
	# exit(0)
	return data

print (getStudentId("cemery"))
