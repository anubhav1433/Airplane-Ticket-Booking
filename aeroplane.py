from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from PIL import Image,ImageTk
import webbrowser
root=Tk()
def starter():
    root1=Tk()
    def show():
        root2=Tk()
        def morn():
            root3=Tk()
            def price():
                root4=Tk()
                def congo():
                   messagebox.showinfo("CONGRATULATIONS","YOUR TICKET IS CONFIRMED")
                l=Label(root4,text="YOUR TICKET PRICE IS RS.7489").pack()
                b=Button(root4,text="CLICK TO CONFIRM",command=congo).pack()
            l=Label(root3,text="AVAILABLE FLIGHTS ARE-:").pack()
            c=Checkbutton(root3,text="AIR ASIA (7:05 a.m.)",command=price).pack()
            c1=Checkbutton(root3,text="GO FIRST (9:20 a.m.)",command=price).pack()
            root3.mainloop()
        def aft():
            root3=Tk()
            def price():
                root4=Tk()
                def congo():
                   messagebox.showinfo("CONGRATULATIONS","YOUR TICKET IS CONFIRMED")
                l=Label(root4,text="YOUR TICKET PRICE IS RS.9427").pack()
                b=Button(root4,text="CLICK TO CONFIRM",command=congo).pack()
            l=Label(root3,text="AVAILABLE FLIGHTS ARE-:").pack()
            c=Checkbutton(root3,text="INDIGO (12:20 p.m.)",command=price).pack()
            c1=Checkbutton(root3,text="SPICE JET (2:30 p.m.)",command=price).pack()
            root3.mainloop()
        def ev():
            root3=Tk()
            def price():
                root4=Tk()
                def congo():
                   messagebox.showinfo("CONGRATULATIONS","YOUR TICKET IS CONFIRMED")
                l=Label(root4,text="YOUR TICKET PRICE IS RS.13258").pack()
                b=Button(root4,text="CLICK TO CONFIRM",command=congo).pack()
            l=Label(root3,text="AVAILABLE FLIGHTS ARE-:").pack()
            c=Checkbutton(root3,text="VISTARA (05:15 p.m.)",command=price).pack()
            root3.mainloop()
        def ni():
            root3=Tk()
            def price():
                root4=Tk()
                def congo():
                   messagebox.showinfo("CONGRATULATIONS","YOUR TICKET IS CONFIRMED")
                l=Label(root4,text="YOUR TICKET PRICE IS RS.12267").pack()
                b=Button(root4,text="CLICK TO CONFIRM",command=congo).pack()
            l=Label(root3,text="AVAILABLE FLIGHTS ARE-:").pack()
            c=Checkbutton(root3,text="AIR INDIA (08:00 P.M.)",command=price).pack()
            root3.mainloop()
        l3=Label(root2,text="CHOOSE THE TIME-:").pack()
        b2=Button(root2,text="MORNING FLIGHT",command=morn).pack()
        b3=Button(root2,text="AFTERNOON FLIGHT",command=aft).pack()
        b4=Button(root2,text="EVENING FLIGHT",command=ev).pack()
        b5=Button(root2,text="NIGHT FLIGHT",command=ni).pack()
        b6=Button(root2,text='EXIT',bg='red',command=root1.quit).pack()
    ll=Label(root1,text="CHOOSE THE DATE(in mm/dd/yy) FORMAT FOR TRAVEL:-").pack()
    cal=DateEntry(root1,selectmode='day').pack(padx=20,pady=20)
    l2=Label(root1,text="CHOOSE THE ROUTE").pack()
    c1=Checkbutton(root1,text="BANGALORE TO RANCHI",command=show).pack()
    c2=Checkbutton(root1,text="DELHI TO MUMBAI",command=show).pack()
    c3=Checkbutton(root1,text="KOLKATA TO CHENNAI",command=show).pack()
    c4=Checkbutton(root1,text="HYDERABAD TO BANGALORE",command=show).pack()
    c5=Checkbutton(root1,text="SURAT TO DELHI",command=show).pack()
    b6=Button(root1,text='EXIT',bg='red',command=root1.quit).pack()
    root1.mainloop()
def pay():
    webbrowser.open("file:///C:/Users/Kunal/Desktop/MICKEY/1234.html",new=2)
