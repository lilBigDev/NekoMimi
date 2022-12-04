# __init__.py
from pyfiglet import Figlet
import random
import requests
import json


version = "1.0.8"

def figlet(text, mode="small"):
    f = Figlet(font=mode)
    render = f.renderText(text)
    return render

def urban(query):
    try:
        urban = requests.get(f'https://api.urbandictionary.com/v0/define?term={query}')
        url = json.loads(urban.text)
    except Exception:
        return "Urban API returned invalid data... might be down or your IP is banned."

    if not url:
        return "I think the API broke..."

    if not len(url['list']):
        return "Couldn't find your search in the dictionary..."

    result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]
    return result

def jsonAPI(endpoint):
    url = requests.get(endpoint)
    outputJson = json.loads(url.text)
    return outputJson

def write(data,file):
    try:
        fappen = open(file,"w")
        fappen.write(data)
        fappen.close()
        return "Done !"
    except(Exception):
        print (Exception)
        return "Failed !"

def read(file):
    fappen = open(file,"r")
    rd = fappen.read()
    fappen.close()
    return rd

def brainshopAi(bid,secret,msg):
    url = f'http://api.brainshop.ai/get?bid={bid}&key={secret}&uid=[42]&msg={msg}'
    response = jsonAPI(url)
    return response['cnt']

def banner(name):
    fonts = ['small' , 'slant' , 'mini' , 'banner' , 'big']
    mode = random.choice(fonts)
    benner = figlet(name,mode)
    return benner

def isUp(url):
    try:
        req = requests.get(url)
    except:
        return False
    if req.status_code == 200:
        return True
    else:
        return req.status_code