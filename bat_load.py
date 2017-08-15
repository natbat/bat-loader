from fastkml import kml
import json
import datetime
import requests

# ipython
# reload(bat_load)
# bat_load.bat_stuff()

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


def upload_mixcloud(arg):
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


def upload_inaturalist(observation_info,inat_access_token):

    print('\ngoing to construct iNaturalist arguments')
    inat_url='https://api.inaturalist.org/v1'

    #r = requests.get('http://example.com')

    # r = requests.get(inat_url+'/observations/7083815.json')
    # this returns a dictionary
    # r.json()[u'taxon_id']

    # r = requests.get(inat_url+'/projects/225/members.json', headers={'Authorization': 'Bearer '+inat_access_token})
    # returns a list of dictionarys!
    # r.json()[0][u'created_at']

    payload = {
        'observation[species_guess]': observation_info['species_en'],
        'observation[taxon_id]': observation_info['species_inat'],
        'observation[id_please]': '0',
        'observation[observed_on_string]': observation_info['date_string'], # can not be in the future
        'observation[time_zone]': 'Pacific Time (US & Canada)',
        'observation[description]': observation_info['species_en']+ ' ('+observation_info['species_latin']+') in $human_location. Note $track_note',
        'observation[tag_list]': 'bats, EchoMeter, '+observation_info['species_en']+', '+observation_info['species_latin'],
        #'observation[place_guess]': '$human_location',
        'observation[latitude]': observation_info['lat'],
        'observation[longitide]': observation_info['lon'],
        'observation[map_scale]': '5',
        'observation[positional_accuracy]': '2',
        'observation[geoprivacy]': 'open'
    }
    payload_min = {
        'observation[species_guess]': observation_info['species_en'],
        'observation[taxon_id]': observation_info['species_inat'],
        'observation[description]': observation_info['species_en']+ ' ('+observation_info['species_latin']+') in $human_location. Note $track_note',
    }


    post_url = inat_url+'/observations'
    print(post_url, payload_min)

    print('calling iNat with URL')
    r = requests.post(post_url, data=payload, headers={'Authorization': 'Bearer '+inat_access_token})
    # https://www.inaturalist.org/pages/api+reference#post-observations
    print(r, type(r))


    if r.status_code == 200 and r.json():
        print('Successfully added observation\n\n\n')
    else:
        print('whoops')
        print(r.status_code,r.text)
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

    '''
    observation[observation_field_values_attributes][order]
    Nested fields for observation field values are specified in the observation_field_values_attributes param. order is just an integer starting with zero specifying the order of entry.
    Allowed values: ObservationFieldValue attributes. So you might specify an entire observation field value for an observation field with an ID of 1 as observation[observation_field_values_attributes][0][observation_field_id]=1&observation[observation_field_values_attributes][0][value]=foo.
    flickr_photos[]
    List of Flickr photo IDs to add as photos for this observation. User must have their Flickr and iNat accounts connected and the user must own the photo on Flickr.
    Allowed values: Valid Flickr photo ID of a photo belonging to the user. Flickr photo IDs are integers.
    picasa_photos[]
    List of Picasa photo IDs to add as photos for this observation. User must have their Picasa and iNat accounts connected and the user must own the photo on Picasa.
    Allowed values: Valid Flickr photo ID of a photo belonging to the user.
    facebook_photos[]
    List of Facebook photo IDs to add as photos for this observation. User must have their Facebook and iNat accounts connected and the user must own the photo on Facebook.
    Allowed values: Valid Facebook photo ID of a photo belonging to the user.
    local_photos[]
    List of fields containing uploaded photo data. Request must have a Content-Type of "multipart." We recommend that you use the POST /observation_photos endpoint instead.
    Allowed values: Photo data
    '''

    '''
    iNaturalist Params

    identification[observation_id]
    ID of the associated observation
    Allowed values: Valid iNat observation ID

    identification[taxon_id]
    ID of the associated taxon
    Allowed values: Valid iNat taxon ID

    identification[body]
    Optional user remarks on the identification.

    timezones: Allowed values: Abu Dhabi | Adelaide | Africa/Johannesburg | Alaska | Almaty | American Samoa | Amsterdam | Arizona | Asia/Magadan | Astana | Athens | Atlantic Time (Canada) | Atlantic/Cape_Verde | Auckland | Australia/Perth | Azores | Baghdad | Baku | Bangkok | Beijing | Belgrade | Berlin | Bern | Bogota | Brasilia | Bratislava | Brisbane | Brussels | Bucharest | Budapest | Buenos Aires | Cairo | Canberra | Cape Verde Is. | Caracas | Casablanca | Central America | Central Time (US & Canada) | Chennai | Chihuahua | Chongqing | Copenhagen | Darwin | Dhaka | Dublin | Eastern Time (US & Canada) | Edinburgh | Ekaterinburg | Europe/London | Fiji | Georgetown | Greenland | Guadalajara | Guam | Hanoi | Harare | Hawaii | Helsinki | Hobart | Hong Kong | Indiana (East) | International Date Line West | Irkutsk | Islamabad | Istanbul | Jakarta | Jerusalem | Kabul | Kamchatka | Karachi | Kathmandu | Kolkata | Krasnoyarsk | Kuala Lumpur | Kuwait | Kyiv | La Paz | Lima | Lisbon | Ljubljana | London | Madrid | Magadan | Marshall Is. | Mazatlan | Melbourne | Mexico City | Mid-Atlantic | Midway Island | Minsk | Monrovia | Monterrey | Moscow | Mountain Time (US & Canada) | Mumbai | Muscat | Nairobi | New Caledonia | New Delhi | Newfoundland | Novosibirsk | Nuku'alofa | Osaka | Pacific Time (US & Canada) | Pacific/Majuro | Pacific/Port_Moresby | Paris | Perth | Port Moresby | Prague | Pretoria | Quito | Rangoon | Riga | Riyadh | Rome | Samoa | Santiago | Sapporo | Sarajevo | Saskatchewan | Seoul | Singapore | Skopje | Sofia | Solomon Is. | Sri Jayawardenepura | St. Petersburg | Stockholm | Sydney | Taipei | Tallinn | Tashkent | Tbilisi | Tehran | Tijuana | Tokelau Is. | Tokyo | UTC | Ulaan Bataar | Urumqi | Vienna | Vilnius | Vladivostok | Volgograd | Warsaw | Wellington | West Central Africa | Yakutsk | Yerevan | Zagreb
    '''

    return r


