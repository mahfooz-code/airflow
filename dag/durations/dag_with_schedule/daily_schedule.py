import datetime as dt
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="daily_schedule",
    start_date=dt.datetime(2019, 1, 1),
    schedule_interval="@daily",
)

fetch_events = BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /opt/airflow/data && "
        "curl -o /opt/airflow/data/events.json "
        "https://gorest.co.in/public/v2/users"
    ),
    dag=dag,
)


def _calculate_stats(input_path, output_path):
    """Calculates event statistics."""
    print(Path(__file__).parent.resolve())
    print(Path().resolve())
    events = pd.read_json(input_path)
    stats = events.groupby(["gender", "status"]).size().reset_index()
    Path(output_path).parent.mkdir(exist_ok=True)
    stats.to_csv(output_path, index=False)


calculate_stats = PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    op_kwargs={
        "input_path": "/opt/airflow/data/events.json",
        "output_path": "/opt/airflow/data/stats.csv",
    },
    dag=dag,
)

fetch_events >> calculate_stats
