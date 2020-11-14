import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from Recommender import News_Outlet_Recommender

#style rendering through HTML

Body_html = """
  <style>
  h1{
    color: #E6E6FA;
  }
  h2{
    color: #f73448;

  }
  h3{
    color: #E6E6FA;
  }
  h4{
    color: #E6E6FA;
  }
  h5{
    color: #E6E6FA;
  }

    body{
    color: #E6E6FA;
    background-color: #1c1c1c;
}
}



}
</style>
"""
st.markdown(Body_html, unsafe_allow_html=True)


#app text rendering
st.markdown(
'''
# Digital News Subscription Recommender
#### *Find your perfect news source, based on your interests...*'''
)

st.markdown('''### On a scale of 0% to 100%, how interested are you in reading about the subjects below?
#''')

st.markdown('''#### COVID-19''')
st.write('ie. pandemic impact, COVID-19 spread, vaccine research, global lockdown.')
covid = st.slider('',0, 100 , 50, format="%d percent")
st.write("You're ", covid, '%', 'interested in reading about COVID-19.')


st.markdown('''#
#### Staying At Home''')
st.write('ie. working from home, education, parenting.')
home = st.slider(' ', 0, 100 , 50, format="%d percent")
st.write("You're ", home, '%', 'interested in reading about staying at home.')

st.markdown('''#
#### U.S. Politics''')
st.write('ie. Trump, Biden, elections, Supreme Court.')
us_politics = st.slider('  ', 0, 100 , 50, format="%d percent")
st.write("You're ", us_politics, '%', 'interested in reading about U.S. politics.')

st.markdown('''#
#### Global Politics''')
st.write('ie. China, Brexit & European Union, Hong Kong protests.')
global_politics = st.slider('   ', 0, 100 , 50, format="%d percent")
st.write("You're ", global_politics, '%', 'interested in reading about global politics.')

st.markdown('''#
#### Global Economy''')
st.write('ie. economic analysis, (un)employeement.')
economy = st.slider('    ', 0, 100 , 50, format="%d percent")
st.write("You're ", economy, '%', 'interested in reading about global economy.')

st.markdown('''#
#### Social Issues''')
st.write('ie. police brutality, gender equality, climate change.')
social = st.slider('     ', 0, 100 , 50, format="%d percent")
st.write("You're ", social, '%', 'interested in reading about social issues.')

st.markdown('''#
#### Business''')
st.write('ie. business news, stock market, technology.')
business = st.slider('      ', 0, 100 , 50, format="%d percent")
st.write("You're ", business, '%', 'interested in reading about business.')

st.markdown('''#
#### Personal Development''')
st.write('ie. health & wellness, self help, personal finance.')
personal = st.slider('       ', 0, 100 , 50, format="%d percent")
st.write("You're ", personal, '%', 'interested in reading about personal development.')

st.markdown('''#
#### Hobbies''')
st.write('ie. cars.')
cars = st.slider('        ',0, 100 , 50, format="%d percent")
st.write("You're ", cars, '%', 'interested in reading about hobbies.')


outlet_df = pd.read_csv('outlet_df.csv', index_col = 0 )
#st.dataframe(df)

recommendation = News_Outlet_Recommender(outlet_df, covid/50, home/50, us_politics/50, global_politics/50, economy/50, social/50, business/50, personal/50, cars/50)


st.write('''
#
### *Based off your interests, we recommend that you subscribe to:*
##''', recommendation)


st.markdown(
'''
#
#
More details:

[Github](https://github.com/JuliaQiao/NLP_News_Recommender)

[LinkedIn](https://www.linkedin.com/in/juliaqiao/)
#'''
)
