import requests as rq
import json

parameters = {
   "requestHeader": {
      "requestMessageId": "6da6b8b024532a2e0eacb1af58581",
      "messageDateTime": "2019-02-35 05:25:12.327"
   },
   "requestData": {
      "pANs": [
         4072208010000000
      ],
      "group": "STANDARD"
   }
}

response = rq.get("https://sandbox.api.visa.com/cofds-web/v1/datainfo")


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())