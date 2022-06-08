import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#pick some fruits with default
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruitivice fruit advice")
try:
  fruit_choise=streamlit.text_input('What fruit you wand to chose?')
  if not fruit_choise:
    streamlit.error("Please select a fruit to get info")
  else:
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
  streamlit,error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("FRUIT_LOAD_LIST")
streamlit.dataframe(my_data_rows)

add_fruit=streamlit.text_input('What fruit you want to add?','Jackfruit')
streamlit.write('The user entered',add_fruit)
