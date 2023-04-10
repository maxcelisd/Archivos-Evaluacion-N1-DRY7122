# Fill in this file with the code from parsing JSON exercise

import json
import yaml

with open ('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as json_file:
    ourjson = json.load (json_file)
    print("Token de acceso: {}".format(ourjson['access_token']))
    print("Caduca en: {} segundos".format(ourjson['expires_in']))
    print("Token de refresco: {}".format(ourjson['refresh_token']))
    print("Caduca en: {} segundos".format(ourjson['refreshtokenexpires_in']))
    
    
    
