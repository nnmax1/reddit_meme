from reddit_db import MemeDatabase

from flask import Flask,render_template, jsonify
from api import  memeAPI, getUrls

db = MemeDatabase()

# api endpoints (reddit meme api)

app = Flask(__name__, template_folder='templates') 


def add_memes(db):
    i =0
    while i < 5: 
        r = memeAPI()
        # only add if author is not automoderator
        if r['authors'][0]['name'] != "/u/AutoModerator":
            db.add_data(r)
            i = i + 1


@app.route('/api/meme')
def memeAPIendpoint1():
    data = memeAPI()
    return jsonify(data)
@app.route('/api/meme/only_image')
def memeAPIendpoint2():
    data = memeAPI()
    return jsonify({"img": data['img']})

@app.route('/subreddits', methods=['GET'])
def subreddits():
    file = "api_data/subreddits.txt"
    r = getUrls(file)
    return render_template('subreddits.html', subreddits=r)


@app.route('/', methods = ['GET'])
def  reddit_meme_page():
    # for meme reddit feed 
    db.delete_data()
    add_memes(db)    
    r = db.get_data()
    num = len(r['data'])
    return render_template('reddit.html', memes=r, maxRange = num)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(port=5000)


