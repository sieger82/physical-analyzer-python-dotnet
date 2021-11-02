from physical import *

import simplejson
import time

myMarktplaatsConversations = []							# empty result array
mySourceValue = 'Marktplaats berichten'					# source app indicator

def parse_mp_json(data):
	if data.has_key('_embedded'):							# do some checks, and then just get the fields
		if data['_embedded'].has_key('mc:conversations'):	# you need and put them in you Content Model
			for _conv in data['_embedded']['mc:conversations']:
				myConv = GenericModel ()
				myConv.Field1.Value = str(_conv['itemId'])
				myConv.Field2.Value = _conv['title'].strip()
				myConv.Field3.Value = str(_conv['sellerId'])
				myConv.Field4.Value = str(_conv['otherParticipant']['id'])
				myConv.Field5.Value = _conv['otherParticipant']['name']
				myConv.Field6.Value = str(_conv['_embedded']['mc:latest-message']['senderId'])
				myConv.Field7.Value = _conv['_embedded']['mc:latest-message']['text']
				myConv.TimeStamp1.Value = TimeStamp.FromUnixTime(time.mktime(time.strptime(_conv['_embedded']['mc:latest-message']['receivedDate'], "%Y-%m-%dT%H:%M:%S")))
				myConv.Field1.Source = f.Data
				myConv.Source.Value = mySourceValue
				myMarktplaatsConversations.append(myConv)

for fs in ds.FileSystems:
	for f in fs.Search(".*"):										# search any file (use a smarter regex in your script!)
		if f != None and f.Data != None:							# check if it's not an empty file
			data = None
			try:
				data = simplejson.loads(f.read(), encoding='utf-8')	# try to parse as JSON
			except:
				pass 												# if not valid json, do nothing
			if data != None:
				if isinstance(data, list):							# if type = list -> multiple json objects in one file
					for i in data:
						parse_mp_json(i)							# parse each json object indiviually for content
				else:
					parse_mp_json(data)								# otherwise, just parse the json object

ds.Models.AddRange(myMarktplaatsConversations)				# add the results to the DataStore
				









