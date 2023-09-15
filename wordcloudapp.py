import streamlit as st
import os
from os import path
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords




# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = st.text_area('Write your article')

# Read the whole text.
#text = open(path.join(d, 'article.txt')).read()
stopwords = stopwords.words('english')


# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
# lower max_font_size
# Specify a font for Matplotlib
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
# Define a TrueType font file (you can change this to your preferred font)
font_path = path.join(d, 'Roboto-Light.ttf')
wordcloud = WordCloud(font_path=font_path, stopwords=stopwords).generate(text)
st.image(wordcloud.to_array(), use_column_width=True)
