import xmltodict
xmlfile = xmltodict.parse(open("xml_stationslijst.xml").read())
print("Dit zijn de codes en types van de 4 stations:")
for station in xmlfile['Stations']['Station']: print(station['Code'],"-",station['Type'])
print("\nDit zijn alle stations met een of meer synoniemen:")
for station in xmlfile['Stations']['Station']:
    if station['Synoniemen'] != None and len(station['Synoniemen']['Synoniem']) > 1: print(station['Code'],"-",station['Synoniemen'])
print("\nDit is de lange naam van elk station:")
for station in xmlfile['Stations']['Station']: print(station['Code'],"-",station['Namen']['Lang'])
