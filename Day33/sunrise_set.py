import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -33.426666
MY_LON = 151.341660

MY_EMAIL = "smtppythontest.sample@gmail.com"
MY_PASSWORD = "qrpqrp0101"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0
}


def is_night():
    r = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    r.raise_for_status()
    data = r.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LON - 5 <= longitude <= MY_LON + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='sgh0115@gmail.com',
            msg="Subject:This is the time to look up \n\n Hey Chase, This is the time to look ISS.")
        connection.close()
