from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

window = 1  # in minutes
inteval = window * 60 // 24 // 2


default_args = {
    'owner': 'Kevin Lin',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['klin@bigdataprocessor.me'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),

}
dag = DAG(
    'druid_batch',
    default_args=default_args,
    description='Druid batch DAG',
    schedule_interval=timedelta(seconds=inteval),
)


task = BashOperator(
    task_id='batch_processing',
    bash_command='cd /home/ubuntu ; python3 druid_batch.py',
    dag=dag,
)