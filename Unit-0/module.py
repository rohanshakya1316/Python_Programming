# pip is the packet manager for python. pip can be used to install module on the system
# pip install django or flask  
import pyjokes

joke = pyjokes.get_joke()
print(joke)