# 1.Celery+Redis+Sqlite.py

# from celery import Celery

# app = Celery('hello',broker='redis://localhost:6379/0')

# @app.task
# def hello():
#     return 'hello world'


from celery import Celery
from time import sleep

# app = Celery('tasks', broker='redis://localhost:6379/0')
app = Celery('tasks', backend= "db+sqlite:///db.sqlite3"
)

app.conf.broker_url = 'redis://localhost:6379/0'
# app.conf.result_backend = 'redis://localhost:6379/0'
# app.conf.broker_url = 'redis://localhost:6379/0'


CELERY_TASK_ROUTES = {
 'app1.tasks.*': {'queue': 'queue1'},
 'app2.tasks.*': {'queue': 'queue2'},
}
CELERY_BEAT_SCHEDULE = {
    'app1_test': {
        'task': 'app1.tasks.app1_test',
        'schedule': 15,
        'options': {'queue': 'queue1'}
    },
    'app2_test': {
        'task': 'app2.tasks.app2_test',
        'schedule': 15,
        'options': {'queue': 'queue2'}
    },

}


@app.task(queue='queue1')
def app1_test():
    print('I am app1_test task!')
    sleep(10)



@app.task(queue='queue2')
def app1_test():
    print('I am app1_test task!')
    sleep(10)
    
# @app.task()
# def app1_test():
#     print('I am app1_test task!')
#     sleep(10)

# @app.task()
# def app2_test():
#     print('I am app2_test task!')
#     sleep(10)