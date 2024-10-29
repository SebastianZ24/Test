from website import create_app

app = create_app()

#inicializavimas programos
if __name__ == '__main__':
    app.run(debug=True)