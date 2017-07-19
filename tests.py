# Check that the number of features is correct
# This corresponds to the single ``Document``
>>> features = list(k.features())
>>> len(features)
1

# Check that we can access the features as a generator
# (The two Placemarks of the Document)
>>> features[0].features()
<generator object features at 0x2d7d870>
>>> f2 = list(features[0].features())
>>> len(f2)
2

# Check specifics of the first Placemark in the Document
>>> f2[0]
<fastkml.kml.Placemark object at 0x2d791d0>
>>> f2[0].description
>>> f2[0].name
'Document Feature 1'

# Check specifics of the second Placemark in the Document
>>> f2[1].name
'Document Feature 2'
>>> f2[1].name = "ANOTHER NAME"

# Verify that we can print back out the KML object as a string
>>> print k.to_string(prettyprint=True)
<kml:kml xmlns:ns0="http://www.opengis.net/kml/2.2">
  <kml:Document>
    <kml:name>Document.kml</kml:name>
    <kml:visibility>1</kml:visibility>
    <kml:open>1</kml:open>
    <kml:Style id="exampleStyleDocument">
      <kml:LabelStyle>
        <kml:color>ff0000cc</kml:color>
        <kml:scale>1.0</kml:scale>
      </kml:LabelStyle>
    </kml:Style>
    <kml:Placemark>
      <kml:name>Document Feature 1</kml:name>
      <kml:visibility>1</kml:visibility>
      <kml:open>0</kml:open>
      <kml:Point>
        <kml:coordinates>-122.371000,37.816000,0.000000</kml:coordinates>
      </kml:Point>
    </kml:Placemark>
    <kml:Placemark>
      <kml:name>ANOTHER NAME</kml:name>
      <kml:visibility>1</kml:visibility>
      <kml:open>0</kml:open>
      <kml:Point>
        <kml:coordinates>-122.370000,37.817000,0.000000</kml:coordinates>
      </kml:Point>
    </kml:Placemark>
  </kml:Document>
</kml:kml>
