import amino
import os
import json
import threading
import heroku3
def restart():
    key='e36bb985-e2f1-43fd-b85e-e4569be5d05b'
    app_name="accgen123"
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
client=amino.Client("17A7F633BD2668F5C58AC8FF2E0DDB52FE738274220CF20A44FBD5C421B24F47D483B642ED67AE381E")
client.login("e8bf0gjt9@xojxe.com","tempmail")
bb=client.get_from_code("http://aminoapps.com/p/x8nptuj")
chatId=bb.objectId
print(chatId)
cid=bb.path[1:bb.path.index("/")]
client.join_community(cid)
sub=amino.SubClient(comId=cid,profile=client.profile)
sub.join_chat(chatId)
def find():
  while True:
    p=sub.get_chat_messages(chatId=chatId,size=1).content
    for j in p:
      g=j
    length=str(len(g))
    if "6"==length:
      break
  return g
password=input("password for all: ")
de=client.devicee()
client=amino.Client(de)
for _ in range(3):
  dev=client.device_id
  email=client.gen_email()
  client.request_verify_code(email = email)
  link=client.get_message(email)
  sub.send_message(chatId,link)
  code=find()
  client.register(email = email,password = password,nickname = "uyyyutytt", verificationCode = code,deviceId=dev)
  try:
    d={}
    with open ("newmail.txt","a") as f:
      d["email"]=str(email)
      d["password"]=str(password)
      d["device"]=str(dev)
      t=json.dumps(d)
      f.write(t+',')
      print("Saved in File newmail.txt")
      f.close()
  except:
    pass
restart()
