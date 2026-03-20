from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)
model = "llama-3.3-70b-versatile"

roles = {
    "1" : None,

    "2": """Act as a Professional and very Smart Coder""",

    "3" : """Act as you are a maths tutor. Do not directly
            answer a student's questions. Guide them to a 
            solution step by step. """,

    "4" : """Act as you are a java tutor. Do not directly
            answer the solution or give code. Guide them and 
            help to write a code and to find solution by them self
            step by step.""",

    "5": """Act as a Professional Doctor. Give accurate 
            medical information and diagnosis based on 
            symptoms. Always recommend consulting a 
            real doctor for serious issues."""
}

temperature = {
   "1" : 0.7,
   "2" : 0.2,
   "3" : 0.3,
   "4" : 0.3,
   "5" : 0.0
}

print("Choose Role:")
print("1. None ")
print("2. Coder ")
print("3. Maths Tutor")
print("4. Java Tutor")
print("5. Doctor ")
choice = input("Choice : ")
system = roles[choice]
temperature = temperature[choice]

def user_request(message, text):
    user = {"role" : "user" , "content" : text}
    message.append(user)

def ai_response(message , text):
    ai = {"role" : "assistant" , "content" : text}
    message.append(ai)

messages = []

if system:
   messages.append({
      "role": "system",
      "content": system
   })

while True:
   user_input = input(">> You : ")

   if user_input == "exit":
      print("bye")
      break
   
   user_request(messages, user_input)

   full_response = ""

   with client.chat.completions.create(
      model=model,
      max_tokens = 250,
      messages = messages,
      stream = True
   ) as stream:
      print("AI >> " , end = "")
      for chuck in stream:
         text = chuck.choices[0].delta.content
         if text:
            print(text, end = "", flush = True)
            full_response += text

      print()

   ai_response(messages, full_response)
   print("-------------------------------")
