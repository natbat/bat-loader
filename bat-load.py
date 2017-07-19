from fastkml import kml

filename = "audio/2017-07-05_AlamoSquare/Session 20170705_203949.kml"
file = open(filename, "r")
#for line in file:
#   print line,

# Setup the string which contains the KML file we want to read
# close the file
bat_locations = file.read()
file.close()

# Create the KML object to store the parsed result
k = kml.KML()

# Read in the KML string
k.from_string(bat_locations)
f = list(k.features())
observations = list(f[0].features())

for o in observations:



"""
<Placemark>
	<name>LASCIN_20170705_204103</name>
	<description><![CDATA[5 July 2017 at 20:41<br/>Latitude:37.77658<br/>Longitude:-122.4353]]></description>
	<styleUrl>#MarkerStyleLASCIN</styleUrl>
	<Point>
		<coordinates>-122.435272,37.776577,71.763763</coordinates>
        # Longitude, Latitude, Altitude
	</Point>
</Placemark>
"""

""" LINKS
Read a KML file :
https://fastkml.readthedocs.io/en/latest/usage_guide.html#read-a-kml-file
"""
