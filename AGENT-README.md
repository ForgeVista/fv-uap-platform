# fv-uap-platform (Technical)

## Architecture overview
Dagster is the orchestration hub. dbt lives as a project mounted into the containers. Docker Compose wires Postgres, Dagster services, and dbt into a single local stack.

## Service structure
- `dagster-webserver`: Dagster UI on port 3000
- `dagster-daemon`: background executor for schedules and sensors
- `dagster-api`: gRPC API service on port 4000
- `postgres`: metadata store for Dagster and dbt
- `redis`: queue/cache layer (optional)
- `dbt-runner`: dbt execution container with project mount

## Volume mounting strategy
- `./dagster` -> `/opt/dagster/app` (Dagster code)
- `./dbt` -> `/opt/dbt` (dbt project)
- `dagster_home` volume -> `/opt/dagster/dagster_home` (Dagster state)
- `postgres_data` volume -> Postgres data directory

## How to add new pipelines
1. Add assets in `dagster/assets/`.
2. Register jobs in `dagster/jobs/` (or use asset jobs).
3. Add schedules in `dagster/schedules/` and sensors in `dagster/sensors/`.
4. Wire everything in `dagster/definitions.py`.

## Environment variables
Defined in `.env.example` and loaded by Docker Compose.
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `DBT_SCHEMA`

## Extending docker-compose.yml
- Add new services under `services:`.
- Attach them to the `orchestration` network.
- Mount code with volumes if the service needs access to project files.
- Add health checks so Dagster can depend on readiness.
