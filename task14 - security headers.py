# # TASK: security header checker
# # 1. Define a list of security headers checked
# # 2. Send request to the link - user's input
# # 3. Show which headers exist with [+]
# # 4. Show which headers don't exist with [-]

# # Additional functionality: Show recommended setting for missing headers
import requests

security_headers = [
    "X-Frame-Options",
    "X-XSS-Protection",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "Access-Control-Allow-Origin",
    "Cross-Origin-Opener-Policy"
]

url = input("URL: ")
response = requests.get(url)
print(type(response.headers))
for header in security_headers:
    if header in response.headers:
        print(f"{header} exists: {response.headers[header]}")
    else:
        print(f"{header}: not found")
