import requests

endpoints = {
	'admin': 'admin_url',
	'login': 'login_url'
}

payload = {
	'username': 'your_username',
	'password': 'your_password',
}

session = requests.Session()
print('Connecting to site...', session.get(endpoints['admin']))
# Connecting to site <Response [200]>

payload['csrfmiddlewaretoken'] = session.cookies['csrftoken']
response = session.post(endpoints['admin'], data=payload)
print('Logging in...', response)
# Logging in <Response [200]>

# Do the rest!
