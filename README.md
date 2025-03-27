Music Recommendation System

Overview

This is a simple music recommendation system that allows users to input their favorite artists and receive personalized recommendations based on the preferences of other users. The system maintains a database of user preferences and provides various features to analyze popularity metrics.

Features

User Preference Management

Users can enter their favorite artists.

New users are prompted to input their preferences upon first login.

Preferences are stored in a database file (musicrecplus.txt).

Data Storage and Retrieval

The system loads user preferences from musicrecplus.txt.

Any updates to user preferences are saved to the file.

Recommendation System

Identifies the most similar user based on shared preferences.

Suggests new artists that the current user has not yet listened to.

Privacy Feature

Users can mark their profile as private by appending a $ symbol to their name.

Private users' preferences do not influence public recommendations.

Popularity Metrics

Most Popular Artists: Identifies the most liked artists.

Popularity of the Top Artist: Shows how many users like the most popular artist.

Most Active User: Determines which user likes the most artists.

Interactive Menu

Users can select from the following options:

e - Enter preferences

r - Get recommendations

p - Show most popular artists

h - Display the number of likes for the most popular artist

m - Show the user who likes the most artists

q - Save and quit the program

Installation and Usage

Clone the repository:

git clone https://github.com/yourusername/music-recommendation.git
cd music-recommendation

Run the program:

python musicrec.py

Follow the interactive prompts to enter preferences and receive recommendations.
