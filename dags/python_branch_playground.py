"""Python branch operator examples."""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime


default_args = {
    'owner': 'jagadish',
    'start_date': datetime(2019, 12, 10),
    'email': ['jagadish@nineleaps.com']}

with DAG('python_branch_playground', schedule_interval='@daily', default_args=default_args) as dag:

    first_task = BashOperator(
        task_id='first_task',
        bash_command='echo 2',
        xcom_push=True)

    def next_branch(**kwargs):
        """Get next branch task."""
        ti = kwargs.get('ti')
        xcom_value = int(ti.xcom_pull(task_ids='first_task'))
        if xcom_value >= 5:
            return 'continue_task'
        else:
            return 'stop_task'

    second_task = BranchPythonOperator(
        task_id='second_task',
        provide_context=True,
        python_callable=next_branch)

    continue_task = DummyOperator(task_id='continue_task')
    stop_task = DummyOperator(task_id='stop_task')

    first_task >> second_task >> [continue_task, stop_task]
