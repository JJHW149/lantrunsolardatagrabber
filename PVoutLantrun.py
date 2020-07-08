import requests
import json
import datetime
import time

serial = "ENTER INVERTER SERIAL NUMBER"
apikey = "PV OUTPUT API KEY"
sid = "PV OUTPUT SITE ID"

r = requests.session()

# Login
URL = "http://www.lantrunsolar.com//api/login"
PARAMS = {"account": serial, "password":serial}
out = r.post(url= URL, data = PARAMS)
r_json = out.json()


# Retrieve Data
URL = "http://www.lantrunsolar.com//api/storage/getStorageRuntime"
PARAMS = {"serialNum" : serial}
out = r.post(url= URL, data = PARAMS)
if(out.status_code != 200):
    exit(1)
r_json = out.json()

x = datetime.datetime.now()

URL = "https://pvoutput.org/service/r2/addstatus.jsp?key=" + apikey + "&sid=" + sid + "&v2=" + str(int(r_json["pInvText"][:-2])) + "&d=" + x.strftime('%Y%m%d') + "&t=" + x.strftime('%H:%M')
out = r.get(url=URL)

r.close()