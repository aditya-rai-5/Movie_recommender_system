# Movie_recommender_system
  1. download the dataset
  2. readd the dataset using pandas
  3. then clean the dataset
  4. if any duplicates present then remove the duplicates
  5. convert raw data into a usable data
  6. extract the main characters and the dirctor from the dataset
  7. then add the column tags with the combination of cast, crew, genres and overview
  8. then separate the useful columns for the recommender model
  9. remove the stopwords from the tags
     
   ## content based recommendation
     1. the convert tags to vector by using 'all-MiniLM-L6-v2' SentenceTransformer from HuggingFace. also the sentence transformers remove the problem of sparsity which is the major factor of overfitting
     2. use cosine similarity to calculate the similarity btw each pair of vectors.
     3. add the column for score in the dataset
     4. then define a function named content_based_recommendation which recommend the movies on your choice

   ## collaborative-based-recommendation
     1. use sklearn to train the model
     2. create a piplinr of the model.
     3. model pipeline includes StandardScaler() and then TrunctedSVD which reduce the dimentions of the vectors.
     4. the add KMeans layer
     5. fit the train_dataset in the model to train the model
     6. then predict the test data from the model.
     7. and the we can evalute the model by different different evaluation metrics.
     8. then define the function to return the collaborative based recommended movies.
   ## Hybrid recommendation
     1. then combine the result of content based and collaborative based movies. this give us the hybrid recommendations.

   ## deploying the model
     1. use the streamlit lib in python.
     2. use css to make the interface good looking
     3. use Api key from the TMBD dataset.
     4. the define a function to get the details of the movie from the movie id. and extract the poster, homepage link and casting actors.
     5. the define the function same as in the collab notebook. 
     6. set the content based and collab based movies alternate for good experience.
     7. using the streamlit web deploy the app. 
     
