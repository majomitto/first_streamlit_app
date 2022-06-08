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

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#pick some fruits with default
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choise):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruitivice fruit advice")
try:
  fruit_choise=streamlit.text_input('What fruit you wand to chose?')
  if not fruit_choise:
    streamlit.error("Please select a fruit to get info")
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choise))
    
except URLError as e:
  streamlit,error()

streamlit.header("Get list from snowflake")
def get_fruit_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
    return my_cur.fetchall()
  
#add button to load the fruit
if streamlit.button('Get fruit load list')
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_list()
  streamlit.dataframe(my_data_rows)


add_fruit=streamlit.text_input('What fruit you want to add?','Jackfruit')
streamlit.write('The user entered',add_fruit)
