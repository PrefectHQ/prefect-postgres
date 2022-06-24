from . import _version
from prefect_postgres.credentials import PostgresCredentials  # noqa

__version__ = _version.get_versions()["version"]
