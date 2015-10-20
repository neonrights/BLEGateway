import re
import os
import subprocess
import json

def reset():
	# resetting bluetooth dongle
	os.system("sudo hciconfig hci0 down")
	os.system("sudo hciconfig hci0 up")

def getDevices():
	# getting nearby devices, runs for 5 seconds
	p = subprocess.Popen(['sudo', 'timeout', '5', 'hcitool', 'lescan'], stdout=subprocess.PIPE)
	# (out, err) = p.communicate()
	return p.communicate()

def getJSON(out, error=None):
	# regex removes improperly formatted id's
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
	
	# putting information into a dictionary
	jsonDict = {}
	jsonDict['gateway'] = {}

	BLEInfo = subprocess.Popen('hciconfig', stdout=subprocess.PIPE)
	(out, err) = BLEInfo.communicate()
	gatewayID = out.split('\n')[1].split(' ')[2]

	jsonDict['gateway']['car'] = 'car-number';
	jsonDict['gateway']['id'] = gatewayID
	
	jsonDict['gateway']['luggage'] = list(idSet);
	
	return json.dumps(jsonDict, indent=4)

if __name__ == "__main__":
	reset()
	out, error = getDevices()
	jsonText = getJSON(out, error)
	print jsonText

