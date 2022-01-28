import pandas as pd
import numpy as np
import pandas_datareader as data
from datetime import date
import matplotlib.pyplot as plt
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
def stock1(df):
    # Create lists to store the returns of each day in that month
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    June = []
    July = []
    Aug = []
    Sept = []
    Oct = []
    Nov = []
    Dec = []

    # Create a function to get returns for each month and append it to the corresponding list
    def get_returns(month, returns):
        if month == '01':
            Jan.append(float(returns))
        elif month == '02':
            Feb.append(float(returns))
        elif month == '03':
            Mar.append(float(returns))
        elif month == '04':
            Apr.append(float(returns))
        elif month == '05':
            May.append(float(returns))
        elif month == '06':
            June.append(float(returns))
        elif month == '07':
            July.append(float(returns))
        elif month == '08':
            Aug.append(float(returns))
        elif month == '09':
            Sept.append(float(returns))
        elif month == '10':
            Oct.append(float(returns))
        elif month == '11':
            Nov.append(float(returns))
        elif month == '12':
            Dec.append(float(returns))
        else:
            print('Wrong')

    # calculate and show the daily simple returns
    DSR = df['Close'].pct_change(1)
    df['DSR'] = DSR

    # Remove first row of data from dataset
    df = df[1:]

    # create a loop to gather daily simple returns of each month from the dataset and append them to list
    for i in range(0, len(df)):
        df_date = str(df.index[i])
        df_returns = df['DSR'][i]
        df_month = df_date.split('-')[1]
        # add returns to list corresponding to month
        get_returns(df_month, df_returns)

    # create a function to average the returns of each month
    def AVG(month):
        return [sum(month) / len(month)]

    # Create new dataframe
    df_AVG = pd.DataFrame()
    # Get the average returns for each month and add the values under a new column 'AVG'
    df_AVG['AVG'] = AVG(Jan) + AVG(Feb) + AVG(Mar) + AVG(Apr) + AVG(May) + AVG(June) + AVG(July) + AVG(Aug) + AVG(
        Sept) + AVG(Oct) + AVG(Nov) + AVG(Dec)
    # set index to be the corresponding integer value of month
    df_AVG1 = df_AVG * 100
    df_AVG1['Month'] = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    df_AVG1 = df_AVG1.set_index(df_AVG1.index + 1)

    return df_AVG1





def stock2(df):
    # Create lists to store the returns of each day in that month
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    June = []
    July = []
    Aug = []
    Sept = []
    Oct = []
    Nov = []
    Dec = []

    # Create a function to get returns for each month and append it to the corresponding list
    def get_returns(month, returns):
        if month == '01':
            Jan.append(float(returns))
        elif month == '02':
            Feb.append(float(returns))
        elif month == '03':
            Mar.append(float(returns))
        elif month == '04':
            Apr.append(float(returns))
        elif month == '05':
            May.append(float(returns))
        elif month == '06':
            June.append(float(returns))
        elif month == '07':
            July.append(float(returns))
        elif month == '08':
            Aug.append(float(returns))
        elif month == '09':
            Sept.append(float(returns))
        elif month == '10':
            Oct.append(float(returns))
        elif month == '11':
            Nov.append(float(returns))
        elif month == '12':
            Dec.append(float(returns))
        else:
            print('Wrong')

    # calculate and show the daily simple returns
    DSR = df['Close'].pct_change(1)
    df['DSR'] = DSR

    # Remove first row of data from dataset
    df = df[1:]

    # create a loop to gather daily simple returns of each month from the dataset and append them to list
    for i in range(0, len(df)):
        df_date = str(df.index[i])
        df_returns = df['DSR'][i]
        df_month = df_date.split('-')[1]
        # add returns to list corresponding to month
        get_returns(df_month, df_returns)

    # create a function to average the returns of each month
    def AVG(month):
        return [sum(month) / len(month)]

    # Create new dataframe
    df_AVG = pd.DataFrame()
    # Get the average returns for each month and add the values under a new column 'AVG'
    df_AVG['AVG'] = AVG(Jan) + AVG(Feb) + AVG(Mar) + AVG(Apr) + AVG(May) + AVG(June) + AVG(July) + AVG(Aug) + AVG(
        Sept) + AVG(Oct) + AVG(Nov) + AVG(Dec)
    # set index to be the corresponding integer value of month
    df_AVG2 = df_AVG * 100
    df_AVG2['Month'] = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    df_AVG2 = df_AVG2.set_index(df_AVG2.index + 1)

    return df_AVG2



if __name__ == '__main__':
    # Load stock data
    start = '2019-09-15'
    user_input1 = st.text_input('Enter The Stock Ticker', 'AAPL')
    user_input2 = st.text_input('Enter The Stock Ticker', 'MSFT')
    df1 = data.DataReader(user_input1, 'yahoo', start, date.today())
    df2 = data.DataReader(user_input2, 'yahoo', start, date.today())
    aapl = stock1(df1)
    msft = stock2(df2)




    X = aapl['Month']
    Yaapl = aapl['AVG']
    Zmsft = msft['AVG']

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.2, Yaapl, 0.4, label=user_input1)
    plt.bar(X_axis + 0.2, Zmsft, 0.4, label=user_input2)

    plt.xticks(X_axis, X)
    plt.xlabel("Months")
    plt.ylabel("Daily Simple Return")
    plt.title("Monthly Performance comparision between "+user_input1+" & "+user_input2)
    plt.legend()
    ab = plt.show()
    st.pyplot(ab)
