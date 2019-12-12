"""Python related opertaor to practise with airflow."""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from time import sleep

default_args = {
    'owner': 'jagadish',
    'start_date': datetime(2019, 12, 8),
    'email': None}


dag = DAG(
    'python_playground',
    schedule_interval='@daily',
    default_args=default_args)


def print_hello_world():
    """
    Print hello world.

    @params: return hello world
    """
    return 'hello world'


task1 = PythonOperator(
    task_id='python_hello_world',
    python_callable=print_hello_world,
    dag=dag)


def sleep_args(interval):
    """Sleep based on given interval seconds."""
    print(interval)
    sleep(interval)


task2 = PythonOperator(
    task_id='sleep_args',
    python_callable=sleep_args,
    op_kwargs={'interval': 6},
    dag=dag)

for i in range(10):
    task = BashOperator(
        task_id='task_id' + str(i),
        bash_command='date',
        dag=dag)
    task1.set_upstream(task)
