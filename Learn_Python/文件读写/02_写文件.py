file = open("./test.txt", "a", encoding="UTF-8")
file.write("\nhello!!")
file.flush() # 将内存缓冲区的内容写入磁盘
file.close() # 也会写入磁盘