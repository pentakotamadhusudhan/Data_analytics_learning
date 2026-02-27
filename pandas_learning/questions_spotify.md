# Spotify Data Analysis Questions

Based on the `spotify.csv` dataset, here are some questions to practice your Pandas skills:

### 1. Basic Exploration
- How many rows and columns are in the dataset?
- What are the data types of each column?
- List all unique `playlist_genre` values present in the data.

### 2. Data Cleaning
- Which column(s) contain null values, and how many are there?
- Fill the null values in `track_album_name` with the string "Unknown".
- Find and remove any duplicate `track_id` rows if they exist.

### 3. Filtering and Selection
- What are the top 5 most popular tracks (`track_popularity`)?
- Filter the tracks that have a `danceability` score greater than 0.8 and a `tempo` over 120.
- Find all tracks by the artist "Bad Bunny" (if present, or choose a common artist from the counts).

### 4. Grouping and Aggregation
- What is the average `energy` level for each `playlist_genre`?
- Which `playlist_subgenre` has the highest average `track_popularity`?
- Count how many tracks are in each `playlist_genre`.

### 5. Advanced Analysis
- Find the track with the longest duration (`duration_ms`).
- Create a new column called `energy_to_loudness_ratio` by dividing `energy` by `loudness`.
- Which month has the most song releases? (You'll need to parse `track_album_release_date`).

### 6. Correlation
- Is there a correlation between `danceability` and `valence` (happiness)?
- Does higher `speechiness` correlate with lower `track_popularity`?
