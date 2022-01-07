# bash operator

    run_this = BashOperator(
        task_id='run_after_loop',
        bash_command='echo 1',
        dag=dag,
    )
