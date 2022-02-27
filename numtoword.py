
from tkinter import *
app=Tk()
root = Frame()

# specify size of window.

app.geometry("470x400")

# Create text widget and specify size.

T = Text(root, height=15, width=55,bg="#FFFFFF")

# Create label

l = Label(root, text="Enter number...",)

l.config(font=("Courier", 14))
# Function for convertion
def con():
    number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    tens=["Ten", "Eleven", "Twelve", " Thirteen", " Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    nty=["","","Twenty","Thirty","Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

# List used for converting to words
    org=float(T.get(1.0,END))
    n = int(org)


    deci=abs(org%1)  #to get decimal poin number



    if(deci==0): #Condiotion for non decimal point
        out1=""
        org=n

    else:
        org=org
        out1=str(int(deci*100))+"/100 Only" #condition for decimal point




    if org>99999999.99:
        T.delete(1.0, END)
        T.insert(END, "cant solve more than 8 digit or less than 0") #condition for grater 9,99,99,999 and 00
    else:
        T.delete(1.0, END)
        d=[0,0,0,0,0,0,0,0]             #list to store the number which is reversd
        i=0
        while n>0:                      #loop use to reverse the number
            d[i]=n%10
            i+=1
            n=n//10

        num=""                                              #Varible to store the words
        if d[7] != 0:                                       #condition used to print crores
            if (d[7] == 1):
                num += number[d[7]] + " Crore "
            else:
                num += number[d[7]] + " Crore "
        if d[6]!=0:                                         #condition used to print lakhs
            if (d[6]== 1):
                num+=tens[d[5]]+" Lakh "
            else:
                num+=nty[d[6]]+" "+number[d[5]]+" Lakh "
        else:
            if d[5]!=0:
                num+=number[d[5]]+" Lakh "
        if d[4]!=0:                                         #condition used to print Thousands
            if (d[4]== 1):
                num+=tens[d[3]]+" Thousand "
            else:
                num+=nty[d[4]]+" "+number[d[3]]+" Thousand "
        else:
            if d[3]!=0:
                num+=number[d[3]]+" Thousand "
        if d[2]!=0:                                                 #condition used to print Hundreds
            num += number[d[2]] + " Hundred And "
        if d[1] != 0:
            if (d[1] == 1):
                num += tens[d[0]]
            else:
                num += nty[d[1]] + " " + number[d[0]]               #condition used to print Tens
        else:
            if d[0] != 0:                                           #condition used to print ones
                num += number[d[0]]
        if org==0:
            num="zero"
        output=num+ " " +out1



        T.insert(END,str(org)+" in Words is \n"+output)                #print concated statement to print words and decimal point
# Clear the text
def clr():
    T.delete(1.0, END)

# Create button for convert text.

b1 = Button(root, text="Convert",command=con,bg='#191970',fg='#FFFFFF',width=25,padx=10,pady=10)

# Create an Exit button.


b2 = Button(root, text="  Clear  ", command=clr,bg='#191970',fg='#FFFFFF',padx=10,pady=10,)
l.grid(row=0,column=0)
T.grid(row=1,column=0)
b1.grid(row=2,column=0)
b2.grid(row=3,column=0)


root.pack()

app.mainloop()
