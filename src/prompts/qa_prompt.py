from langchain_core.prompts import ChatPromptTemplate


def get_qa_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        (
            "system",
            """You are an expert document analyst. Answer the user's question
based ONLY on the provided context. If the answer is not in the context,
say "I couldn't find that information in the provided documents."

Always be concise, accurate, and cite which document/page your answer comes from.

Context:
{context}"""
        ),
        ("human", "{question}"),
    ])
