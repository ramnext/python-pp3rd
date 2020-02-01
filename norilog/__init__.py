import json
from datetime import datetime


from flask import Flask, render_template, redirect, request, Markup, escape


application = Flask(__name__)


DATA_FILE = "norilog.json"


def save_data(start, finish, memo, created_at):
    """Record data.
    :param start: getting on station
    :type start: str
    :param finish: getting off station
    :type finish: str
    :param memo: note
    :type memo: str
    :param created_at: getting on and off date-time
    :type created_at: datetime.datetime
    :return: None
    """
    try:
        # Open database file by json module.
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []

    database.insert(0, {
        "start": start,
        "finish": finish,
        "memo": memo,
        "create_at": created_at.strftime("%Y-%m-%d %H:%M")
    })

    json.dump(
            database, open(DATA_FILE, mode="w", encoding="utf-8"),
            indent=4, ensure_ascii=False)


def load_data():
    """Return Getting on and off data."""
    try:
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []
    return database


@application.route('/')
def index():
    """Top page
    Return screen data for top page.
    """
    # Reading saved data.
    rides = load_data()
    return render_template('index.html', rides=rides)


@application.route('/save', methods=['POST'])
def save():
    """Remember URL
    :returns: redirect url.
    """
    # correct recording datas.
    start = request.form.get('start')    # start time.
    finish = request.form.get('finish')  # arrival time.
    memo = request.form.get('memo')      # note.
    create_at = datetime.now()           # recording time that system datetime.
    save_data(start, finish, memo, create_at)

    # move top page after saveing.
    return redirect('/')


@application.template_filter('nl2br')
def nl2br_fileter(s):
    """Template filter that replace to <br> from new line character.

    :s: target string.
    :returns: replaced string.

    """
    return escape(s).replace('\n', Markup('<br>'))


def main():
    application.run('0.0.0.0', 8000)


if __name__ == '__main__':
    # Boot Application by ip 0.0.0.0:8000.
    application.run('0.0.0.0', 8000, debug=True)
