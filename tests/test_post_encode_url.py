from http import HTTPStatus
import pytest

import constant
from .conftest import mock_payload

url = '/api/shortener'


@pytest.mark.first
def test_create_new_vm(client):
    r = client.post(url, json=mock_payload)
    assert r.content_type == constant.APPLICATION_JSON  # header check
    assert r.status_code == HTTPStatus.CREATED  # status check

