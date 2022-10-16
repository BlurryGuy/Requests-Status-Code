import requests

response = requests.get("https://google.com")

if response.status_code == 200:
   print("The request passed successfully")
else:
     print("The request didnt go thru.")
     
input()
