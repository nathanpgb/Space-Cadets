import re,requests

validEmail = "[a-zA-Z0-9.-]+@ecs.so(uthamp)?ton.ac.uk"
emailID = str(input("enter user email\n"))
if re.match(validEmail,emailID):
	id = emailID
	url = "https://ecs.soton.ac.uk/people/"+id
	response = requests.get()
	if response == 404:
		print("Error reaching the web page")
	elif response == 200:
		responseText = response.text
		names = re.findall('"name": ".*"', responseText)
	else:
		print("Error\nResponse Code:", str(response.code))
	
else:
	print("invalid email")
