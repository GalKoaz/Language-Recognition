# Language Recognition

In this project, we took an existing language recognition model and tried to improve it with several methods. This model applies x-vectors to the task of spoken language recognition. This framework consists of a deep neural network that maps sequences of speech features to fixed-dimensional embeddings, called x-vectors. Long-term language characteristics are captured in the network by a temporal pooling layer that aggregates information across time. Once extracted, x-vectors utilize the same classification technology developed for i-vectors.
our work utilized datasets sourced from Common Voice, a valuable resource for multilingual speech data. We specifically focused on ten languages, carefully selected from three distinct language families: Indo-European, Semitic, and East Asian.

The main method we used to improve the existing model is changing the architecture of the TDNN layers. The first significant change is the addition of 1X1 TDNN intermediate layers between the existing layers. Another change is in the structure of the TDNN network to a funnel structure which has extensive theoretical significance by changing the number of neurons in these layers. In addition, a grid search was performed to find the optimal dilation and context size values in the TDNN layers. 

These optimal values help to find the complex patterns that represent the different languages in the audio segments. Finally, after significant training on the original data, additional training was performed for the purpose of fine-tuning the model on data with augmentations such as: changing the audio speed, adding Gaussian noise, and changing the pitch. This additional training improves the generalization ability of the model and its resistance to changes.
The purpose of the research is to present approaches to improve language recognition models and in particular, models based on the TDNN and x-vector methods. The study presents a significant improvement in relation to the existing model with the help of each of these methods and finally presents an integrated model, which contains all these changes together.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Architecture](#architecture)
- [Contributing](#contributing)

## Project Description

Our project based on the Spoken Language Recognition using X-vectors paper:

Paper: [2018 odyssey X vector lid](https://danielpovey.com/files/2018_odyssey_xvector_lid.pdf)

Source repo : [X vector repository](https://github.com/KrishnaDN/x-vector-pytorch)



## Features

* Language recognition using X-vectors: The project implements the X-vector methodology described in the paper for identifying spoken languages.
* Deep neural network (DNN) embeddings: X-vectors are DNN-based embeddings that capture speaker and language characteristics.
* PyTorch implementation: The project utilizes PyTorch, a popular deep learning framework, for efficient implementation and training of the X-vector model.

## Installation

Clone the ripo:
```bash
https://github.com/GalKoaz/Language-Recognition.git
```

## Architecture
<p align="center">
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/GHByLJL/Untitled-Diagram-drawio-3.png" alt="Untitled-Diagram-drawio-3" border="0" /></a>
</p>


Our Final Model for download:

https://easyupload.io/y85342



## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

