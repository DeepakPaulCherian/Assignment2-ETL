import requests
from pandas.io.json import json_normalize

url = "https://jsonplaceholder.typicode.com/users"
resp = requests.get(url=url)
# Handling nested JSON:
df1 = json_normalize(resp.json())
df1.rename(columns = {'address.street':'street','address.suite':'suite','address.city':'city','address.zipcode':'zipcode','address.geo.lat':'latitude','address.geo.lng':'longitude','company.name':'compname','company.catchPhrase':'compcatchPhrase','company.bs':'compbs'}, inplace=True)
df1.head()
df1.to_csv('users.csv')


url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url=url)
# Handling nested JSON:
df2 = json_normalize(resp.json())
df2.head()
df2.to_csv('posts.csv')


url = " https://jsonplaceholder.typicode.com/comments"
resp = requests.get(url=url)
# Handling nested JSON:
df3 = json_normalize(resp.json())
df3.head()
df3.to_csv('comments.csv')


url = "https://jsonplaceholder.typicode.com/todos"
resp = requests.get(url=url)
# Handling nested JSON:
df4 = json_normalize(resp.json())
df4.head()
df4.to_csv('todos.csv')