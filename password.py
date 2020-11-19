l=0
c=0
s=0
spc=0
n=0
capi_let="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
sma_let="abcdefghijklnopqrstuvwxyz"
spcl_char="$#@"
password=input("Enter the pasdword: ")
if  len(password)>8:
    l=1
for elements in password:
 if elements in capi_let:
    c=1
 elif elements in num:
     n=1
 elif elements in sma_let:
    s=1
 elif elements in spcl_char:
    spc=1
  

if l==1 and c==1 and n==1 and s==1and spc==1:
	print("Valid password")
else:
	print("not valid password")