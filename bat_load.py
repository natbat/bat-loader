from fastkml import kml
import json
import datetime

def fetch_bats():

    bats = json.loads(
        # Read the local config file
        open("bats.json").read()
    )
    print('fetched the bats')
    return bats


def human_location(lat, lon, alt):
    # returns a human readable location, eg "Alamo Square" or "Lake Merced"
    return


def earliest_recording_date(observations):
    # returns a date object of the earliest recording
    return


def list_of_bat_species_en(observations):
    # returns a string
    return


def upload_soundcloud(arg):
    '''
    Playlist Name: Bats in $human_location
    Playlist Description:
        Sounds of bats in $human_location recorded on the Echo Meter by
        Wildlife Acoustics. $num_recordings bats observed include
        $list_of_bat_species_en
    Playlist Image: ?
    Playlist Release Date: $earliest_recording_date
    Playlist Genre: Science
    Playlist Tags: #bats #EchoMeter #$human_location
    Playlist Privacy: Public
    '''

    '''
    Track Title: $bat_en in $human_location
    Track Genre: Science:
    Track Tags:
        #bats #EchoMeter #$human_location $bat_en $bat_latin
        +(machine tags for geo)
    Track Description:
        Recording of a $bat_en ($bat_latin) in $human_location
        (lat:$lat, lon:$lon, alt:$alt)
        Note $track_note
    Track Privacy: Public:
    Track Image: ?
    '''

    return


def upload_inaturalist(arg):
    '''
    Species: $bat_latin
    When: "$date $time" '2017-07-16T16:15:47-07:00' YYYY-MM-DDTHH:MM:SS-TZoffset
    Where: "$lat, $lon"
    Description:
        $bat_en ($bat_latin) in $human_location
        Note $track_note
    Tags:
        #bats #EchoMeter #$human_location $bat_en $bat_latin
        +(machine tags for soundcloud?)
    Captive: No
    Photos: ?

    How detected: Heard
    Certainty: sure (can be pretty sure because of identification in app)
    '''

    return


def bat_stuff():

    bats = fetch_bats()

    filename = "audio/2017-07-05_AlamoSquare/Session 20170705_203949.kml"
    file = open(filename, "r")

    # Setup the string which contains the KML file we want to read
    # close the file
    bat_locations = file.read()
    file.close()

    # Create the KML object to store the parsed result
    k = kml.KML()

    # Read in the KML string and create list of kml nodes aka 'features'
    k.from_string(bat_locations)
    f = list(k.features())
    observations = list(f[0].features())

    print('starting to loop through the observations')

    for o in observations:

        # The last node in the KML file seems to not be an observation,
        # it doesnt have a name, so we are skipping it
        if o.name is None:
            print('NO NAME so skipping item')
            continue

        observation = extract_info(o, bats)


    return


def extract_info(node, bats):

    # set up empty dictionary
    observation_info = {}

    # This has data encoded into it, its also the .wav file name
    file_name = observation_info['file_name'] = node.name

    # Extract the date and turn into a python date object
    # YYYYMMDD HHMMSS
    # Totally ignoring timezones right now, seems to be local time on phone
    date_raw = observation_info['date_raw'] = file_name.split("_")[1]
    time_raw = observation_info['time_raw'] = file_name.split("_")[2]
    observation_info['date'] = datetime.datetime.strptime(date_raw+time_raw, "%Y%m%d%H%M%S")

    # Get species information and match to config file of bats
    species_ref = observation_info['species_ref'] = observation_info['file_name'].split("_")[0]


    observation_info['species_latin'] = bats[species_ref]['latin']
    observation_info['species_en'] = bats[species_ref]['en']

    # Location information
    lon = observation_info['lon'] = node.geometry.x
    lat = observation_info['lat'] = node.geometry.y
    alt = observation_info['alt'] = node.geometry.z

    # Aditional notes from file to add as descriptions
    # TODO from wav file https://www.wildlifeacoustics.com/blog/wildlife-acoustics-contributes-technology-as-open-source

    print observation_info['date'], observation_info['species_en'], observation_info['species_latin'], lat, lon, alt

    return observation_info


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
