from unittest.mock import MagicMock

import pytest

from prefect_postgres.credentials import PostgresCredentials


def test_postgres_credentials_get_connection_override(monkeypatch):
    connect_mock = MagicMock()
    monkeypatch.setattr("psycopg2.connect", connect_mock)

    PostgresCredentials("user", "password", database="database").get_connection(
        database="override_database"
    )
    connect_mock.assert_called_with(
        database="database",
        user="user",
        password="password",
        host="localhost",
        port=5432,
    )


def test_postgres_credentials_get_connection_missing_database():
    with pytest.raises(ValueError, match="The database must be set in either"):
        PostgresCredentials("user", "password").get_connection()
