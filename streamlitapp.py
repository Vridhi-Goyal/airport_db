'''APP'''
import psycopg2
import streamlit as st 
import pandas as pd
from passenger_db import delete_passenger_ssn

global ROLE
ROLE = 'casual'

def passenger(new_user):
    '''Passenger Table UI'''
    if new_user == 'admin':
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = 'postgres',
            password = 'gautham1234'
        )
    elif new_user == '':
        st.subheader('please choose a user to display')
        return
    else:
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = new_user
        )
    st.header('Passengers')
    cur = con.cursor()
    try:
        cur.execute('select * from passenger')
        p = cur.fetchall()
        p = pd.DataFrame(p)
        tableref = st.empty()
        tableref.dataframe(p)
        form = st.radio('',['update', 'new booking', 'cancellations'])
        with st.container():
            if form == 'new booking':
                st.subheader('new booking')
                fname = st.text_input('', key='ins_fname', placeholder='passenger first name')
                st.button('confirm booking ?')
            
            if form == 'cancellations':
                st.subheader('cancellations')
                delid = st.text_input('', key='delpass_ssn', placeholder='enter ssn of passenger')
                st.button('Delete ?', on_click=delete_passenger_ssn(delid, con))
            
            if form == 'update':
                st.subheader('update')
                st.button('update ?')
        return
    except psycopg2.errors.InsufficientPrivilege as e:
        st.write(f'insufficient permissions for user: {new_user}')
        st.caption(f'{str(e)}')
        return
    finally:
        cur.execute('select * from passenger;')
        p = cur.fetchall()
        tableref.dataframe(p)
        cur.close()
        con.commit()
        con.close()

def crew(new_user):
    st.subheader('Crew')
    if new_user == 'admin':
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = 'postgres',
            password = 'gautham1234'
        )
    else:
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = new_user
        )
    cur = con.cursor()
    try:
        cur.execute('select * from crew')
        c = cur.fetchall()
        st.dataframe(c)
    except psycopg2.OperationalError as e:
        st.caption(e)
    finally:
        con.commit()
        cur.close()
        con.close()

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
    '''Login using role new_user'''
    try:
        if new_user == 'admin':
            con = psycopg2.connect(
                host = 'localhost',
                database = 'airport_db',
                user = 'postgres',
                password = 'gautham1234'
            )
            con.close()
            st.sidebar.caption('\tlogged in as admin')
            return True
        
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = new_user
        )
        ROLE = new_user
        st.sidebar.caption('\tlogged in as ' + ROLE)
        con.close()
        return
    except psycopg2.OperationalError as e:
        st.sidebar.caption('\tnot logged in')
        return


title = st.container()
title.title('Welcome to airport_db')
option = st.sidebar.selectbox('Choose user', options=('', 'atc', 'security', 'admin', 'scheduler'))
ref = st.container()
login(option)
page = st.sidebar.selectbox('Choose page', options=('flight', 'passenger', 'crew'))
with ref:
    if page == 'flight':
        st.header('Flight Schedule ✈️ ')
        schedule()
    if page == 'passenger':
        passenger(option)
    if page == 'crew':
        crew(option)
