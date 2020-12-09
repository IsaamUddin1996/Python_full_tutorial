# install pywin32
# Use Json module
# USe Request Module
# Read top 10 news
# Get account on News API
import requests
import json
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.Speak("How are you Sam Zam")

response = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=74961e439f6644e9a8ac41bdc39dd686")

#print(response.text) # response is a data type which comes when we request RESPONSE
jsonData = response.json() #Dictionary mai convert kia
#print("\t\t\tJsonData")
#print(jsonData) # JSON
articles = jsonData.get("articles")
#print("\t\t\tarticles")
#print(articles) # LIST
titleList = []
for index in range(0,len(articles)):
    article = articles[index]
    title = article.get("title")
    titleList.append(title)
print(titleList)
# speak.Speak(titleList)
# for index in range(0,len(titleList)):
    # speak.Speak(titleList[index])
