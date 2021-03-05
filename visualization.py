import database
import pandas as pd

df = database.query("SELECT * FROM messages")
print(df['content'])