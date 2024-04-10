from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from PIL import Image
import requests
import os

HF_KEY = os.environ.get('HF_KEY')
GOOGLE_KEY = os.environ.get("GOOGLE_API_KEY")

# image to text
def img_to_text(img_path):

 # model presets
  model_id = "vikhyatk/moondream2"
  revision = "2024-04-02"
 # model loading
  model = AutoModelForCausalLM.from_pretrained("vikhyatk/moondream2", trust_remote_code=True)
  tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
  # extracts and generates results
  image = Image.open(img_path)
  enc_image = model.encode_image(image)

  return model.answer_question(enc_image, "Describe this image.", tokenizer)




def text_to_speech(scenario):
  """Text to Speech Model"""

  llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_KEY)

  template = """
    You are a story teller;
    You can generate a short story based on a simple narrative, the story should be no more than 50 words;


    CONTEXT: {scenario}

    STORY: """

  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm

  return chain.invoke({"scenario": scenario})

# text to audio
def speech_to_audio(message):
  # Serverless Inference API
  API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
  headers = {"Authorization": f"Bearer {HF_KEY}"}
  payloads ={
      'inputs': message
  }

 # Generates and saves the audio
  response = requests.post(API_URL, headers=headers, json=payloads)
  with open("audio.flac", "wb") as file:
    file.write(response.content)




