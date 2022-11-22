import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Bakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index('Fruit')

# Creating a pick list so they can pick the fruit they want to include

streamlit.multiselect('Pick up some fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)

