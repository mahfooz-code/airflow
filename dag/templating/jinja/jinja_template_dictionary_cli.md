# Template rendering

    airflow tasks render [dag id] [task id] [desired execution date]

## Template rendering for a dag run

    airflow tasks render 05_passing_context_variable_template get_data '2023-09-15, 03:00:00'

## Testing dag

    airflow tasks test 07_fetch_extract_aggregate_insert_query get_data
