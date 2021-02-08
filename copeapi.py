import json
import requests


class Partner:
    def __init__(self, name=None, date=None, email=None):
        self.name = name
        self.date = date
        self.email = email
        

    # @classmethod
    def all(self):
        print("+:"*25)
        print(f'Name: {(self.name).title()}')
        print(f'Date: {(self.date)}')
        print(f'Email: {(self.email)}')
        print(":+"*25)


class Run:
    def __init__(self,url=None ):
        self.url= f'https://ct-api-challenge.herokuapp.com/'

    def sort(self):
        url = requests.get(self.url)
        jnfo = url.json()
        name =   jnfo['partners'][i]['firstName']
        date =  jnfo['partners'][i]['availableDates']
        email = jnfo['partners'][i]['email']
        p = Partner(name, email, date)
        p.all()



for i in range(len(jnfo['partners'])):
    program = Run(i)
#     program.get_name()
    program.sort()
