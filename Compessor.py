def Encoding(stri):
	endodedstring=""
	index=0
	while(index<len(stri)):
		if index<=(len(stri)-1):
			t=index+1
			cnt=1
			while(t<=(len(stri)-1) and stri[t]==stri[index]):
				cnt+=1
				t+=1
			endodedstring+=(str(stri[index])+str(cnt))
			index=t
	if(len(endodedstring)<=len(stri)):
		return endodedstring
	else:
		endodedstring=stri
		return endodedstring
def Decoding(strr):
	decodedstring=""
	index=0
	while(index<len(strr)):
		if index<=(len(strr)-1):
			t=index+1
			times=1
			nu=0
			while(t<=(len(strr)-1) and strr[t].isdigit()):
				nu=(nu*10)+int(strr[t])
				t=t+1
			if nu==0:
				decodedstring=decodedstring+(strr[index])
			else:
				decodedstring=decodedstring+(strr[index]*nu)
			index=t

	return decodedstring

st=input()
r=Encoding(st)
print("encoded string is :"+ r)
s=Decoding(r)
print("decoded string is :"+ s)

