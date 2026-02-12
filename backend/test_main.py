from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import pytest

from main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "endpoints" in data


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@patch("main.get_datacenters")
def test_get_datacenters_success(mock_get_datacenters):
    """Test successful retrieval of datacenters."""
    # Mock data
    mock_data = [
        {"id": 1, "name": "East US", "country": "United States", "city": "Virginia"},
        {"id": 2, "name": "West Europe", "country": "Netherlands", "city": "Amsterdam"},
        {"id": 3, "name": "Southeast Asia", "country": "Singapore", "city": "Singapore"},
    ]
    mock_get_datacenters.return_value = mock_data

    response = client.get("/datacenters")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["id"] == 1
    assert data[0]["name"] == "East US"
    assert data[0]["country"] == "United States"
    assert data[0]["city"] == "Virginia"


@patch("main.get_datacenters")
def test_get_datacenters_empty(mock_get_datacenters):
    """Test retrieval when no datacenters exist."""
    mock_get_datacenters.return_value = []

    response = client.get("/datacenters")

    assert response.status_code == 200
    assert response.json() == []


@patch("main.get_datacenters")
def test_get_datacenters_database_error(mock_get_datacenters):
    """Test handling of database connection errors."""
    import psycopg2
    mock_get_datacenters.side_effect = psycopg2.OperationalError("Connection failed")

    response = client.get("/datacenters")

    assert response.status_code == 503
    assert "Database connection error" in response.json()["detail"]


@patch("main.get_datacenters")
def test_get_datacenters_server_error(mock_get_datacenters):
    """Test handling of general server errors."""
    mock_get_datacenters.side_effect = Exception("Unexpected error")

    response = client.get("/datacenters")

    assert response.status_code == 500
    assert "Internal server error" in response.json()["detail"]


def test_datacenters_response_shape():
    """Test that datacenters endpoint returns correct schema."""
    with patch("main.get_datacenters") as mock_get:
        mock_get.return_value = [
            {"id": 1, "name": "Test DC", "country": "Test Country", "city": "Test City"}
        ]

        response = client.get("/datacenters")

        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0

        # Verify schema
        datacenter = data[0]
        assert "id" in datacenter
        assert "name" in datacenter
        assert "country" in datacenter
        assert "city" in datacenter
        assert isinstance(datacenter["id"], int)
        assert isinstance(datacenter["name"], str)
        assert isinstance(datacenter["country"], str)
        assert isinstance(datacenter["city"], str)
