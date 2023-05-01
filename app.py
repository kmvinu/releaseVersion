import requests
import json
import os
from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'
    
 #adding variables
@app.route('/greet/<groupid>/<artifact>')
def get_latest(groupid,artifact):
  #returns the groupid

  g="org.springframework.webflow"
  a="org.springframework.webflow"
  endpoint_url = "https://search.maven.org/solrsearch/select?q=g:"+groupid+"%20AND%20a:"+artifact+"%20&rows=20&wt=json"
  
  response = requests.get(endpoint_url)

  # Parse the JSON data from the response
  parsed_data = json.loads(response.text)
  #print(parsed_data["response"])

    # Accessing the data
  for post in parsed_data["response"]["docs"]:
    epoch=post["timestamp"]
    if len(str(epoch)) == 13:
        datetime_obj = datetime.fromtimestamp(int(epoch)/1000)
    else:
        datetime_obj = datetime.fromtimestamp(int(epoch))
    date_time = datetime_obj.strftime("%m/%d/%Y, %H:%M:%S")
    print("Release date is:" , date_time)
    if  "latestVersion" in post:
        version=post["latestVersion"]
        print("Latest Version is:" + version)
    if "g" in post:
        groupid=post["a"]
        print("Group ID:" + groupid)
    if "a" in post:
        artifact=post["a"]
        print("Artifact:" + artifact)
 
  result = "Latest Version:" + version + "\n\r" + "Release Date:"+date_time + "\nGroupId:"+groupid

  return 'Result: %s' % result
