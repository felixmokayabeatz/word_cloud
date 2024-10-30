import json
import random
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import scipy.ndimage

def load_sampled_words(filename, num_words=4000):
    with open(filename, 'r') as file:
        words = json.load(file)
    return dict(random.sample(list(words.items()), num_words))

def create_spiral_mask(width, height):

    mask = np.zeros((height, width), dtype=np.float32)
    
    t = np.linspace(0, 20*np.pi, 1000)
    a = 0.5
    b = 0.5
    x = width/2 + a*t*np.cos(t)
    y = height/2 + b*t*np.sin(t)
    
    valid_points = (x >= 0) & (x < width) & (y >= 0) & (y < height)
    x = x[valid_points].astype(int)
    y = y[valid_points].astype(int)
    
    mask[y, x] = 255
    
    mask = scipy.ndimage.gaussian_filter(mask, sigma=5)
    mask = mask > mask.mean()
    return mask

sampled_words = load_sampled_words('words.json')

width = 800
height = 800
spiral_mask = create_spiral_mask(width, height)

spiral_wordcloud = WordCloud(
    width=width,
    height=height,
    background_color='white',
    mask=spiral_mask,
    collocations=False,
    prefer_horizontal=0.5,
    random_state=42
).generate_from_frequencies(sampled_words)

def position_color_func(word, font_size, position, orientation, **kwargs):

    x, y = position
    center_x, center_y = width/2, height/2
    angle = np.arctan2(y - center_y, x - center_x)

    hue = ((angle + np.pi) / (2*np.pi) * 360) % 360
    
    return f"hsl({hue:.1f}, 70%, 50%)"

plt.figure(figsize=(10, 10))
plt.imshow(spiral_wordcloud.recolor(color_func=position_color_func), interpolation='bilinear')
plt.axis('off')
plt.title('Spiral Word Cloud')
plt.show()