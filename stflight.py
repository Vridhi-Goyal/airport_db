import psycopg2
import streamlit as st 
import pandas as pd
from passenger_db import delete_passenger_ssn

#delete entry on runs_on
#
def flightpage():

        con = psycopg2.connect(
                host = "localhost",
                database="airport_db",
                user="postgres",
                password="vridhi"
        )
        cur=con.cursor()

        st.title("Flight Details")
        st.header(" Header ")

        #st.sidebar.write("Sidebar")
        #option = st.sidebar.selectbox("Which Department?", ('Cabin crew','Ground','Security Team','Service','Operations'))
        #st.subheader(option)

        with st.expander('View Flight Details'):
            cur.execute("select * from flight")
            counts=cur.fetchall()
            #for i in counts:
             #   st.write(i)
            df=pd.DataFrame(
                counts,columns=['flight_id','no_of_seats','destination', 'airline_id', 'gateno'])
            st.dataframe(df)

        with st.expander("Insert new flight details"):
            with st.form(key="f1",clear_on_submit=True):

                fid = st.text_input(label="flight_id")
                nseats = st.text_input(label='Enter no of seats')
                ddest = st.text_input(label='Enter destination')
                aid = st.text_input(label="Enter airline id")
                gno = st.text_input(label="Enter gateno")
                submit = st.form_submit_button(label="Submit")
            if fid and nseats and ddest and aid and gno:
                record_to_insert = [fid,nseats,ddest,aid,gno]
                cur.execute("INSERT INTO Flight VALUES(%s,%s,%s,%s,%s)", record_to_insert)
                con.commit()
                st.balloons()

        with st.expander("Update member details"):
            sql = "UPDATE FLIGHT"
            df=pd.DataFrame(
                counts,columns=['flight_id','no_of_seats','destination', 'airline_id', 'gateno'])
            #st.dataframe(df)
            with st.form(key="f2",clear_on_submit=True):
                opt = st.selectbox("Which flight details would you like to update? ",[i for i in df['flight_id']])
                opt2 = st.selectbox('Select field to update',['Select','destination', 'airline_id', 'gateno'])
                inp = st.text_input(label='Enter the new value')
                submit2 = st.form_submit_button(label='Submit')
            if opt2 == 'destination':
                cur.execute(sql+" SET destination='"+inp.split()[0]+"'where flight_id="+str(opt[0]),(inp.split()[0],inp.split()[1],(opt[0])))
                con.commit()
                st.balloons()
            if opt2 == 'airline_id':
                cur.execute(sql+" SET airline_id='"+inp.split()[0]+"'where flight_id="+str(opt[0]),(inp.split()[0],inp.split()[1],(opt[0])))
                con.commit()
                st.balloons()
            if opt2 == 'gateno':
                cur.execute(sql+" SET getno='"+inp.split()[0]+"'where flight_id="+str(opt[0]),(inp.split()[0],inp.split()[1],(opt[0])))
                con.commit()
                st.balloons()
        """  
        with st.expander('Delete flight data'):
            sql = "DELETE FROM FLIGHT"
            df=pd.DataFrame(
                counts,columns=['flight_id','no_of_seats','destination', 'airline_id', 'gateno'])
            #df['flight_id'].add('flight id')
            with st.form(key="f3",clear_on_submit=True):
                opt3 = st.selectbox("Which flight_id details do you want to delete?",[i for i in df['flight_id']])
                submit = st.form_submit_button(label='Submit')
            cur.execute(sql+' where id='+str(opt3[0]))
            con.commit()
        """
        cur.close()
        con.close() 

