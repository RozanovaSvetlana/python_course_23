from hw_4.app import app
from datetime import datetime


@app.task
def hello():
    return "Hello world!"


@app.task
def mult(x, y):
    print("Multiply ", x, "by", y)
    return x * y


@app.task
def sum(x, y):
    print("Add", x, " by ", y)
    return x + y


@app.task
def get_date():
    date = datetime.now().date()
    print("Now is ", date)
    return date
