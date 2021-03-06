# prefect-postgres

See https://github.com/PrefectHQ/prefect-sqlalchemy instead.

## Welcome!

Prefect integrations for interacting with prefect-postgres.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-postgres` with `pip`:

```bash
pip install prefect-postgres
```

### Write and run a flow

```python
from prefect import flow
from prefect_postgres.tasks import (
    goodbye_prefect_postgres,
    hello_prefect_postgres,
)


@flow
def example_flow():
    hello_prefect_postgres
    goodbye_prefect_postgres

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-postgres`, feel free to open an issue in the [prefect-postgres](https://github.com/PrefectHQ/prefect-postgres) repository.

If you have any questions or issues while using `prefect-postgres`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-postgres` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-postgres.git

cd prefect-postgres/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