def webc():
    root1=Tk()
    def show():
        root2=Tk()
        def morn():
            root3=Tk()
            def win():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7989")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7939")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7889")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7839")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7739")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def mid():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7739")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7689")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7639")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7589")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7489")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def ais():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7839")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7789")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7739")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7689")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.7589")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            l=Label(root3,text="CHOOSE THE SEAT").pack()
            c1=Checkbutton(root3,text="WINDOW(Rs.250)",command=win).pack()
            c2=Checkbutton(root3,text="MIDDLE(Rs.0)",command=mid).pack()
            c3=Checkbutton(root3,text="AISLE(Rs.100)",command=ais).pack()
            root3.mainloop()
        def aft():
            root3=Tk()
            def win():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9927")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9877")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9827")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9787")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9687")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def mid():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9677")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9627")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9577")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9527")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9427")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def ais():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9787")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9727")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9687")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9627")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.9527")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            l=Label(root3,text="CHOOSE THE SEAT").pack()
            c1=Checkbutton(root3,text="WINDOW(Rs.250)",command=win).pack()
            c2=Checkbutton(root3,text="MIDDLE(Rs.0)",command=mid).pack()
            c3=Checkbutton(root3,text="AISLE(Rs.100)",command=ais).pack()
            root3.mainloop()
        def ev():
            root3=Tk()
            def win():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13758")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13708")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13658")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13608")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13508")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def mid():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13508")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13458")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13408")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13358")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13258")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def ais():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13608")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13558")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13508")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13458")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.13358")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            l=Label(root3,text="CHOOSE THE SEAT").pack()
            c1=Checkbutton(root3,text="WINDOW(Rs.250)",command=win).pack()
            c2=Checkbutton(root3,text="MIDDLE(Rs.0)",command=mid).pack()
            c3=Checkbutton(root3,text="AISLE(Rs.100)",command=ais).pack()
            root3.mainloop()
        def ni():
            root3=Tk()
            def win():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12767")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12717")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12667")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12617")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12517")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def mid():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12517")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12467")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12317")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12267")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12167")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            def ais():
                root4=Tk()
                def san():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12617")
                def dry():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12567")
                def bhel():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12517")
                def pap():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12467")
                def ne():
                    messagebox.showinfo("CONGRATULATIONS","YOUR WEB CHECK-IN IS CONFIRMED.YOUR FINAL PRICE IS Rs.12367")
                l=Label(root4,text="CHOOSE THE MEAL FOR FLIGHT").pack()
                c1=Checkbutton(root4,text="SANDWICH(Rs.250)",command=san).pack()
                c2=Checkbutton(root4,text="DRY FRUITS(Rs.200)",command=dry).pack()
                c3=Checkbutton(root4,text="BHEL PURI(Rs.150)",command=bhel).pack()
                c4=Checkbutton(root4,text="WAFERS(Rs.150)",command=bhel).pack()
                c5=Checkbutton(root4,text="PAPER BOAT(Rs.100)",command=pap).pack()
                b=Button(root4,text="NEXT",command=ne).pack()
                root4.mainloop()
            l=Label(root3,text="CHOOSE THE SEAT").pack()
            c1=Checkbutton(root3,text="WINDOW(Rs.250)",command=win).pack()
            c2=Checkbutton(root3,text="MIDDLE(Rs.0)",command=mid).pack()
            c3=Checkbutton(root3,text="AISLE(Rs.100)",command=ais).pack()
            root3.mainloop()
        l3=Label(root2,text="CHOOSE YOUR FLIGHT TIME-:").pack()
        b2=Button(root2,text="MORNING FLIGHT",command=morn).pack()
        b3=Button(root2,text="AFTERNOON FLIGHT",command=aft).pack()
        b4=Button(root2,text="EVENING FLIGHT",command=ev).pack()
        b5=Button(root2,text="NIGHT FLIGHT",command=ni).pack()
        b6=Button(root2,text='EXIT',bg='red',command=root1.quit).pack()
        root2.mainloop()
    l2=Label(root1,text="CHOOSE YOUR FLIGHT ROUTE").pack()
    c1=Checkbutton(root1,text="BANGALORE TO RANCHI",command=show).pack()
    c2=Checkbutton(root1,text="DELHI TO MUMBAI",command=show).pack()
    c3=Checkbutton(root1,text="KOLKATA TO CHENNAI",command=show).pack()
    c4=Checkbutton(root1,text="HYDERABAD TO BANGALORE",command=show).pack()
    c5=Checkbutton(root1,text="SURAT TO DELHI",command=show).pack()
    b6=Button(root1,text='EXIT',bg='red',command=root1.quit).pack()
    root1.mainloop()
root.title("AIRPLANE_TICKET_BOOKING")
l1=Label(root,text="WELCOME TO SUNSHINE TRAVELLS").pack()
button_continue=Button(root,text="START BOOKING",bg='blue',command=starter).pack()
b=Button(root,text="WEB CHECK-IN",bg='yellow',command=webc).pack()
b1=Button(root,text="PAYMENT",bg='green',command=pay).pack()
button_quit=Button(root,text='EXIT',bg='red',command=root.quit).pack()
im=ImageTk.PhotoImage(Image.open("aeroimage.jpg"))
i=Label(image=im).pack()
root.mainloop()