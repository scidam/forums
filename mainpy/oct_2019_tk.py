from tkinter import *



storage = dict()



def drop_dwn():
    OPTIONS = ["DEV","LB","ST"] #etc
 
    master = Tk()
 
    variable = StringVar(master)
    variable.set("Select_the_Regions") # default value
 
    w = OptionMenu(master, variable, *OPTIONS)
    w.pack()
 
    def ok():
        print ("value is:" + variable.get())
        storage['Region'] = variable.get()
        master.destroy()
    button = Button(master, text="OK", command=ok)
    button.pack()
    print("Exiting")
    
 

def Run_in_soap():
    drop_dwn()
    print("YOU_SELECTED"+storage.get('Region', 'Not defined'))  
   
# create a tkinter window 



root = Tk()               
   
# Open window having dimension 100x100 
root.geometry('100x100')  
   
# Create a Button 
btn = Button(root, text = 'Click me !', bd = '5', 
                          command = Run_in_soap)  
   
# Set the position of button on the top of window.    
btn.pack(side = 'top')     
   
root.mainloop()
