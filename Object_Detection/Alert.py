import geocoder

import datetime #for reading present date
from playsound import playsound
import time
from plyer import notification #for getting notification on your PC

import requests


# ------------Location ----------
g = geocoder.ip('me')
g = g.latlng
lat = g[0]
lon = g[1]
print(lat, " " , lon)

# --------------Send SMS -------------


# url = "https://www.fast2sms.com/dev/bulkV2"

# mob_number = "8554048883"
# querystring = {"authorization":"xOSsBMdErgo6U9eN4AY8ab25mJtFDfi3LcC1hzvwK0yHQpXTuVMO4yBlsVkNvCmX93FaZRzbPunESj5L","message":"Threat object detected!\nFollowing are aproximate location cordinates: \nLatitude = " + str(lat) + " Longitude = " + str(lon) + "\nTime: " + str(time.ctime()),"language":"english","route":"q","numbers": mob_number}
# headers = {
#     'cache-control': "no-cache"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)



# ------------------- Desktop Alert ---------------



notification.notify(
    title = "Threat Detected!",
    message = str(time.ctime()),  
    app_icon = "Paomedia-Small-N-Flat-Bell.ico",
    timeout  = 20
)

# Play Sound 
playsound('Alert.wav')


