import wikipedia

def search(query):

    try:
        return wikipedia.summary(query,2)

    except:
        return "I could not find information."