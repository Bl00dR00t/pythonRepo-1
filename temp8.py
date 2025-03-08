import requests

baseUrl = "https://api.batmanapi.com/v1"

def aFunctionThatFetchesAfuckingApi(MakeAfuckingChoice):
    apifetch = f"{baseUrl}/{MakeAfuckingChoice}"
    requestNow = requests.get(apifetch)
    
    if requestNow.status_code == 200: 
        makereq = requestNow.json()
        return makereq
    else:
        print("error")

charChoice = 'characters'
variableThatreturnsFun = aFunctionThatFetchesAfuckingApi(charChoice)

print(variableThatreturnsFun)
