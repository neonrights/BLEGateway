# gets bluetooth id's from a text doc
file = open("results.txt", r)

# finds unique id's in text doc
for line in file:
	String[] tokens = line.split(" ")
	String id = tokens[0]
	String name = tokens[1]
	# if name is correct continue
		# if unique, add to array
		# alternatively could just add to a hash table, guaranteed unique

f.close()
	
# format unique id's into xml / json
String xml = "<results><gateway id="
# get gateway id and append to xml string
xml.append("'gateway id'")
# for each unique id, add to xml

# send xml and json
