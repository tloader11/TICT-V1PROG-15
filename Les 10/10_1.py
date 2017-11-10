import xmltodict
xmlfile = xmltodict.parse(open("10_1_dict.xml").read())
for product in xmlfile['artikelen']['artikel']: print(product['naam'])


