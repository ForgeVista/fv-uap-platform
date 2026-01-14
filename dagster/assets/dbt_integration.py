from dagster import asset


@asset(description="Placeholder asset representing a dbt build step.")
def dbt_build_stub() -> str:
    return "dbt build would run here"
