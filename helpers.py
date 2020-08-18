'''All the validation and helper functions are written here'''
from email.utils import parseaddr
import json
import re
from models.Author import Author

def initialize_db(db_file):
    ''' 
        Read the database and create author objects
    '''
    try:
        with open(db_file) as file_pointer:
            database = json.load(file_pointer)
        file_pointer.close()

        authors = []

        for user in database['users']:
            author = Author(user['user_id'], user['name'], user['email'], user['password'])
            author.set_posts(user['posts'])
            authors.append(author)
    
        return authors
    except FileNotFoundError as file_exception:
        return file_exception

    

def get_all_posts(authors):
    '''
    Get all the posts of the author
    '''
    all_posts = []

    for user in authors:
        all_posts = all_posts + user.get_posts()

    return all_posts

def get_all_users(authors):

    '''
    Get all the users
    '''

    all_users = []
    for user in authors:
        all_users.append({
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email
        })

    return all_users

def authenticate_user(authors, email, password):
    '''
    Authenticate user with email and password
    '''
    for user in authors:
        if email == user.email and password == user.password:
            return user.user_id
    return -1

def generate_post_id(authors):
    '''
    Generate unique id for each post
    '''
    return authors[-1].posts[-1]['post_id'] + 1

def validate_email(email):
    ''' 
    Validates the input email
    '''
    return '@' in parseaddr(email)[1]