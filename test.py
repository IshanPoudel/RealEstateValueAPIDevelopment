import requests

BASE = "http://127.0.0.1:5000/"


response = requests.put(BASE + "video/1" , {"likes" : 10 , "name" :"Ishan" ,  "views":200000} )


#when you do request.put(Base + "getvalue/" , {}") , you can pass in an additonal list
print(response.json())

# input()

#get request .
response = requests.get(BASE + "video/6" )
print(response.json())