'''Database'''
class Author:
    '''
        Author class is for managing users with their posts
    '''
    def __init__(self, user_id, name, email, password):
        '''
            Arguments: 
            user_id: Integer(Unique)
        '''
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.posts = []

    def set_posts(self, posts):
        '''
            Set posts for particular user
            Arguments:
            posts: list()
        '''
        self.posts = posts

    def get_posts(self):
        '''
            Returns: Posts written by user
        '''
        return self.posts

    def add_post(self, post):
        '''
            Add a new post to user
        '''
        self.posts.append(post)
