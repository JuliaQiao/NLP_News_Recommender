import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from Recommender import News_Outlet_Recommender

st.markdown(
'''
# Digital News Subscription Recommender
#### *Find your perfect news source, based on your interests...*'''
)

st.markdown('''### On a scale of 0% to 100%, how interested are you in reading about the subjects below?
#''')

st.markdown('''#### COVID-19''')
covid = st.slider('ie. pandemic impact, COVID-19 spread, vaccine research, global lockdown.', 0, 100 , 50, format="%d percent")
st.write("You're ", covid, '%', 'interested in reading about COVID-19.')


st.markdown('''#
#### Staying At Home''')

home = st.slider('ie. working from home, education, parenting.', 0, 100 , 50, format="%d percent")
st.write("You're ", home, '%', 'interested in reading about Staying at Home.')

st.markdown('''#
#### U.S. Politics''')
us_politics = st.slider('ie. Trump, Biden, elections, Supreme Court.', 0, 100 , 50, format="%d percent")
st.write("You're ", us_politics, '%', 'interested in reading about U.S. Politics.')

st.markdown('''#
#### Global Politics''')
global_politics = st.slider('ie. China, Brexit & European Union, Hong Kong protests.', 0, 100 , 50, format="%d percent")
st.write("You're ", global_politics, '%', 'interested in reading about Global Politics.')

st.markdown('''#
#### Global Economy''')
economy = st.slider('ie. economic analysis, (un)employeement.', 0, 100 , 50, format="%d percent")
st.write("You're ", economy, '%', 'interested in reading about Global Economy.')

st.markdown('''#
#### Social Issues''')
social = st.slider('ie. police brutality, gender equality, climate change.', 0, 100 , 50, format="%d percent")
st.write("You're ", social, '%', 'interested in reading about Social Issues.')

st.markdown('''#
#### Business''')
business = st.slider('ie. business news, stock market, technology.', 0, 100 , 50, format="%d percent")
st.write("You're ", business, '%', 'interested in reading about Business.')

st.markdown('''#
#### Personal Development''')
personal = st.slider('ie. health & wellness, self help, personal finance.', 0, 100 , 50, format="%d percent")
st.write("You're ", personal, '%', 'interested in reading about Personal Development.')

st.markdown('''#
#### Cars''')
cars = st.slider('',0, 100 , 50, format="%d percent")
st.write("You're ", cars, '%', 'interested in reading about Cars.')


outlet_df = pd.read_csv('outlet_df.csv', index_col = 0 )
#st.dataframe(df)

recommendation = News_Outlet_Recommender(outlet_df, covid/50, home/50, us_politics/50, global_politics/50, economy/50, social/50, business/50, personal/50, cars/50)


#st.markdown('''
            #based off recommendation''')

#st.write(recommendation)

st.write('''
#
### *Based off your interests, we recommend that you subscribe to:*
#''', recommendation)

#st.write(recommendation)




st.markdown(
'''
#
#
More details on this recommender:

[Github](https://github.com/JuliaQiao/NLP_News_Recommender)

[LinkedIn](https://www.linkedin.com/in/juliaqiao/)
#'''
)

#st.write(
#f'Predicted Sale Price of House: ${pred:.2f}'
#
