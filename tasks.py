# 1.Celery+Redis+Sqlite.py

# from celery import Celery

# app = Celery('hello',broker='redis://localhost:6379/0')

# @app.task
# def hello():
#     return 'hello world'


from celery import Celery
from time import sleep

# app = Celery('tasks', broker='redis://localhost:6379/0')
app = Celery('tasks', backend= "db+sqlite:///db.sqlite3",
             broker= 'redis://localhost:6379/0' ,

)

# app.conf.broker_url = '
# app.conf.result_backend = 'redis://localhost:6379/0'
# app.conf.broker_url = 'redis://localhost:6379/0'

@app.task
def add(x):
  sleep(2)
  for i in range(x):
    print(i)
  return x 