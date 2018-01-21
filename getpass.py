# Scrapes the username and password for VPNbook from it's website and saves it into password.txt
# Uses BeautifulSoup to Parse the html webpage

import urllib.request
from bs4 import BeautifulSoup

weblink = "https://www.vpnbook.com/freevpn" # From where the username and password is taken

wbpage = urllib.request.urlopen(weblink)
websoup = BeautifulSoup(wbpage, "html.parser")

mainsection = websoup.find("ul", {"class" : "disc"})    # Gets the table containing the username and password

vpncontent = []
vpncontent.append(mainsection.contents[15].strong.string) # Username
vpncontent.append(mainsection.contents[17].strong.string) # Password

# Save in password.txt

targetfile = open("password.txt", "w")
targetfile.write(vpncontent[0])
targetfile.write("\n")
targetfile.write(vpncontent[1])
targetfile.close()

print("Username: %s\nPassword: %s\nWritten to password.txt" % (vpncontent[0], vpncontent[1]))
