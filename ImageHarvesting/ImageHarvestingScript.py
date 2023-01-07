import pandas as pd
import openai
import requests
import time
data_path = "YOUR_PATH"
key = "YOUR_OPENAI_KEY"
folder = "YOUR_FOLDER_TO_STORE_IMAGES"

openai.api_key = key



def ImageQueryBuilder(prompt):
    modifier = "In the style of a black-and-white book illustration, draw this: "
    return modifier + prompt

def ImageFetcher(query):
    try:
        imgData = openai.Image.create(
                                  prompt=query,
                                  n=1,
                                  size="512x512"
                                    )
    except Exception as e:
        print(e)
        return "No URL Found."
    
    time.sleep(2)
    print("Image Successfully created!")
    return imgData['data'][0]['url']

def QuoteIndexer(df):
    return {i:ImageQueryBuilder(j) for i,j in zip(df['Index'], df['Quote'])}

def URLIndexer(dicty):
    urls = [ImageFetcher(i) for i in dicty.values()]
    return {i:j for i,j in zip(dicty,urls)}

def ImageWriter(folder, indexed_urls):
    filenames = ["\\Image_{}.jpg".format(index) for index in indexed_urls]
    paths = [folder+filename for filename in filenames]
    
    for i,j in zip(paths,indexed_urls.values()):
        if j == "No URL Found.":
            continue
        img_data = requests.get(j).content
        with open(i, 'wb') as handler:
            handler.write(img_data)

segment_start = 100
segment_end = 200
segment = (segment_start,segment_end)
print(segment)

def Main(data_path, folder, segment):

    df = pd.read_excel(data_path)
    df = df[segment[0]:segment[1]]
    
    print("{} quotes to parse through. Wish me luck! :) ".format(len(df)))

    indexed_quotes = QuoteIndexer(df)
    
    indexed_urls = URLIndexer(indexed_quotes)
    
    ImageWriter(folder, indexed_urls)
    
    return indexed_quotes, indexed_urls


quotes, urls = Main(data_path, folder,segment)            
