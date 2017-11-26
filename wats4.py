import pandas as pd
from pandas.io.json import json_normalize
import json


from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
  username='id',
  password='pass',
  version='2017-06-16'
)

with open('out1.txt', 'r') as f:
    json_string = f.read()

datas_from_json = json.loads(json_string)

#for data in datas_from_json:
#    tone = tone_analyzer.tone(data['text'])
#    tones='emotion',
#    content_type='text/plain'
#    print(json.dumps(tone, indent=2))

#with open('watsdata.txt', 'w') as outfile:
    
for data in datas_from_json:
    tone = tone_analyzer.tone(data['text'], tones='emotion',content_type='text/plain')
    
#        print (data['text'])
    str = (json.dumps(tone, indent=2))
    print type(str)
    