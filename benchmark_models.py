import os
from openai import OpenAI
import requests
import json


def ClaimReview(query, API_KEY):
    payload = {
      'key': API_KEY,
      'query':query
    }
    url = 'https://factchecktools.googleapis.com/v1alpha1/claims:search'
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        result = json.loads(response.text)
        # Arbitrarily select 1
        try:
            topRating = result["claims"][0]
            # arbitrarily select top 1
            claimReview = topRating["claimReview"][0]["textualRating"]
            claimVal = "According to " + str(topRating["claimReview"][0]['publisher']['name'])+ " that claim is " + str(claimReview)
            return claimVal
        except:
            print("No claim review field found.")
            return 0
    else:
        return response

def ClaimBuster(query, API_KEY):
  api_endpoint = f"https://idir.uta.edu/claimbuster/api/v2/score/text/{query}"

  request_headers = {"x-api-key": API_KEY}
  api_response = requests.get(url=api_endpoint, headers=request_headers)
  return api_response.json()['results'][0]['score']


# categories: ["0 = true; 1 = mostly true; 2 = half true; 3 = mostly false; 4 = false; 5 = pants on fire", 
#              "0 = not misinforming; 1 = misinforming"]

def VanillaGPT(query, categories, API_KEY):
  os.environ["OPENAI_API_KEY"] = API_KEY #insert OpenAI key here
  client = OpenAI(
      api_key=os.environ.get("OPENAI_API_KEY"),
  )

  chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"You are a model that takes in a transcription of a video and outputs a number prediction pertaining to whether the video is misinforming or not misinforming. Classify the following transcription of a short-form video: '{query}' into one of the following categories: '{categories}'. Only output a single number (your prediction); do not have words in your response.",
        }
    ],
    model="gpt-4",
    max_tokens = 1,
  )

  return chat_completion;



