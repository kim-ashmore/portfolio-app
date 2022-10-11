from flask import Flask
import app

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


def main():
    # RUN LOCAL SERVER
    # app = create_app()
    app.run()


if __name__ == "__main__":
    main()
