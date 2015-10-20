import re
import os
import subprocess
import json

# resetting bluetooth dongle
os.system("sudo hciconfig hci0 down")
os.system("sudo hciconfig hci0 up")

# getting nearby devices, runs for 5 seconds
p = subprocess.Popen(['sudo', 'timeout', '5', 'hcitool', 'lescan'], stdout=subprocess.PIPE)
(out, err) = p.communicate()

# regex removies improperly formatted id's
# matches any 5 hexadecimals with a colon between each
idSet = set()
r = re.compile('^..:..:..:..:..:..$')

ids = out.split('\n')
for i in range(0, len(ids)):
	tokens = ids[i].split(' ')
	if len(tokens) == 2:
		id = tokens[0]
		name = tokens[1]
		
		# will normally be (luggage ble) or something
		if (r.match(id) is not None):
			idSet.add(id)

jsonText = '{\n\t\"gateway": {\n\t\t\"car\": \"'
jsonDict = {}
jsonDict['gateway'] = {}

BLEInfo = subprocess.Popen('hciconfig', stdout=subprocess.PIPE)
(out, err) = BLEInfo.communicate()
gatewayID = out.split('\n')[1].split(' ')[2]

jsonDict['gateway']['car'] = 'car-number'
jsonDict['gateway']['id'] = gatewayID
jsonDict['gateway']['luggage'] = list(idSet)

print json.dumps(jsonDict, indent=4)
