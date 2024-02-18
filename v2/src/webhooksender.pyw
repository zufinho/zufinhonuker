import sys
import requests

if len(sys.argv) !=4:
    print("Usage: <webhook_url> <message> <many_times>")
    sys.exit(1)
webhook_url,message,many_times=sys.argv[1],sys.argv[2],int(sys.argv[3])
count=0
while not count==many_times:
    send=requests.post(webhook_url,json={"content": message})
    count +=1
    with open("result.log","a") as log:
        log.write(str(send.status_code))
        log.write("\n")