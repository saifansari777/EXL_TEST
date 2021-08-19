import requests

#api url
url = "https://my-json-server.typicode.com/typicode/demo"


posts_url = url+"/posts"

comments_url = url+'/comments'

#post respone
posts_response = requests.get(posts_url)


post_data = posts_response.json()

#comment response
comments_response = requests.get(comments_url)

comments_data = comments_response.json()

response_data = {}

#putting data into object
for post in post_data:

    id = post["id"]

    for comment in comments_data:
        post_id = comment["postId"]

        if id == post_id :

            if not response_data.get(id):
                
                response_data[id] = {post["title"]:[comment["body"]]}
            else:
                response_data[id][post["title"]].append(comment["body"])


print(response_data)


