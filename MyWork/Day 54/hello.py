from flask import Flask
import time

app = Flask(__name__)


# print(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()


def delay_decorator(function):  # a function that wraps another and gives that function some additional functionality
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
        return werapper_function


@delay_decorator
def say_hello():
    print("Hello")


decorated_func = delay_decorator(say_hello)
decorated_func


@app.route("/bye")
def say_bye():
    return "Bye"



@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"
