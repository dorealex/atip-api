
import requests
import json
# local url
url = 'http://127.0.0.1:5000/api/' # change to your url
input_data={}
input_data['text'] = "medical marijuana" 
input_data['what'] = "dept-only" 
        
data = json.dumps(input_data)



send_request = requests.post(url,data)



print("Sending request")
print(send_request.status_code)
print("request:", input_data)
print(send_request)
print(send_request.json())
