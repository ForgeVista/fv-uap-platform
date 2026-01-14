import os

from dagster import resource


@resource(description="Postgres connection settings sourced from environment variables.")
def postgres_resource():
    return {
        "host": os.getenv("POSTGRES_HOST", "postgres"),
        "port": int(os.getenv("POSTGRES_PORT", "5432")),
        "db": os.getenv("POSTGRES_DB", "dagster"),
        "user": os.getenv("POSTGRES_USER", "dagster"),
        "password": os.getenv("POSTGRES_PASSWORD", "dagster"),
    }
