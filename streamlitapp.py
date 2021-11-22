'''APP'''
import psycopg2
import streamlit as st 
import pandas as pd
from passenger_db import delete_passenger_ssn

global ROLE
ROLE = 'casual'

def passenger(new_user, pw):
    '''Passenger Table UI'''
    if new_user == 'admin':
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = 'postgres',
            password = pw
        )
    elif new_user == '':
        st.subheader('please choose a user to display')
        return
    else:
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = pw
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
        st.error(e)
        return
    finally:
        cur.execute('select * from passenger;')
        p = cur.fetchall()
        tableref.dataframe(p)
        cur.close()
        con.commit()
        con.close()

def crew(new_user, pw):
    st.subheader('Crew')
    if new_user == 'admin':
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = 'postgres',
            password = pw
        )
    else:
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = pw
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

def login(new_user, pw):
    '''Login using role new_user'''
    try:
        if new_user == 'admin':
            con = psycopg2.connect(
                host = 'localhost',
                database = 'airport_db',
                user = 'postgres',
                password = pw
            )
            con.close()
            st.sidebar.caption('\tlogged in as admin')
            st.balloons()
            return True
        
        con = psycopg2.connect(
            host = 'localhost',
            database = 'airport_db',
            user = new_user,
            password = pw
        )
        ROLE = new_user
        st.sidebar.info('\tlogged in as ' + ROLE)
        con.close()
        st.balloons()
        return True
    except psycopg2.OperationalError as e:
        st.sidebar.warning('\tnot logged in')
        st.error(e)
        return False


title = st.container()
title.title('Welcome to airport_db')
with st.sidebar.form(key='loginform', clear_on_submit=False):
    option = st.sidebar.selectbox('Choose user', options=('', 'atc', 'security', 'admin', 'scheduler'), key='username')
    passw = st.sidebar.text_input('password',placeholder=f'enter password for {option}', type='password')
    st.sidebar.button('sign in', key='login')
ref = st.container()
login(option, passw)
page = st.sidebar.selectbox('Choose page', options=('flight', 'passenger', 'crew'))
with ref:
    if passw == '' or option == '':
        st.subheader('please enter password and username')
    else:
        try:
            if page == 'flight':
                st.header('Flight Schedule ✈️ ')
                schedule()
            if page == 'passenger':
                passenger(option, passw)
            if page == 'crew':
                crew(option, passw)
        except psycopg2.errors.InFailedSqlTransaction as e:
            pass
        except psycopg2.OperationalError:
            pass
        except psycopg2.errors.InsufficientPrivileges:
            pass
