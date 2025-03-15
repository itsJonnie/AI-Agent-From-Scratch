from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# Define the tools
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="search the web for information"
)
api_wrapper = WikipediaAPIWrapper(top_k_results= 1, doc_content_chars_max= 1000)
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper) 
