# Lantrun Solar Data Grabber
Data collection tool for Lantrun solar systems

## PVoutLantrun.py  
This python tool makes a request to lantruns solar monitor system to collect the current solar generation and uploads it to PVoutput.org   
By providing the tool the Serial number of your inverter along with the api key and site id for your PVoutput account,
It can automatically update the site with live solar data.  
  
Update these python values:  
```python
serial = "ENTER INVERTER SERIAL NUMBER"
apikey = "PV OUTPUT API KEY"
sid = "PV OUTPUT SITE ID"
```  
For automation of this program use crontab  
