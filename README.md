# Tweet Depression Detection


## Motivation 💡
The Tweet Depression Detection project aims to create a machine learning model that can classify tweets as either "normal" or "depressive." As depression becomes an increasingly important topic in mental health, social media platforms such as Twitter provide a unique opportunity to study and potentially identify individuals at risk of depression 📈. By analyzing large amounts of tweet data, I hope to develop a model that can accurately classify tweets and provide insights into how individuals express depressive symptoms on social media. 💭


## Dataset 📊
For this project, I will be using two datasets: the Sentiment140 dataset and a dataset of depressive tweets scraped by Twint.

The Sentiment140 dataset https://www.kaggle.com/datasets/kazanova/sentiment140 contains 1.6 million tweets. While this dataset is not specifically designed for detecting depression, I will use a subset of this dataset containing approximately 8000 to 10,000 randomly sampled tweets for our "normal" tweet class.

To create our "depressive" tweet class, we found a separate dataset of tweets that had been scraped by Twint using keywords related to depression https://github.com/eddieir/Depression_detection_using_Twitter_post/blob/master/depressive_tweets_processed.csv. This dataset contains approximately 4,000 tweets that have been labeled as depressive. 😞

## Data Processing 🤔

I will combine these two datasets to create a labeled dataset for training our machine learning model. By using these two datasets, I aim to create a model that can accurately distinguish between "normal" and "depressive" tweets, and potentially identify individuals who may be at risk of depression based on their social media activity. 💻

## Tools 🔧
Text Feature Extraction : TF-IDF and Word Counter

Classification Model : Support Vector Machine

## Sample Web UI (Tweet Predictor) 💻
Depressive Tweet:
![Image text](https://github.com/Jingxuan-Bao/Tweet_Depression_Detection/blob/a18d2508d04f108fd43d8d937f6d951da22c7381/image/depressive_tweet.png)

Normal Tweet:
![Image text](https://github.com/Jingxuan-Bao/Tweet_Depression_Detection/blob/a18d2508d04f108fd43d8d937f6d951da22c7381/image/normal_tweet.png)
