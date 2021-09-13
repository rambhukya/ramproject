'''
import json
import random
data = json.load(open("quotes.json",encoding="utf8"))
def get_quote(data):
    print(random.choice(data))
    

get_quote(data)
'''
