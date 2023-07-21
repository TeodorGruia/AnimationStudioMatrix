"""
Library/Module name: lib_io

Author: Sam Goldberg

For opening the animation studion file and creating a folder to store new versions.
"""
import os
import io
from openpyxl import workbook
from openpyxl import load_workbook

#Make a folder for the file, if one does not already exist.
if os.path.exists("AnimationStudioMatrixFiles") == False:
  os.mkdir("Carts")


def save_to_folder(fname):
  #This needs to refelect saving an excel file
  if os.path.exists("AnimationStudioMatrixFiles") == True:
    workbook.save(rf"AnimationStudioMatrixFiles\{fName}", "w+")

def open_file(name):
  #Open a workbook with the specified name
  load_workbook(filename = name)

