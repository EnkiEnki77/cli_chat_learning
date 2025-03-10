# The Open AI API gives access to all of Open AI's various LLM's in your application
import os
from dotenv import  load_dotenv
from openai import OpenAI
from pyexpat.errors import messages

load_dotenv()

api_key = os.environ.get("open_ai_api_key")
base_url = os.environ.get("base_url")

client = OpenAI(api_key=api_key, base_url=base_url)


def get_chat_completion(messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1
    )

# Zero shot prompting is a prompting technique where the model generates responses without specific examples.
# The model receives a prompt, and then it generates a response based on the info in the prompt, and its
# existing knowledge through training. LLM's are trained on large data sets, in which they develop an
# understanding of various language patterns, facts, and relationships. They can then apply this knowledge
# to new prompts, even if unrelated to their training data, without being given an example output.

# In zero shot prompting, LLM's generalize from their training data to produce a relevant output for a prompt
# involving tasks it has not been explicitly trained on.

# The downside of zero-shot prompting is that with no examples the LLM may make incorrect assumptions, or
# offer incomplete answers. Its not great for tasks relying on context or specialized knowledge.

# Below is an example of zero shot prompting, giving the LLM a task to complete, without an example of a
# desired output.
zero_shot_prompt = "Write a short paragraph about the importance of learning how to code with AI tools."

# messages = [
#     {   "role": "user",
#         "content": zero_shot_prompt}
# ]

# Few shot prompts not only provide instructions like zero shot, but also a few examples to guide the
# model's response. The additional context helps models better understand and execute tasks. The examples
# serve as reference points, teaching the model to recognize patterns and context.

# Also allows us to get the LLM to format the response in a more appropriate way for our needs.

# Few shot prompting is best for tasks that rely on examples for generating accurate output. Such as
# natural language processing, and machine translation.

# One of the drawbacks of few shot prompting is if you provide too many examples you can overload the
# model, confusing it. Quality of examples is also important. Choose only a few of the best examples.

# To train the LLM to give you the kind of outputs you want you can give it input and output examples.

# Write an example input, and show the LLM what youd want the example output to be.

few_shot_prompt = "Come up with 5 questions and answers on geography and write them in the following style: Question: What is the capital of France? Answer: Paris."

messages = [
    {   "role": "user",
        "content": few_shot_prompt}
]

# messages = [
#     {"role": "system", "content": "You are a ferocious pirate, traversing the seven seas in search of all it's riches."},
#     {"role": "user", "content": "What are you?"},
# ]

chat_completion = get_chat_completion(messages)
gpt_response = chat_completion.choices[0].message.content

print(gpt_response)


# An AI coding workflow could consist of zero shot prompting to lay out the boilerplate of a program, and
# then zero prompting for more context driven aspects.