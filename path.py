file_path="d:\susmitha74\python\pythonlab\path.txt"
with open("d:\susmitha74\python\pythonlab\path.txt","w")as file:
    file.write("HELLO,SUCHIIII")
with open("d:\susmitha74\python\pythonlab\path.txt","r")as file:
    content=file.read()
    print("file content:",content)
