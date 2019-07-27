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
        'ann_halvorsen': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/ann_halvorsen.html'
        },
        'benjamin_juitt': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/benjamin_juitt.html'
        },
        'chris_salveson': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/chris_salveson.html'
        },
        'eliot_cardinaux': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/elliot_cardinaux.html'
        },
        'emilie_menzel': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/emilie_menzel.html'
        },
        'gerard_sarnat': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/gerard_sarnat.html'
        },
        'laurie_kolp': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/laurie_kolp.html'
        },
        'margaret_foley': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/margaret_foley.html'
        },
        'robert_okaji': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/robert_okaji.html'
        },
        'shriram_sivaramakrishnan': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/shriram_sivaramakrishnan.html'
        },
        'sonya_lara': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/sonya_lara.html'
        },
        'tara_dasso': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/tara_dasso.html'
        },
        'william_doreski': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/william_doreski.html'
        },
        'zachery_elbourne': {
            'img': '/img/two/bw_test_bg.png',
            'page': 'issues/two/zachery_elbourne.html'
        },
    }
    if name in template_map.keys():
        return render_template(template_map[name]['page'],
                               img=template_map[name]['img']
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
