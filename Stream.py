tobesentdata=dict()
receiveddata=dict()
def ShowData(no,le):
	print(receiveddata)
	n=no
	cnt=0
	try:
		for i in range(le) :
			v=receiveddata.get(n)
			cnt+=1
			n=n+1
		if(cnt==le):
			print(no+le-1)
	except(e):
		print(cnt)
def ToyTcpStream(chunkno,randomchunkk):
	var=chunkno
	for j in randomchunkk:
		receiveddata.update({var:j})
		var+=1
print("Enter the input Stream")
st=input()

for i in range(len(st)):
	tobesentdata.update({(i+1):st[i]})
#print(tobesentdata)
while(True):
		print("enter chunk number enter 0 to show data ")
		chunkno=int(input())
		if(chunkno==0):
			break
		print("enter random size of data that you want to send")
		randomchunk=input()
		if(len(randomchunk)>len(st)):
			print("invalid chunk size")
			continue
		else:
			ToyTcpStream(chunkno,randomchunk)
			ShowData(chunkno,len(randomchunk))#Read Function
