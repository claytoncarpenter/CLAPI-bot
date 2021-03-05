import sqlite3
import pandas as pd

def all_messages():
        df = pd.read_sql_query("SELECT * FROM messages", con)
        print(df)

def insert(id, author, author_id, content, guild, channel, created_at):
        with sqlite3.connect(r'database\discord.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO messages (message_id, author, author_id, content, guild, channel, created_at) VALUES (?,?,?,?,?,?,?)",(id, author, author_id, content, guild, channel, created_at))
                con.commit()

if __name__ == '__main__':
        con = sqlite3.connect(r'database\discord.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS messages (message_id PRIMARY KEY, author, author_id, content, guild, channel, created_at)""")
        #cur.execute("""DROP TABLE messages""")
        all_messages()

        





