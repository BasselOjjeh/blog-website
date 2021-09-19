from website import create_app
#Setting the website on local host 5000 using flask by importing a sub-package
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
