'''Entry point for blog application'''
from pprint import pprint
import sys
import helpers

# initialize db
authors = helpers.initialize_db("./data/Database.json")
if isinstance(authors, FileNotFoundError):
    sys.exit("Please specify valid file path")

while True:

    # End user message
    print("\nBlog Post app")
    print("1. Read posts")
    print("2. Read posts by user")
    print("3. Create new post")
    print("-1. Exit")

    try:
        choice = int(input("Enter the choice: "))

        #Get all the posts from all the users
        if choice == 1:
            all_posts = helpers.get_all_posts(authors)
            pprint(all_posts)

        #Get all users except posts
        elif choice == 2:
            all_users = helpers.get_all_users(authors)
            pprint(all_users)
            user_id = int(input("Enter the user_id from the above list: "))
            pprint(authors[user_id].get_posts())

        # Authenticate user first and then add new post
        elif choice == 3:
            email = input("Enter email: ")
            password = input("Enter password: ")

            if helpers.validate_email(email):
                user_id = helpers.authenticate_user(authors, email, password)
                title = input("Enter title: ")
                post_id = helpers.generate_post_id(authors)
                authors[user_id-1].add_post({
                    "post_id": post_id,
                    "title": title
                })
                print("Post added successfully!")
            else:
                print("Please enter valid email")
        elif choice == -1:
            break

    except TypeError as cached_exception:
        print(cached_exception)
    