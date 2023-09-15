# This is used to test the image datatype of Embedchain

A random selection of a few images from https://www.kaggle.com/datasets/puneet6060/intel-image-classification is cloned in the data folder


## How to Use
1. Install [Embedchain][https://github.com/embedchain/embedchain]
2. Add the dataset -> `python add_image_dataset.py`
3. Query the dataset -> `python query_image_dataset.py <QUERY>`, where QUERY can be any context we are looking for in the images e.g. "A Glacier", "A forest", "A mountain by the sea". This will return the most relevant image from the images in the `data` folder


