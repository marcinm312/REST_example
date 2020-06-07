import json
from flask import jsonify
from flask import request
from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/')
def api_root():
    return 'Welcome to my REST service'


@app.route('/books')
def api_books():
    result = []
    with open('books.json') as json_data:
        data = json.load(json_data)
        for book in data['books']:
            result.append(book['isbn'])
    return jsonify(result)


@app.route('/title/<search>')
def api_title(search):
    result = []
    with open('books.json') as json_data:
        data = json.load(json_data)
        for book in data['books']:
            if search in str(book['title']):
                result.append(book['title'])
    return jsonify(result)


@app.route('/book/<isbn>')
def api_book_isbn(isbn):
    result = ''
    with open('books.json') as json_data:
        data = json.load(json_data)
        for book in data['books']:
            if book['isbn'] == isbn:
                result = jsonify(book)
                return result
        if result == '':
            return not_found()


@app.route('/book/<isbn>', methods=['PUT'])
def api_update_book(isbn):
    title = request.args.get('title', default='*', type=str)
    with open("books.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        for book in data['books']:
            if book['isbn'] == isbn:
                book["title"] = str(title)
                jsonFile.seek(0)  # rewind
                json.dump(data, jsonFile)
                jsonFile.truncate()
    return 'Tytul w ksiazce o ISBN: ' + isbn + ' zmieniony na: ' + title


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
