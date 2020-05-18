import requests
from datetime import datetime 

res = requests.get("http://localhost:8080")
print(res.content)

payload = "blahblahblabhlah" 


res = requests.post("http://localhost:8080", data=payload)
print(res.content)

res = requests.get('http://localhost:8080/query?name=hello&age=26')
print(res.content)

res = requests.get('http://localhost:8080/path/test/55')
print(res.content)

count = 0 

time_start = datetime.now() 

for i in range(0, 61):
    res = requests.get("http://localhost:8080")
    print(res.content)
    count += 1

time_end = datetime.now() - time_start
print("**************************")
print(time_end)

