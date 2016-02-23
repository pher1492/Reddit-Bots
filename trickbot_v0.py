import praw
import time

r = praw.Reddit(user_agent='Trick List v0 by /u/pher1492')
#get login from file
print("Logging in..")
r.login()

call_bot = ["trickbot:"]
#need to write to file
cache = []
f = open('mem', 'a+')

def run_bot():
  print("Grabbing  Subreddit")
  subreddit = r.get_subreddit("test")
  print("Grabbing Comments")
  comments = subreddit.get_comments(limit=25)
  for comment in comments:
    comment_text = comment.body.lower()
    isMatch = any(string in comment_text for string in call_bot)

#for line in f:
    match = str(f.readline())
#  if str(comment.id) != match and isMatch:
    #make response, shorten string
#    print("1")
    if comment.id not in cache and isMatch:
      print("good")
      f.write(comment.id +'\n')
      trick_list = comment_text.split(': ')
      trick = ''.join(trick_list[1])
      print("Comment ID: " + comment.id)
      comment.reply('[Trick is '+trick+'](https://www.theberrics.com/catalogsearch/result/index?p=1&q='+ trick+')' )
      print("replied")
      cache.append(comment.id)
  print("done looping")

while True:
  run_bot()
  time.sleep(10)


#for line in f:
#  match = str(f.readline())
#  if str(comment.id) != match
  
