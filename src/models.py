from typing import List, Dict
import google.generativeai as palm

class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

class BardModel(ModelInterface):

    # When using Azure OpenAI API, use following lines. Original OpenAI API are being commented below
    
    def __init__(self,
               api_key: str):
        palm.configure(api_key)

    def chat_completion(self, messages) -> str:
        response = palm.chat(messages=messages)
        return response