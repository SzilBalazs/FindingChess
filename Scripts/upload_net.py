import requests

URL      = 'http://findingchess.shaheryarsohail.com/scripts/'
FILENAME = ''

data = {
    'engine'   : '',
    'name'     : '',
    'username' : '',
    'password' : '',
    'action'   : 'UPLOAD',
}

with open(FILENAME, 'rb') as file:
    r = requests.post(URL, data=data, files={'netfile' : file})

print(r.text)