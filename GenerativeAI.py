# Importamos Gemini Pro
import google.generativeai as genai
import os
import openai
from dotenv import load_dotenv

# importamos textwrap
import textwrap
# Importamos Markdown de IPython
from IPython.display import Markdown

# Soporte Para Caracteres Especiales en la Terminal de Python
import sys
sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()
openai.api_key = 'sk-proj-tgxTn3tNKXqJmGQ15RRpT3BlbkFJtdBMz4xSkkUlIZET6d0q'
# Usamos el modelo generativo de la IA
modelo = genai.GenerativeModel('gemini-1.5-pro-latest')
# Configuramos la API KEY
GOOGLE_API_KEY=''
genai.configure(api_key=GOOGLE_API_KEY)

#for model in genai.list_models():
def rebajar(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Obtenemos la respuesta
respuesta = modelo.generate_content("Where is new York located")
#audio = open("prueba.mp3", "rb")
#respuesta = openai.Audio.transcribe("whisper-1", audio)
# Imprimimos la respuesta
print(respuesta)