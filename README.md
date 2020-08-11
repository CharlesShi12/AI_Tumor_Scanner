## Medical Scanner
I collaborated with a team of developers to create a Convolutional Neural Network that is capable of identifying tumors from brain MRI Scans. We used data augmentation to train it with over 7,000 images. We tested and modified the neural network to obtain a final average accuracy of 95%. 

## General Technical Description
We extracted features, preserved the spatial relationship between pixels, and captured the local dependencies of the input image to generate distinct feature maps for the training process. We then employed MaxPooling in 2D to define a spatial neighborhood, normalize the dimensionality of the dataset, and avoid overfitting.
Finally, we applied a multi-layer perceptron that uses a softmax activation function in the output layer to connect all the neurons in the CNN. The output from these neurons and layers represent high-level features of the input image, which are used to categorize the input image into various classes based on the training dataset. 

## Screenshots

## Tech/Framework used
Built with 
* Python
* TenserFlow
* Keras
* Numpy
* Streamlit

## Features
* Users are able to input an image via Streamlit
* Streamlit application outputs whether your brain MRI scan has a tumor or not.

## Installation
Run this command in your terminal: 
```
git clone https://github.com/CharlesShi12/ImageFilters.git
```
Import the folder into your respected IDE. Open your terminal, navigate to this github repository folder, and run the following command:
```
streamlit run main.py
```

## Credit
Collaborators
* Tejesh: https://github.com/tejesh-ch
* Rohan: https://github.com/rohanshiva
* Amogh: https://github.com/amogh1155

## License
MIT © Charles Shi
