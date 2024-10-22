import numpy as np
from PIL import Image
import json
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data from the JSON file and sample 4000 words
def load_sampled_words(filename, num_words=40):
    with open(filename, 'r') as file:
        words = json.load(file)
    return dict(random.sample(list(words.items()), num_words))

# Load sampled words
sampled_words = load_sampled_words('words.json')

# Load a mask image
mask = np.array(Image.open('piano.jpg'))  # Replace 'mask.png' with your mask image

# Create a masked word cloud
masked_wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    mask=mask, 
    contour_color='black', 
    contour_width=1,
    random_state=42
).generate_from_frequencies(sampled_words)

# Display the masked word cloud
plt.figure(figsize=(10, 5))
plt.imshow(masked_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Masked Word Cloud')
plt.show()
