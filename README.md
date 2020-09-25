# Project 3

In this project, we used movie data from grouplens and made a movie recommender. I approached this problem by training different models and then inputting a movie to get out of list of recommendations. 

Some of the features we created in this dataset were:
* One-Hot encoding the genres for each movie
* Normalizing the ratings by subtracting the average rating for a given user for each of the user's ratings

## Clustering Methods
We attempted to run two different clustering methods for our recommender: by correlation and by agglomerative clustering.

### Correlation Clusters
In this model, we found the correlation between a given movie ratings and the other movie ratings in our dataset. It was very important in this one that all the ratings were normalized, so it was essential that we had previously normalized the ratings. Given a movie, this prints the top 50 recommendations and the correlation between the given movie and each of the movies. This is an ordered recomendation.

### Agglomerative Clustering

In this model, we found clusters of all the movies. After we clustered them, I wrote a function that given a movie it would identify its cluster and then find all the other movies in its cluster. So, if you give this model a movie you will get an unordered recommendation of other movies you may like.  

