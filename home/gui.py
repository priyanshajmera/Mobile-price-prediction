import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Battery_power(mah)").grid(row=0)
tk.Label(master, text="dual_sim").grid(row=1)
tk.Label(master, text="frontcam(MP)").grid(row=2)
tk.Label(master, text="4g").grid(row=3)
tk.Label(master, text="ROM(GB)").grid(row=4)
tk.Label(master, text="rearcam(MP)").grid(row=5)
tk.Label(master, text="RAM(Mb)").grid(row=6)
tk.Label(master, text="RUN/charge(hr)").grid(row=7)
tk.Label(master, text="Touchscreen").grid(row=8)
tk.Label(master, text="Wifi").grid(row=9)
tk.Label(master, text="PRICE").grid(row=11)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)
e11=tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

e3.grid(row=2, column=1)

e4.grid(row=3, column=1)

e5.grid(row=4, column=1)

e6.grid(row=5, column=1)

e7.grid(row=6, column=1)

e8.grid(row=7, column=1)

e9.grid(row=8, column=1)

e10.grid(row=9, column=1)
e11.grid(row=11, column=1)

def suba():
    l=[]
    l.append(int(e1.get()))
    l.append(int(e2.get()))
    l.append(int(e3.get()))
    l.append(int(e4.get()))
    l.append(int(e5.get()))
    l.append(int(e6.get()))
    l.append(int(e7.get()))
    l.append(int(e8.get()))
    l.append(int(e9.get()))
    l.append(int(e10.get()))
    
    
    
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    
    
    dataset=pd.read_csv('train.csv')
    
    #battery_power	dual_sim	fc	four_g	int_memory	pc	ram	talk_time	touch_screen	wifi
    
    
    
    
    x=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.33,random_state=101)
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    
    
    y_pred=reg.predict(np.array(l).reshape(1,-1))
    
    e11.insert(0,str(int(y_pred))+" Rs.")




    
    
tk.Button(master, 
          text='Submitt', 
          command=suba).grid(row=10, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
master.mainloop()
