import re
import openai
import time
import configparser

#创建ConfigParser对象
config = configparser.ConfigParser()

#读取配置文件
config.read("config.ini")

#读取节(section)和键(key)的值(value)
value = config.get("SECTION1", "key1")

# Set up OpenAI API key
openai.api_key = value

# Define a function to prompt the user for input and send it to ChatGPT for a response
def chat(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=2048,
      n=1,
      stop=None,
      temperature=0.5
    )
    return response.choices[0].text.strip()

# Main loop
while True:
    user_input = input("You: ")
    #if re.search(r'[\u4e00-\u9fff]+', user_input):
        #print("Please use English only.")
        #print()
        #continue
    if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
        print("ChatGPT: Goodbye!")
        break
    prompt = f"You say: '{user_input}'. ChatGPT says:"
    print("ChatGPT:")
    print(chat(prompt))
    print()
    time.sleep(1) # wait for a moment to avoid rate limiting
