from website import create_app

app = create_app()

if __name__ == '__name__': # len ak spustim main, tak sa spusti apka
    app.run(debug=True) # debug=true znamena, ze ak nieco zmenim alebo ulozim v kode, tak sa web server refreshne