import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/egsuser/Desktop/madhu/next_web/ai-tasks/spotify.csv")
music_genres = df['playlist_genre'].unique()
## cloumns list
# col_list = df.columns
# # print(f"columns list {col_list}")
# for i in col_list:
#     print(i)

## Fill the null values in `track_album_name` with the string "Unknown".
# s =  df.columns[df.isnull().any()]
# df[s] = df[s].fillna("Unknown")


## Find and remove any duplicate `track_id` rows if they exist.
# dp = df['track_id'].duplicated()
# c = df['track_id'].duplicated().sum()
# print("duplicated count",c)
# df = df.drop_duplicates(subset =['track_id'],keep = 'first')
# dp = df['track_id'].duplicated()
# d = df['track_id'].duplicated().sum()
# print("duplicated removed",d)

## What are the top 5 most popular tracks (`track_popularity`)?
# top_pop = df['track_popularity'].head()
# print("top 5 track_popularity \n",top_pop)

## Filter the tracks that have a `danceability` score greater than 0.8 and a `tempo` over 120.
# fileter_rows =  df[(df['tempo']>120) & (df['danceability']>0.8)]
# print("filter data",fileter_rows[['tempo','danceability']])

## find all tracks by the artist "Bad Bunny" (if present, or choose a common artist from the counts).
## only bad bunny 
# grp_tracks = df[df['track_artist'].str.lower()=="Bad Bunny".lower()]
# print("Bad Bunny tracks ",len(grp_tracks))

# ## combine with bad bunny
# track_artist = df['track_artist']
# c =track_artist.str.contains('bad bunny',case = False, na =False).sum()
# print("count of track of artist",c)
# print("Bad Bunny tracks ",len(track_artist))

## What is the average `energy` level for each `playlist_genre`?
# avg_energy = df.groupby('playlist_genre')['energy'].mean()
# print(avg_energy)
# avg_energy.plot()
# plt.show()


## Which `playlist_subgenre` has the highest average `track_popularity`?
# high_avg_track= df.groupby('playlist_subgenre')['track_popularity'].mean().sort_values(ascending =False).head(1)
# print("high_avg_track_popularity",high_avg_track)

## Count how many tracks are in each `playlist_genre`.
# count_playlist_genre = df.groupby('playlist_genre').size().reset_index(name="count_track")
# print("count of playlist_genre",count_playlist_genre)

# count_playlist_genre.plot()
# plt.show()


### Advance Analysis
## Find the track with the longest duration (`duration_ms`)
# dur_long = df['duration_ms'].sort_values(ascending=False).head(1)
# print("longest duration ",dur_long)

# dur_long_track = df.iloc[df['duration_ms'].idxmax()]
# print("longest duration ",dur_long_track[['duration_ms','track_name']])

## create a new column called `energy_to_loudness_ratio` by dividing `energy` by `loudness`.
# df['energy_to_loudness_ratio'] = df['energy']/df['loudness'].abs()
# print("energy_to_loudness_ratio :\n ",df['energy_to_loudness_ratio'])

# df[['energy_to_loudness_ratio','energy','loudness']].plot()
# plt.show()

## Which month has the most song releases? (You'll need to parse `track_album_release_date`).
df['track_album_release_date'] = pd.to_datetime(df['track_album_release_date'],format="mixed").dt.month
grp_date = df.groupby(['track_album_release_date']).sum()
print("track_album_release_date", grp_date)