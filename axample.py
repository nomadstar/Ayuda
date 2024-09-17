import requests

# Define the URL and query parameters
url = 'http://localhost:8800/vulnerabilities/brute/'
params = {
    'username': 'admin',
    'password': 'password',
    'Login': 'Login'
}
cookies = {
    'PHPSESSID': 'kg1kc38q6uoj9pcptkcm91ogv5',
    'security': 'low'
}
response = requests.get(url, params=params, cookies=cookies)
if 'incorrect' in response.text:
    print('wrong')
elif 'Welcome' in response.text:
    print('yeah')
else:
    print('FAIL')
