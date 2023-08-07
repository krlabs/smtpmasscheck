#!/usr/bin/env python3

import smtplib
import socket
import sys

def check_smtp_auth(smtp_server, port, login, password):
    try:
        if port == 465:
            server = smtplib.SMTP_SSL(smtp_server, port)
        else:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
        server.login(login, password)
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        return False
    except socket.gaierror:
        return "Invalid Hostname"
    except Exception as e:
        return f"Error occurred: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py path_to_auth_file")
        sys.exit(1)

    auth_file = sys.argv[1]

    try:
        with open(auth_file, 'r') as file:
            for line in file:
                login, password, smtp_server, port = line.strip().split('|')
                port = int(port)  # Convert port to integer
                result = check_smtp_auth(smtp_server, port, login, password)
                if result is True:
                    print(f"SUCCESS: {login}:{password} - SMTP Server: {smtp_server} - Port: {port}")
                elif result is False:
                    print(f"FAILED: {login}:{password} - SMTP Server: {smtp_server} - Port: {port}")
                else:
                    print(f"ERROR: {result} - SMTP Server: {smtp_server} - Port: {port}")
    except FileNotFoundError:
        print(f"File '{auth_file}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
