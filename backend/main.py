"""DeepAgents backend exposed to CopilotKit over AG-UI."""

import os

from ag_ui_langgraph import add_langgraph_fastapi_endpoint
from copilotkit import CopilotKitMiddleware, LangGraphAGUIAgent
from deepagents import create_deep_agent
from dotenv import load_dotenv
from fastapi import FastAPI
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

app = FastAPI(title="DeepAgent Chat Demo")

agent = create_deep_agent(
    model=os.getenv("MODEL", "openai:gpt-4o-mini"),
    tools=[],
    middleware=[CopilotKitMiddleware()],
    system_prompt=(
        "You are a helpful, friendly assistant. Reply in the language used by the user. "
        "Keep answers clear and concise."
    ),
    checkpointer=MemorySaver(),
)

add_langgraph_fastapi_endpoint(
    app=app,
    agent=LangGraphAGUIAgent(
        name="deep_agent",
        description="A conversational LangChain DeepAgent.",
        graph=agent,
    ),
    path="/",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8124, reload=True)
