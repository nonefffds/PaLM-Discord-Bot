from typing import List, Dict
import google.generativeai as palm

class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

class BardModel(ModelInterface):
    
    def __init__(self,
               api_key: str):
        palm.configure(api_key = "BARD_API_KEY")

    def chat_completion(self, messages) -> str:
        response = palm.chat(messages=messages)
        return response