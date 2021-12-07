from typing import List, Dict
from fastapi import FastAPI

app = FastAPI()

#list_of_URLS = []

@app.put("/crawled_URLS")
def crawled_URLS(crawl_URLS: Dict[str,List[str]]):
    #for x in crawl_URLS:
    #    print(x)
    #list_of_URLS = crawl_URLS
    return #list_of_URLS


@app.get("/get_outgoing_URLS")
def get_outgoing_URLS(get_URLS: List[str]):
    return #list_of_URLS

@app.delete("/uncrawl_URLS")
def uncrawl_URLs(delete_URLS: List[str]):
    #for x in list_of_URLS:
    #    for y in delete_URLS:
    #        if(x == y):
    #            list_of_URLS.remove(x)
    return #list_of_URLS

@app.put("/run_PageRank")
def run_PageRank():
    return 