Operators run independently of each other, although you can define the order of execution, which we call dependencies in Airflow.

In Airflow, we can use the binary right shift operator (i.e., "rshift" [>>]) to define dependencies between tasks.

# Note

In Python, the rshift operator (>>) is used to shift bits, which is a common operation in, for example, cryptography libraries. In Airflow, there is no use case for bit shifting, and the rshift operator was overridden to provide a readable way to define dependencies between tasks.

# amazon

    apache-airflow-providers-amazon
