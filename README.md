# ForgeVista UAP Platform (Run Tier)

## What orchestration solves
Orchestration turns manual data runs into reliable, repeatable workflows. It schedules jobs, monitors outcomes, and gives teams visibility into what is running now and what failed last night.

## When to use this tier
Use the Platform (Run) tier if your team:
- Needs scheduled, automated dbt runs
- Wants a UI to monitor pipelines
- Is ready for Docker-based workflows
- Has outgrown one-off scripts or manual dbt execution

## Prerequisites
- Docker Desktop or Docker Engine
- Docker Compose (v2+)

## Quick start
1. Review `.env.example` and update values as needed (this template loads it directly).
2. Start the stack:
   ```bash
   docker compose up --build
   ```
3. Open the Dagster UI at `http://localhost:3000`.

## What’s included
- Dagster UI (webserver) for orchestration
- Dagster daemon for background schedules and sensors
- Dagster gRPC API for agents and tooling
- Postgres for metadata and dbt state
- Redis for queues and caching (optional)
- dbt runner container with a starter project

## Troubleshooting FAQ
**Docker daemon isn’t running**
- Start Docker Desktop or run `sudo systemctl start docker` on Linux.

**Port 3000 is already in use**
- Stop the conflicting service or change the port mapping in `docker-compose.yml`.

**Dagster UI loads but jobs fail**
- Confirm Postgres is healthy and your `.env.example` values match your environment.

**dbt can’t connect**
- Ensure the `POSTGRES_*` values align with the Postgres container configuration.
