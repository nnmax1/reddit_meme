import sqlite3 
import random, string
from sqlite3 import Error


class MemeDatabase :
    def __init__(self):
        self.database = "db/memes.db"
    def set_db(self, db):
        self.database = db

    def generateMemeId(self): 
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        return x

    def validateMeme(self, id):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        curr = c.execute("SELECT * from memes")
        for row in curr:
            if row[0] == id: 
                return False
        return True
    
    # create a connection to a SQLite db
    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database)
            #print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
            
    # create a table to store memes
    def create_table(self):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        #create table
        c.execute('''CREATE TABLE memes
            (id,title,author,subreddit,img,postLink,published)''')
	    #commit the changes to db			
        conn.commit()
        #close the connection
        conn.close()
    # insert data into memes table
    def add_data(self,r):
        conn = sqlite3.connect(self.database)
        id_str = self.generateMemeId()
        while not self.validateMeme(id_str):
            id_str = self.generateMemeId()
        with conn:
            # insert meme into database i
            meme = (id_str, r['title'], r['authors'][0]['name'], r['subreddit'], r['img'], r['postLink'], r['published'])
            sql = '''INSERT INTO memes(id,title,author,subreddit,img,postLink,published ) VALUES(?,?,?,?,?,?,?) '''
            cur = conn.cursor()
            cur.execute(sql, meme)
            conn.commit()
        conn.close()
    # retrieve data from memes tables
    def get_data(self):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.execute('SELECT * FROM memes')
        data = c.fetchall()
        response = {"data": data}
        c.close
        conn.close()
        return response
    # delete memes from memes table
    def delete_data(self):
        conn = sqlite3.connect(self.database)
        sql = 'DELETE FROM memes'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

