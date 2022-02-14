# from celery import Celery
# from proj.helprs import successc_pr
# # from proj.celery import app

# def my_monitor(app):
#     state = app.events.State()

#     def announce_failed_tasks(event):
#         state.event(event)
#         task = state.tasks.get(event['uuid'])

#         print(f'TASK FAILED: {task.name}[{task.uuid}]')

#     def announce_succeeded_tasks(event):
#         state.event(event)
#         task = state.tasks.get(event['uuid'])
#         successc_pr()

#         print(f'TASK SUCCEEDED: {task.name}[{task.uuid}]')

#     def worker_online_handler(event):
#         state.event(event)
#         print("New worker gets online")
#         print(event['hostname'], event['timestamp'], event['freq'], event['sw_ver'])

#     with app.connection() as connection:
#         recv = app.events.Receiver(connection, handlers={
#                 'task-failed': announce_failed_tasks,
#                 'task-succeeded': announce_succeeded_tasks,
#                 'worker-online': worker_online_handler,
#                 '*': state.event,
#         })
#         recv.capture(limit=None, timeout=None, wakeup=True)

# if __name__ == '__main__':
#     app = Celery("proj", broker="redis://localhost:6379")

#     # app = Celery('proj')
#     my_monitor(app)


from celery import Celery


def my_monitor(app):
  state = app.events.State()

  def worker_online_handler(event):
    state.event(event)
    print("New worker gets online")
    print(event['hostname'],'-', event['timestamp'],'-', event['freq'],'-',event['sw_ver'])

  def announce_failed_tasks(event):
    state.event(event)
    task = state.tasks.get(event['uuid'])
    print('TASK FAILED: %s[%s] %s' % (
      task.name, task.uuid, task.info(),))
  
  def announce_succeeded_tasks(event):
    state.event(event)
    task = state.tasks.get(event['uuid'])
    print('TASK SUCCEEDED: %s[%s] %s' % (
      task.name, task.uuid, task.info(),))

  def on_task_sent(event):
    print('on_task_sent')
  def on_task_received(event):
    print('on_task_received')
  def on_task_started(event):
    print('on_task_started')
  def on_task_rejected(event):
    print('on_task_rejected')
  def on_task_revoked(event):
    print('on_task_revoked')
  def on_task_retried(event):
    print('on_task_retried')
  def worker_heartbeat(event):
    state.event(event)
    print("Worker Heart-Beat ")
    print(event['hostname'],'-', event['timestamp'],'-', event['freq'],'-',event['sw_ver'])
  def worker_offline(event):
    state.event(event)
    print("Worker Get Offilne")
    print(event['hostname'],'-', event['timestamp'],'-', event['freq'],'-',event['sw_ver'])
  with app.connection() as connection:
    recv = app.events.Receiver(connection, handlers={
      'task-received': on_task_received,   #Done
      'task-started': on_task_started,     #Done
      
      'task-sent': on_task_sent,          # 
      'task-succeeded': announce_succeeded_tasks,      #Done

      'task-rejected': on_task_rejected,
      'task-revoked': on_task_revoked,     #  Done Cannel Task Manully
      'task-retried': on_task_retried,
      'task-failed': announce_failed_tasks,            #Done

      'worker-online': worker_online_handler,          #Done
      # 'worker-heartbeat': worker_heartbeat,            #Done # Not Clear
      'worker-offline':worker_offline,                 #Done

    })
    recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
  app = Celery("proj", broker="redis://localhost:6379")

  # app = Celery('proj')
  my_monitor(app)