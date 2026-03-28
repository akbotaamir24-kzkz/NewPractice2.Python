#Assignment2
#Variant A (251152)
#Amir Akbota // BDA-2504
#Task A1 
name=str(input("Enter customer name:"))
productName=str(input("Enter product name(or 'done' to finish):"))
count=0
subTotal=0

while(productName!="done"):
     price=float(input("Enter price:"))
     subTotal+=price
     count+=1

     productName=str(input("Enter product name:"))

#Task A2
if ( subTotal < 3000):
     dcTier=str("No discount")
     dcRate=0.0

elif(3000<=subTotal<7000):
     dcTier="5%"
     dcRate=0.05

else:   
    dcTier="15%"
    dcRate=0.15

dcAmount=subTotal*dcRate
Total=subTotal-dcAmount

 #Task A3
nLength=len(name)
if len(name)>5:
     resultName="Long name"
else:
     resultName="Short name"

print("-"*20)
print("Name uppercase:",(name.upper()))
print("Name lowercase:",(name.lower()))
print("Name length:", nLength)
print(resultName)
print("Items:", count)
print("Subtotal:", subTotal,"KZT")
print("Discount tier:", dcTier)
print("Discount:", dcAmount, "KZT")
print("Total:", Total , "KZT")