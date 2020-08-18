'''Entry point for blog application'''
from pprint import pprint
import sys
import helpers

# initialize db
authors = helpers.initialize_db("./data/Database.json")
if isinstance(authors, FileNotFoundError):
    sys.exit("Please specify valid file path")

choices_list = [1, 2, 3, -1]

for choice in choices_list:

    # End user message
    print("\nBlog Post app")
    print("1. Read posts")
    print("2. Read posts by user")
    print("3. Create new post")
    print("-1. Exit")

    try:
        #Get all the posts from all the users
        if choice == 1:
            all_posts = helpers.get_all_posts(authors)
            pprint(all_posts)

        #Get all users except posts
        elif choice == 2:
            all_users = helpers.get_all_users(authors)
            pprint(all_users)
            #user_id = int(input("Enter the user_id from the above list: "))

            #Hardcoding value for jenkins deployment
            USER_ID = 1
            pprint(authors[USER_ID].get_posts())

        # Authenticate user first and then add new post
        elif choice == 3:
            EMAIL = "abc@gmail.com"
            PASSWORD = "abcd"

            if helpers.validate_email(EMAIL):
                user_id = helpers.authenticate_user(authors, EMAIL, PASSWORD)
                TITLE = "Welcome to Quantiphi!"
                post_id = helpers.generate_post_id(authors)
                authors[user_id-1].add_post({
                    "post_id": post_id,
                    "title": TITLE
                })
                print("Post added successfully!")
            else:
                print("Please enter valid email")
        elif choice == -1:
            break

    except TypeError as cached_exception:
        print(cached_exception)
    finally:
        print("Code executed!")
