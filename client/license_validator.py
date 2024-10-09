import requests
import json

class LicenseValidator:
    def __init__(self, license_key):
        self.license_key = license_key
        self.server_url = 'http://localhost:5000/validate_license'

    def validate_license(self):
        payload = {'license_key': self.license_key}
        try:
            response = requests.post(self.server_url, json=payload)
            if response.status_code == 200:
                print("License is valid.")
            else:
                print("License is invalid.")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {e}")

# Example Usage:
if __name__ == "__main__":
    license_validator = LicenseValidator("SAMPLE-LICENSE-KEY")
    license_validator.validate_license()