import os
import re
import requests
from app.models import QARequest, QAResponse
from app.vector_store import create_index, upsert_chunks, search
from llama_parse import LlamaParse
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.messages import HumanMessage

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-70B-Instruct",
    temperature=0.3,
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN")
)

def fetch_pdf(source):
    if source.startswith("http"):
        resp = requests.get(source)
        resp.raise_for_status()
        return resp.content
    with open(source, "rb") as f:
        return f.read()

def chunk_by_headings(text: str):
    pattern = re.compile(r'^(#{1,6}) .+', re.MULTILINE)
    matches = list(pattern.finditer(text))
    chunks = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunks.append(text[start:end].strip())
    return chunks

async def process_qa(request: QARequest) -> QAResponse:
    pdf_bytes = fetch_pdf(request.documents)
    parser = LlamaParse(result_type="markdown")
    docs = parser.load_data(pdf_bytes, extra_info={"file_name": request.documents})
    markdown_text = "\n\n".join(d.text for d in docs)

    chunks = chunk_by_headings(markdown_text)
    create_index(request.index_name, 384)
    index = upsert_chunks(request.index_name, chunks)

    answers = []
    for question in request.questions:
        context = "\n---\n".join(search(index, question, top_k=5))
        prompt = f"""
You are an intelligent assistant that answers insurance policy questions precisely. Answer in one line using only the relevant information.

Context:
{context}

Question:
{question}

Answer:
"""
        message = HumanMessage(content=prompt)
        result = llm([message])
        answers.append(result.content.strip().replace("\n", " "))

    return QAResponse(answers=answers)
