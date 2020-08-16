from keras.models import load_model
from keras.preprocessing import image
import numpy as np

def load_image(img_path):

    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.

    return img_tensor


if __name__ == "__main__":

    # load model
    model = load_model("model.h5")

    # image path
    img_path = 'test1.jpg'

    # load a single image
    new_image = load_image(img_path)

    # check prediction
    pred = model.predict(new_image)

    print(pred)
