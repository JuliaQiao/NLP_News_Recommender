import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#outlet_df = pd.read_pickle('outlet_df.pickle')

def News_Outlet_Recommender(outlet_df, Covid = 1, Staying_at_Home = 1, US_Politics = 1, Global_Politics = 1, Global_Economy = 1, Social_Issues = 1, Business = 1, Personal_Development =1, Hobbies=1):

    """
    Takes in weights for each news theme and returns recommended news outlet based on topics behind each theme.
    """

    #define themes for our topics
    Covid_topics = ['Pandemic_Impact','Covid_Spread', 'Covid_Vaccine', 'Global_Lockdown']
    Staying_at_Home_topics = ['Work_From_Home', 'Education', 'Parenting']
    US_Politics_topics = ['Trump', 'Biden', 'US_Election', 'US_Supreme_Court']
    Global_Politics_topics = ['China', 'Brexit_EU', 'Hong_Kong']
    Global_Economy_topics = ['Economy', '(Un)employeement']
    Social_Issues_topics = ['Police_Protests', 'Gender_Equality', 'Climate_Change']
    Business_topics = ['Business', 'Stock_Market', 'Technology' ]
    Personal_Development_topics = [ 'Health_Wellness', 'Self-Help', 'Personal_Finance']
    Hobbies_topics = ['Cars']

    #define our average tweet
    average_tweet  = outlet_df.describe().iloc[1]

    #find each topic using the topic themes and multiply the average tweet's topic coefficient by the user weights, averaged out across theme.
    for i in average_tweet.index:
        if str(i) in Covid_topics:
            weight = Covid/len(Covid_topics)
        elif str(i) in Staying_at_Home_topics:
            weight = Staying_at_Home/len(Staying_at_Home_topics)
        elif str(i) in US_Politics_topics:
            weight = US_Politics/len(US_Politics_topics)
        elif str(i) in Global_Politics_topics:
            weight = Global_Politics/len(Global_Politics_topics)
        elif str(i) in Global_Economy_topics:
            weight = Global_Economy/len(Global_Economy_topics)
        elif str(i) in Social_Issues_topics:
            weight = Social_Issues/len(Social_Issues_topics)
        elif str(i) in Business_topics:
            weight = Business/len(Business_topics)
        elif str(i) in Personal_Development_topics:
            weight = Personal_Development/len(Personal_Development_topics)
        elif str(i) in Hobbies_topics:
            weight = Hobbies
        else:
            weight = 1

        #apply weights to each average tweet topic coefficient, transforming vector into one that contains user topic preferences
        average_tweet[str(i)] = average_tweet[str(i)]*weight
        user_vector = average_tweet.values.reshape(1,-1)

    #compare the average tweet--now manipulated with user weights to be the user vector, to the outlet vectors in the dataframe
    similarity_matrix = []
    #computing the cosine similarity between each news vector( each row in outlet_df) and the user vector(average_tweet)
    similarity_matrix = cosine_similarity(outlet_df.iloc[:,1:], user_vector)

    #find the max index of list
    max_index = np.argmax(similarity_matrix)
    #use max index to find its referred outlet
    similar_outlet = outlet_df.iloc[max_index, 0]

    #return the outlet with the highest cosine similarity to our user vector
    return similar_outlet
