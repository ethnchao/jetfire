#!/usr/bin/python
import sys
import urllib

# ------------------------------------------------------------------
# get all groups and their values
def getlist():
    try:
        result = urllib.urlopen('http://192.168.120.234:5000/api/v1.0/lists')
        print result.read()
    except Exception as e:
        raise e

# ------------------------------------------------------------------
# get host variables
def getdetails(host):
    result = urllib.urlopen('http://192.168.120.234:5000/api/v1.0/hostdetail/' + host)
    print result.read()

# ------------------------------------------------------------------
# command line options
if len(sys.argv) == 2 and (sys.argv[1] == '--list'):
    getlist()

elif len(sys.argv) == 3 and (sys.argv[1] == '--host'):
    host = sys.argv[2]
    getdetails(host)

else:
    print "usage --list or --host <hostname>"
    sys.exit(1)
