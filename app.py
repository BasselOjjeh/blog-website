from website import create_app
#initializing flask
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)