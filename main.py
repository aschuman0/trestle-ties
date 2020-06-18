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
            'img': '/img/two/halvorsen.jpg',
            'page': 'issues/two/ann_halvorsen.html',
            'theme': 'light'
        },
        'benjamin_juitt': {
            'img': '/img/two/juitt.jpg',
            'page': 'issues/two/benjamin_juitt.html',
            'theme': 'light'
        },
        'chris_salveson': {
            'img': '/img/two/salveson.jpg',
            'page': 'issues/two/chris_salveson.html',
            'theme': 'dark'
        },
        'eliot_cardinaux': {
            'img': '/img/two/cardinaux.jpg',
            'page': 'issues/two/elliot_cardinaux.html',
            'theme': 'dark'
        },
        'emilie_menzel': {
            'img': '/img/two/menzel.jpg',
            'page': 'issues/two/emilie_menzel.html',
            'theme': 'light'
        },
        'gerard_sarnat': {
            'img': '/img/two/sarnat.jpg',
            'page': 'issues/two/gerard_sarnat.html',
            'theme': 'dark'
        },
        'laurie_kolp': {
            'img': '/img/two/kolp.jpg',
            'page': 'issues/two/laurie_kolp.html',
            'theme': 'light'
        },
        'margaret_foley': {
            'img': '/img/two/foley.jpg',
            'page': 'issues/two/margaret_foley.html',
            'theme': 'dark'
        },
        'robert_okaji': {
            'img': '/img/two/okaji.jpg',
            'page': 'issues/two/robert_okaji.html',
            'theme': 'dark'
        },
        'shriram_sivaramakrishnan': {
            'img': '/img/two/sivaramakrishnan.jpg',
            'page': 'issues/two/shriram_sivaramakrishnan.html',
            'theme': 'light'
        },
        'sonya_lara': {
            'img': '/img/two/lara.jpg',
            'page': 'issues/two/sonya_lara.html',
            'theme': 'dark'
        },
        'tara_dasso': {
            'img': '/img/two/dasso.jpg',
            'page': 'issues/two/tara_dasso.html',
            'theme': 'light'
        },
        'william_doreski': {
            'img': '/img/two/doreski.jpg',
            'page': 'issues/two/william_doreski.html',
            'theme': 'light'
        },
        'zachery_elbourne': {
            'img': '/img/two/elbourne.jpg',
            'page': 'issues/two/zachery_elbourne.html',
            'theme': 'light'
        },
        'theodore_blackshear_bowen': {
            'img': '/img/two/theo.jpg',
            'page': 'issues/two/theodore_blackshear_bowen.html',
            'theme': 'light'
        }
    }

    light_style_url = '/css/issue_two_light_book.css'
    dark_style_url = '/css/issue_two_dark_book.css'

    if name in template_map.keys():

        css_url = dark_style_url
        if template_map[name]['theme'] == 'light':
            css_url = light_style_url

        return render_template(template_map[name]['page'],
                               img=template_map[name]['img'],
                               css=css_url
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
