from flask import Flask


def factory():
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    app = factory()
    app.run()
