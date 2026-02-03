import tkinter as tk
from tkinter import ttk,messagebox

class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.title=("Restaurant Management App")
        self.menu_items={
            "Fries":2,
            "Pizza":4,
            "Tapioca":3,
            "Burger":3,
            "Chicken":4,
            "Japchae":2,
            "Drinks":1
        }

        self.exchange_rate=780

        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Restaurant Order Management",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)

        self.menu_labels={}
        self.menu_quantities={}

        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} (${price}):", font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_labels[item]=label
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item]=quantity_entry

        self.currency_var=tk.StringVar()
        ttk.Label(frame,text="Currency",font=("Arial",12)).grid(row=len(self.menu_items)+1,column=0,padx=10,pady=5)
        currency_dropdown=ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,value=("USD","NAIRA"))
        currency_dropdown.grid(row=len(self.menu_items)+1,column=1,padx=10,pady=5)

        order_button=ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2,columnspan=3,padx=10,pady=5)

    def setup_background(self,root):
        bg_width=800
        bg_height=600
        canvas=tk.Canvas(root,width=bg_width,height=bg_height)
        canvas.pack()
        original_image=tk.PhotoImage(file="menu.png")
        background_image=original_image.subsample(original_image.width()//bg_width,original_image.height()//bg_height)
        canvas.create_image(0,0,anchor=tk.NW,image=background_image)
        canvas.image=background_image

    def update_menu_prices(self,*args):
        currency=self.currency_var.get()
        symbol="#" if currency=="NAIRA" else "$"
        rate=self.exchange_rate if currency=="NAIRA" else 1

        for item,label in self.menu_labels.items():
            price=self.menu_items[item]*rate
            label.config(text=f"{item}({symbol}{price}):")

def place_order(self):
    total_cost = 0
    order_summary = "Order Summary:\n"
    currency = self.currency_var.get()
    symbol = "#" if currency == "NAIRA" else "$"
    rate = self.exchange_rate if currency == "NAIRA" else 1

    for item, entry in self.menu_quantities.items():
        quantity = entry.get()
        if quantity.isdigit():
            quantity = int(quantity)
            price = self.menu_items[item] * rate
            cost = quantity * price
            total_cost += cost

            if quantity > 0:
                order_summary += (f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n")

    if total_cost > 0:
        order_summary += f"\nTotal Cost: {symbol}{total_cost}"
        messagebox.showinfo("Order Placed", order_summary)
    else:
        messagebox.showerror("Error","Please an order for at least one item.")
if __name__=="main":
    root=tk.Tk()
    app=RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()