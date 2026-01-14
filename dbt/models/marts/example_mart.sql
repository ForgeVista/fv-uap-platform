select
  example_id,
  created_at
from {{ ref('example_stg') }}
