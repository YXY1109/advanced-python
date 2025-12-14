import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

base_url = os.environ["OPENAI_BASE_URL"]
api_key = os.environ["OPENAI_API_KEY"]
model_name = "gpt-3.5-turbo"
model_client = OpenAIChatCompletionClient(model=model_name, base_url=base_url, api_key=api_key)


def demo1():
    async def main() -> None:
        agent = AssistantAgent("assistant", model_client=model_client)
        print(await agent.run(task="Say 'Hello World!'"))
        await model_client.close()

    asyncio.run(main())


def demo2():
    async def main() -> None:
        math_agent = AssistantAgent(
            "math_expert",
            model_client=model_client,
            system_message="You are a math expert.",
            description="A math expert assistant.",
            model_client_stream=True,
        )
        math_agent_tool = AgentTool(math_agent, return_value_as_last_message=True)

        chemistry_agent = AssistantAgent(
            "chemistry_expert",
            model_client=model_client,
            system_message="You are a chemistry expert.",
            description="A chemistry expert assistant.",
            model_client_stream=True,
        )
        chemistry_agent_tool = AgentTool(chemistry_agent, return_value_as_last_message=True)

        agent = AssistantAgent(
            "assistant",
            system_message="You are a general assistant. Use expert tools when needed. use chinese to output",
            model_client=model_client,
            model_client_stream=True,
            tools=[math_agent_tool, chemistry_agent_tool],
            max_tool_iterations=10,
        )
        await Console(agent.run_stream(task="What is the integral of x^2?"))
        print("--------------------------------------------------------------------------------")
        await Console(agent.run_stream(task="What is the molecular weight of water?"))

    asyncio.run(main())


if __name__ == '__main__':
    # demo1()
    demo2()
