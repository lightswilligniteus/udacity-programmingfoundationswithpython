import os

def rename_files():
  #(1) get file names from a folder
  #() is location path for files
  file_list = os.listdir()
  saved_path = os.getcwd()
  print("Current Working Directory is " + saved_path)
  os.chdir()
  #(2) for each file, rename file
  for file_name in file_list:
      os.rename(file_name, file_name.translate(None, "0123456789"))
  os.chdir(saved_path)

rename_files()
