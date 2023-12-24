
-- Use the `ref` function to select from other models

--select *
--from {{ ref('my_first_dbt_model') }}
--where id = 1
{{ config(materialized='view') }}

with source_data as (

    select * from trajectories where speed>40

)

select *
from source_data
