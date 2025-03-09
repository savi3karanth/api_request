import requests

correct_url = "http://api.open-notify.org/iss-now.json"
wrong_url = "http://api.open-notify.org/is-now.json"
#response = requests.get(url=correct_url)   # if given this we get 202 success
response = requests.get(url=wrong_url)      #if we miss a single letter in url we get an error
print(response)
print(response.status_code)

response.raise_for_status()

# if response.status_code != 200:
#     print("Error")
#     raise Exception("Bad response from ISS API")

# if response.status_code == 404:
#     raise Exception("That resource does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data")