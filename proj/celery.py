from celery import Celery


app = Celery('proj',
             backend= "db+sqlite:///db.sqlite3",
             include=['proj.tasks'],
            broker= 'redis://localhost:6379/0',
)

# app.conf.broker_url = 'redis://localhost:6379/0'

# app = Celery('proj',
#              broker='amqp://',
#              backend='rpc://',
#              include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)


if __name__ == '__main__':
    app.start()