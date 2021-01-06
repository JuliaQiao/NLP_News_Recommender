def preprocess(tweet):
    """
    Takes in tweet and performs initial text cleaning/preprocessing.
    """
    #make sure doc is string
    tweet=str(tweet)
    #get rid of urls
    rem_url=re.sub(r'http\S+', '', tweet)
    #gets rid of @ tags
    rem_tag = re.sub('@\S+', '', rem_url)
    #gets rid of # in hashtag but keeps content of hashtag
    rem_hashtag = re.sub('#', '', rem_tag)
    #gets rid of apostrophes 
    rem_apos = re.sub("'.\S", '', rem_hashtag)
    rem_apos_0 = re.sub("’.\S", '', rem_apos)
    rem_apos_1 = re.sub("'\S", '', rem_apos_0)
    rem_apos_2 = re.sub("’\S", '', rem_apos_1)
    #gets rid of special characters, numbers, etc.
    clean_text = re.sub(r'[^A-Za-z\s]','', rem_apos_2)

    return clean_text

def english_only(x):
    """
    Take tweet, detect language, and only return English tweets, coding foreign language tweets as NaNs.
    """
    try:
        if detect(x) == 'en':
            return x
        else:
            return np.nan
    except:
        pass

def noun_lemmatize_pipe(doc):
    """
    Takes in tweet and returns only the lemmatized version of nouns (including proper nouns).
    """
    lemma_list = [token.lemma_.lower() for token in doc if token.pos_ == "NOUN" or token.pos_ =="PROPN"] 
    return lemma_list

#create a pipeline in order to shorten processing time
def preprocess_pipe(texts):
    """
    Inputs noun_lemmative_pipe function into NLP pipeline for faster processing.
    """
    preproc_pipe = []
    for doc in nlp.pipe(texts, batch_size=50):
        preproc_pipe.append(noun_lemmatize_pipe(doc))
    return preproc_pipe

def display_topics(model, feature_names, no_top_words, topic_names=None):
    """
    Takes in model, features and displays n number of top topics from model.
    """
    for idx, topic in enumerate(model.components_):
        if not topic_names or not topic_names[idx]:
            print("\nTopic ", idx)
        else:
            print("\nTopic: '",topic_names[idx],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

def top_tweets(tweet_topic_matrix_df, topic, n_tweets):
    """
    Takes in tweet_topic_matrix, the topic, and displays n number of top tweets from that topic.
    """
    return (tweet_topic_matrix_df
            .sort_values(by=topic, ascending=False)
            .head(n_tweets)['content']
            .values)

def top_words(word_topic_matrix_df, topic, n_words):
    """
    Takes in word_topic_matrix, the topic, and displays n number of top words from that topic.
    """
    return (word_topic_matrix_df
            .sort_values(by=topic, ascending=False)
            .head(n_words))[topic]
