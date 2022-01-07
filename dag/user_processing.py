from airflow.models import DAG
from datetime import datetime
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

default_args = {
    'start_date': datetime(2022, 1, 1),
    'owner': 'malam'
}

with DAG("user_processing", schedule_interval="@daily",start_date=datetime(2022, 1, 1)) as dag:
    creating_table=SqliteOperator(
    task_id='creating_table',
    sqlite_conn_id='db_sqlite',
    sql='''
    create table users(
    firstname text not null,
    lastname text not null,
    country text not null,
    username text not null,
    password text not null,
    email text not null primary  key );
    '''
    )