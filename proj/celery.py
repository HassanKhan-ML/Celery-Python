from celery import Celery
import time

app = Celery('proj',
             backend= "db+sqlite:///db.sqlite3",
            #  include=['proj.tasks'],
            broker= 'redis://localhost:6379/0',
            
)
# timezone = 'Europe/London'

# app.conf.timezone = 'Europe/London'

# app.conf.broker_url = 'redis://localhost:6379/0'

# app = Celery('proj',
#              broker='amqp://',
#              backend='rpc://',
#              include=['proj.tasks'])

# Optional configuration, see the application user guide.
# app.conf.update(
#     result_expires=3600,
#     task_routes = {
#         'proj.tasks.add': {'queue': 'hipri'},  
#     },
#     timezone='Europe/London',
# )

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()
