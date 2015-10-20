from getBLEIds2 import *

if __name__ == "__main__":
	while True:
		reset()
		out, error = getDevices()
		jsonText = getJSON(out, error)
		# transmit to cloud here
		# add delay to loop if a slower response is desired
		# current delay is ~5 seconds, (the time it takes to perform one scan)
		print jsonText
	
