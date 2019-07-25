from flask import Flask, render_template, abort

app = Flask(__name__, static_url_path='')
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submissions')
def submissions():
    return render_template('submissions.html')


@app.route('/issues')
def issue_index():
    return render_template('issues/issue_index.html')


@app.route('/issues/one')
def issue_one():
    return render_template('issues/one/index.html')


@app.route('/issues/one/contributors')
def issue_one_contributors():
    return render_template('issues/one/contributors.html')


@app.route('/issues/two')
def issue_two():
    return render_template('issues/two/index.html')


@app.route('/issues/two/<name>')
def issue_two_page(name):
    template_map = {
        'test': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/ann_halvorsen.html'
        }
    }
    if name in template_map.keys():
        return render_template('issues/two/poem_page.html',
                               img=template_map[name]['img'],
                               page=template_map[name]['page']
                               )
    else:
        abort(404)


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
