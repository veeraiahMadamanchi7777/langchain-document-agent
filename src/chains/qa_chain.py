from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.vectorstores import VectorStoreRetriever
from src.chains.llm_provider import get_llm
from src.prompts.qa_prompt import get_qa_prompt
from src.utils.logger import get_logger

logger = get_logger(__name__)


def format_docs(docs) -> str:
    return "\n\n".join(
        f"[Source: {doc.metadata.get('filename', 'unknown')} | "
        f"Page: {doc.metadata.get('page', 'N/A')}]\n{doc.page_content}"
        for doc in docs
    )


def build_qa_chain(retriever: VectorStoreRetriever):
    llm = get_llm()
    prompt = get_qa_prompt()

    chain = (
        RunnableParallel(
            context=retriever | format_docs,
            question=RunnablePassthrough(),
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    logger.info("QA chain built")
    return chain
