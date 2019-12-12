"""List of all subdags."""
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

def sub_dag(parent_dag, child_dag, start_date, schedule_interval):
    with DAG(f'{parent_dag}.{child_dag}', start_date=start_date, schedule_interval=schedule_interval) as dag:
        list_tasks = [DummyOperator(task_id=f"task_{i}") for i in range(10)]
        for index, task in enumerate(list_tasks):
            if index > 0:
                list_tasks[index-1] >> task
    return dag