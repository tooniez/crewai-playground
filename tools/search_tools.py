import json
import requests
import streamlit as st
from langchain.tools import tool


class SearchTools():

  @tool("Search the internet")
  def search_internet(query: str):
    """Useful to search the internet about a given topic and return relevant results"""
    top_result_to_return = 4
    url = "https://google.serper.dev/search"
    
    # If query is a dict, extract the 'topic' value
    if isinstance(query, dict):
      query = query.get('topic', '')
    
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': st.secrets['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # check if there is an organic key
    if 'organic' not in response.json():
      return "Sorry, I couldn't find anything about that, there could be an error with your serper api key."
    else:
      results = response.json()['organic']
      string = []
      for result in results[:top_result_to_return]:
        try:
          string.append('\n'.join([
              f"Title: {result['title']}", f"Link: {result['link']}",
              f"Snippet: {result['snippet']}", "\n-----------------"
          ]))
        except KeyError:
          continue

      return '\n'.join(string)
