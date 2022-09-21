from flask import Flask
import app


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def main():
    # RUN LOCAL SERVER
    app.run()


if __name__ == "__main__":
    main()
