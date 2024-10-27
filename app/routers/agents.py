"""Agent router."""

from collections.abc import Callable

from fastapi import APIRouter
from langchain_core.runnables import Runnable as LangchainRunnable

from app.internal.data.agents import AgentInvoke

router = APIRouter(prefix="/v1", tags=["agents"])


def create_agent_handler(agent: LangchainRunnable) -> Callable:
    """Create an agent."""

    async def invoke_agent_handler(payload: AgentInvoke) -> dict[str, str]:
        res = await agent.ainvoke({"messages": payload.messages})
        return res

    return invoke_agent_handler


# from langgraph.graph import StateGraph, START, END
# from typing import TypedDict


# class State(TypedDict):
#     """State."""

#     messages: str


# async def fake_llm(state: State) -> dict[str, str]:
#     """Fake LLM."""
#     return {"messages": "Hello, world!"}


# graph_builder = StateGraph(State)
# graph_builder.add_node("llm", fake_llm)
# graph_builder.add_edge(START, "llm")
# graph_builder.add_edge("llm", END)

# graph = graph_builder.compile()


router.add_api_route("/agents/invoke", create_agent_handler(graph), methods=["POST"])
