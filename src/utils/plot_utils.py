import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter, MonthLocator
from wordcloud import WordCloud

def plot_sentiment_trends(data):

    # Make sure 'date' column is in datetime format
    data['date'] = pd.to_datetime(data['date'])

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='date', y='sentiment_score', hue='bank')

    plt.title('Sentiment Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.legend(title='Bank')

    # Set weekly x-axis ticks
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_rating_distributions(data):

    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='rating', hue='bank', multiple='stack', kde=True)
    plt.title('Rating Distributions by Bank')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_keyword_clouds(data):
    
    for bank in data['bank'].unique():
        keywords = ' '.join(data[data['bank'] == bank]['keyword_ready'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(keywords)

        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f'Keyword Cloud for {bank}')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def plot_theme_distributions(data):
    theme_counts = data.explode('identified_theme') \
                       .groupby(['bank', 'identified_theme']).size().reset_index(name='count')
    theme_counts= theme_counts[theme_counts["count"] > 10]

    plt.figure(figsize=(12, 8))
    sns.barplot(data=theme_counts, x='identified_theme', y='count', hue='bank')
    plt.title('Theme Distributions by Bank')
    plt.xlabel('Theme')
    plt.ylabel('Count')
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sentiment_counts(data):
    import matplotlib.pyplot as plt
    import seaborn as sns

    sentiment_counts = data.groupby(['bank', 'sentiment_label']) \
                           .size().reset_index(name='count')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=sentiment_counts, x='sentiment_label', y='count', hue='bank')
    plt.title('Sentiment Label Counts by Bank')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_sentiment_variability(data):

    variability = data.groupby('bank')['sentiment_score'].std().reset_index(name='std_dev')

    plt.figure(figsize=(8, 6))
    sns.barplot(data=variability, x='bank', y='std_dev')
    plt.title('Sentiment Score Variability by Bank')
    plt.xlabel('Bank')
    plt.ylabel('Standard Deviation')
    plt.tight_layout()
    plt.show()

def plot_sentiment_vs_rating(data):

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='rating', y='sentiment_score', hue='bank', alpha=0.6)
    plt.title('Sentiment Score vs. Rating')
    plt.xlabel('Rating')
    plt.ylabel('Sentiment Score')
    plt.tight_layout()
    plt.show()