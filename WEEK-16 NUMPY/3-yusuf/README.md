WEEK-16 NUMPY HOMEWORK

# IMPORTANT
 
### 1- Use the given NumPy_HomeWork.ipynb file to complete the steps.

### 2- DO NOT CHANGE the original NumPy_HomeWork.ipynb file, but just copy and paste in your homework folder.

### 3- Jupyter Notebook use is recommended.

### 4- You can also find the requirement steps on this Readme.md file on your NumPy_HomeWork.ipynb notebook.


# A
## 1) import numpy library with his usual alias!
## 2) Create a random matrix, which has 2 columns and 20 rows. With this we will then create a pandas DataFrame!
## 3) Create two vectors from the previous DataFrame. We will use the same values from the previous DataFrame which we already have been created. The first one contains the evaluations which show the customer satisfaction for the prices, and the second one contains for the quality. How big how good! We will then print the vectors.
## 4) Find the total numbers of visitors.
## 5) Find and print the average ratings for each column using numpy functions (we will find the mean and median values)
## 6) Create a new vector which is the average of the ratings of two columns, price and quality. We will name it as mean_ratings. It will show the average rating for each customer. Round elements of the array to the nearest integer.
## 7) Create ratings_values matrix again with the all three vectors. Average ratings, which has just been calculated in the previous exercise, should be the third column of the new matrix. All values in the matrix should be integer! New matrix should have 20 rows and 3 columns!

# B
## 1) Create *Mean Absolute Error (MAE)* function
## 2) Create two arrays each of them has 100 observations. We will use them for *target* and *predictions* labelling. The target array should consist only 0 or 1 values which are random created, while predictions only integer 1. The target array should have a *binomial distribution* which gives 1 with 60% probability.
## 3) Find the *MAE* with your mae function
## 4)  Run the code in this step. Observe the printed outputs. Try to run the codes a few times from step 2. What do you think about the results? Give your thoughts shortly with 3 - 5 sentences about why two outputs are the same. What is your conclusion?
## 5) We have always chosen 1 in our predictions, but the actual values at the target have changed each time. How likely is it that we got it right each time, and what determines this?
## 5) We have always chosen 1 in our predictions, but the actual values at the target have changed each time. How likely is it that we got it right each time, and what determines this?

# C
## 1) Create a Pythagorean function using *np.dot()* to calculate vector length
## 2) Calculate the length of the given vector using your *pythagorean_length* function and check your result comparing with the given
## 3) Find the shortest distance (Euclidean distance) using *np.dot()* between the given two vectors and compare the results to check

# D - Obfuscating Data
## 1) Protect customers' personal data. It is necessary to develop a data transformation algorithm that makes it difficult to recover personal information in case the data falls into the wrong hands. This is called data masking or data obfuscation. However, the data must be protected in such a way that the quality of the machine learning models does not suffer. You don't need to choose the best model, just prove that the algorithm works correctly.
## 2) Can you guess the customers' ages or income after the transformation?
## 3) Can you recover the original data from X' if you know P? Try to check that with calculations by moving P from the right side of the formula above to the left one. The rules of matrix multiplication are helpful here.
