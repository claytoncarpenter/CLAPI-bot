import database
import pandas as pd
import matplotlib.pyplot as plt

def plot():
    classics = 'The Classics'
    data = database.query("SELECT * FROM messages WHERE guild = (?)", {classics})
    #print(data)
    print(data.guild.unique())

    # plt.style.use('fivethirtyeight')

    # x_values = []
    # y_values = []

    # index = count()


    fig = plt.figure()
    fig.set_size_inches(15,15)
    grouped_data = data.groupby(by='author').describe()
    #print(grouped_data)
    x_values = grouped_data.index
    y_values = grouped_data['message_id']['count']
    plt.bar(x_values, y_values)
    plt.xlabel('Author')
    plt.ylabel('Number of Comments')
    plt.title('Discord Posts')
    plt.xticks(rotation = 45)
    #plt.show()
    # fig.savefig(r'static\plot.png')
    # pass

plot()