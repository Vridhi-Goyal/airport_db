'''Passenger operations'''
import streamlit as st
import pandas as pd
import psycopg2 as psql

def delete_passenger_ssn(ssn, con):
    '''delete from passenger where ssn=ssn'''
    if ssn != '':
        cur = con.cursor()
        try:
            cur.execute(f'delete from luggage where pass_ssn={ssn};')
            cur.execute(f'delete from passenger where ssn={ssn};')
            st.write(f'deleted passenger ssn {ssn}')
            return
        except psql.errors.UndefinedColumn as e:
            st.write(str(e))
            return
        finally:
            cur.close()
