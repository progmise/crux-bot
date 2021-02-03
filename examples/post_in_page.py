import facebook

# It allows us to log in Facebook, using GraphAPI class
# and It creates an object that we can use later to
# use facebook allowed methods.
graph = facebook.GraphAPI(access_token="PAGE_ACCESS_TOKEN",
                          version="2.12")

# By passing parent_object and message parameters
# it allows us to post in feed.
graph.put_object(parent_object='page_id', connection_name='feed',
                 message='post_message')