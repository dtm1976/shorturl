from flask import redirect, render_template
from flask import request

from app import app
from app import db
from models import Url, generate_shorturl


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Generate start page. If entered url exists in db it is got from db else a new one is created
    :return: starting page
    """
    resp = None
    if request.method == 'POST':
        resp = dict()
        long_url = request.form['url']

        if long_url:
            url = db.session.query(Url).filter(Url.long_url == long_url).first()
            if not url:
                short_url = generate_shorturl()
                url = Url(long_url=long_url, short_url=short_url)
                db.session.add(url)
                db.session.commit()

            resp = {"id": url.id, "long_url": url.long_url, "short_url": url.short_url, "count": url.reference_count}

        return render_template('index.html', response=resp)
    return render_template('index.html', response=resp)


@app.route('/count/<int:id_url>')
def count_references(id_url):
    """
    Incrementing reference_count for url with id_url
    :param id_url: url id in database
    :return: redirect in real url
    """
    url = Url.query.filter_by(id=id_url).first()
    url.reference_count += 1
    db.session.add(url)
    db.session.commit()
    return redirect(url.long_url)
