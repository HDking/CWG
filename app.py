import os
from flask import Flask, request, session, flash, redirect, url_for, g
from flask import Flask, render_template
import sqlite3
import datetime

from flask import request

#Configuration
DATABASE = 'blog.db'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# Media team
@app.route('/media_center')
def mediaCenter():
    g.db = connect_db()
    cur = g.db.execute('select task_id, title, post from posts where published=0')
    open_posts =[dict(task_id=row[0], title=row[1], post=row[2]) for row in cur.fetchall()]
    cur = g.db.execute('select task_id, title, post from posts where published=1')
    published_posts =[dict(task_id=row[0], title=row[1], post=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('media_overview.html',  open_posts=open_posts, published_posts=published_posts)
    
    # form=AddArticleForm(request.form),
    
@app.route('/add/', methods=['POST'])
def add():
    g.db = connect_db()
    title = request.form['title']
    post = request.form['post']
    summary = request.form['summary']
    if not title or not post:
        return redirect(url_for('mediaCenter'))
    else: 
        g.db=connect_db()
        date = datetime.datetime.utcnow()
        g.db.execute('insert into posts (title, post, summary, posted_date, published) values (?,?,?, ? ,0)' ,[request.form['title'], request.form['post'], request.form['summary'], date])
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
    cur = g.db.execute('select title, summary, posted_date, task_id from posts where published=1')
    articles =[dict(title=row[0], summary=row[1], date=row[2], task_id=row[3]) for row in cur.fetchall()]
    
    
    g.db.close()
    return render_template('timeline.html', articles=articles)

#public during games
@app.route('/articles/<int:task_id>/')
def show(task_id):
    g.db = connect_db()
    cur = g.db.execute('select title, post, posted_date from posts where task_id='+str(task_id))
    article =[dict(title=row[0], post=row[1], date=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('articles.html', article=article)
    


    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))