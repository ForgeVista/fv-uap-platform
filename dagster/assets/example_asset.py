from dagster import asset


@asset(description="Example asset to validate Dagster is running.")
def example_asset() -> str:
    return "example-asset-ok"
