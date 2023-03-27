from bs4 import BeautifulSoup
import requests as req
import pandas as pd


target_url="https://opentutorials.org/course/1"

res=req.get(target_url)
res.text