import json
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_sampled_words(filename, num_words=4000):
    with open(filename, 'r') as file:
        words = json.load(file)
    return dict(random.sample(list(words.items()), num_words))

sampled_words = load_sampled_words('words.json')

def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"hsl({random.randint(0, 360)}, 100%, 50%)"

random_color_wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    color_func=random_color_func,
    random_state=42
).generate_from_frequencies(sampled_words)

plt.figure(figsize=(10, 5))
plt.imshow(random_color_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Random Color Word Cloud')
plt.show()
