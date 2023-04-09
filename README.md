# Generating Embeddings for Deep Learning Based Recommender Systems

This repository contains all the code in relation to the topic of generating embeddings for the purpose of recommendations. The goal is to find out what methods of embedding are the most effective and what sort of information when embedded gives the best results.

## Dataset

The dataset used is the [GroupLens' MovieLens 100K Dataset](https://grouplens.org/datasets/movielens/). It contains 100K ratings that users have given to movies from 1-5. In addition to this, content metadata and user metadata is available although in different versions of the dataset.

## Steps to Run
1. Run Most_Common_Tags Notebook
2. Run User Metadata Creation notebook
3. Run Movie Metadata Creation Notebook
4. Run Final Metadata Creation Notebook
<!-- ## Model(s) Used

This needs to be a description of the model used and a brief overview of how it works in theory (e.g taken of a CNN Model): 

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. Input images are resized to an optimal size and then fed into the **Convolutional layer**. These images are converted to their pixel values, which can be imagined as a three-dimensional matrix for the purpose of visualization. The **Convolutional layer** has a kernel. This kernel is generally a small matrix of specified kernel size mxnx3 (3 for RGB images). 
<br>

**Rectified Linear Unit (ReLU)** is the activation layer used in CNNs.The activation function is applied to increase non-linearity in the CNN. Images are made of different objects that are not linear to each other.


**Max Pooling:** A limitation of the feature map output of Convolutional Layers is that they record the precise position of features in the input. This means that small movements in the position of the feature in the input image will result in a different feature map. This can happen with re-cropping, rotation, shifting, and other minor changes to the input image. A common approach to addressing this problem from signal processing is called down sampling. This is where a lower resolution version of an input signal is created that still contains the large or important structural elements, without the fine detail that may not be as useful to the task.

## Future Work
Good ideas or strategies that you were not able to implement which you think can help  improve performance. -->
