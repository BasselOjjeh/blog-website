from website import create_app
#Running the website and __init__.py on the flask web server
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
