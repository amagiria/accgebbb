import os
import wget
import string
#from PIL import Image
from base64 import b64decode
#from hashlib import sha1
from os import system
from io import BytesIO
import names
from hashlib import sha1
import names
import random
import hmac
import platform,socket,re,uuid 
import base64
import hmac
import time
import json
from hashlib import sha1
import secmail
import random
import platform,socket,re,uuid
import json
#import webbrowser
import requests
from time import sleep
from bs4 import BeautifulSoup
from time import time as timestamp
from fancy_text import fancy
import os
import amino

import json

import urllib.parse
import heroku3
from os import path
from hashlib import sha1
import names
import random
from time import sleep
import hmac
import platform,socket,re,uuid 
client=amino.Client()
client.login("2ek9q37vn5v@1secmail.net","31 SxVBWnHu e3f4e1a8-e884-4782-b16e-539fd5c5f22d 35.192.215.234 a8d0ac7f9c85e442d092c0b94d28c41396603d6b 1 1637792655 RcJDXUltE26VIRAFxMjmxFX4498")
bb=client.get_from_code("http://aminoapps.com/p/x8nptuj")
chatId=bb.objectId
print(chatId)
cid=bb.path[1:bb.path.index("/")]
client.join_community(cid)
sub=amino.SubClient(comId=cid,profile=client.profile)
sub.join_chat(chatId)
def restart():
    key='e36bb985-e2f1-43fd-b85e-e4569be5d05b'
    app_name="accgen123"
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()

def sig(data):
        #at=json.dumps(data)
        key='fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("32") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")




def device():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    mac = hmac.new(bytes.fromhex('76b4a156aaccade137b8b1e77b435a81971fbd3e'), b"\x32" + identifier, sha1)
    return (f"32{identifier.hex()}{mac.hexdigest()}").upper()

 
def gen_email():
    mail = secmail.SecMail()
    email = mail.generate_email()
    return email
    
def upload(url):
    link = requests.get(url)
    result = BytesIO(link.content)
    return result
 
def get_message(email):
                try:
                    sleep(4)
                    f=email
                    mail = secmail.SecMail()
                    inbox = mail.get_messages(f)
                    print('done')
                    for Id in inbox.id:
                        msg = mail.read_message(email=f, id=Id).htmlBody
                        bs = BeautifulSoup(msg, 'html.parser')
                        images = bs.find_all('a')[0]
                        url = (images['href']+'\n')
                        if url is not None:
                         print('Vrification Url\n')
                         print(url)
                         return url
                         #wget.download(url=url,out="code.png")
                except:
                    pass
def hwid():
    return names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor()

  
            
def register(nickname: str, email: str, password: str,deviceId: str,verificationCode: str):
        data = {
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "validationContext": {
                "data": {
                    "code": verificationCode
                },
                "type": 1,
                "identity": email
            },
            "type": 1,
            "identity": email,
            "timestamp": int(timestamp() * 1000)
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)', 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    }
        data=json.dumps(data)
        heads["NDC-MSG-SIG"]=sig(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/register", data=data, headers=heads)
        if response.json()['api:message'] == "OK":
            secret=response.json()['secret']
            d={}
            #with open ("new.txt","a") as f:
            d["email"]=str(email)
            d["password"]=str(password)
            d["device"]=str(deviceid)
            d['secret']=str(secret)
            print(d)
        
        #print(response.text)
def request_verify_code(email: str,deviceId: str):
        data = {
            "identity": email,
            "type": 1,
            "deviceID": deviceId
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)', 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
        }
        data = json.dumps(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        heads["NDC-MSG-SIG"]=sig(data)
        
        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/request-security-validation", data=data, headers=heads)
        print(response.text)
        #if response.json()['api:message'] != "OK":
 
def find():
  while True:
    p=sub.get_chat_messages(chatId=chatId,size=1).content
    for j in p:
      g=j
    length=str(len(g))
    if "6"==length:
      break
  return g


def verify(values):
        imgs=get_message(values)
        #post_something(imgs)
        sub.send_message(chatId,imgs)
        code=find()
        #print(imgs)
        verifycode=code
        #print(code)
        return verifycode
 
 
 
        
        
 

 
def fancy_name():
    nm=''
    for i in names.get_first_name():
        n=random.randint(1, 5)
        if n==1:
            nm+=fancy.bold(i)
        if n==2:
            nm+=fancy.light(i)
        if n==3:
            nm+=fancy.box(i)
        if n==4:
            nm+=fancy.sorcerer(i)
        if n==5:
            nm+=i
    return nm
    
#no=int(input("how many accounts to create:  "))
password='tempmail'
 
for _ in range(5):
    deviceid=device()
    #print(deviceid)
    #saveemail="echo "+deviceid+">>devused.txt"
    
    print('------------------------------')
    values=gen_email()
    email=values
    print(email)
    #print(pas)
    nick=names.get_first_name()
    req=request_verify_code(email=email, deviceId=deviceid)
    #sleep(20)
    vcode=verify(values)
    print(vcode)
    register(nickname=nick, email=email, password=password,deviceId=deviceid,verificationCode=vcode)
