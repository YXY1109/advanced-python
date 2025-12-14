import os

from agno.agent import Agent
from agno.agent import RunOutput
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv

load_dotenv()

base_url = os.environ["OPENAI_BASE_URL"]
api_key = os.environ["OPENAI_API_KEY"]
model_name = "gpt-3.5-turbo"

agent = Agent(
    model=OpenAIChat(api_key=api_key, id=model_name, base_url=base_url),
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the report. limit the report to 50 words. 使用中文输出",
    markdown=True,
)


def demo1():
    agent.print_response("Trending startups and products.", stream=True)


def demo2():
    response: RunOutput = agent.run(input="Trending startups and products.")
    # Print the response in markdown format
    pprint_run_response(response, markdown=True)


if __name__ == '__main__':
    demo2()
