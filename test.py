from pymongo import MongoClient


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://atiqur:120125@cluster.5gmbmlt.mongodb.net/book_collection?retryWrites=true&w=majority&appName=Cluster"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["book_collection"]


if __name__ == "__main__":

    dbname = get_database()
    print(dbname)
