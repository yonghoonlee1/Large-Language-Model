# pip install -U langchain-community faiss-cpu

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

api_key = ""

loader = TextLoader("rag_example_250905.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embedding = OpenAIEmbeddings(api_key = api_key)
db = FAISS.from_documents(docs, embedding)

retriever = db.as_retriever()
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=api_key)
llm_rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = ""
response = llm_rag_chain.run(query)
print(response)