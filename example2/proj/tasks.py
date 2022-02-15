from .celery import app
from time import sleep

@app.task
def add(x, y):
	for i in range(x):
		sleep(4)
		print("X : ",i)
	return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)


# $ celery flower --auth="me@gmail.com|you@gmail.com" --oauth2_key=631896940196-73ee802a2cko4paci1e25n3a1jp3n1k5.apps.googleusercontent.com --oauth2_secret=TQza-0xY8VR6VX-3MLVDZmb4 --oauth2_redirect_uri=http://flower.example.com/login
