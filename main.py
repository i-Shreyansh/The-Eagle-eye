
import os


PATH = os.getcwd()
os.chdir(PATH+"\GUI\LOGIN")
path=os.getcwd()
os.system('python window.py')

os.chdir(PATH+"\GUI\HOME_PAGE")

os.system('python window2.py')

