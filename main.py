"""
Program name: AnimationStudioMatrix
Date of first writing: 7/21/2023
Author: Sam Goldberg
"""

import requests
from openpyxl import load_workbook

def main():
  print("hello")
  'to download and save the Animation Studios Review file'
  url = "https://docs.google.com/spreadsheets/d/1aJHCQSA2dFdu4Fy__T3yDyiNqO0jMUBcku0EjKX3SZI/edit?pli=1#gid=1656768414"
  r = requests.get(url, allow_redirects=True)
  open('AnimationStudioReviewMatrix', 'wb').write(r.content)


  


if __name__=='main': main()