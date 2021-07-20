from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
from datetime import datetime
from bson import ObjectId
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.sgalls

@app.route('/')
def main():
    return render_template('SGmain.html')

@app.route('/gohome')
def home():
    return render_template('SGhome.html')

@app.route('/posting')
def posting():
    return render_template('SGpost.html')

@app.route('/view/1')
def picture_view():
    return render_template('SGnyc.html')

@app.route('/view/2')
def picture_view01():
    return render_template('SGla.html')

@app.route('/view/3')
def picture_view02():
    return render_template('SGsea.html')

@app.route('/gall1')
def load():
    return render_template('SGgall01.html')


@app.route('/gall', methods=['POST'])
def savepic():

   print(request.files)
   ncity = {'Newyork': '1', 'LosAngeles': '2', 'Seattle': '3'}

   f = request.files["img_give"]

   title_receive = request.form['title_give']
   ncity_receive = request.form['ncity_give']
   story_receive = request.form['story_give']
   address_receive = request.form['address_give']

   extension = f.filename.split('.')[-1]
   today = datetime.now()
   mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
   filename = f'file-{mytime}'
   save_to = f'static/{filename}.{extension}'
   f.save(save_to)

   doc = {

       'img': f'{filename}.{extension}',
       'title': title_receive,
       'ncity': ncity_receive,
       'story': story_receive,
       'address': address_receive
   }

   db.sgalls.insert_one(doc)
   f.save(secure_filename(f.filename))

   return jsonify(result='success',city= ncity[ncity_receive])


@app.route('/coll', methods= ['GET'])
def viewpic():

    sgall = db.sgalls.find_one({'_id': ObjectId(request.args['id'])})
    sgall['_id'] = str(sgall['_id'])

    return jsonify ({'sgall':sgall})


@app.route('/gall', methods=['GET'])
def cardpic():
    ncity = {'newyork': 'Newyork', 'la': 'LosAngeles', 'seattle': 'Seattle'}
    sgalls = list(db.sgalls.find({'ncity': ncity[request.args['ncity']]}))
    for elem in sgalls:
        elem['_id'] = str(elem['_id'])

    print(db.sgalls.find_one({'ncity': 'Newyork'}))
    return jsonify({'sgalls':sgalls})


if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)