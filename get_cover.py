#import json
#import requests
#import os, sys
#import urllib
#from PIL import Image
#access_token="CAACEdEose0cBAPqZBJhlt0IW19ZCMaat4ZAlVV8lJa8PbXDmuYZCMWrTUcDhaNK69jcRAU4cqj0L6Wh7DhKZCARqgxHRx1WdPzq4Fq2x3HuK0bXymCJOEQoal0MRK2SuZAEv0Bz2OM7u8NqcKc0kjWwhIioeaxOzl3sNrrY9e5T6r00AKGDbFmqHZBm7qNC89DEf2me7tvf5SBZASw4XIgUO"
#fileR=open("event-id","r")
#fileW=open("json", "w")
#def get_cover():
#	count = 0
#	for line in fileR:
#		url = "https://graph.facebook.com/v2.5/"+line+"?fields=cover&access_token="+access_token
#		r = requests.get(url)
#		if r.status_code == 200:
#			dic=r.json()
#			if dic.has_key('cover'):
#				dic2=dic['cover']
#			if dic2.has_key('source'):
#				download_cover(dic2['source'], str(count)+".jpg")
#				count = count + 1
#				url2 = "https://graph.facebook.com/v2.5/"+line+"?&access_token="+access_token
#				r2=requests.get(url2)
#				if r2.status_code == 200:
#						json.dump(r2.json(), fileW);
#
#def download_cover(url,name):
#	image=urllib.URLopener()
#	image.retrieve(url,"cover/"+name)
#	im = Image.open("cover/"+name)
#	im_resize = im.resize((650, 350), Image.ANTIALIAS)
#	im_resize.save("cover/"+name)
#get_cover()
#fileR.close()
#fileW.close()

import json
import requests
import os, sys
import urllib
from PIL import Image
access_token="CAACEdEose0cBAB1etwhIVYGWdU8acW7oysXfA273b2hKpvZCnttDklhFy30kZBxSchF1HiAXmunj1SLmMqKY0QE8THLCDcBi3vaEIuJDOi21xjWZBPRHbSQlcjxTS0Vut560kSudY6TMZA3jXIQct1q6WZCbNqI8qBgvwxTSTZB8ZBdbxLiB6FObO8joJ0ZCiiyZC5YeoOHkSv5VNMKw12Rfg"
fileR=open("event-id","r")
fileW=open("json", "w")
def get_cover():
    # param={
    #     "name": "",
    #     "id":"",
    #     "description":"",
    #     "start_time":"",
    #     "end_time":"",
    #     "longtitude":0,
    #     "latitude":0,
    #     "city":"",
    #     }
    # }
    fileW.write("{\"data\": [")
    count = 0
    for line in fileR:
        if count > 6:
            break;
        url = "https://graph.facebook.com/v2.5/"+line+"?fields=cover&access_token="+access_token#has cover
        r = requests.get(url)
        if r.status_code == 200:
            dic=r.json()
            if dic.has_key('cover'):
                dic2=dic['cover']
                if dic2.has_key('source'):
                    url2 = "https://graph.facebook.com/v2.5/"+line+"?&access_token="+access_token
                    r2=requests.get(url2)
                    if r2.status_code == 200:
                        eventjson=r2.json();
                        if eventjson.has_key('place')==False or eventjson.has_key('description')==False or eventjson.has_key('name')==False or eventjson.has_key('start_time')==False or eventjson.has_key('end_time')==False :
                            continue
                        placejson=eventjson['place']
                        if(placejson.has_key('location') and placejson['location'].has_key('longitude') and placejson['location'].has_key('latitude') and placejson['location'].has_key('city')):
                            download_cover(dic2['source'], str(count)+".jpg")
                            count = count + 1
                            param={}
                            param['name']=eventjson['name']
                            param['id']=str(count)
                            param['description']=eventjson['description']
                            param['start_time']=eventjson['start_time']
                            param['end_time']=eventjson['end_time']
                            param['longitude']=placejson['location']['longitude']
                            param['latitude']=placejson['location']['latitude']
                            param['city']=placejson['location']['city']
                            param['url']="https://www.facebook.com/events/"+line[:len(line)-1];
                            # print param
                            if(count>1):
                                fileW.write(',')
                            json.dump(param, fileW,sort_keys=True);
                            
    fileW.write("]}")
                            
def download_cover(url,name):
	image=urllib.URLopener()
	image.retrieve(url,"cover/"+name)
	im = Image.open("cover/"+name)
	im_resize = im.resize((650, 350), Image.ANTIALIAS)
	im_resize.save("cover/"+name)
get_cover()
fileR.close()
fileW.close()
# with open('json') as data_file:
#     data = json.load(data_file)
#
# print(data)
