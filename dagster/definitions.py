from dagster import Definitions, load_assets_from_modules

from assets import dbt_integration, example_asset
from jobs.example_job import example_job
from resources.postgres_resource import postgres_resource
from schedules.example_schedule import example_schedule
from sensors.example_sensor import example_sensor

asset_modules = [example_asset, dbt_integration]
all_assets = load_assets_from_modules(asset_modules)


defs = Definitions(
    assets=all_assets,
    jobs=[example_job],
    schedules=[example_schedule],
    sensors=[example_sensor],
    resources={"postgres": postgres_resource},
)
