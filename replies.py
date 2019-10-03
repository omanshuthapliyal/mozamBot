#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:10:39 2019

@author: omanshu
"""
import mozambiqueHere as mozBot

import praw
import time
import os

r = praw.Reddit('bot1')
subreddit = r.subreddit("apexlegends")

start = time.time()
    
# Reading file
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
       
replyCounter = 0
lifetime_readCounter = 0
for submission in subreddit.gilded(limit=None):
    print("-----------READING-----------\n")
    print("ID: ", submission.id)
    print("Score: ", submission.score)
    lifetime_readCounter+=1
    if submission.id not in posts_replied_to:
        print("Congratulations on being gilded!\nGold Mozambique here!!!")
        print("Bot replying to : ", submission.id)
        posts_replied_to.append(submission.id)
        replyCounter+=1
        
print("==============================\nRead ",lifetime_readCounter,
      " comments in total")
# Writing to file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
end = time.time()
print(end - start, " seconds elapsed in replying to ", replyCounter, " comments")    
