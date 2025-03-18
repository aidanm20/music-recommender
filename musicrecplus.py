def loadIn(filename="musicrecplus.txt"):
    "Loads the music database from file named musicreccplus.txt"
    try:
        with open(filename, "r") as file:
            database = {}
            for line in file:
                user, artists = line.strip().split(":")
                database[user] = artists.split(",")
                database[user].sort()
            return database
    except FileNotFoundError:
        return {}

def save(database, filename="musicrecplus.txt"):
    "Saves database to a file"
    with open(filename, "w") as file:
        for (user, artists) in sorted(database.items()):
            file.write(f"{user}:{','.join(sorted(artists))}\n")

def enterPreferences():
    '''allows user to enter artists they like'''
    newArtist = []
    while True:
        artist = input("Enter an artist that you like (Enter to finish): ")
        if artist == '':
            break
        newArtist.append(artist.title())
    return newArtist

def mostPopularArtists(database):
    likes = {}
    for user, artists in database.items():
        if isPrivate(user) != True:
            for user in artists:
                likes[user] = len(artists)
    if not likes == True:
        print("Sorry, no users found.")
        return []
    sortedVal = sorted(likes.keys(), reverse=True)

    return sortedVal

def getRecommendations(current, preferences, userMap):
    bestUser = findBestUser(current, preferences, userMap)
    #print(userMap[bestUser])
    #print(preferences)
    #print(drop(preferences, userMap[bestUser]))
    recommendations = drop(preferences, userMap[bestUser])
    if recommendations == []:
        print("No recommendations available at this time.")
    else:
        for recommendation in recommendations:
            print(recommendation)


def findBestUser(current, preferences, userMap):
    best = None
    bestScore = -1
    for user in userMap.keys():
        score = numMatches(preferences, userMap[user])
        if score > bestScore and current != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    newList = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            print("Skipping", list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            newList.append(list2[j])
            j += 1
    while j < len(list2):
        newList.append(list2[j])
        j += 1
    return newList

def numMatches(list1, list2):
    matches = 0
    i = 0
    j = 0
    while(i < len(list1) and j < len(list2)):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def isPrivate(user):
    if user[len(user)-1:] == "$":
        return True

def howPopular(database):
    count = {}
    for user, artists in database.items():
        if isPrivate(user) != True:
            for artist in artists:
                count[artist] = count.get(artist, 0) + 1

    if not count:
        print("Sorry, no artists found.")
        return 0

    return max(count.values())


def userLikesMostArtists(database):
    likes = {}
    for user, artists in database.items():
        if isPrivate(user) != True:
            likes[user] = len(artists)
    if not likes:
        print("Sorry, no users found.")
        return []

    likeVal = max(likes.values())
    mostLikedUsers = [user for user, count in likes.items() if count == likeVal]
    return sorted(mostLikedUsers)

def saveAndQuit(database, filename="musicrecplus.txt"):
    try:
        with open(filename, "w") as file:
            for user, artists in sorted(database.items()):
                file.write(f"{user}:{','.join(sorted(artists))}\n")
        print(f"Database successfully saved to {filename}. Exiting program.")
    except e:
        print(f"An error occurred while saving the database: {e}")

artists = []
recs = []
def startUpMenu():
    database = loadIn()
    userInput = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private): ")
    if userInput not in database:
        preferences = input("Looks like you are a new user! Please enter your favorite artists:")
        database[userInput] = preferences.split(",")
        save(database)
    while True:
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        userDecision = input("Choose an option: ").strip().lower()
        if userDecision == "e":
            while True:
                favArtist = input("Enter an artist that you like ( Enter to finish ):")
                artists.append(favArtist)
                if favArtist == "":
                    break
                database[userInput] = preferences.split(",")
                save(database)

        elif userDecision == "r":
            recs = getRecommendations(userInput, database[userInput], database)

        elif userDecision == "p":
            sortedVal = mostPopularArtists(database)
            if len(sortedVal) < 3:
                for i in range(len(sortedVal)):
                    print(sortedVal[i])
            else:
                for i in range(3):
                    print(sortedVal[i])

        elif userDecision == "h":
            "gives the number of likes the most popular artist received"
            popularity = howPopular(database)
            if popularity != 0:
                print(popularity)

        elif userDecision == "m":
            "prints full name of user who likes the most artists"
            print("User(s) with the Most Likes:")
            mostLikedUsers = userLikesMostArtists(database)
            for user in mostLikedUsers:
                print(user)
                
        elif userDecision == "q":
            saveAndQuit(database, filename="musicrecplus.txt")
            break
        else:
            print("Invalid option. Please try again")

startUpMenu()

