from http import HTTPStatus

from tests.constants import HEALTH_PATH


class TestHealthCheck:
    def test_system_health(self, client):
        response = client.get(HEALTH_PATH)
        assert response.status_code == HTTPStatus.OK

    def test_response_in_json_format(self, client):
        response = client.get(HEALTH_PATH)
        assert response.headers["Content-type"] == "application/json"

    def test_response_content(self, client):
        response = client.get(HEALTH_PATH)
        assert response.json() == {"status": "ok"}
