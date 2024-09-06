import json 
import os 
if __name__ == '__main__':
   app = json.load(open("configmap.json"))
   print(app['database_host'])
   print(app['database_port'])