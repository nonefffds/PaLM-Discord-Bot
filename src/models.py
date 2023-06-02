from typing import List, Dict
import google.generativeai as palm

#class ModelInterface:
#    def chat_completion(self, messages: List[Dict]) -> str:
#        pass

class BardModel(ModelInterface):
    
    def __init__(self,
               api_key: str):
        palm.configure(api_key = "BARD_API_KEY")

    def chat_completion(self, message) -> str:
    # Get the PaLM API response
        response = palm.chat(messages=message, candidate_count = 0)
        output = response.messages[1]
        print (output['content'])