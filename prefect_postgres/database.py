"""Module for querying against Postgres database."""

from functools import partial
from typing import Any, Dict, List, Optional, Tuple, Union

from anyio import to_thread
from prefect import task

from prefect_postgres.credentials import PostgresCredentials


@task
async def postgres_query(
    query: str,
    postgres_credentials: PostgresCredentials,
    params: Union[Tuple[Any], Dict[str, Any]] = None,
    database: Optional[str] = None,
) -> List[Tuple[Any]]:
    """
    Executes a query against a Postgres database.

    Args:
        query: The query to execute against the database.
        params: The params to replace the placeholders in the query.
        postgres_credentials: The credentials to use to authenticate.
        database: The name of the database to use; overrides
            the credentials definition if provided.

    Returns:
        The output of `response.fetchall()`.

    Examples:
        Query Postgres table with the ID value parameterized.
        ```python
        from prefect import flow
        from prefect_postgres import PostgresCredentials
        from prefect_postgres.database import postgres_query


        @flow
        def postgres_query_flow():
            postgres_credentials = PostgresCredentials(
                user="user",
                password="password",
                database="postgres",
            )
            result = postgres_query(
                "SELECT * FROM table WHERE id=%{id_param}s LIMIT 8;",
                postgres_credentials,
                params={"id_param": 1}
            )
            return result

        postgres_query_flow()
        ```
    """
    connection = postgres_credentials.get_connection(database=database)
    try:
        with connection, connection.cursor() as cursor:
            partial_execute = partial(cursor.execute, query, params)
            await to_thread.run_sync(partial_execute)
            partial_fetchall = partial(cursor.fetchall)
            result = await to_thread.run_sync(partial_fetchall)
    finally:
        # Unlike file objects or other resources, exiting the
        # connection’s with block doesn’t close the connection,
        # https://www.psycopg.org/docs/usage.html#with-statement
        # cursor does indeed get closed though
        connection.close()

    return result
