import requests

MY_LAT =18.520430
MY_LONG = 73.856743

parameters = {
    "lat": MY_LAT,
    "long":MY_LONG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)





