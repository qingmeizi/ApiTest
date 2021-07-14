import requests
data = {
    "username":"20200015",
    "password":"e10adc3949ba59abbe56e057f20f883e",
}
r = requests.post("http://121.41.14.39:9097/api/loginS",json=data)
print(r)
print(r.status_code)
print(r.json())
print(r.text)
print ("oee")
print("112")
