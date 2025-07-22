try:
    f = open("Advance-Python/Exception-Handling/file.txt", 'w')
    try:
        f.write("I am Rohan Shakya")
    except:
        print("Something went wrong when writing to the file")
    finally:
        print("Closing file...")
        f.close()
except:
    print("Something went wrong when opening the file")
finally: 
    print("File has been successfully written.")