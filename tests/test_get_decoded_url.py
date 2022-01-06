import pytest
from http import HTTPStatus

import constant
from .conftest import mock_short_url

url = '/api/shortener/' + mock_short_url


@pytest.mark.first
def test_get_invalid_short_URL(client):
    r = client.get(url)
    assert r.content_type == constant.APPLICATION_JSON  # header check
    assert r.status_code == HTTPStatus.NOT_FOUND  # status check


@pytest.mark.second_to_last
def test_get_valid_short_URL(client):
    r = client.get(url)
    assert r.content_type == constant.APPLICATION_JSON  # header check
    assert r.status_code == HTTPStatus.OK  # status check
