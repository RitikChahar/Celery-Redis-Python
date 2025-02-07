from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_script():
    print("Running the script...")
    with open("output.txt", "w") as f:
        f.write("Hello from Celery!")
    return "Task completed!"