from tasks import run_script

task = run_script.delay()
print(f"Task ID: {task.id}")