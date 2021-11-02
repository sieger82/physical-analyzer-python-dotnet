from physical import *

# we need these to change the python search path so we can load custom modules
import sys
import os

# add the current dir to python search path
parent = os.path.dirname(__file__)
sys.path.append(parent)

# import protobuf decoder
import protobuf_decoder.parse as pbparser

# for SQLite databases
import SQLiteParser
from System.Convert import IsDBNull

for fs in ds.FileSystems:
	for f in fs.Search("google\-app\-measurement\.sql$"):
		db = SQLiteParser.Database.FromNode(f)
		for row in db["raw_events"]:
			print pbparser.Decode(bytes(row["data"].Value))
