def strip_emoticons(s):
    import re
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', s.strip())


import operator
import csv
import os
import json
from watson_developer_cloud import ToneAnalyzerV3
from _codecs import encode

watson_tau="<ea0e446f-7798-403c-9d76-72c80b49066f>" 
watson_tap="<J6IVlX4btGmY>"

tone_analyzer = ToneAnalyzerV3(
    username=watson_tau,
    password=watson_tap,
    version='2016-02-11')
    
with open('output3.csv', "r") as f:
    reader=csv.reader(f)
    for row in reader:
    
        tone_analyzer_result = tone_analyzer.tone(row)
        print row
        print(str(strip_emoticons(s.row)))
    
        document_tone = tone_analyzer_result["document_tone"]
        for tone_categories in document_tone["tone_categories"]:

            # Store emotional attributes
            emotions = {}

            if tone_categories["category_id"] == "emotion_tone":
                for tone in tone_categories["tones"]:
                    print(str(tone["tone_name"]) + ": " + str(round(tone["score"] * 100, 2)))

                print("---------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        