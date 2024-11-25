# Blind SQL Injector

A Python tool designed to automate Blind SQL Injection attacks on MySQL databases. This tool performs time-based Blind SQL injection to exfiltrate data from vulnerable web applications, helping penetration testers efficiently identify and exploit Blind SQL Injection vulnerabilities.

## Features:
- **Time-Based SQL Injection**: Uses delays in the server's response time to exfiltrate data.
- **Automated Data Exfiltration**: Guesses data character by character and appends it to the injection payload.
- **Customizable Configuration**: Easily modify the target URL, parameters, and charset for different web applications.

## Requirements:
- Python 3.x
- `requests` library

To install the required libraries, run:
```bash
pip install requests
```

## Setup:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/blind-sql-injector.git
    ```

2. **Navigate to the repository**:
    ```bash
    cd blind-sql-injector
    ```

3. **Modify the necessary variables in the script**:
   - `url`: Set the target URL of the vulnerable application.
   - `data_key`: Specify the parameter to test (e.g., "username").
   - `charset`: Define the character set used for the attack (e.g., letters, digits).

    Example modification in the script:
    ```python
    url = "http://example.com/vulnerable-endpoint.php"
    success_indicator = "Welcome"
    data_key = "username"
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    ```

4. **Run the script**:
    ```bash
    python3 blind_sql_injector.py
    ```

## Example Output:
The tool will begin exfiltrating data one character at a time. You’ll see something like the following:

```
[!] Starting Blind SQL Injection...
Guessed so far: a
Guessed so far: ab
Guessed so far: abc
Guessed so far: abcd
...
```

## How It Works:
1. **Oracle Function**: The script sends a request to the target URL with the current injection payload. If the `success_indicator` string is found in the response, it means the guess was correct.
   
2. **Time-Based Blind Injection**: The tool uses SQL's `SLEEP()` function to delay the response from the server if the injected condition is true. By measuring the delay in response time, it determines if the current character is part of the correct data.

3. **Character-by-Character Guessing**: The tool tests characters from the defined `charset` and builds the injected data step by step.

## Usage Tips:
- **Charset**: Make sure to customize the `charset` to include all possible characters you need (e.g., letters, numbers, special characters).
- **Success Indicator**: Modify the `success_indicator` to match text that appears only when the query executes successfully (e.g., a successful login message).
- **Slow Responses**: If the application responds too quickly, adjust the sleep time threshold in the script to ensure accurate timing.

## Disclaimer:
This tool is intended for **educational purposes only**. It should **only** be used in penetration tests where you have explicit permission to test the target application. Unauthorized use of this tool is illegal and unethical.
