import os
import openai

openai.api_key = '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'
prompt = "how to stop rain?"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
output_text = response['choices'][0]['text']
print(output_text)
# python integrate_openai.py