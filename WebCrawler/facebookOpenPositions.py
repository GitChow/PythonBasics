# beautifulsoup
from bs4 import BeautifulSoup
import urllib.request

# print(soup.encode("utf-8"))

# list all facebook singapore open positions
facebookCareerSingapore = "https://m.facebook.com/careers/search/?q&location=singapore"
result = urllib.request.urlopen(facebookCareerSingapore)
resulttext = result.read()
soup = BeautifulSoup(resulttext, "html.parser")
allPositionLink = soup.find_all('a',class_="w")
for position in allPositionLink:
    if position["href"].find("careers/jobs") != -1:
        print(position.contents[0])

