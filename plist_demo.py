from physical import *

# we need these to change the python search path so we can load custom modules
import sys
import os

# add the current dir to python search path
parent = os.path.dirname(__file__)
sys.path.append(parent)

# import bplist decoder
sys.path.append(parent+os.path.sep+"ccl-bplist")
import ccl_bplist

# use this for converting plists in NSKeyedArchiver format
ccl_bplist.set_object_converter(ccl_bplist.NSKeyedArchiver_common_objects_convertor)

for fs in ds.FileSystems:
	for f in fs.Search("com\.marktplaats\.iphone\.plist$"):
		plist = ccl_bplist.load(f)
		print plist["LastDateAppWasOpened"].strftime("%d-%m-%Y %H:%M:%S")



import StringIO
emulated_file = StringIO.StringIO(plist["com.facebook.sdk:serverConfiguration1652748041707995"])
embedded_plist = ccl_bplist.load(emulated_file)
print embedded_plist


