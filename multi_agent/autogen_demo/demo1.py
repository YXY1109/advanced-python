import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.tools import AgentTool
from autogen_agentchat.ui import Console
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

base_url = os.environ["OPENAI_BASE_URL"]
api_key = os.environ["OPENAI_API_KEY"]
model_name = "gpt-3.5-turbo"
model_client = OpenAIChatCompletionClient(model=model_name, base_url=base_url, api_key=api_key)


def demo0():
    async def main() -> None:
        result = await model_client.create([UserMessage(content="What is the capital of France?", source="user")])
        print(result)
        await model_client.close()

    asyncio.run(main())


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


def demo3():
    # Define a simple function tool that the agent can use.
    # For this example, we use a fake weather tool for demonstration purposes.
    async def get_weather(city: str) -> str:
        """Get the weather for a given city."""
        return f"The weather in {city} is 73 degrees and Sunny."

    # Define an AssistantAgent with the model, tool, system message, and reflection enabled.
    # The system message instructs the agent via natural language.
    agent = AssistantAgent(
        name="weather_agent",
        model_client=model_client,
        tools=[get_weather],
        system_message="You are a helpful assistant.",
        reflect_on_tool_use=True,
        model_client_stream=True,  # Enable streaming tokens from the model client.
    )

    # Run the agent and stream the messages to the console.
    async def main() -> None:
        await Console(agent.run_stream(task="What is the weather in New York?"))
        # Close the connection to the model client.
        await model_client.close()

    # NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
    asyncio.run(main())


def demo4():
    async def main():
        # Create the primary agent.
        primary_agent = AssistantAgent(
            "primary",
            model_client=model_client,
            system_message="You are a helpful AI assistant.",
        )

        # Create the critic agent.
        critic_agent = AssistantAgent(
            "critic",
            model_client=model_client,
            system_message="Provide constructive feedback. Respond with 'APPROVE' to when your feedbacks are addressed.",
        )

        # Define a termination condition that stops the task if the critic approves.
        text_termination = TextMentionTermination("APPROVE")

        # Create a team with the primary and critic agents.
        team = RoundRobinGroupChat([primary_agent, critic_agent], termination_condition=text_termination)

        result = await team.run(task="Write a short poem about the fall season.")
        print(result)

    asyncio.run(main())


if __name__ == '__main__':
    # demo0()
    # demo1()
    # demo2()
    # demo3()
    demo4()
