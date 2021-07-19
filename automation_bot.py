from skpy import Skype,SkypeChats
import subprocess

def connect_skype(user, pwd, token):
    s = Skype(connect=False)
    s.conn.setTokenFile(token)
    try:
            s.conn.readToken()
    except SkypeAuthException:
            s.conn.setUserPwd(user, pwd)
            s.conn.getSkypeToken()
            s.conn.writeToken()
    finally:
            sk = Skype(user, pwd, tokenFile=token)
            return sk
sk = connect_skype('*****', '*****',".token") # connect to Skype - Enter skype user and pass insted of ****
skc = SkypeChats(sk)
group_id=skc.recent()
#print(group_id)
sk.user # you
sk.contacts # your contacts
sk.chats # your conversations
#ch = sk.contacts["19:62300e7a67b24b789cb6955bdc3ca349@thread.skype"].chat # 1-to-1 conversation
value=subprocess.check_output("cat file",shell=True)
ch=sk.chats.chat('19:62300e7a67b24b789cb6955bdc3ca349@thread.skype')
print(sk)
print(value)
ch.sendMsg("Hello from @automation bot!")
ch.sendMsg(value) # plain-text message
