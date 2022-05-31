import streamlit

streamlit.title("My parents healthy dinner")

streamlit.header('Breakfast favourite')
streamlit.text('🥣 Omega 3 & Blueberry otmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#list for picking a fruit
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#dispaly the table on the page
#streamlit.dataframe(my_fruit_list)

#list for the picked fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input("What fruit would you like information about?", "Kiwi")
streamlit.write("The user entered", fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it screen as a table
streamlit.dataframe(fruityvice_normalized)

# stremlit stop
streamlit.stop()
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_rows)

streamlit.header('Smoothie is getting ready')
add_my_fruit = streamlit.text_input("What fruit would you like to add", "Kiwi")
streamlit.write("The user's choice", add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
