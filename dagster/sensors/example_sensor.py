from dagster import SkipReason, sensor

from jobs.example_job import example_job


@sensor(job=example_job)
def example_sensor(_context):
    return SkipReason("No external trigger configured.")
