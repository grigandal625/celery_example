import os
from celery import Celery

REDIS_HOST='localhost'
REDIS_PORT=6379

app = Celery("tasks")
app.conf.broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}"
app.conf.result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}"

@app.task
def simple_task(x, y):
    print(x, y)
    print("do something long")
    data = str(x) + " " + str(y)
    with open("tmp.txt", "w") as f:
        f.write(data)
    # send_data_to_telegram(data)
    # save_data_to_db()
    return data


@app.task
def monitor_file():
    readed = open("tmp.txt", "r").read()
    # if condition(readed): send_response_to_telegram(readed)
    print("READED ", readed)
    return readed


app.conf.beat_schedule = {
    'do-monitor': {'task': 'monitor_file', 'shedule': 5.0}
}