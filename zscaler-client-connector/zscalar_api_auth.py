"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import requests, time
from connectors.core.connector import ConnectorError, get_logger

logger = get_logger('zscaler-client-connector')


class ZscalerAuth:

    def __init__(self, config):
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.verify_ssl = config.get('verify_ssl')
        self.host = config.get("server_url").strip('/')

        if self.host.startswith("http://"):
            self.host = self.host.replace("http://", "https://")
        elif not self.host.startswith("https://"):
            self.host = f"https://{self.host}"

        self.token = None
        self.token_acquired_time = None
        self.token_expiry_seconds = 3600  # 1 hour

    def get_auth_token(self):
        endpoint = f"{self.host}/papi/auth/v1/login"
        data = {
            "apiKey": self.client_id,
            "secretKey": self.client_secret
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url=endpoint, headers=headers, json=data, verify=self.verify_ssl)

        if response.status_code == 200:
            result = response.json()
            self.token = result.get("jwtToken")
            self.token_acquired_time = time.time()
            return self.token
        else:
            logger.error(f"Failed to get auth token: {response.status_code} {response.text}")
            raise ConnectorError(f"Failed to acquire token: {response.text}")

    def is_token_expired(self):
        if not self.token or not self.token_acquired_time:
            return True
        return (time.time() - self.token_acquired_time) >= self.token_expiry_seconds

    def ensure_token(self):
        if self.is_token_expired():
            return self.get_auth_token()
        return self.token
