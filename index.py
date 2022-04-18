import time
import random
from colorama import Fore
import tweepy
import secret


client = tweepy.Client(
   consumer_key=secret.CONSUMER_KEY,
   consumer_secret=secret.CONSUMER_SECRET,
   access_token=secret.ACCESS_TOKEN,
   access_token_secret=secret.ACCESS_TOKEN_SECRET
)


def get_txt(quote):
   dots = 1
   for char in quote:
      if char == ':':
         dots += 1
   first = quote.rsplit(':', dots)[0]
   second = quote.rsplit(':', dots)[1]
   if dots <= 3:
      txt = quote.rsplit(':', dots)[2]
   else:
      txt_list = []
      for x in range(dots - 2):
         txt = quote.rsplit(':', dots)[dots - x - 1]
         txt_list.append(txt)
      
      rev_txt = list(reversed(txt_list))
      if len(rev_txt) == 2: txt = rev_txt[0] +":"+ rev_txt[1]
      if len(rev_txt) == 3: txt = rev_txt[0] +":"+ rev_txt[1] +":"+ rev_txt[2]
      if len(rev_txt) == 4: txt = rev_txt[0] +":"+ rev_txt[1] +":"+ rev_txt[2] + rev_txt[3]
      if len(rev_txt) == 5: txt = rev_txt[0] +":"+ rev_txt[1] +":"+ rev_txt[2] +":"+ rev_txt[3] +":"+ rev_txt[4]

   tweet = "("+first+":"+second+")"+txt
   return tweet

def tweet():
   testaments = ["Genesis","exodus","leviticus","numbers","deuteronomy","joshua","judges","ruth","1samuel","2samuel","1kings","2kings","1chronicles","2chronicles","ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","SongofSolomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi"]
   testament = testaments[random.randrange(len(testaments))]

   def getFileLength():
      file_length = open("bible/"+testament+".txt", 'r')
      lines_file = 0
      with file_length as f:
         for _ in f:
            lines_file += 1
      return lines_file

   file = open("bible/"+testament+".txt", 'r')
   rand_quote_num = random.randrange(int(getFileLength()))
   quote_num = 0

   with file as f:
      for line in f:
         if int(quote_num) == int(rand_quote_num): quote = line
         quote_num += 1

   status = client.create_tweet(text=get_txt(quote)+" - " + testament)
   print(status)

while True:
   tweet()
   time.sleep(40000)