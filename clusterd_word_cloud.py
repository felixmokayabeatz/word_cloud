import json
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data from the JSON file and sample 4000 words
def load_sampled_words(filename, num_words=4000):
    with open(filename, 'r') as file:
        words = json.load(file)
    return dict(random.sample(list(words.items()), num_words))

# Load sampled words
sampled_words = load_sampled_words('words.json')

# Create a clustered word cloud with distinct colors for each word
clustered_wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    collocations=False,
    prefer_horizontal=0.9,
    random_state=42
).generate_from_frequencies(sampled_words)

# Display the clustered word cloud
plt.figure(figsize=(10, 5))
plt.imshow(clustered_wordcloud.recolor(color_func=lambda *args, **kwargs: "hsl(120, 100%, 50%)"), interpolation='bilinear')
plt.axis('off')
plt.title('Clustered Word Cloud')
plt.show()
