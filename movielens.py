import re#regular expression
#this program is used to load the data from the files and store them in the arrays
#this program basically has three methods that are used to load the data from the files
#the three methods are load_users, load_items, load_ratings
#the three classes are User, Item, Rating that are used to store the data of the users, movies and ratings respectively

#this class is used to store the data of the users
class User:
    def __init__(self, id, age, sex, occupation, zip):
        self.id = int(id)
        self.age = int(age)
        self.sex = sex
        self.occupation = occupation
        self.zip = zip
        self.avg_r = 0.0

#this class is used to store the data of the movies
class Item:
    def __init__(self, id, title, release_date, video_release_date, imdb_url, unknown, action, adventure, animation, childrens, comedy, crime, documentary, drama, fantasy, film_noir, horror, musical, mystery ,romance, sci_fi, thriller, war, western):
        self.id = int(id)
        self.title = title
        self.release_date = release_date
        self.video_release_date = video_release_date
        self.imdb_url = imdb_url
        self.unknown = int(unknown)
        self.action = int(action)
        self.adventure = int(adventure)
        self.animation = int(animation)
        self.childrens = int(childrens)
        self.comedy = int(comedy)
        self.crime = int(crime)
        self.documentary = int(documentary)
        self.drama = int(drama)
        self.fantasy = int(fantasy)
        self.film_noir = int(film_noir)
        self.horror = int(horror)
        self.musical = int(musical)
        self.mystery = int(mystery)
        self.romance = int(romance)
        self.sci_fi = int(sci_fi)
        self.thriller = int(thriller)
        self.war = int(war)
        self.western = int(western)

#this class is used to store the ratings of the users
class Rating:
    def __init__(self, user_id, item_id, rating, time):
        self.user_id = int(user_id)
        self.item_id = int(item_id)
        self.rating = int(rating)
        self.time = time

class Dataset:
    #the load_user method stores the data from the file into the array u
    def load_users(self, file, u):
        f = open(file, "r", encoding="ISO-8859-1")#the encoding is for the special characters

        text = f.read()
        entries = re.split("\n+", text)#split on the basis of new line character
        for entry in entries:#entries is a list of strings entered by the user
            e = entry.split('|', 5)#splitting on the basis of pipe
            if len(e) == 5:
                for i in range(5):
                    u.append(User(e[i]))
        f.close()

    #the load_items method stores the data from the file into the array i
    def load_items(self, file, i):
        f = open(file, "r", encoding="ISO-8859-1")

        text = f.read()
        entries = re.split("\n+", text)#split on the basis of new line character
        for entry in entries:
            e = entry.split('|', 24)#splitting on the basis of pipe
            if len(e) == 24:
                for i in range(24):
                    i.append(e[i])
        f.close()

    #the load_ratings method stores the data from the file into the array r
    def load_ratings(self, file, r):
        f = open(file, "r", encoding="ISO-8859-1")

        text = f.read()
        entries = re.split("\n+", text)#split on the basis of new line character
        for entry in entries:
            e = entry.split('\t', 4)#split on the basis of tab
            if len(e) == 4:
                for i in range(4):
                    r.append(Rating(e[i]))
        f.close()
#closing the files within the function after using is a very good habit so use f.close() 
