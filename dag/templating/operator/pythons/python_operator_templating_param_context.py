from urllib import request

import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="python_operator_templating_param",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@hourly",
)


def _get_data(data_interval_start):
    print(data_interval_start)
    year, month, day, hour, *_ = data_interval_start.timetuple()
    url = (
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month:0>2}/pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    output_path = "/opt/airflow/data/wikipageviews.gz"
    request.urlretrieve(url, output_path)


get_data = PythonOperator(task_id="get_data", python_callable=_get_data, dag=dag)