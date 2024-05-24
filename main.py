from openai import OpenAI
client = OpenAI(api_key="sk-proj-maJ8LTTnbnAuIoNdfvXoT3BlbkFJisebZVtCCYJ09Reu2lmo")

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "Ты - Влад, живёшь в Каннах, играешь в гранд мобайл, любишь..."},
    {"role": "user", "content": "броу как быстро пропылесосить "}])
print(response.choices[0].message.content)





