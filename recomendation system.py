
import numpy as np
import pandas as pd
     

credits_df = pd.read_csv('credits.csv')
movies_df = pd.read_csv('movies.csv')
     

credits_df
     
movie_id	title	cast	crew
0	19995	Avatar	[{"cast_id": 242, "character": "Jake Sully", "...	[{"credit_id": "52fe48009251416c750aca23", "de...
1	285	Pirates of the Caribbean: At World's End	[{"cast_id": 4, "character": "Captain Jack Spa...	[{"credit_id": "52fe4232c3a36847f800b579", "de...
2	206647	Spectre	[{"cast_id": 1, "character": "James Bond", "cr...	[{"credit_id": "54805967c3a36829b5002c41", "de...
3	49026	The Dark Knight Rises	[{"cast_id": 2, "character": "Bruce Wayne / Ba...	[{"credit_id": "52fe4781c3a36847f81398c3", "de...
4	49529	John Carter	[{"cast_id": 5, "character": "John Carter", "c...	[{"credit_id": "52fe479ac3a36847f813eaa3", "de...
...	...	...	...	...
933	6038	Shanghai Knights	[{"cast_id": 1, "character": "Chon Wang", "cre...	[{"credit_id": "55a675c2c3a36845a900000f", "de...
934	9975	Curious George	[{"cast_id": 17, "character": "Ted - Man with ...	[{"credit_id": "52fe4555c3a36847f80c84fb", "de...
935	11451	Herbie Fully Loaded	[{"cast_id": 1, "character": "Maggie Peyton", ...	[{"credit_id": "59620742925141790403a4fe", "de...
936	12103	Don't Say a Word	[{"cast_id": 13, "character": "Nathan R. Conra...	[{"credit_id": "555dcd3ac3a36868c900138d", "de...
937	60304	Hansel & Gretel: Witch Hunters	[{"cast_id": 3, "character": "Hansel", "credit...	NaN
938 rows × 4 columns


movies_df
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	production_countries	release_date	revenue	runtime	spoken_languages	status	tagline	title	vote_average	vote_count
0	237000000	[{"id": 28, "name": "Action"}, {"id": 12, "nam...	http://www.avatarmovie.com/	19995	[{"id": 1463, "name": "culture clash"}, {"id":...	en	Avatar	In the 22nd century, a paraplegic Marine is di...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	[{"iso_3166_1": "US", "name": "United States o...	10-12-2009	2787965087	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800
1	300000000	[{"id": 12, "name": "Adventure"}, {"id": 14, "...	http://disney.go.com/disneypictures/pirates/	285	[{"id": 270, "name": "ocean"}, {"id": 726, "na...	en	Pirates of the Caribbean: At World's End	Captain Barbossa, long believed to be dead, ha...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	[{"iso_3166_1": "US", "name": "United States o...	19-05-2007	961000000	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500
2	245000000	[{"id": 28, "name": "Action"}, {"id": 12, "nam...	http://www.sonypictures.com/movies/spectre/	206647	[{"id": 470, "name": "spy"}, {"id": 818, "name...	en	Spectre	A cryptic message from Bond’s past sends him o...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	[{"iso_3166_1": "GB", "name": "United Kingdom"...	26-10-2015	880674609	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466
3	250000000	[{"id": 28, "name": "Action"}, {"id": 80, "nam...	http://www.thedarkknightrises.com/	49026	[{"id": 849, "name": "dc comics"}, {"id": 853,...	en	The Dark Knight Rises	Following the death of District Attorney Harve...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	[{"iso_3166_1": "US", "name": "United States o...	16-07-2012	1084939099	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106
4	260000000	[{"id": 28, "name": "Action"}, {"id": 12, "nam...	http://movies.disney.com/john-carter	49529	[{"id": 818, "name": "based on novel"}, {"id":...	en	John Carter	John Carter is a war-weary, former military ca...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	[{"iso_3166_1": "US", "name": "United States o...	07-03-2012	284139100	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
4798	220000	[{"id": 28, "name": "Action"}, {"id": 80, "nam...	NaN	9367	[{"id": 5616, "name": "united states\u2013mexi...	es	El Mariachi	El Mariachi just wants to play his guitar and ...	14.269792	[{"name": "Columbia Pictures", "id": 5}]	[{"iso_3166_1": "MX", "name": "Mexico"}, {"iso...	04-09-1992	2040920	81.0	[{"iso_639_1": "es", "name": "Espa\u00f1ol"}]	Released	He didn't come looking for trouble, but troubl...	El Mariachi	6.6	238
4799	9000	[{"id": 35, "name": "Comedy"}, {"id": 10749, "...	NaN	72766	[]	en	Newlyweds	A newlywed couple's honeymoon is upended by th...	0.642552	[]	[]	26-12-2011	0	85.0	[]	Released	A newlywed couple's honeymoon is upended by th...	Newlyweds	5.9	5
4800	0	[{"id": 35, "name": "Comedy"}, {"id": 18, "nam...	http://www.hallmarkchannel.com/signedsealeddel...	231617	[{"id": 248, "name": "date"}, {"id": 699, "nam...	en	Signed, Sealed, Delivered	"Signed, Sealed, Delivered" introduces a dedic...	1.444476	[{"name": "Front Street Pictures", "id": 3958}...	[{"iso_3166_1": "US", "name": "United States o...	13-10-2013	0	120.0	[{"iso_639_1": "en", "name": "English"}]	Released	NaN	Signed, Sealed, Delivered	7.0	6
4801	0	[]	http://shanghaicalling.com/	126186	[]	en	Shanghai Calling	When ambitious New York attorney Sam is sent t...	0.857008	[]	[{"iso_3166_1": "US", "name": "United States o...	03-05-2012	0	98.0	[{"iso_639_1": "en", "name": "English"}]	Released	A New Yorker in Shanghai	Shanghai Calling	5.7	7
4802	0	[{"id": 99, "name": "Documentary"}]	NaN	25975	[{"id": 1523, "name": "obsession"}, {"id": 224...	en	My Date with Drew	Ever since the second grade when he first saw ...	1.929883	[{"name": "rusty bear entertainment", "id": 87...	[{"iso_3166_1": "US", "name": "United States o...	05-08-2005	0	90.0	[{"iso_639_1": "en", "name": "English"}]	Released	NaN	My Date with Drew	6.3	16
4803 rows × 20 columns


movies_df = movies_df.merge(credits_df, on ='title')
     

movies_df.shape
     
(938, 23)

movies_df.head()
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	runtime	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew
0	237000000	[{"id": 28, "name": "Action"}, {"id": 12, "nam...	http://www.avatarmovie.com/	19995	[{"id": 1463, "name": "culture clash"}, {"id":...	en	Avatar	In the 22nd century, a paraplegic Marine is di...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[{"cast_id": 242, "character": "Jake Sully", "...	[{"credit_id": "52fe48009251416c750aca23", "de...
1	300000000	[{"id": 12, "name": "Adventure"}, {"id": 14, "...	http://disney.go.com/disneypictures/pirates/	285	[{"id": 270, "name": "ocean"}, {"id": 726, "na...	en	Pirates of the Caribbean: At World's End	Captain Barbossa, long believed to be dead, ha...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[{"cast_id": 4, "character": "Captain Jack Spa...	[{"credit_id": "52fe4232c3a36847f800b579", "de...
2	245000000	[{"id": 28, "name": "Action"}, {"id": 12, "nam...	http://www.sonypictures.com/movies/spectre/	206647	[{"id": 470, "name": "spy"}, {"id": 818, "name...	en	Spectre	A cryptic message from Bond’s past sends him o...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[{"cast_id": 1, "character": "James Bond", "cr...	[{"credit_id": "54805967c3a36829b5002c41", "de...
3	250000000	[{"id": 28, "name": "Action"}, {"id": 80, "nam...	http://www.thedarkknightrises.com/	49026	[{"id": 849, "name": "dc comics"}, {"id": 853,...	en	The Dark Knight Rises	Following the death of District Attorney Harve...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[{"cast_id": 2, "character": "Bruce Wayne / Ba...	[{"credit_id": "52fe4781c3a36847f81398c3", "de...
4	260000000	[{"id": 28, "name": "Action"}, {"id": 12, "nam...	http://movies.disney.com/john-carter	49529	[{"id": 818, "name": "based on novel"}, {"id":...	en	John Carter	John Carter is a war-weary, former military ca...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[{"cast_id": 5, "character": "John Carter", "c...	[{"credit_id": "52fe479ac3a36847f813eaa3", "de...
5 rows × 23 columns


movies_df.info()
     
<class 'pandas.core.frame.DataFrame'>
Int64Index: 938 entries, 0 to 937
Data columns (total 23 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   budget                938 non-null    int64  
 1   genres                938 non-null    object 
 2   homepage              503 non-null    object 
 3   id                    938 non-null    int64  
 4   keywords              938 non-null    object 
 5   original_language     938 non-null    object 
 6   original_title        938 non-null    object 
 7   overview              938 non-null    object 
 8   popularity            938 non-null    float64
 9   production_companies  938 non-null    object 
 10  production_countries  938 non-null    object 
 11  release_date          938 non-null    object 
 12  revenue               938 non-null    int64  
 13  runtime               938 non-null    float64
 14  spoken_languages      938 non-null    object 
 15  status                938 non-null    object 
 16  tagline               908 non-null    object 
 17  title                 938 non-null    object 
 18  vote_average          938 non-null    float64
 19  vote_count            938 non-null    int64  
 20  movie_id              938 non-null    int64  
 21  cast                  938 non-null    object 
 22  crew                  937 non-null    object 
dtypes: float64(3), int64(5), object(15)
memory usage: 175.9+ KB

movies_df.isnull() .sum()
     
budget                    0
genres                    0
homepage                435
id                        0
keywords                  0
original_language         0
original_title            0
overview                  0
popularity                0
production_companies      0
production_countries      0
release_date              0
revenue                   0
runtime                   0
spoken_languages          0
status                    0
tagline                  30
title                     0
vote_average              0
vote_count                0
movie_id                  0
cast                      0
crew                      1
dtype: int64

movies_df.dropna(inplace = True)
     

movies_df.duplicated().sum()
     
0

movies_df.iloc[0].genres
     
'[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]'

import ast
     

def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
     

movies_df['genres']= movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)
movies_df.head()
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	runtime	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew
0	237000000	[Action, Adventure, Fantasy, Science Fiction]	http://www.avatarmovie.com/	19995	[culture clash, future, space war, space colon...	en	Avatar	In the 22nd century, a paraplegic Marine is di...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[{"cast_id": 242, "character": "Jake Sully", "...	[{"credit_id": "52fe48009251416c750aca23", "de...
1	300000000	[Adventure, Fantasy, Action]	http://disney.go.com/disneypictures/pirates/	285	[ocean, drug abuse, exotic island, east india ...	en	Pirates of the Caribbean: At World's End	Captain Barbossa, long believed to be dead, ha...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[{"cast_id": 4, "character": "Captain Jack Spa...	[{"credit_id": "52fe4232c3a36847f800b579", "de...
2	245000000	[Action, Adventure, Crime]	http://www.sonypictures.com/movies/spectre/	206647	[spy, based on novel, secret agent, sequel, mi...	en	Spectre	A cryptic message from Bond’s past sends him o...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[{"cast_id": 1, "character": "James Bond", "cr...	[{"credit_id": "54805967c3a36829b5002c41", "de...
3	250000000	[Action, Crime, Drama, Thriller]	http://www.thedarkknightrises.com/	49026	[dc comics, crime fighter, terrorist, secret i...	en	The Dark Knight Rises	Following the death of District Attorney Harve...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[{"cast_id": 2, "character": "Bruce Wayne / Ba...	[{"credit_id": "52fe4781c3a36847f81398c3", "de...
4	260000000	[Action, Adventure, Science Fiction]	http://movies.disney.com/john-carter	49529	[based on novel, mars, medallion, space travel...	en	John Carter	John Carter is a war-weary, former military ca...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[{"cast_id": 5, "character": "John Carter", "c...	[{"credit_id": "52fe479ac3a36847f813eaa3", "de...
5 rows × 23 columns


def convert3(obj):
    L=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter +=1
        else:
            break
        return L
     

movies_df['cast'] = movies_df['cast'].apply(convert3)
     

movies_df.head()
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	runtime	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew
0	237000000	[Action, Adventure, Fantasy, Science Fiction]	http://www.avatarmovie.com/	19995	[culture clash, future, space war, space colon...	en	Avatar	In the 22nd century, a paraplegic Marine is di...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[Sam Worthington]	[{"credit_id": "52fe48009251416c750aca23", "de...
1	300000000	[Adventure, Fantasy, Action]	http://disney.go.com/disneypictures/pirates/	285	[ocean, drug abuse, exotic island, east india ...	en	Pirates of the Caribbean: At World's End	Captain Barbossa, long believed to be dead, ha...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[Johnny Depp]	[{"credit_id": "52fe4232c3a36847f800b579", "de...
2	245000000	[Action, Adventure, Crime]	http://www.sonypictures.com/movies/spectre/	206647	[spy, based on novel, secret agent, sequel, mi...	en	Spectre	A cryptic message from Bond’s past sends him o...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[Daniel Craig]	[{"credit_id": "54805967c3a36829b5002c41", "de...
3	250000000	[Action, Crime, Drama, Thriller]	http://www.thedarkknightrises.com/	49026	[dc comics, crime fighter, terrorist, secret i...	en	The Dark Knight Rises	Following the death of District Attorney Harve...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[Christian Bale]	[{"credit_id": "52fe4781c3a36847f81398c3", "de...
4	260000000	[Action, Adventure, Science Fiction]	http://movies.disney.com/john-carter	49529	[based on novel, mars, medallion, space travel...	en	John Carter	John Carter is a war-weary, former military ca...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[Taylor Kitsch]	[{"credit_id": "52fe479ac3a36847f813eaa3", "de...
5 rows × 23 columns


def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']== 'Director':
            L.append(i['name'])
            break
    return L
     

movies_df['crew'] = movies_df['crew'].apply(fetch_director)
     

movies_df
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	runtime	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew
0	237000000	[Action, Adventure, Fantasy, Science Fiction]	http://www.avatarmovie.com/	19995	[culture clash, future, space war, space colon...	en	Avatar	In the 22nd century, a paraplegic Marine is di...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[Sam Worthington]	[James Cameron]
1	300000000	[Adventure, Fantasy, Action]	http://disney.go.com/disneypictures/pirates/	285	[ocean, drug abuse, exotic island, east india ...	en	Pirates of the Caribbean: At World's End	Captain Barbossa, long believed to be dead, ha...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[Johnny Depp]	[Gore Verbinski]
2	245000000	[Action, Adventure, Crime]	http://www.sonypictures.com/movies/spectre/	206647	[spy, based on novel, secret agent, sequel, mi...	en	Spectre	A cryptic message from Bond’s past sends him o...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[Daniel Craig]	[Sam Mendes]
3	250000000	[Action, Crime, Drama, Thriller]	http://www.thedarkknightrises.com/	49026	[dc comics, crime fighter, terrorist, secret i...	en	The Dark Knight Rises	Following the death of District Attorney Harve...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[Christian Bale]	[Christopher Nolan]
4	260000000	[Action, Adventure, Science Fiction]	http://movies.disney.com/john-carter	49529	[based on novel, mars, medallion, space travel...	en	John Carter	John Carter is a war-weary, former military ca...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[Taylor Kitsch]	[Andrew Stanton]
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
921	50000000	[Drama, Comedy, Family]	http://www.weboughtazoo.com/	74465	[zoo]	en	We Bought a Zoo	Benjamin has lost his wife and, in a bid to st...	38.629763	[{"name": "Twentieth Century Fox Film Corporat...	...	124.0	[{"iso_639_1": "en", "name": "English"}]	Released	A True Zoo Story	We Bought a Zoo	6.5	909	74465	[Matt Damon]	[Cameron Crowe]
922	50000000	[Action, Adventure, Drama, Mystery, Science Fi...	http://knowing-themovie.com/	13811	[cataclysm, code, suspense, end of the world, ...	en	Knowing	A teacher opens a time capsule that has been d...	32.693093	[{"name": "Summit Entertainment", "id": 491}, ...	...	121.0	[{"iso_639_1": "en", "name": "English"}]	Released	Knowing is everything...	Knowing	5.9	1486	13811	[Nicolas Cage]	[Alex Proyas]
925	50000000	[Comedy, Drama, Romance]	http://crazystupidlove.warnerbros.com/index.html	50646	[soulmates, midlife crisis, marriage crisis, w...	en	Crazy, Stupid, Love.	Cal Weaver is living the American dream. He ha...	37.990705	[{"name": "Warner Bros.", "id": 6194}]	...	118.0	[{"iso_639_1": "en", "name": "English"}]	Released	This Is Stupid	Crazy, Stupid, Love.	7.0	2443	50646	[Steve Carell]	[Glenn Ficarra]
928	50000000	[Drama]	http://www.moneyball-movie.com/	60308	[underdog, based on novel, baseball, teamwork,...	en	Moneyball	The story of Oakland Athletics general manager...	46.180421	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	133.0	[{"iso_639_1": "en", "name": "English"}]	Released	What are you really worth?	Moneyball	7.0	1381	60308	[Brad Pitt]	[Bennett Miller]
932	54000000	[Action, Thriller, Fantasy]	http://vforvendetta.warnerbros.com/	752	[detective, vatican, fascism, satanism, fascis...	en	V for Vendetta	In a world in which Great Britain has become a...	84.630969	[{"name": "Studio Babelsberg", "id": 264}, {"n...	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	People should not be afraid of their governmen...	V for Vendetta	7.7	4442	752	[Natalie Portman]	[James McTeigue]
482 rows × 23 columns


movies_df['overview'][0]
     
'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.'

movies_df['overview']=movies_df['overview'].apply(lambda x:x.split())
     

movies_df
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	runtime	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew
0	237000000	[Action, Adventure, Fantasy, Science Fiction]	http://www.avatarmovie.com/	19995	[culture clash, future, space war, space colon...	en	Avatar	[In, the, 22nd, century,, a, paraplegic, Marin...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[Sam Worthington]	[James Cameron]
1	300000000	[Adventure, Fantasy, Action]	http://disney.go.com/disneypictures/pirates/	285	[ocean, drug abuse, exotic island, east india ...	en	Pirates of the Caribbean: At World's End	[Captain, Barbossa,, long, believed, to, be, d...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[Johnny Depp]	[Gore Verbinski]
2	245000000	[Action, Adventure, Crime]	http://www.sonypictures.com/movies/spectre/	206647	[spy, based on novel, secret agent, sequel, mi...	en	Spectre	[A, cryptic, message, from, Bond’s, past, send...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[Daniel Craig]	[Sam Mendes]
3	250000000	[Action, Crime, Drama, Thriller]	http://www.thedarkknightrises.com/	49026	[dc comics, crime fighter, terrorist, secret i...	en	The Dark Knight Rises	[Following, the, death, of, District, Attorney...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[Christian Bale]	[Christopher Nolan]
4	260000000	[Action, Adventure, Science Fiction]	http://movies.disney.com/john-carter	49529	[based on novel, mars, medallion, space travel...	en	John Carter	[John, Carter, is, a, war-weary,, former, mili...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[Taylor Kitsch]	[Andrew Stanton]
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
921	50000000	[Drama, Comedy, Family]	http://www.weboughtazoo.com/	74465	[zoo]	en	We Bought a Zoo	[Benjamin, has, lost, his, wife, and,, in, a, ...	38.629763	[{"name": "Twentieth Century Fox Film Corporat...	...	124.0	[{"iso_639_1": "en", "name": "English"}]	Released	A True Zoo Story	We Bought a Zoo	6.5	909	74465	[Matt Damon]	[Cameron Crowe]
922	50000000	[Action, Adventure, Drama, Mystery, Science Fi...	http://knowing-themovie.com/	13811	[cataclysm, code, suspense, end of the world, ...	en	Knowing	[A, teacher, opens, a, time, capsule, that, ha...	32.693093	[{"name": "Summit Entertainment", "id": 491}, ...	...	121.0	[{"iso_639_1": "en", "name": "English"}]	Released	Knowing is everything...	Knowing	5.9	1486	13811	[Nicolas Cage]	[Alex Proyas]
925	50000000	[Comedy, Drama, Romance]	http://crazystupidlove.warnerbros.com/index.html	50646	[soulmates, midlife crisis, marriage crisis, w...	en	Crazy, Stupid, Love.	[Cal, Weaver, is, living, the, American, dream...	37.990705	[{"name": "Warner Bros.", "id": 6194}]	...	118.0	[{"iso_639_1": "en", "name": "English"}]	Released	This Is Stupid	Crazy, Stupid, Love.	7.0	2443	50646	[Steve Carell]	[Glenn Ficarra]
928	50000000	[Drama]	http://www.moneyball-movie.com/	60308	[underdog, based on novel, baseball, teamwork,...	en	Moneyball	[The, story, of, Oakland, Athletics, general, ...	46.180421	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	133.0	[{"iso_639_1": "en", "name": "English"}]	Released	What are you really worth?	Moneyball	7.0	1381	60308	[Brad Pitt]	[Bennett Miller]
932	54000000	[Action, Thriller, Fantasy]	http://vforvendetta.warnerbros.com/	752	[detective, vatican, fascism, satanism, fascis...	en	V for Vendetta	[In, a, world, in, which, Great, Britain, has,...	84.630969	[{"name": "Studio Babelsberg", "id": 264}, {"n...	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	People should not be afraid of their governmen...	V for Vendetta	7.7	4442	752	[Natalie Portman]	[James McTeigue]
482 rows × 23 columns


movies_df['genres']=movies_df['genres'].apply(lambda x:[i.replace(" "," ")for i in x])
movies_df['keywords']=movies_df['keywords'].apply(lambda x:[i.replace(" "," ")for i in x])
movies_df['cast']=movies_df['cast'].apply(lambda x:[i.replace(" "," ")for i in x])
movies_df['crew']=movies_df['crew'].apply(lambda x:[i.replace(" "," ")for i in x])
     

movies_df
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	runtime	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew
0	237000000	[Action, Adventure, Fantasy, Science Fiction]	http://www.avatarmovie.com/	19995	[culture clash, future, space war, space colon...	en	Avatar	[In, the, 22nd, century,, a, paraplegic, Marin...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	162.0	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[Sam Worthington]	[James Cameron]
1	300000000	[Adventure, Fantasy, Action]	http://disney.go.com/disneypictures/pirates/	285	[ocean, drug abuse, exotic island, east india ...	en	Pirates of the Caribbean: At World's End	[Captain, Barbossa,, long, believed, to, be, d...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	169.0	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[Johnny Depp]	[Gore Verbinski]
2	245000000	[Action, Adventure, Crime]	http://www.sonypictures.com/movies/spectre/	206647	[spy, based on novel, secret agent, sequel, mi...	en	Spectre	[A, cryptic, message, from, Bond’s, past, send...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	148.0	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[Daniel Craig]	[Sam Mendes]
3	250000000	[Action, Crime, Drama, Thriller]	http://www.thedarkknightrises.com/	49026	[dc comics, crime fighter, terrorist, secret i...	en	The Dark Knight Rises	[Following, the, death, of, District, Attorney...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	165.0	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[Christian Bale]	[Christopher Nolan]
4	260000000	[Action, Adventure, Science Fiction]	http://movies.disney.com/john-carter	49529	[based on novel, mars, medallion, space travel...	en	John Carter	[John, Carter, is, a, war-weary,, former, mili...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[Taylor Kitsch]	[Andrew Stanton]
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
921	50000000	[Drama, Comedy, Family]	http://www.weboughtazoo.com/	74465	[zoo]	en	We Bought a Zoo	[Benjamin, has, lost, his, wife, and,, in, a, ...	38.629763	[{"name": "Twentieth Century Fox Film Corporat...	...	124.0	[{"iso_639_1": "en", "name": "English"}]	Released	A True Zoo Story	We Bought a Zoo	6.5	909	74465	[Matt Damon]	[Cameron Crowe]
922	50000000	[Action, Adventure, Drama, Mystery, Science Fi...	http://knowing-themovie.com/	13811	[cataclysm, code, suspense, end of the world, ...	en	Knowing	[A, teacher, opens, a, time, capsule, that, ha...	32.693093	[{"name": "Summit Entertainment", "id": 491}, ...	...	121.0	[{"iso_639_1": "en", "name": "English"}]	Released	Knowing is everything...	Knowing	5.9	1486	13811	[Nicolas Cage]	[Alex Proyas]
925	50000000	[Comedy, Drama, Romance]	http://crazystupidlove.warnerbros.com/index.html	50646	[soulmates, midlife crisis, marriage crisis, w...	en	Crazy, Stupid, Love.	[Cal, Weaver, is, living, the, American, dream...	37.990705	[{"name": "Warner Bros.", "id": 6194}]	...	118.0	[{"iso_639_1": "en", "name": "English"}]	Released	This Is Stupid	Crazy, Stupid, Love.	7.0	2443	50646	[Steve Carell]	[Glenn Ficarra]
928	50000000	[Drama]	http://www.moneyball-movie.com/	60308	[underdog, based on novel, baseball, teamwork,...	en	Moneyball	[The, story, of, Oakland, Athletics, general, ...	46.180421	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	133.0	[{"iso_639_1": "en", "name": "English"}]	Released	What are you really worth?	Moneyball	7.0	1381	60308	[Brad Pitt]	[Bennett Miller]
932	54000000	[Action, Thriller, Fantasy]	http://vforvendetta.warnerbros.com/	752	[detective, vatican, fascism, satanism, fascis...	en	V for Vendetta	[In, a, world, in, which, Great, Britain, has,...	84.630969	[{"name": "Studio Babelsberg", "id": 264}, {"n...	...	132.0	[{"iso_639_1": "en", "name": "English"}]	Released	People should not be afraid of their governmen...	V for Vendetta	7.7	4442	752	[Natalie Portman]	[James McTeigue]
482 rows × 23 columns


movies_df['tags']= movies_df['overview']+movies_df['genres']+movies_df['keywords']+movies_df['cast']+movies_df['crew']
     

movies_df
     
budget	genres	homepage	id	keywords	original_language	original_title	overview	popularity	production_companies	...	spoken_languages	status	tagline	title	vote_average	vote_count	movie_id	cast	crew	tags
0	237000000	[Action, Adventure, Fantasy, Science Fiction]	http://www.avatarmovie.com/	19995	[culture clash, future, space war, space colon...	en	Avatar	[In, the, 22nd, century,, a, paraplegic, Marin...	150.437577	[{"name": "Ingenious Film Partners", "id": 289...	...	[{"iso_639_1": "en", "name": "English"}, {"iso...	Released	Enter the World of Pandora.	Avatar	7.2	11800	19995	[Sam Worthington]	[James Cameron]	[In, the, 22nd, century,, a, paraplegic, Marin...
1	300000000	[Adventure, Fantasy, Action]	http://disney.go.com/disneypictures/pirates/	285	[ocean, drug abuse, exotic island, east india ...	en	Pirates of the Caribbean: At World's End	[Captain, Barbossa,, long, believed, to, be, d...	139.082615	[{"name": "Walt Disney Pictures", "id": 2}, {"...	...	[{"iso_639_1": "en", "name": "English"}]	Released	At the end of the world, the adventure begins.	Pirates of the Caribbean: At World's End	6.9	4500	285	[Johnny Depp]	[Gore Verbinski]	[Captain, Barbossa,, long, believed, to, be, d...
2	245000000	[Action, Adventure, Crime]	http://www.sonypictures.com/movies/spectre/	206647	[spy, based on novel, secret agent, sequel, mi...	en	Spectre	[A, cryptic, message, from, Bond’s, past, send...	107.376788	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	[{"iso_639_1": "fr", "name": "Fran\u00e7ais"},...	Released	A Plan No One Escapes	Spectre	6.3	4466	206647	[Daniel Craig]	[Sam Mendes]	[A, cryptic, message, from, Bond’s, past, send...
3	250000000	[Action, Crime, Drama, Thriller]	http://www.thedarkknightrises.com/	49026	[dc comics, crime fighter, terrorist, secret i...	en	The Dark Knight Rises	[Following, the, death, of, District, Attorney...	112.312950	[{"name": "Legendary Pictures", "id": 923}, {"...	...	[{"iso_639_1": "en", "name": "English"}]	Released	The Legend Ends	The Dark Knight Rises	7.6	9106	49026	[Christian Bale]	[Christopher Nolan]	[Following, the, death, of, District, Attorney...
4	260000000	[Action, Adventure, Science Fiction]	http://movies.disney.com/john-carter	49529	[based on novel, mars, medallion, space travel...	en	John Carter	[John, Carter, is, a, war-weary,, former, mili...	43.926995	[{"name": "Walt Disney Pictures", "id": 2}]	...	[{"iso_639_1": "en", "name": "English"}]	Released	Lost in our world, found in another.	John Carter	6.1	2124	49529	[Taylor Kitsch]	[Andrew Stanton]	[John, Carter, is, a, war-weary,, former, mili...
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
921	50000000	[Drama, Comedy, Family]	http://www.weboughtazoo.com/	74465	[zoo]	en	We Bought a Zoo	[Benjamin, has, lost, his, wife, and,, in, a, ...	38.629763	[{"name": "Twentieth Century Fox Film Corporat...	...	[{"iso_639_1": "en", "name": "English"}]	Released	A True Zoo Story	We Bought a Zoo	6.5	909	74465	[Matt Damon]	[Cameron Crowe]	[Benjamin, has, lost, his, wife, and,, in, a, ...
922	50000000	[Action, Adventure, Drama, Mystery, Science Fi...	http://knowing-themovie.com/	13811	[cataclysm, code, suspense, end of the world, ...	en	Knowing	[A, teacher, opens, a, time, capsule, that, ha...	32.693093	[{"name": "Summit Entertainment", "id": 491}, ...	...	[{"iso_639_1": "en", "name": "English"}]	Released	Knowing is everything...	Knowing	5.9	1486	13811	[Nicolas Cage]	[Alex Proyas]	[A, teacher, opens, a, time, capsule, that, ha...
925	50000000	[Comedy, Drama, Romance]	http://crazystupidlove.warnerbros.com/index.html	50646	[soulmates, midlife crisis, marriage crisis, w...	en	Crazy, Stupid, Love.	[Cal, Weaver, is, living, the, American, dream...	37.990705	[{"name": "Warner Bros.", "id": 6194}]	...	[{"iso_639_1": "en", "name": "English"}]	Released	This Is Stupid	Crazy, Stupid, Love.	7.0	2443	50646	[Steve Carell]	[Glenn Ficarra]	[Cal, Weaver, is, living, the, American, dream...
928	50000000	[Drama]	http://www.moneyball-movie.com/	60308	[underdog, based on novel, baseball, teamwork,...	en	Moneyball	[The, story, of, Oakland, Athletics, general, ...	46.180421	[{"name": "Columbia Pictures", "id": 5}, {"nam...	...	[{"iso_639_1": "en", "name": "English"}]	Released	What are you really worth?	Moneyball	7.0	1381	60308	[Brad Pitt]	[Bennett Miller]	[The, story, of, Oakland, Athletics, general, ...
932	54000000	[Action, Thriller, Fantasy]	http://vforvendetta.warnerbros.com/	752	[detective, vatican, fascism, satanism, fascis...	en	V for Vendetta	[In, a, world, in, which, Great, Britain, has,...	84.630969	[{"name": "Studio Babelsberg", "id": 264}, {"n...	...	[{"iso_639_1": "en", "name": "English"}]	Released	People should not be afraid of their governmen...	V for Vendetta	7.7	4442	752	[Natalie Portman]	[James McTeigue]	[In, a, world, in, which, Great, Britain, has,...
482 rows × 24 columns


new_df = movies_df[['movie_id','title','tags']]
     

new_df
     
movie_id	title	tags
0	19995	Avatar	[In, the, 22nd, century,, a, paraplegic, Marin...
1	285	Pirates of the Caribbean: At World's End	[Captain, Barbossa,, long, believed, to, be, d...
2	206647	Spectre	[A, cryptic, message, from, Bond’s, past, send...
3	49026	The Dark Knight Rises	[Following, the, death, of, District, Attorney...
4	49529	John Carter	[John, Carter, is, a, war-weary,, former, mili...
...	...	...	...
921	74465	We Bought a Zoo	[Benjamin, has, lost, his, wife, and,, in, a, ...
922	13811	Knowing	[A, teacher, opens, a, time, capsule, that, ha...
925	50646	Crazy, Stupid, Love.	[Cal, Weaver, is, living, the, American, dream...
928	60308	Moneyball	[The, story, of, Oakland, Athletics, general, ...
932	752	V for Vendetta	[In, a, world, in, which, Great, Britain, has,...
482 rows × 3 columns


new_df['tags']= new_df['tags'].apply(lambda x: ' ' .join(x))
     
<ipython-input-40-12274e493146>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  new_df['tags']= new_df['tags'].apply(lambda x: ' ' .join(x))

new_df
     
movie_id	title	tags
0	19995	Avatar	In the 22nd century, a paraplegic Marine is di...
1	285	Pirates of the Caribbean: At World's End	Captain Barbossa, long believed to be dead, ha...
2	206647	Spectre	A cryptic message from Bond’s past sends him o...
3	49026	The Dark Knight Rises	Following the death of District Attorney Harve...
4	49529	John Carter	John Carter is a war-weary, former military ca...
...	...	...	...
921	74465	We Bought a Zoo	Benjamin has lost his wife and, in a bid to st...
922	13811	Knowing	A teacher opens a time capsule that has been d...
925	50646	Crazy, Stupid, Love.	Cal Weaver is living the American dream. He ha...
928	60308	Moneyball	The story of Oakland Athletics general manager...
932	752	V for Vendetta	In a world in which Great Britain has become a...
482 rows × 3 columns


new_df['tags'][0]
     
'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. Action Adventure Fantasy Science Fiction culture clash future space war space colony society space travel futuristic romance space alien tribe alien planet cgi marine soldier battle love affair anti war power relations mind and soul 3d Sam Worthington James Cameron'

new_df['tags']=new_df['tags'].apply(lambda X:X.lower())
     
<ipython-input-43-69ed892c51dc>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  new_df['tags']=new_df['tags'].apply(lambda X:X.lower())

new_df.head()
     
movie_id	title	tags
0	19995	Avatar	in the 22nd century, a paraplegic marine is di...
1	285	Pirates of the Caribbean: At World's End	captain barbossa, long believed to be dead, ha...
2	206647	Spectre	a cryptic message from bond’s past sends him o...
3	49026	The Dark Knight Rises	following the death of district attorney harve...
4	49529	John Carter	john carter is a war-weary, former military ca...

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features= 5000, stop_words='english')
     

cv.fit_transform(new_df['tags']).toarray().shape
     
(482, 5000)

vectors = cv.fit_transform(new_df['tags']).toarray()
     

vectors[0]
     
array([0, 0, 0, ..., 0, 0, 0])

len(cv.get_feature_names_out())
     
5000

import nltk
     

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
     

def stem(text):
  y=[]
  for i in text.split():
      y.append(ps.stem(i))
  return ' '.join(y)
     

new_df['tags']= new_df['tags'].apply(stem)
     
<ipython-input-58-72f81276ac33>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  new_df['tags']= new_df['tags'].apply(stem)

!pip install sklearn
     
Collecting sklearn
  Downloading sklearn-0.0.post10.tar.gz (3.6 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: sklearn
  Building wheel for sklearn (setup.py) ... done
  Created wheel for sklearn: filename=sklearn-0.0.post10-py3-none-any.whl size=2959 sha256=9492665c779caefab716fa424ea5165b528dadf1a6ae6936286ec585bfdaf57e
  Stored in directory: /root/.cache/pip/wheels/5b/f6/92/0173054cc528db7ffe7b0c7652a96c3102aab156a6da960387
Successfully built sklearn
Installing collected packages: sklearn
Successfully installed sklearn-0.0.post10

from sklearn.metrics.pairwise import cosine_similarity
     

cosine_similarity(vectors)
     
array([[1.        , 0.0717496 , 0.0493197 , ..., 0.01324765, 0.        ,
        0.03899064],
       [0.0717496 , 1.        , 0.04364358, ..., 0.035169  , 0.        ,
        0.05175492],
       [0.0493197 , 0.04364358, 1.        , ..., 0.        , 0.04850713,
        0.07905694],
       ...,
       [0.01324765, 0.035169  , 0.        , ..., 1.        , 0.01954408,
        0.02548236],
       [0.        , 0.        , 0.04850713, ..., 0.01954408, 1.        ,
        0.        ],
       [0.03899064, 0.05175492, 0.07905694, ..., 0.02548236, 0.        ,
        1.        ]])

cosine_similarity(vectors).shape
     
(482, 482)

similarity = cosine_similarity(vectors)
     

similarity[0]
     
array([1.        , 0.0717496 , 0.0493197 , 0.02226901, 0.30139814,
       0.13181243, 0.02360632, 0.12781718, 0.03874921, 0.07154548,
       0.06387136, 0.05446449, 0.02478408, 0.1302234 , 0.10418789,
       0.10959932, 0.13631244, 0.06458202, 0.03266277, 0.0531828 ,
       0.03987261, 0.05446449, 0.0614102 , 0.17242311, 0.06756757,
       0.05369248, 0.07837414, 0.14763465, 0.06539441, 0.15949044,
       0.15134153, 0.089687  , 0.03899064, 0.09580705, 0.03193568,
       0.17437146, 0.        , 0.07632031, 0.04244764, 0.07048548,
       0.17732712, 0.08930391, 0.06855912, 0.08348729, 0.23951762,
       0.111154  , 0.02122382, 0.04355036, 0.0717496 , 0.0572711 ,
       0.01453095, 0.25077841, 0.04649906, 0.05086938, 0.03310121,
       0.20475972, 0.07983921, 0.04142465, 0.07261932, 0.11284453,
       0.01911099, 0.26155719, 0.0651117 , 0.01971999, 0.07503753,
       0.01944223, 0.07220717, 0.08664587, 0.07278253, 0.06855912,
       0.17139779, 0.04883378, 0.04595091, 0.20218402, 0.04292729,
       0.24844292, 0.24786635, 0.07352146, 0.04982042, 0.07798129,
       0.15134153, 0.10884606, 0.0833655 , 0.03321361, 0.0856989 ,
       0.02666904, 0.10333123, 0.17860782, 0.17329175, 0.03026831,
       0.02861819, 0.06387136, 0.04702449, 0.03193568, 0.00989566,
       0.05812382, 0.        , 0.0493197 , 0.07974522, 0.06898028,
       0.0585833 , 0.13788836, 0.08053873, 0.01476346, 0.089687  ,
       0.04985222, 0.0551411 , 0.07859775, 0.        , 0.01553424,
       0.02247617, 0.08863799, 0.07009996, 0.19936306, 0.05086938,
       0.09964083, 0.05980892, 0.21137013, 0.09687303, 0.0358748 ,
       0.05299059, 0.01937461, 0.01324765, 0.05733298, 0.05980892,
       0.0572711 , 0.07209373, 0.13880487, 0.07441992, 0.03630966,
       0.0158193 , 0.02861819, 0.01476346, 0.02279804, 0.01476346,
       0.01333452, 0.01275984, 0.07381732, 0.05619042, 0.27820061,
       0.0474579 , 0.05333807, 0.05541889, 0.0847823 , 0.04359286,
       0.03465835, 0.07565296, 0.14523865, 0.01695646, 0.0179374 ,
       0.01420191, 0.04317329, 0.10308798, 0.01861452, 0.03899064,
       0.04604093, 0.06059827, 0.0354552 , 0.06418702, 0.02739983,
       0.1434992 , 0.04874425, 0.04982042, 0.07543143, 0.06782584,
       0.21010508, 0.12304528, 0.17098528, 0.02840382, 0.14704292,
       0.16702954, 0.04054054, 0.03504998, 0.09442528, 0.2908717 ,
       0.0493197 , 0.06269931, 0.03193568, 0.04393748, 0.        ,
       0.12329924, 0.01239204, 0.09802862, 0.04429039, 0.        ,
       0.07009996, 0.06003002, 0.02216755, 0.29255014, 0.04502252,
       0.07974522, 0.01732917, 0.21463643, 0.10397505, 0.03851221,
       0.        , 0.04109975, 0.        , 0.01316245, 0.01232223,
       0.01253531, 0.03193568, 0.0358748 , 0.07009996, 0.0177276 ,
       0.06642722, 0.03487429, 0.        , 0.13709361, 0.03504998,
       0.07916525, 0.03391292, 0.02828679, 0.09320546, 0.03874921,
       0.02721151, 0.        , 0.04109975, 0.0551411 , 0.0531828 ,
       0.0328798 , 0.        , 0.10067341, 0.09964083, 0.04109975,
       0.06387136, 0.04702449, 0.03771571, 0.18693324, 0.0128374 ,
       0.01732917, 0.03929887, 0.        , 0.03805097, 0.        ,
       0.05198752, 0.        , 0.05657357, 0.04047223, 0.03321361,
       0.12708382, 0.12837404, 0.0167789 , 0.0693167 , 0.07091039,
       0.02492611, 0.01627793, 0.        , 0.03987261, 0.01316245,
       0.        , 0.14384911, 0.0179374 , 0.05783536, 0.01732917,
       0.01464583, 0.0585833 , 0.03676073, 0.        , 0.01526406,
       0.07837414, 0.03052813, 0.10283868, 0.01453095, 0.0264953 ,
       0.05442303, 0.02023612, 0.04502252, 0.0614102 , 0.09695723,
       0.1097238 , 0.06269931, 0.02583281, 0.05166562, 0.05841664,
       0.01815483, 0.01993631, 0.01964944, 0.        , 0.0179374 ,
       0.05446449, 0.03391292, 0.01168333, 0.02551967, 0.06855912,
       0.14856673, 0.06711561, 0.1423737 , 0.08948747, 0.06418702,
       0.01732917, 0.03487429, 0.        , 0.13678823, 0.02313414,
       0.        , 0.14384911, 0.        , 0.04796011, 0.        ,
       0.06475993, 0.0847823 , 0.0693167 , 0.02666904, 0.01464583,
       0.        , 0.01351351, 0.03026831, 0.10397505, 0.0474579 ,
       0.06711561, 0.04956816, 0.04317329, 0.27395616, 0.04244764,
       0.05657357, 0.244225  , 0.01660681, 0.02632491, 0.        ,
       0.01964944, 0.        , 0.03321361, 0.0277885 , 0.01218606,
       0.11177489, 0.02840382, 0.09163376, 0.01453095, 0.24198876,
       0.04054054, 0.28593138, 0.09238426, 0.10463105, 0.01815483,
       0.07503753, 0.04229129, 0.03106849, 0.0474579 , 0.04109975,
       0.        , 0.02336665, 0.08108108, 0.04138817, 0.04502252,
       0.06053661, 0.03134966, 0.14474856, 0.        , 0.05198752,
       0.01316245, 0.01513415, 0.05086938, 0.02158664, 0.0930726 ,
       0.08762495, 0.05141934, 0.04393748, 0.        , 0.15007506,
       0.18809794, 0.04660273, 0.        , 0.01612065, 0.01218606,
       0.07974522, 0.05812382, 0.04413495, 0.04168275, 0.        ,
       0.10397505, 0.04175738, 0.02279804, 0.04292729, 0.02976797,
       0.03899064, 0.06642722, 0.05014122, 0.        , 0.16647569,
       0.01389425, 0.04109975, 0.01732917, 0.10283868, 0.04359286,
       0.        , 0.02478408, 0.06448259, 0.25302774, 0.        ,
       0.02536731, 0.0493197 , 0.0164399 , 0.05733298, 0.01211965,
       0.01488398, 0.01513415, 0.02798914, 0.06164962, 0.        ,
       0.        , 0.03224129, 0.        , 0.03052813, 0.        ,
       0.08651247, 0.01971999, 0.0316386 , 0.02324953, 0.03504998,
       0.06711561, 0.01513415, 0.        , 0.03134966, 0.02372895,
       0.23301366, 0.01316245, 0.01911099, 0.        , 0.02798914,
       0.08219949, 0.05638839, 0.06667259, 0.20194517, 0.06590622,
       0.06448259, 0.01861452, 0.10171668, 0.04229129, 0.10171668,
       0.06164962, 0.07983921, 0.06756757, 0.        , 0.07194017,
       0.15288795, 0.        , 0.03193568, 0.0316386 , 0.03427956,
       0.01596784, 0.01369992, 0.        , 0.0164399 , 0.04026936,
       0.02054987, 0.        , 0.03630966, 0.03427956, 0.        ,
       0.02177518, 0.02437213, 0.        , 0.        , 0.03676073,
       0.03106849, 0.0316386 , 0.03771571, 0.01596784, 0.01156707,
       0.05723638, 0.04956816, 0.0328798 , 0.        , 0.02906191,
       0.08053873, 0.08219949, 0.0503367 , 0.0847823 , 0.0354552 ,
       0.08219949, 0.        , 0.01420191, 0.02054987, 0.        ,
       0.01695646, 0.01513415, 0.0164399 , 0.06711561, 0.01324765,
       0.        , 0.03899064])

similarity[0].shape
     
(482,)

sorted(list(enumerate(similarity[0])), reverse= True, key=lambda x:x[1])[1:6]
     
[(4, 0.30139814339315507),
 (188, 0.29255014200233365),
 (174, 0.29087169933823176),
 (331, 0.28593138470052),
 (139, 0.27820060638966515)]

def recommend(movie):
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key= lambda x:x[1])[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)
     

recommend('Avatar')
     
John Carter
Ender's Game
Gravity
Battle: Los Angeles
Home

recommend('Iron Man')
     
Captain America: The First Avenger
Captain America: Civil War
The Avengers
Avengers: Age of Ultron
Ant-Man

recommend('Captain America: Civil War')
     
Spider-Man 3
Spider-Man
The Amazing Spider-Man 2
Batman Begins
The Amazing Spider-Man
