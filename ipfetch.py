import requests, sys, json
ip = sys.argv[1]

# Fetch data
r = requests.get(f"http://ip-api.com/json/{ip}?fields=18039807")
data = r.json()

# Handle errors
if data.get("status") == "fail":
    print("An error occurred.")
    exit(1)

# Output
del data["status"]
for key, value in data.items():
    print(f"{key}: {value}")