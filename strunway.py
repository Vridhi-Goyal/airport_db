import psycopg2
import streamlit as st 
import pandas as pd
from passenger_db import delete_passenger_ssn

#delete entry on runs_on
#
def runwaypage():

        con = psycopg2.connect(
                host = "localhost",
                database="airport_db",
                user="postgres",
                password="vridhi"
        )
        cur=con.cursor()

        st.title("Runway Details")
        st.header(" Header ")

        #st.sidebar.write("Sidebar")
        #option = st.sidebar.selectbox("Which Department?", ('Cabin crew','Ground','Security Team','Service','Operations'))
        #st.subheader(option)

        with st.expander('View Runway Details'):
            cur.execute("select * from runway")
            counts=cur.fetchall()
            #for i in counts:
             #   st.write(i)
            df=pd.DataFrame(
                counts,columns=['r_id','length'])
            st.dataframe(df)

        with st.expander("Insert new runway details"):
            with st.form(key="f1",clear_on_submit=True):

                rid = st.text_input(label="r_id")
                rlen= st.text_input(label='Enter length')
                submit = st.form_submit_button(label="Submit")
            if rid and rlen:
                record_to_insert = [rid,rlen]
                cur.execute("INSERT INTO runway VALUES(%s,%s)", record_to_insert)
                con.commit()
                st.balloons()

        with st.expander("Update runway details"):
            sql = "UPDATE RUNWAY"
            df=pd.DataFrame(
                counts,columns=['r_id','length'])
            df['r_id'].add('Runway id')
            #st.dataframe(df)
            with st.form(key="f2",clear_on_submit=True):
                opt = st.selectbox("Which runway details would you like to update? ",[i for i in df['r_id']])
                #opt2 = st.selectbox('Select field to update',['Select','destination', 'airline_id', 'gateno'])
                inp = st.text_input(label='Enter the new value of length')
                submit2 = st.form_submit_button(label='Submit')
            
            cur.execute(sql+" SET ='length"+inp.split()[0]+"'r_id="+str(opt[0]),(inp.split()[0],inp.split()[1],(opt[0])))
            con.commit()
            st.balloons()
            
        """   
        with st.expander('Delete flight data'):
            sql = "DELETE FROM FLIGHT"
            df=pd.DataFrame(
                counts,columns=['flight_id','no_of_seats','destination', 'airline_id', 'gateno'])
            df['flight_id'].add('flight id')
            with st.form(key="f3",clear_on_submit=True):
                opt3 = st.selectbox("Which flight_id details do you want to delete?",[i for i in df['flight_id']])
                submit = st.form_submit_button(label='Submit')
            cur.execute(sql+' where id='+str(opt3[0]))
            con.commit()
        """
        cur.close()
        con.close() 

