from flask import Flask,render_template,request
import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        # conn.execute('''DROP TABLE users''')
        conn.execute('''
            CREATE TABLE news (
                news_id INTEGER   PRIMARY KEY AUTOINCREMENT,
                auth_name TEXT NOT NULL,
                title TEXT NOT NULL,
                news TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        conn.close()

create_db_table()  

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello, Flask!"

@app.route("/") 
def home():   
    return render_template("index.html")

@app.route("/news") 
def news():   
    return render_template("blog.html")

@app.route("/add-news") 
def add_news():   
    return render_template("add-news.html")

@app.route("/contact") 
def contact():   
    return render_template("contact.html")

@app.route("/about") 
def about():   
    return render_template("about.html")

@app.route("/single-post") 
def single_post():   
    return render_template("single-post.html")



@app.route('/api/v1/add-news', methods = ['POST'])
def add():

    print("**SERVICE WORKING - START**")
    model_result(news1)
    print("**SERVICE WORKING - END**")

#    content = request.json
#    age = request.json['age']
#    print(age)

    
       

news1 = ['Specter of Trump Loosens Tongues, if Not Purse Strings, in Silicon Valley - The New York Times'
            ,'David Streitfeld'
            ,'adasd']

def model_result(news):
  
        import joblib
        from sklearn.feature_extraction.text import TfidfVectorizer
        from numpy import load
        # load array
        X1 = load('model/data.npy',allow_pickle=True)
        model_l = joblib.load('model/fake_news_model.sav')

        vectorizer = TfidfVectorizer()
        vectorizer.fit(X1)
        X_new = vectorizer.transform(news)

        prediction = model_l.predict(X_new)
        #print(prediction)

        if (prediction[0]==0):
            print('The news is Real')
            return True
        else:
            print('The news is Fake')
            return False






if __name__ == "__main__":
    app.run(debug=True)