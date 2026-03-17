from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def training_pipeline():
    print("Running training pipeline...")

dag = DAG(
    "clove_ml_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@monthly",
    catchup=False
)

task = PythonOperator(
    task_id="train_model",
    python_callable=training_pipeline,
    dag=dag
)