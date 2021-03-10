from flask import Flask, render_template, abort
from random import randrange

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


@app.route('/issues/three')
def issue_three():
    return render_template('issues/three/index.html')


@app.route('/issues/three/<name>')
def issue_three_page(name):
    template_map = {
        'thompkins': {
            'template_url': 'simone.html',
            'image_num': '14'
        },
        'marshall': {
            'template_url': 'marshall.html',
            'image_num': '2'
        },
        'brems': {
            'template_url': 'brems.html',
            'image_num': '3'
        },
        'choudhury': {
            'template_url': 'choudhury.html',
            'image_num': '4'
        },
        'fabian': {
            'template_url': 'fabian.html',
            'image_num': '5'
        },
        'gallagher': {
            'template_url': 'gallagher.html',
            'image_num': '6'
        },
        'lapinel': {
            'template_url': 'lapinel.html',
            'image_num': '7'
        },
        'lee': {
            'template_url': 'lee.html',
            'image_num': '8'
        },
        'sayeed': {
            'template_url': 'sayeed.html',
            'image_num': '9'
        },
        'sibra': {
            'template_url': 'sibra.html',
            'image_num': '1'
        },
        'zimmerman': {
            'template_url': 'zimmerman.html',
            'image_num': '12'
        }
    }
    if name not in template_map.keys():
        abort(404)

    page_info = template_map.get(name)

    return render_template(f'issues/three/{page_info.get("template_url")}',
                           img_num=page_info.get("image_num")
                           )


@app.route('/issues/four')
def issue_four():
    return render_template('issues/four/index.html')


@app.route('/issues/four/<name>')
def issue_four_page(name):
    template_map = {
        'awoke': 'awoke.html',
        'cardinaux': 'cardinaux.html',
        'doreski': 'doreski.html',
        'good': 'good.html',
        'lauer': 'lauer.html',
        'whittenberg': 'whittenberg.html',
        'maolalai': 'maolalai.html',
        'medeiros': 'medeiros.html',
        'ooto': 'ooto.html',
        'saint-marie': 'saint-marie.html',
        'smith': 'smith.html',
        'vermass': 'vermaas.html',
        'walsh': 'walsh.html',
        'withington': 'withington.html',
        'romo': 'romo.html',
        'pritchard': 'pritchard.html',
        'sampsell': 'sampsell.html'
    }
    style_names = ['fruit_salad', 'tomato', 'spinach', 'soursop',
                   'pumpkin', 'pickle', 'olive', 'avacado', 'coconut',
                   'cherry']

    if name not in template_map.keys():
        abort(404)

    return render_template(f'issues/four/{template_map.get(name)}',
                           style=style_names[randrange(len(style_names))])


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
