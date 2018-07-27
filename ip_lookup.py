#ip_lookup

#!/usr/bin/env python
import json, os, sys, urllib, re
IP = sys.argv[1]
IP2 = IP.split(".")
if IP in ["--self", "-s"]:
    urllib.urlretrieve("https://api.ipify.org?format=json", 'data.json')
    file = open('data.json')
    data = json.load(file)
    IP = data["ip"]
else:
    IP2A = IP2[0] + "." + IP2[1]
    IP2B = IP2[0] + "." + IP2[1] + "." + IP2[2]
    regexpattern = re.compile("[:alpha:]")
    if regexpattern.match(IP):
        print "ERROR: Invalid IP address."
    elif IP2[0] == "0": print "ERROR: 0.x.x.x is reserved for software."; exit(1)
    elif IP2[0] == "10": print "ERROR: 10.x.x.x is reserved for the private network."; exit(1)
    elif IP2[0] == "100" and int(IP2[1]) in xrange(64, 127): print "ERROR: 100.64.x.x-100.127.x.x is reserved for the private network."; exit(1)
    elif IP2[0] == "127": print "ERROR: 127.x.x.x is reserved for the host."; exit(1)
    elif IP2A == "169.254": print "ERROR: 169.254.x.x is reserved for the subnet."; exit(1)
    elif IP2[0] == "172" and int(IP2[1]) in xrange(16, 31): print "ERROR: 172.16.x.x-172.31.x.x is reserved for the private network"; exit(1)
    elif IP2B == "192.0.0": "ERROR: 192.0.0.x is reserved for the private network."; exit(1)
    elif IP2B == "192.0.2": "ERROR: 192.0.2.x is reserved for documentation."; exit(1)
    elif IP2B == "192.88.99": "ERROR: 192.88.99.x is reserved for 6to4."; exit(1)
    elif IP2A == "192.168": "ERROR: 192.168.x.x is reserved for the private network."; exit(1)
    elif IP2A == "198.18" or IP2A == "198.19": print "ERROR: 198.18.x.x and 198.19.x.x are reserved for the private network."; exit(1)
    elif IP2B == "198.51.100": print "ERROR: 198.51.100.x is reserved for documentation."; exit(1)
    elif IP2B == "203.0.113": print "ERROR: 203.0.113.x is reserved for documentation."; exit(1)
    elif int(IP2[0]) in xrange(224, 239): print "ERROR: 224.x.x.x-239.x.x.x is reserved for multicast."
    elif int(IP2[0]) in xrange(240, 255): print "ERROR: 240.x.x.x-255.x.x.x is reserved."
print "Getting data for %s..." %IP,
urllib.urlretrieve("http://ip-api.com/json/%s" %IP, 'data.json')
file = open('data.json')
data = json.load(file)
if data["status"] != "success": 
    print "\nUh oh - the API encountered an error trying to get the data for %s - stopping." %IP
    exit(1)
else: print "OK."
for k in data:
    if data[k] == "": data[k] = "Unknown"
print "####### QUERY %s #######" %data["query"]
print "ISP                            %s    " %data["isp"]
print "CITY                           %s    " %data["city"]
print "REGION                         %s    " %data["regionName"]
print "COUNTRY                        %s    " %data["country"]
print "APPROX. LAT/LON                %s, %s" %(data["lat"], data["lon"])
os.system('/bin/rm *.json')