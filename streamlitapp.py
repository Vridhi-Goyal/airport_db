'''APP'''
import psycopg2
import streamlit as st 
import pandas as pd

global user
user = None

def schedule():
    '''
        Landing page for flight schedule
        !!set password to your postgres user password!!
    '''
    con = psycopg2.connect(
        host = 'localhost',
        database = 'airport_db',
        user = 'postgres',
        password = 'gautham1234'
    )
    cur = con.cursor()
    cur.execute('select * from flight natural join airline')
    sched = cur.fetchall()
    sched = pd.DataFrame(sched).drop(columns=[0, 1, 2, 4])
    sched.columns = ['Destination', 'Airline']
    st.table(sched)
    cur.close()
    con.close()


def login(new_user):
    '''
        gets the user logged in and updates caption and sets global user value
    '''
    if new_user == 'admin':
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = 'postgres',
            password = 'gautham1234'
        )
        con.close()
        st.caption('logged in as admin')
        return True
    try:
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = new_user
        )
        con.close()
        user = new_user
        st.caption('logged in as ' + user)
        return True

    except psycopg2.OperationalError as e:
        st.caption('not logged in')
        return False


st.title('Welcome to airport_db')
option = st.sidebar.selectbox('Choose user', options = ('atc','security','admin', 'scheduler'))
login(option)
st.header('Flight Schedule')
schedule()
