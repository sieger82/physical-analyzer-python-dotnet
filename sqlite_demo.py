from physical import *

import SQLiteParser
from System.Convert import IsDBNull

results = []																									# prepare empty results array
for fs in ds.FileSystems:
	for file in fs.Search("Marktplaats.sqlite$"):
		db = SQLiteParser.Database.FromNode(file)
		if db != None:
			print("> db %s found" % file.Name)
			i = 0
			ts = SQLiteParser.TableSignature("ZRECENTSEARCH")													# create empty table signature
			SQLiteParser.Tools.AddSignatureToTable(ts, 'ZTIMESTAMP', SQLiteParser.Tools.SignatureType.Float)	# define timestamp field
			SQLiteParser.Tools.AddSignatureToTable(ts, 'ZSEARCHTERM', SQLiteParser.Tools.SignatureType.Text)	# define searchterm field
			for row in db.ReadTableRecords(ts, True):															# read table using table signature
				if not IsDBNull(row["ZSEARCHTERM"].Value):														#  the 'True' means 'use deleted'
					zk = SearchedItem()																			# create a model of type SearchedItem
					zk.Value.Value = row["ZSEARCHTERM"].Value													# add the 'searchterm value'
					zk.Value.Source = MemoryRange(row["ZSEARCHTERM"].Source)									# add source indicator
					zk.TimeStamp.Value = TimeStamp.FromUnixTime(row["ZTIMESTAMP"].Value+978307200)				# add timestamp
					zk.Deleted = row.Deleted 																	# add intact / deleted indicator
					zk.Source.Value = "script test 1"															# add source app
					results.append(zk) 																			# append to results array
					print("zoekopdracht: %s, status: %s" % (row["ZSEARCHTERM"].Value, str(row.Deleted)))
					i += 1
			print("> aantal items = %d" % i)
ds.Models.AddRange(results)																						# add all results to DataStore


