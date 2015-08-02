# to read text from a website 
import urllib
# to parse XML tags 
import xml.etree.ElementTree as ET 
# to send message to phone 
import smtplib
# to send at a regular interval 
import time 

"""
Reads the file from the NOAA website containing the weather for Boston. Uses ElementTree to parse certain parameters of the XML file and stores in variable master. 
"""

# read file 
link = "http://w1.weather.gov/xml/current_obs/KBOS.xml" #this one is for Logan Airport. For other locations try: http://w1.weather.gov/xml/current_obs/
f = urllib.urlopen(link)
myfile = f.read()
print myfile 

# parse as XML 
tree = ET.fromstring(myfile)
weather = tree.find('weather').text
temp_f = tree.find('temp_f').text
temp_c = tree.find('temp_c').text
relative_humidity = tree.find('relative_humidity').text
wind_string = tree.find('wind_string').text
wind_mph = tree.find('wind_mph').text
visibility_mi = tree.find('visibility_mi').text

# consolidates 'the weather' into 1 string 
master = str("James! It is %r. Visibility %r miles. Temp %r f. Humidity %r percent." % (weather, visibility_mi, temp_f, relative_humidity))
print master # for good measure 

# sends message to phone via SMS
def send_to_phone():
	me = '9083582178@vtext.com'
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login('iamtheweatherman2', "asdfjkl;asd")
	server.sendmail( 'Me', me, master)
	print "Message sent." #for good measure 

def main(): 
	while True:
		send_to_phone()
		time.sleep(86399) # sends everyday (60 s / 1 min * 60 min / hr * 24h / 1 day - 1s)

# to run only when it is the main program 
if __name__ == '__main__': 
	main()
