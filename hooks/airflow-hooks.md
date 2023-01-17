Hooks are interfaces to external platforms and databases, implementing a common interface when possible and acting as building blocks for operators. 

All hooks are derived from BaseHook.

Hooks are interfaces to services external to the Airflow Cluster. 

While Operators provide a way to create tasks that may or may not communicate with some external service, hooks provide a uniform interface to access external services like S3, MySQL, Hive, Qubole, etc. 

Hooks are the building blocks for operators to interact with external services.

