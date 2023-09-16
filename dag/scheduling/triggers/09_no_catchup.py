import datetime as dt
from pathlib import Path

import pandas as pd

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="09_no_catchup",
    schedule_interval="@daily",
    start_date=dt.datetime(year=2023, month=9, day=13),
    end_date=dt.datetime(year=2023, month=9, day=16),
    catchup=False,
)

fetch_events = BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /home/airflow/data/events /home/airflow/data/stats && "
        "curl -o /home/airflow/data/events/{{ds}}.json "
        "http://events_api:5000/events?"
        "start_date={{ds}}&"
        "end_date={{next_ds}}"
    ),
    dag=dag,
)


def _calculate_stats(**context):
    """Calculates event statistics."""
    input_path = context["templates_dict"]["input_path"]
    output_path = context["templates_dict"]["output_path"]
    events = pd.read_json(input_path)
    events["date"] = events["date"].astype("string")
    events["user"] = events["user"].astype("string")
    events.columns = events.columns.str.strip()
    stats = events.groupby(["date", "user"]).size().reset_index()

    Path(output_path).parent.mkdir(exist_ok=True)
    stats.to_csv(output_path, index=False)


calculate_stats = PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    templates_dict={
        "input_path": "/home/airflow/data/events/{{ds}}.json",
        "output_path": "/home/airflow/data/stats/{{ds}}.csv",
    },
    dag=dag,
)


fetch_events >> calculate_stats
