from dagster import schedule

from jobs.example_job import example_job


@schedule(job=example_job, cron_schedule="0 * * * *")
def example_schedule(_context):
    return {}
