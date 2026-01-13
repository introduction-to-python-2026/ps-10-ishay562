from skimage.filters import median
from skimage.morphology import ball
from PIL import Image
#import matplotlib.pyplot as plt
#import numpy as np
def my_load_imageload_image(file_path):
   
    img = Image.open(file_path)
    img_array = np.array(img)
    img.close()
    return img_array
treshold_val = 50
img = my_load_image('/content/s_p_i_2.png')
clean_image = median(img, ball(1))
edgeMAG = edge_detection(clean_image)
edge_binary = edgeMAG > treshold_val#edge_detection(my_load_image('/content/s_p_i_2.png'))


plt.figure(figsize=(10, 8))
plt.imshow(clean_image) # Use 'gray' colormap for grayscale images
plt.title('Edge Detected Image')
plt.axis('off') # Hide axes for a cleaner image display
plt.show()

edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
