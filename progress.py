from time import sleep

ESC ="\033"

def progressbar(title, progress, total):
	percent = 100 *(progress/float(total))
	bar = (ESC + "[2;32m━" + ESC + "[m") * int(percent / 2) + (ESC + "[2;0m━" + ESC + "[m") * int((100 - percent) / 2)
	print(f" {title}[{bar}]{percent:.2f}%",end="\r") 
	if progress == total:
		print() 

items = list(range(0,50))
l = len(items)

for i in items:
    progressbar("Processing..",items.index(i)+1, l) 
    sleep(0.1)

for i in items:
    progressbar("Downloading..",items.index(i)+1, l) 
    sleep(0.1)