def bat_stuff():

    #inat_application_key=os.environ['INAT_APPLICATION_KEY'],
    inat_application_key='ad221c6fce7eeb6801db886708db3c1edcda8c9474be2e090edddc673fc0591f'

    #inat_application_secret=os.environ['INAT_APPLICATION_SECRET']
    inat_application_secret='26117aad300e424e65d9513e6f6e9446c17d9b966c1d2038c6b4372258435b95'

    # inat_access_token=os.environ['INAT_ACCESS_TOKEN'],
    inat_access_token='5d625f9c0ba506110a4f18ec7bd932fccca4b7890090ebcd475a4943e461d977'

    test_url='https://requestb.in/14wwdcp1'
    #https://requestb.in/14wwdcp1?inspect

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

        observation_info = extract_info(o, bats)
        r = upload_inaturalist(observation_info,inat_access_token)

        break

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
    observation_info['date_string'] = observation_info['date'].ctime()

    print(observation_info['date'])

    # may need something like this instead of a date object to pass to inat
    '''
    January 21st, 2010
    2012-01-05
    October 30, 2008 10:31PM
    2011-12-23T11:52:06-0500
    July 9, 2012 7:52:39 AM ACST
    September 27, 2012 8:09:50 AM GMT+01:00
    '''

    # Get species information and match to config file of bats
    species_ref = observation_info['species_ref'] = observation_info['file_name'].split("_")[0]


    observation_info['species_latin'] = bats[species_ref]['latin']
    observation_info['species_en'] = bats[species_ref]['en']
    observation_info['species_inat'] = bats[species_ref]['inat_id']

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
