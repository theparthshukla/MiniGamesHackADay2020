from tkinter import *
import os
root = Tk()
root.title("Games")

def snakeg():
  os.system('python3 /Users/parth/Desktop/games/snake.py')

def pongg():
  os.system('python3 /Users/parth/Desktop/games/pong.py')

def ticc():
  os.system('python3 /Users/parth/Desktop/games/tic.py')

myButton = Button(root, text = "Snake", command = snakeg, padx = 50, fg = "red")
myButton.pack()

myButton2 = Button(root, text = "Pong", command = pongg, padx = 50, fg = "green")
myButton2.pack()

myButton3 = Button(root, text = "Tic Tac Toe", command = ticc, padx = 50, fg = "blue")
myButton3.pack()

root.mainloop()