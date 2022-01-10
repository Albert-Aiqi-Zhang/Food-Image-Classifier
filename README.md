# Food-Image-Classifier
Welcome to the world of Gourmets! In this project, I implemented a delicious food image classifier. Yummy, like the following picture.

![food](https://github.com/Albert-Aiqi-Zhang/Food-Image-Classifier/blob/main/images/foods.png)

OK, that's a joke. I learnt deep learning last year, and I hope I can do something interesting about image recognition. I found many people did great job in MNITS and CiFar classification, but I prefer cooking more. Hence, I decided to implement a food image classifier on my own.

## 1. Preparation
As a preparation, I downloaded 10 different genres of food, each of which has about 100 pictures, with a Google Custom Search API. Actually selection of ten food is tricky. I have to choose those whose appearances are not similar. For example, I cannot tell the difference between dried chicken and karaage(唐揚げ) at the first glance, so I think my classifier cannot, either. As a result, I choose the following food to "feed" my model:

(0) beef steak
(1) hamburger
(2) jiaozi
(3) oden
(4) pizza
(5) stirfried minced pork with basil
(6) tom yam kung
(7) fried chicken
(8) indian curry
(9) spagatthi

You can also check the index_food.txt. After all, these foods are what I love. You may select your favorite foods for your model.

## 2. Preprocessing

This preprocessing here doesn't mean normalization or something like that. Here the 1000 pieces of pictures are of different sizes and different formats (png, jpeg, etc.). So I need to reshape them to the same sizes and formats. You can find the preprocess_images.py in the main/ directory. I make all of them 100 * 100. I found some pictures lose their key characteristics in this process. If you have some better ideas, please contact me! 

Next I want to use the GPU of Google Colaboratory to complete my model, so I uploaded all these images in the food_datasets/ directory.

## 3. Model 1. A Simple model with only Convolutional Neural Network (CNN)

I want to find the power of data augmentation in this project, so I decide to split my model into two halves: a simpler one, and a more complicated one. You can find this model in food_image_classifier_simple.ipynb in the main/ directory.

In this model, I defined various layers of CNN, including convolutional layer, pooling layer, flattening layer, etc. Anyway, this is a typical CNN, with a small dataset (less than 1000 pictures). Then I split the datasets into 3 parts:   

(1) training data (65%)   
(2) validation data (10%)   
(3) test data (25%)     

This may not be a conventional splitting method, but I don't have enough data. As a result, I have to distribute data to training as many as I can.

The result can be concluded with the following picture.

![simple_result](https://github.com/Albert-Aiqi-Zhang/Food-Image-Classifier/blob/main/images/accuracy_simple_graph.png)

As you can see, the result is very poor. The training accuracy is close to 100%, while validation accuracy and test accuracy is only about 40%. The reason is that the sample data is too small for the model to learn well. In the next step, I'll use various types of data augmentation to boost our arsenal.

## 4. Model 2. A Complicated model with CNN and data augmentation

In this model I applied many preprocessing and data augmentation techniques.
You can find the model in food_image_classifier_complicated.ipynb in the main/ directory.




