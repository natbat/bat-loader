from fastkml import kml
import json
import datetime


def fetch_bats():
    return json.loads(
        # Read the local config file
        open("bats.json").read()
    )

def bat_stuff():

    filename = "audio/2017-07-05_AlamoSquare/Session 20170705_203949.kml"
    file = open(filename, "r")

    bats = fetch_bats()

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
        file_name = o.name

        if file_name is None:
            continue

        # Extract the date and turn into a python date object
        # YYYYMMDD HHMMSS
        # Totally ignoring timezones right now, seems to be local time on phone
        date_raw = file_name.split("_")[1]
        time_raw = file_name.split("_")[2]
        date = datetime.datetime.strptime(date_raw+time_raw, "%Y%m%d%H%M%S")

        #
        species_ref = file_name.split("_")[0]
        species_latin = bats[species_ref]['latin']
        species_en = bats[species_ref]['en']

        print date_raw, date, species_ref, species_latin, species_en

if __name__ == '__main__':
    bat_stuff()



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
