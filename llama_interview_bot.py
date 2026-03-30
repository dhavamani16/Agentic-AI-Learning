from getpass import getpass
import os
from huggingface_hub import InferenceClient
MODEL_ID="meta-llama/Meta-Llama-3-8B-Instruct"
client=InferenceClient(api_key=os.environ["HF_TOKEN"],model=MODEL_ID)
def extract_text(resp):
  try:
    return resp.choices[0].message.content
  except:
    return str(resp)
messages=[
    {
        "role":"system","content":"Interviewer ask question"

    },{
         "role":"user","content":"What is database with example"
    }

]
resp=client.chat_completion(messages=messages,max_tokens=400)
print(extract_text(resp))
