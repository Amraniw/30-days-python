#PIP = Preferred installer program

import webbrowser 

#list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

#opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)


import requests 

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt.'

response = requests.get(url) # opening a network and fetching data
print(response) 
print(response.status_code) # status code, success:200
print(response.headers) # headers information
print(response.text) # gives all the text from the page 

import requests 
url = 'https://restcountries.com/v3.1/all?fields=name,capital,region,population'
response = requests.get(url)
print(response)
print(response.status_code) 
countries = response.json()
print(countries[:1])

#practise api 