Hello! This is my NBA Player Predictor



First, the program will ask for the first and last name


Then, it will convert the first and last name to a basketball-reference url site that will have the last 5 games info on it.


Using pandas, it then scrapes the data from the url and inputs it into a dataframe.


Then, using sklearn, I use a linear regression model and split test sets for the FGA, 3PA, FTA columns 

After, it predicts how many points the player will score, along with the error associated with that


I have gotten fantastic results. For Lebron James, the error is only 1.624, which is very low. 

Although the default model predict points, you can also predict any other stat based off the features and target


I made this to showcase the full power of Machine Learning and Data Analysis within the Sports World, and how you can use Data to make accurate predictions. 

