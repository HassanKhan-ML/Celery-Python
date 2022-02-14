from celery import Celery
app = Celery('proj',
    backend= "db+sqlite:///db.sqlite3",
    include=['proj.tasks'],
  broker= 'redis://localhost:6379/0',
            
)

# Optional configuration, see the application user guide.
app.conf.update(
  result_expires=3600,
)

if __name__ == '__main__':
  app.start()