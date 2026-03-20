from dotenv import load_dotenv
from groq import Groq
import os
import json

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

model = "llama-3.3-70b-versatile"

def user_request(message, text):
    user = {"role" : "user" , "content" : text}
    message.append(user)

def assistant_response(message, text):
    ai = {"role" : "assistant" , "content" : text}
    message.append(ai)


def start_assistant(system,temperature, mode):
    messages = []
    if system:
        messages.append({
            "role" : "system",
            "content" : system
        })

    while True:
        user_input = input(">> You >> ")
        if user_input == "exit":
            print(" BYE 👋🏻 ")
            break

        if mode == "4":
            user_request(messages,user_input)
            assistant_response(messages, "```json")

            response = client.chat.completions.create(
                model = model,
                max_tokens = 1000,
                messages = messages,
                stop = ["```"]
            )

            raw = response.choices[0].message.content

            try:
                data = json.loads(raw.strip())
                print(data)
            except:
                print(">> AI >> " + raw)


        elif mode == "5":
            user_request(messages,user_input)
            assistant_response(messages,"```json")

            response = client.chat.completions.create(
                model = model,
                max_tokens = 1000,
                messages = messages,
                stop = ["```"]
            )

            raw = response.choices[0].message.content

            try:
                data = json.loads(raw.strip()) 
                print(data)
            except:
                print(">> AI >> " + raw)
        else:
            user_request(messages, user_input)

            full_response = ""

            with client.chat.completions.create(
                model = model,
                max_tokens = 250,
                messages = messages,
                stream = True
            ) as stream:
                print(">> AI >> " , end = "")
                for chuck in stream:
                    text = chuck.choices[0].delta.content
                    if text:
                        print(text, end = "", flush = True)
                        full_response += text
                print()
            assistant_response(messages,full_response)
            print("------------------------------------------")
