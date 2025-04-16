from pyngrok import ngrok
import time

# Set the authentication token
ngrok.set_auth_token("1b2lUYKoaqg4mlHI5xrBxiBsLJi_3rVfdqMPwZoqqMKR19861")  # Replace with your actual token

# Open a tunnel to the API port
public_url = ngrok.connect(5500)
print("Public URL:", public_url)
while True:
    time.sleep(10)