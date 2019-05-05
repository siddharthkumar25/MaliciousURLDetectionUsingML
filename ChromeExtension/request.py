import requests
url = 'http://127.0.0.1:5000/api'
r = requests.get(url,params={'url':'http://gle.cossm/www/12.02.2/www/www/www'})
print(r.json())