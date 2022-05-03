"""Credentials class to authenticate Postgres."""

from dataclasses import dataclass
from typing import Optional

import psycopg2


@dataclass
class PostgresCredentials:
    """
    Dataclass used to manage authentication with Postgres.

    Args:
        user: The user name used to authenticate.
        password: The password used to authenticate.
        database: The name of the Postgres database.
        host: The host address of the database.
        port: The port to connect to the database.
    """  # noqa

    user: str
    password: str
    database: Optional[str] = None
    host: Optional[str] = "localhost"
    port: Optional[int] = 5432

    def get_connection(
        self, database: Optional[str] = None
    ) -> psycopg2.extensions.connection:
        """
        Returns an authenticated connection that can be
        used to query from Postgres databases.

        Args:
            database: The name of the database to use; overrides
                the class definition if provided.

        Returns:
            The authenticated Postgres connection.

        Examples:
            ```python
            from prefect import flow
            from prefect_postgres import PostgresCredentials

            @flow
            def postgres_credentials_flow():
                postgres_credentials = PostgresCredentials(
                    user="user",
                    password="password",
                    database="postgres",
                    host="127.0.0.1"
                )
                return postgres_credentials

            postgres_credentials_flow()
            ```
        """
        database = self.database or database
        if database is None:
            raise ValueError(
                "The database must be set in either " "PostgresCredentials or the task"
            )

        return psycopg2.connect(
            database=database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
