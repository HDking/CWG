import os
from flask import Flask, request, session, flash, redirect, url_for, g
from flask import Flask, render_template
import sqlite3
import datetime

from flask import request

#Configuration
DATABASE = 'blog.db'
DATABASETWO = 'messages.db'
DATABASETHREE = 'crisis_messages.db'


app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
    
def connect_db2():
    return sqlite3.connect(app.config['DATABASETWO'])
    
def connect_db3():
    return sqlite3.connect(app.config['DATABASETHREE'])
    
    
#Facilitator received messages from crisis team
@app.route('/facilitator_messages')
def facilitatorMessages():
    g.db = connect_db3()
    cur = g.db.execute('select title, message, type, posted_date, team from crisis_messages ORDER BY posted_date DESC')
    messages =[dict(title=row[0], message=row[1], type=row[2], date=row[3], team=row[4]) for row in cur.fetchall()]
    g.db.close()
    return render_template('facilitator_messages.html', messages = messages)

#Crisis Team and communications
@app.route('/crisis_center')
def crisisCenter():
    g.db = connect_db2()
    cur = g.db.execute('select title, message, type, posted_date from messages where team=1 ORDER BY posted_date DESC')
    messages =[dict(title=row[0], message=row[1], type=row[2], date=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('crisis_center.html', messages = messages)
    
@app.route('/crisis_communications')
def crisisCommunications():
    g.db = connect_db3()
    cur = g.db.execute('select message_id, title, message, type, posted_date, team from crisis_messages')
    messages = [dict(message_id=row[0], title=row[1], message=row[2], type=row[3], date=row[4], team= row[5]) for row in cur.fetchall()]
    g.db.close()
    return render_template('crisis_communications.html',  messages=messages)
    
    
#media ding    
@app.route('/addCrisisMessage/', methods=['POST'])
def addCrisisMessage():
    g.db = connect_db3()
    title = request.form['title']
    message = request.form['message']
    type = request.form['type']
    team = request.form['team']
    
    if not title or not message:
        return redirect(url_for('crisisCommunications'))
    else: 
        g.db=connect_db3()
        date = datetime.datetime.utcnow()
        g.db.execute('insert into crisis_messages (title, message,type, posted_date, team) values (?,?,?,?,?)' ,[request.form['title'], request.form['message'], request.form['type'], date, request.form['team']])
        g.db.commit()
        g.db.close()
        return redirect(url_for('crisisCommunications'))
    
@app.route('/facilitator_center')
def facilitatorCenter():
    g.db = connect_db2()
    cur = g.db.execute('select title, message, type, posted_date from messages where team =1 ORDER BY posted_date DESC')
    messages =[dict(title=row[0], message=row[1], type=row[2], date=row[3]) for row in cur.fetchall()]
    cur = g.db.execute('select title, message, type, posted_date from messages where team =2 ORDER BY posted_date DESC')
    media_messages =[dict(title=row[0], message=row[1], type=row[2], date=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('facilitator_center.html', messages = messages, media_messages = media_messages)
    
#media ding    
@app.route('/addMessage/', methods=['POST'])
def addMessage():
    g.db = connect_db2()
    title = request.form['title']
    post = request.form['message']
    summary = request.form['type']
    team = request.form['team']
    
    if not title or not post:
        return redirect(url_for('facilitatorCenter'))
    else: 
        g.db=connect_db2()
        date = datetime.datetime.utcnow()
        g.db.execute('insert into messages (title, message, type,team, posted_date) values (?,?,?,?,?)' ,[request.form['title'], request.form['message'], request.form['type'],request.form['team'], date])
        g.db.commit()
        g.db.close()
        return redirect(url_for('facilitatorCenter'))


@app.route('/media_messages')
def mediaMessages():
    g.db = connect_db2()
    cur = g.db.execute('select title, message, type, posted_date from messages where team=2 ORDER BY posted_date DESC')
    messages =[dict(title=row[0], message=row[1], type=row[2], date=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('media_messages.html', messages = messages)
    

#########################
#### Different Teams ####
######################### 


# Media team
@app.route('/media_center')
def mediaCenter():
    g.db = connect_db()
    cur = g.db.execute('select task_id, title, post,reporter from posts where published=0')
    open_posts =[dict(task_id=row[0], title=row[1], post=row[2], reporter=row[3]) for row in cur.fetchall()]
    cur = g.db.execute('select task_id, title, post, reporter from posts where published=1')
    published_posts =[dict(task_id=row[0], title=row[1], post=row[2], reporter=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('media_overview.html',  open_posts=open_posts, published_posts=published_posts)
    
    
@app.route('/add/', methods=['POST'])
def add():
    g.db = connect_db()
    title = request.form['title']
    post = request.form['post']
    summary = request.form['summary']
    reporter = request.form['reporter']
    if not title or not post:
        return redirect(url_for('mediaCenter'))
    else: 
        g.db=connect_db()
        date = datetime.datetime.utcnow()
        g.db.execute('insert into posts (title,reporter, post, summary, posted_date, published) values (?,?,?,?, ? ,0)' ,[request.form['title'],request.form['reporter'] , request.form['post'], request.form['summary'], date])
        g.db.commit()
        g.db.close()
        return redirect(url_for('mediaCenter'))
        
@app.route('/publish/<int:task_id>/')
def publish(task_id):
    g.db = connect_db()
    g.db.execute(
        'update posts set published=1 where task_id='+str(task_id)
        )
    g.db.commit()
    g.db.close()
    return redirect(url_for('mediaCenter'))
    
@app.route('/delete/<int:task_id>/')
def delete_article(task_id):
    g.db = connect_db()
    g.db.execute('delete from posts where task_id='+str(task_id))
    g.db.commit()
    g.db.close()
    return redirect(url_for('mediaCenter'))

# Debriefing
@app.route('/timeline')
def timeline():
    g.db = connect_db()
    cur = g.db.execute('select title, summary, posted_date, task_id, reporter from posts where published=1 ORDER BY posted_date DESC')
    articles =[dict(title=row[0], summary=row[1], date=row[2], task_id=row[3], reporter=row[4]) for row in cur.fetchall()]
    g.db.close()
    return render_template('timeline.html', articles=articles)

#public during games
@app.route('/articles/<int:task_id>/')
def show(task_id):
    g.db = connect_db()
    cur = g.db.execute('select title, post, posted_date,reporter from posts where task_id='+str(task_id))
    article =[dict(title=row[0], post=row[1], date=row[2], reporter=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('articles.html', article=article)
    


    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))