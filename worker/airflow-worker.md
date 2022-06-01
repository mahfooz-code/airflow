# Worker

Pick up tasks that are scheduled for execution and execute them.
As such, the workers are responsible for actually "doing the work."

# Celeary executor
All these services allow you to run Airflow with CeleryExecutor.

The workload is distributed on multiple celery workers, which can run on different machines. It is the executor you should use for availability and scalability. It requires infrastructure support—Celery and Celery's backend (Redis or RabbitMQ) additionally

# Sequential executor
Each task is run locally (on the same machine as the scheduler) in its own python subprocess. They are run sequentially so that only one task can be executed at a time.


# Local executor

It is the same as the sequential executor except that multiple tasks can run in parallel. It needs a metadata database (where DAGs and tasks status are stored) that supports parallelism like MySQL.


