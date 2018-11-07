from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    error = 'Page Not Found'
    return render_template('error.html', error=error)

@app.errorhandler(500)
def server_error(error):
    error = 'Server Error'
    return render_template('error.html', error=error)

if __name__ == '__main__':
    app.run()
