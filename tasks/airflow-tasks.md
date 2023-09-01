# Tasks

Tasks in Airflow manage the execution of an operator; they can be thought of as a small wrapper or manager around an operator that ensures the operator executes correctly.

The user can focus on the work to be done by using operators, while Airflow ensures correct execution of the work via tasks.

Tasks are internal components to manage operator state and display state changes (e.g., started/finished) to the user.

## Best practices

### Atomicity

Airflow, tasks should be defined so that they either succeed and produce some proper result or fail in a manner that does not affect the state of the system

### Idempotence
