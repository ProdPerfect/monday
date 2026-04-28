import json

import urllib3

from monday.constants import DEFAULT_TIMEOUT, HTTP_MAX_SIZE, TOKEN_HEADER
from monday.exceptions import MondayQueryError


class GraphQLClient:
    def __init__(self, endpoint, timeout=DEFAULT_TIMEOUT):
        self.endpoint = endpoint
        self.timeout = timeout
        self.token = None
        self.headers = {}
        self._http = urllib3.PoolManager(maxsize=HTTP_MAX_SIZE)

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token):
        self.token = token

    def inject_headers(self, headers):
        self.headers = headers

    def _send(self, query, variables):
        headers = self.headers.copy()

        if self.token is not None:
            headers[TOKEN_HEADER] = self.token

        if variables is not None and variables.get("file") is not None:
            file_path = variables["file"]
            with open(file_path, "rb") as f:
                file_data = f.read()

            response = self._http.request(
                "POST",
                self.endpoint,
                headers=headers,
                fields={"query": query, "variables[file]": (file_path, file_data)},
                timeout=self.timeout,
            )
        else:
            headers.setdefault("Content-Type", "application/json")
            body = json.dumps({"query": query}).encode("utf-8")

            response = self._http.request(
                "POST",
                self.endpoint,
                headers=headers,
                body=body,
                timeout=self.timeout,
            )

        if response.status >= 400:
            raise urllib3.exceptions.HTTPError(
                f"HTTP {response.status}: {response.data.decode('utf-8')}"
            )

        response_data = json.loads(response.data.decode("utf-8"))
        self._throw_on_error(response_data)
        return response_data

    def _throw_on_error(self, response_data):
        if "errors" in response_data:
            raise MondayQueryError(
                response_data["errors"][0]["message"], response_data["errors"]
            )
