# To read text from a website 
import urllib
# To parse XML tags 
import xml.etree.ElementTree as ET 
# To send message to phone 
import smtplib
# To send at a regular interval 
import time 

"""
For other locations try: 
	http://w1.weather.gov/xml/current_obs/
"""

# Read file 
link = "http://w1.weather.gov/xml/current_obs/KBOS.xml" 
f = urllib.urlopen(link)
myfile = f.read()

# Parse as XML 
tree = ET.fromstring(myfile)
weather = tree.find('weather').text
temp_f = tree.find('temp_f').text
temp_c = tree.find('temp_c').text
relative_humidity = tree.find('relative_humidity').text
wind_string = tree.find('wind_string').text
wind_mph = tree.find('wind_mph').text
visibility_mi = tree.find('visibility_mi').text

# Combine into 1 string 
master = str("James! It is %r. Visibility %r miles. \
	Temp %r f. Humidity %r percent." % (weather, \
	visibility_mi, temp_f, relative_humidity))

# Send to phone
def send_to_phone():
	me = '9083582178@vtext.com'
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login('iamtheweatherman2', "asdfjkl;asd")
	server.sendmail( 'Me', me, master)
	print "Message sent" 

def main(): 
	while True:
		send_to_phone()
		time.sleep(86399) 

if __name__ == '__main__': 
	main()
