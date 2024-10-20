import openai
openai.api_key = 'sk-proj-Ef0UPqhS80-Edz6mvn-AexAh04Y6phJvD5GCwhn04_XZjk994dzQpEPTQnZtasEikvjjOQylCaT3BlbkFJm6n7nPd7roKNHsCxUN_9qSUgSbi81xuBQyEIQhbEKwcRkQWFWNB3A1CKSQaoU-IFwzGlmo1AA'
messages = [{"role":"system", "content":
             "You are a AI assitant"}]
while True:
    message = input ("User: ")
    if message:
        messages.append (
            {"role":"user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model = "gpt - 3.5-turbo", messages = messages
        )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append ({"role": "assistant", "content":reply})
