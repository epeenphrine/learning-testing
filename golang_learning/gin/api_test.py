import requests
from datetime import datetime 
import json
#res = requests.get("http://localhost:8080")
#print(res.content)

payload = "TDA" 

res = requests.post("http://localhost:2000", data=payload)
##json_data = json.loads(res.content)

##print(json_data)

#res = requests.get('http://localhost:8080/query?name=hello&age=26')
#print(res.content)

#res = requests.get('http://localhost:8080/path/test/55')
#print(res.content)

count = 0 

time_start = datetime.now() 

for i in range(0, 70):
    res = requests.post("http://localhost:2000",data=payload)
    print(res.content)
    count += 1
    print(count)

count = 0 

for i in range(0,70):
    res = requests.get("http://localhost:2000")
    print(res.content)
    count += 1
    print(count)

time_end = datetime.now() - time_start
print("**************************")
print(time_end)
print(f"requests made : {count}")
