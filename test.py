import requests

BASE = "http://127.0.0.1:5000/"

#
# data = [{"likes" : 10 , 'name' : "Ishan" , 'views':100000},
#         {"likes" : 20 , 'name' : "ABC" , 'views':300000},
#         {"likes" :30 , 'name' : "DEF" , 'views':400000},
#         {"likes" : 40 , 'name' : "GHI" , 'views':420000},
#         {"likes" : 50 , 'name' : "JKL" , 'views':200000}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/"+str(i) , data[i])
#     print (response.json())
#
#
# input()
# response = requests.get(BASE + 'video/6')
# print(response.json())
# input()

response = requests.patch(BASE + "video/2" , {})
print(response.json())
