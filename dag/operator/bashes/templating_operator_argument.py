import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="listing_4_01",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@hourly",
)

get_data = BashOperator(
    task_id="get_data",
    bash_command=(
        "curl -o /opt/airflow/data/wikipageviews.gz "
        "https://dumps.wikimedia.org/other/pageviews/"
        "{{ data_interval_start.year }}/"
        "{{ data_interval_start.year }}-{{ '{:02}'.format(data_interval_start.month) }}/"
        "pageviews-{{ data_interval_start.year }}"
        "{{ '{:02}'.format(data_interval_start.month) }}"
        "{{ '{:02}'.format(data_interval_start.day) }}-"
        "{{ '{:02}'.format(data_interval_start.hour) }}0000.gz"
    ),
    dag=dag,
)

