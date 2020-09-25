#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:46:25 2020

@author: gracemcmonagle
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

links = pd.read_csv('/Users/gracemcmonagle/Desktop/School/Fall 2020/EECS 731/Project 3/src/data/links.csv', delimiter = ',')
movies = pd.read_csv('/Users/gracemcmonagle/Desktop/School/Fall 2020/EECS 731/Project 3/src/data/movies.csv', delimiter = ',')
ratings = pd.read_csv('/Users/gracemcmonagle/Desktop/School/Fall 2020/EECS 731/Project 3/src/data/ratings.csv', delimiter = ',')
tags = pd.read_csv('/Users/gracemcmonagle/Desktop/School/Fall 2020/EECS 731/Project 3/src/data/tags.csv', delimiter = ',')

#normalize the ratings by subtracting the mean for a specific user from all of their scores
ratings_norm = ratings.groupby(['userId']).rating.transform(lambda x: x - x.mean())
ratings = ratings.drop('rating', axis = 1)
ratings_full_norm = pd.concat([ratings, ratings_norm], axis =1)

rating_count = ratings_full_norm.groupby(['movieId'], as_index = False).rating.count()
rating_count = rating_count.rename(columns = {'rating': 'rating_count'})
# join the ratings and the movie genres
movie_full_1 = pd.merge(ratings_full_norm, movies, on = 'movieId')
movie_full = pd.merge(movie_full_1, rating_count, on ='movieId')

plt.figure(figsize=(8,6))
movie_full['rating_count'].hist(bins=25)
plt.show()

#
user_movie_rating = movie_full.pivot_table(index='userId', columns='title', values='rating')

#%% basic correlation method
def corr_Movie(title):
    movie_ratings = user_movie_rating[title]
    corr_movies = user_movie_rating.corrwith(movie_ratings)
    similar_movies = pd.DataFrame(corr_movies, columns = ['Correlation'])
    similar_movies.dropna(inplace=True)
    similar_movies = pd.merge(similar_movies, movie_full[['rating_count', 'title']], on = 'title').drop_duplicates()
    similar_movies = similar_movies[similar_movies ['rating_count']>50].sort_values('Correlation', ascending = False)
    return similar_movies[1:50]

    
movie_list= list(movies['title'])
which_movie = 3574
print('Movies Similar to: ' + movie_list[which_movie])
print(corr_Movie(movie_list[which_movie]))

#%% clustering

scaler = StandardScaler()
movie_standard = scaler.fit_transform(movie_full)

