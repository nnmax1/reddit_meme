import random 
import feedparser


def getUrls(file):
    arr = []
    file1 = open(file, 'r')
    Lines = file1.readlines()
    # Strips the newline character
    for line in Lines:
        arr.append(str(line.strip()))
    file1.close()
    return arr

def redditApi(subreddit):
    xmldata = feedparser.parse("https://www.reddit.com/r/"+subreddit+"/.rss")
    response = []
    for i in range(0, len(xmldata.entries)):
        entry = xmldata.entries[i]
        response.append(entry)
    return response


def memeAPI():
    file = "api_data/subreddits.txt"
    subreddits = getUrls(file)
    value = random.randint(0, len(subreddits)-1)
    sub = subreddits[value]
    memeJson = redditApi(sub)
    response = {}
    response['subreddit'] = "r/"+sub
    memeIndex = random.randint(0, len(memeJson)-1)
    try:
        response['img'] = memeJson[memeIndex]['media_thumbnail'][0]['url']
    except:
        response['img'] = "https://pbs.twimg.com/profile_images/1333471260483801089/OtTAJXEZ_400x400.jpg"
    response['authors'] = memeJson[memeIndex]['authors']    
    response['title'] = memeJson[memeIndex]['title']
    response['updated'] = memeJson[memeIndex]['updated']
    response['published'] = memeJson[memeIndex]['published']
    response['postLink'] = memeJson[memeIndex]['link']
    return response



