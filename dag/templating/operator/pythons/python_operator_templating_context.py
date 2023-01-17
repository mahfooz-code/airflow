from urllib import request

import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="python_operator_templating_context",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)



def _print_context(**context):
    start = context["data_interval_start"]
    end = context["data_interval_end"]
    print(f"Start: {start}, end: {end}")


# Prints e.g.:
# Start: 2019-07-13T14:00:00+00:00, end: 2019-07-13T15:00:00+00:00


print_context = PythonOperator(
    task_id="print_context", python_callable=_print_context, dag=dag
)