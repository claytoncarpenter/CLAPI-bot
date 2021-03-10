import database
import pandas as pd
import matplotlib.pyplot as plt

def bar_plot(serv):
    try:
        data = database.query("SELECT * FROM messages WHERE guild = (?)", {serv})
        print(data)
    except:
        print('Error calling query from database')
    else:
        # plt.style.use('fivethirtyeight')

        # x_values = []
        # y_values = []

        # index = count()


        fig = plt.figure()
        fig.set_size_inches(15,15)
        grouped_data = data.groupby(by='author').describe()
        print(grouped_data)
        x_values = grouped_data.index
        y_values = grouped_data['message_id']['count']
        plt.bar(x_values, y_values)
        plt.xlabel('Author')
        plt.ylabel('Number of Comments')
        plt.title('Discord Posts')
        plt.xticks(rotation = 45)
        #plt.show()
        fig.savefig(r'plots\barplot.png')
        plt.clf()
        # pass



def table_plot():
    try:
        classics = 'The Classics'
        data = database.query("SELECT * FROM messages") #WHERE guild = (?)", {classics})
    except:
        print('Error calling query from database')
    else:
        # plt.style.use('fivethirtyeight')

        # x_values = []
        # y_values = []

        # index = count()
        data = data.groupby(by='author').describe()
        print(data['content'])
        fig, ax = plt.subplots()

# hide axes
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')


        ax.table(cellText=data.values, colLabels=data.columns, loc='center')

        fig.tight_layout()

        # fig = plt.figure()
        fig.set_size_inches(15,15)
        # grouped_data = data.groupby(by='author').describe()
        # print(grouped_data)
        # x_values = grouped_data.index
        # y_values = grouped_data['message_id']['count']
        # plt.bar(x_values, y_values)
        # plt.xlabel('Author')
        # plt.ylabel('Number of Comments')
        # plt.title('Discord Posts')
        # plt.xticks(rotation = 45)
        # #plt.show()
        fig.savefig(r'plots\tableplot.png')
        plt.clf()
        # pass

