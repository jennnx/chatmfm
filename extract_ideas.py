# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

# Goal: Extract "business ideas" from a long-form audio transcription from an interview podcast

system_message = "You are an assistant tasked with analyzing audio transcriptions of an interview podcast."
user_message_1 = "I am giving you a transcription of an interview podcast. The transcription may not be perfect. There might be multiple people speaking at once, making the transcriptions hard to read. Nonetheless, here is your task. In this podcast, there is a lot of random talk, but "

msg = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
)

print(msg)