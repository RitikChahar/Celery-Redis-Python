# Celery-Redis-Python
A guide to setting up Redis and Celery in WSL, including installation, configuration, and running Celery tasks with Redis as the broker. It also covers creating a Python virtual environment for the setup.

## Commands

### Install WSL
To install WSL on your system, run:
```sh
wsl --install
```
This will install the default Linux distribution for WSL (usually Ubuntu). If you want a different distribution, use:
```sh
wsl --install -d <DistroName>
```

### Install Redis in WSL
To install Redis on your WSL distribution, first update the package list, and then install Redis:
```sh
sudo apt update
sudo apt install redis-server
```

### Start Redis Server
To start the Redis server in your WSL instance, use:
```sh
redis-server
```

### Check if Redis is Running
To check if Redis is running, use:
```sh
ps aux | grep redis
```

### Stop Redis Server
To stop the Redis server, use:
```sh
sudo pkill -9 redis-server
```

### Fix Memory Overcommit Issue in Redis
If you see a warning about `Memory overcommit must be enabled!` when starting Redis, run the following command to fix it temporarily:
```sh
sudo sysctl vm.overcommit_memory=1
```
To make this change permanent, add it to `/etc/sysctl.conf`:
```sh
echo 'vm.overcommit_memory = 1' | sudo tee -a /etc/sysctl.conf
```
Then apply the changes:
```sh
sudo sysctl -p
```
If the issue persists, restart your system:
```sh
sudo reboot
```
After this, restart your Redis server and the warning should be gone.

### Install Celery in WSL
To install Celery, first install `pip` if it's not already installed:
```sh
sudo apt install python3-pip
```

Then install Celery and Redis:
```sh
pip3 install celery redis
```

### Create a Virtual Environment in WSL (Recommended)
It is recommended to use a virtual environment to manage Python dependencies separately from the system-wide Python packages. Follow these steps:

1. **Install `python3-venv` if not already installed:**
   ```sh
   sudo apt install python3-venv
   ```

2. **Create a new virtual environment:**
   Navigate to your project directory and run:
   ```sh
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```sh
   source venv/bin/activate
   ```

4. **Install Celery and Redis in the virtual environment:**
   ```sh
   pip install celery redis
   ```

### Run Celery Worker
To start the Celery worker with Redis as the broker, run the following command:
```sh
celery -A tasks worker --loglevel=info
```

---

### Example Celery Setup

#### `tasks.py`

```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_script():
    print("Running the script...")
    with open("output.txt", "w") as f:
        f.write("Hello from Celery!")
    return "Task completed!"
```

#### `main.py`

```python
from tasks import run_script

task = run_script.delay()

print(f"Task ID: {task.id}")
```

After running `celery -A tasks worker --loglevel=info`, the worker will be running and ready to process tasks.

---

Now, you can follow these instructions to get your Redis and Celery set up and running smoothly on WSL within a virtual environment. Let me know if you encounter any issues!

---

This updated guide includes instructions for setting up a virtual environment and installing Celery and Redis inside it, keeping your project dependencies isolated from your system's Python packages.
