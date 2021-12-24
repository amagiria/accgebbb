import amino
import os
import json
import threading
import wget
from new import emaill,passwordd,custompwd,chatlink,private,key,app_name
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
client=amino.Client("17A7F633BD2668F5C58AC8FF2E0DDB52FE738274220CF20A44FBD5C421B24F47D483B642ED67AE381E")
client.login(emaill,passwordd)
bb=client.get_from_code(chatlink)
chatId=bb.objectId
cid=bb.path[1:bb.path.index("/")]
client.join_community(cid)
sub=amino.SubClient(comId=cid,profile=client.profile)
sub.join_chat(chatId)
def find():
  while True:
    p=sub.get_chat_messages(chatId=chatId,size=1).content
    #print(p)
    for j in p:
      g=j
    #print(g)
    l=f"{g}"
    length=str(len(l))
    if "6"==length:
      break
  return g

password=custompwd
de=client.devicee()
client=amino.Client(de)
for _ in range(3):
  try: os.remove("code.png")
  except: pass
  dev=client.device_id
  email=client.gen_email()
  print(email)
  client.request_verify_code(email = email,dev=dev)
  link=client.get_message(email)
  wget.download(url=link,out="code.png")
  with open("code.png","rb") as file:
    sub.send_message(chatId=chatId,fileType="image",file=file)
  p=sub.get_chat_messages(chatId=chatId,size=1).content
  code=find()
  
  try:
    client.register(email = email,password = password,nickname =nickname, verificationCode = code,deviceId=dev)
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    #t=json.dumps(d)
    print(d)
    sub.send_message(chatId=private,message=f"{d}")
  except: pass

de=client.devicee()
client=amino.Client(de)
for _ in range(2):
  try: os.remove("code.png")
  except: pass
  dev=client.device_id
  email=client.gen_email()
  print(email)
  client.request_verify_code(email = email,dev=dev)
  link=client.get_message(email)
  wget.download(url=link,out="code.png")
  with open("code.png","rb") as file:
    sub.send_message(chatId=chatId,fileType="image",file=file)
  code=find()
  
  try:
    client.register(email = email,password = password,nickname = nickname, verificationCode = code,deviceId=dev)
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    #t=json.dumps(d)
    print(d)
    sub.send_message(chatId=private,message=f"{d}")
  except:
    pass



restart()

