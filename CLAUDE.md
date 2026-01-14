# AI Agent Context

This repository is a public template for Docker-first Dagster + dbt orchestration projects.

## Guardrails
- Keep everything generic and template-friendly.
- Do not add secrets or environment-specific values.
- Favor clear scaffolding over production-ready complexity.

## Working conventions
- Docker Compose is the source of truth for local orchestration.
- Dagster code lives in `dagster/` and is mounted into containers.
- dbt project lives in `dbt/` and is mounted into containers.
- Environment configuration comes from `.env.example`.

## Typical changes
- Add assets, jobs, schedules, or sensors in the Dagster scaffold.
- Expand dbt models, tests, macros, and seeds as projects mature.
- Update documentation when the stack or workflow changes.
