from pathlib import Path
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.python import PythonSensor


def _wait_for_supermarket(supermarket_id):
    supermarket_path = Path("/data/" + supermarket_id)
    data_files = supermarket_path.glob("data-*.csv")
    success_file = supermarket_path/"_SUCCESS"
    return data_files and success_file.exists()     


wait_for_supermarket_1 = PythonSensor(
   task_id="wait_for_supermarket_1",
   python_callable=_wait_for_supermarket,
   op_kwargs={"supermarket_id": "supermarket1"},
   dag=dag,
)

wait_for_supermarket_1 = FileSensor(
   task_id="wait_for_supermarket_1",
   filepath="/data/supermarket1/data.csv",
)


