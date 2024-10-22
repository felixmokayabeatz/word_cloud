import json
import random

# Load data from the JSON file and sample 4000 words
def load_sampled_words(filename, num_words=4000):
    with open(filename, 'r') as file:
        words = json.load(file)
    # Convert dictionary items to a list and sample
    return dict(random.sample(list(words.items()), num_words))


import json
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data from the JSON file and sample 4000 words
def load_sampled_words(filename, num_words=4000):
    with open(filename, 'r') as file:
        words = json.load(file)
    # Convert dictionary items to a list and sample
    return dict(random.sample(list(words.items()), num_words))

# Load sampled words
sampled_words = load_sampled_words('words.json')

# Create a classic word cloud
classic_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(sampled_words)

# Display the classic word cloud
plt.figure(figsize=(10, 5))
plt.imshow(classic_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Classic Word Cloud')
plt.show()
