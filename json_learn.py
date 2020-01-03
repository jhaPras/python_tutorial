import json

data = {
    'president':{
        'name':'Zaphod Beeble',
        'species':'Martian'
    }
}


new_data = str({'username':'parsen.jha','password':'prasenjit@2267'})

with open('myfile.txt','r') as fobj:
    obj=fobj.readlines()
    for item in obj:
        if item == 'username':
            print(obj[item])

