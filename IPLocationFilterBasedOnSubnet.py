# to filter csv based on IP

from netaddr import IPNetwork, IPAddress
from array import array

# e.g, these are subnets for one locatoion
LocationAIPRange = ["11.111.1.1/18",
    "22.2.0.0/16"]

originFilePath = "C:\\Users\xxx\\Desktop\\inputIncludesIPInfo.csv"

def belongToLocationA(inputIP):
    for ipRange in LocationAIPRange:
        if IPAddress(inputIP) in IPNetwork(ipRange):
            return True
    return False

i=0
bufsize = 655360
resultStr = ""
# this is a faster way of processing text in python
with open(originFilePath) as infile:
    while True:
        lines = infile.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            i+=1
            print(i)
            if(belongToLocationA(line.split(',')[9])):  #e.g. here column 9 contains the IP info
                resultStr += line

# write to file finally
target = open("allLocationAResult.csv", 'w')
target.write(resultStr)
