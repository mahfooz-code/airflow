import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


trigger_dag_1 = DAG(
    dag_id="trigger_dag_1",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="0 0 * * *",
)
trigger_dag_2 = DAG(
    dag_id="trigger_dag_2",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval=None,
)

DummyOperator(task_id="etl", dag=trigger_dag_1) >> TriggerDagRunOperator(
    task_id="trigger_dag2_task",
    trigger_dag_id="trigger_dag_2",
    dag=trigger_dag_1,
)

PythonOperator(
    task_id="report", dag=trigger_dag_2, python_callable=lambda: print("hello")
)
