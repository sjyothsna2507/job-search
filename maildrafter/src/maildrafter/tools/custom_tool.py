from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
import requests
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

class InternetSearchInput(BaseModel):
    query: str = Field(..., description="Search query to look up on the internet.")

class InternetSearchTool(BaseTool):
    name: str = "Search the internet"
    description: str = "Use this tool to search the internet and return relevant results."
    args_schema: Type[BaseModel] = InternetSearchInput  # No SkipValidation here

    def _run(self, query: str) -> str:
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that. Please check the SERPER API key."
        
        results = response.json()['organic']
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([  # Concatenating the search result info
                    f"Title: {result['title']}", 
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", 
                    "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)
