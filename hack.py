import requests

for i in range(99999):
    url="http://10.41.131.169:5000/clave/"+str(i)
    response=requests.get(url)
    print(url)
    if " correcta" in response.text:
        print("\t"+response.text)
        break
