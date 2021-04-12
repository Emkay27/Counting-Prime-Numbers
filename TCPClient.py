from socket import *
from tkinter import *
import tkinter.messagebox

app = Tk()
app.title("Prime Number")
app.geometry('520x360+200+200')

#heading
labelText = StringVar()
labelText.set("Prime Calculator")
label1 = Label(app, textvariable=labelText).pack()

#lowerbound title
labelText = StringVar()
labelText.set("Enter Lower Bound")
label2 = Label(app, textvariable=labelText).place(x=100, y=60)

#lowerbound input-er
lower_bound = StringVar()
lb = Entry(app,textvariable=lower_bound).place(x=240, y=60)

#Upperbound title
labelText = StringVar()
labelText.set("Enter Upper Bound")
label3 = Label(app, textvariable=labelText).place(x=100, y=120)

#Upperbound input-er
upper_bound = StringVar()
ub = Entry(app,textvariable=upper_bound).place(x=240, y=120)
	
#display text
#Time tanken text
labelText = StringVar()
labelText.set("Number of Primes:")
label4 = Label(app, textvariable=labelText).place(x=100, y=180)

#Number of primes text
labelText = StringVar()
labelText.set("Time taken:")
label5 = Label(app, textvariable=labelText).place(x=100, y=240)


def validateInput():
	if (lower_bound.get().isdigit() == False or upper_bound.get().isdigit() == False):
		tkinter.messagebox.showinfo("Error!", "Expected numerical values only or positive values")
		return False
	elif (int(lower_bound.get()) > int(upper_bound.get())):
		tkinter.messagebox.showinfo("Error!", "Lower Bound > Upper Bound\n i.e Lower Bound should < Upper Bound.")
		return False

	return True

def send_recv():
	low_bound = int(lower_bound.get())
	up_bound = int(upper_bound.get())
	
	med = low_bound + ((up_bound - low_bound)//2)

	range1 = [low_bound, med]

	sub_range1 = str(range1)

	serverName = '10.100.5.42'
	serverPort = 1201	
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	clientSocket.send(sub_range1.encode("utf-8"))
	response = clientSocket.recv(1024).decode("utf-8")
	no_of_primes1 = response.split(',')[0]
	time_taken1 = response.split(',')[1]
	clientSocket.close()

	range2 = [med, up_bound]

	sub_range2 = str(range2)

	serverName = '10.100.5.40'
	serverPort = 1201
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	clientSocket.send(sub_range2.encode("utf-8"))
	response = clientSocket.recv(1024).decode("utf-8")
	no_of_primes2 = response.split(',')[0]
	time_taken2 = response.split(',')[1]
	clientSocket.close()
	tot_no_of_primes = eval(no_of_primes1) + eval (no_of_primes2)
	tot_time = eval(time_taken1) + eval(time_taken2)

	labelText = StringVar()
	labelText.set("")
	labelText.set(str(tot_no_of_primes))
	label6 = Label(app, textvariable=labelText).place(x=240, y=180)

	labelText = StringVar()
	labelText.set("")
	labelText.set(str(tot_time))
	label7 = Label(app, textvariable=labelText).place(x=240, y=240)	

def process():
	if (validateInput() == True):
		send_recv()
	else:	
		labelText = StringVar()
		labelText.set("                          ")
		label6 = Label(app, textvariable=labelText).place(x=240, y=180)

		labelText = StringVar()
		labelText.set("                          ")
		label7 = Label(app, textvariable=labelText).place(x=240, y=240)
	
b = Button(app, text="Send", command=process, width=6).place(x=220, y=300)

app.mainloop()
