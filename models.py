import shortuuid
# from flask import url_for

from app import db
from config import PROTOCOL, SERVER


class Url(db.Model):
    """
    Table that contains:
    id: primary_key
    long_url: source long url
    short_url: url corresponded to source url
    reference_count: number of reference by url
    """
    __tablename__ = 'urls'
    id = db.Column(db.Integer(), primary_key=True)
    long_url = db.Column(db.String(255), unique=True)
    short_url = db.Column(db.String(50), unique=True)
    reference_count = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return "<{}: {}>".format(self.id, self.long_url)


def generate_shorturl(suffix_length=8):
    """
    generating suffix of short url
    :param suffix_length:
    :return: full path reference
    """

    # for production
    # short_url = url_for('index', _external=True) + \
    #             shortuuid.random(length=suffix_length)
    short_url = PROTOCOL + SERVER + '/' + \
                shortuuid.random(length=suffix_length)
    return short_url
