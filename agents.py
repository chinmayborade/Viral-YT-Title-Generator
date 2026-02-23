import asyncio
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from prompts import analyzer_prompt, generator_prompt

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY", "")
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

APP_NAME = "youtube_title_app"
USER_ID = "user1"

analyzer_agent = Agent(
    name="AnalyzerAgent",
    model="gemini-2.5-flash",
    instruction="Analyze YouTube titles and extract viral patterns, hooks, and structures.",
)

generator_agent = Agent(
    name="GeneratorAgent",
    model="gemini-2.5-flash",
    instruction="Generate viral YouTube titles based on patterns provided.",
)

def run_agent(agent, prompt: str, session_id: str) -> str:
    session_service = InMemorySessionService()
    runner = Runner(agent=agent, app_name=APP_NAME, session_service=session_service)

    async def _run():
        await session_service.create_session(
            app_name=APP_NAME, user_id=USER_ID, session_id=session_id
        )
        content = types.Content(role="user", parts=[types.Part(text=prompt)])
        final_response = ""
        async for event in runner.run_async(
            user_id=USER_ID, session_id=session_id, new_message=content
        ):
            if event.is_final_response():
                final_response = event.content.parts[0].text
        return final_response

    return asyncio.run(_run())

def run_multi_agent(titles, topic):
    patterns = run_agent(analyzer_agent, analyzer_prompt(titles), "session_analyzer")
    viral_titles = run_agent(generator_agent, generator_prompt(patterns, topic), "session_generator")
    return patterns, viral_titles