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