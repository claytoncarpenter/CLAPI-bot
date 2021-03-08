import sqlite3
import pandas as pd

pd.options.display.max_colwidth = 100

def query(sql, params=None):
        try:
                with sqlite3.connect(r'database\discord.db') as con:
                        df = pd.read_sql_query(sql , con, params=params)
                        return df
        except:
                print('Failed to query SQLite Database')

def insert_message(id, author, author_id, bot, content, guild, channel, created_at):
        try:
                with sqlite3.connect(r'database\discord.db') as con:
                        cur = con.cursor()
                        cur.execute("INSERT INTO messages (message_id, author, author_id, bot, content, guild, channel, created_at) VALUES (?,?,?,?,?,?,?,?)",(id, author, author_id, bot, content, guild, channel, created_at))
                        con.commit()
        except:
                print('Error inserting message to database')

if __name__ == '__main__':
        con = sqlite3.connect(r'database\discord.db')
        cur = con.cursor()
        #cur.execute("""DROP TABLE messages""")
        cur.execute("""CREATE TABLE IF NOT EXISTS messages (message_id PRIMARY KEY, author, author_id, bot, content, guild, channel, created_at)""")
        
        query("SELECT * FROM messages")

        





