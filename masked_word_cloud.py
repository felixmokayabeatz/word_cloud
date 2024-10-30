import numpy as np
from PIL import Image
import json
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_sampled_words(filename, num_words=40):
    with open(filename, 'r') as file:
        words = json.load(file)
    return dict(random.sample(list(words.items()), num_words))

sampled_words = load_sampled_words('words.json')

mask = np.array(Image.open('piano.jpg'))

masked_wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    mask=mask,
    contour_color='black',
    contour_width=2,
    random_state=42,
    prefer_horizontal=0.7,
    min_font_size=8,
    max_font_size=40
).generate_from_frequencies(sampled_words)

plt.figure(figsize=(15, 8))
plt.imshow(masked_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Masked Word Cloud')
plt.show()