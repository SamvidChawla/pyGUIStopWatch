import tkinter as tk

root = tk.Tk()

screen_width = int((root.winfo_screenwidth())-208)
screen_height = int((root.winfo_screenheight())- 150)

root.title("Stop Watch")
root.configure(background='black')
root.geometry(f'200x120+{screen_width}+{screen_height}')

counter, counterm , counterh = 0, 0,0
Stop = False

#Label to display the counter
title = tk.Label(root, text="Stop Watch", font=("Algerian", 24),bg="black",fg="white")
title.pack()
label = tk.Label(root, text="0m , 0s", font=("Ariel", 16),bg="black",fg="white")
label.pack()

def stopfunc():
    
    global counter , counterm , Stop ,player
    Stop = True
    #my_label.pack_forget()
    label.config(text=f"{counterh}h , {counterm}m , {counter}s Elapsed")
    root.after(1000,root.destroy)
    

button = tk.Button(root, text="Terminate", command=stopfunc)
button.pack()

# Defined the update function
def update_label():
    global counter, counterm, counterh , Stop
    if Stop==False:
        counter += 1
        if counter % 60 == 0 and counterh==0:
            counter = 0
            counterm += 1
            label.config(text=f"{counterm}m , {counter}s")
            if counterm%60 == 0:
                counterm=0
                counterh+=1
                label.config(text=f"{counterh}h , {counterm}m , {counter}s")

        elif counter % 60 == 0 and counterh !=0:
            counter=0
            counterm+=1
            if counterm%60 == 0:
                counterm=0
                counterh+=1
            label.config(text=f"{counterh}h , {counterm}m , {counter}s")
                
        if counter % 60 != 0 and counterh ==0:
            label.config(text=f"{counterm}m , {counter}s")
        elif counter % 60 !=0 and counterh!=0:
             label.config(text=f"{counterh}h , {counterm}m , {counter}s")
            
        root.after(1000, update_label)  # Schedule the next update in 1000 ms (1 second)

# Start the updating process
update_label()
root.mainloop()

