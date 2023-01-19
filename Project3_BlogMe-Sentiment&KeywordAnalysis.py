import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('articles.xlsx')
data.info()

#counting number of article from source name
#format of groupby: df.groupby(['column_to_group])['column_to_count'].count()
source_category = data.groupby(['source_name'])['article_id'].count().sort_values(ascending=True)
source_category.plot.bar(color='green', width = 0.3)
plt.show()

#counting number of reaction from publisher
publisher_numbers_reaction = data.groupby(['source_name'])['engagement_reaction_count'].sum().sort_values(ascending=True)

#dropping column
data = data.drop('engagement_comment_plugin_count', axis=1)

#creating keyword count by using def, for loop, and if statement
#simple 
keyword = 'crash'
keyword_flag = []
for x in range (0,10):
    heading = data['title'][x]
    if keyword in heading:
       flag = 1
    else:
       flag = 0
    keyword_flag.append(flag) 

#complete def
length = len(data)
keyword_flag = []

def keywordflag(keyword):
    for x in range (0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
               flag = 1
            else:
               flag = 0
        except:
            flag = 0
        keyword_flag.append(flag) 
    return keyword_flag

#change into series
keywordflag = pd.Series(keywordflag('murder'))

#adding keywordflag to data
data['keywordflag'] = keywordflag


##import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][5988]
sent = sent_int.polarity_scores(text)

#extract neg, pos, neu into spesific column
neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)

for x in range (0, length):
    try: 
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

#change datatype list into series
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

#adding column
data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#export to excel
data.to_excel('Project3_BlogMe-Sentiment&KeywordAnalysis.xlsx', sheet_name='blogmedata', index=False)










