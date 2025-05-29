import requests

MY_LAT = 18.520430
MY_LONG = 73.856743

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,  # Corrected parameter key for longitude
    "formatted": 0   # Optional: Use unformatted UTC time
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

