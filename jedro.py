import tkinter as tk
from tkinter import messagebox


okno = tk.Tk()
okno.geometry('550x220')
okno.resizable(width=False, height=False)
okno.title('Pretvornik')
Frame1 = tk.Frame(okno)
Frame2 = tk.Frame(okno)


vrednost = tk.IntVar()
vrednost.set(1)

v = tk.IntVar()
v.set(0)


seznam_konstant = [0.8618, 1.1603, 1.0312, 0.9697, 0.8887, 1.1251,
          3.2808, 0.3048, 0.6213, 1.6093, 0.3937, 2.54,
          2.2046, 0.4535, 0.2641, 3.7854, 158.9873, 0.006289,
          0.00027777, 3600, 0.04166, 24, 0.08333, 12]


seznam_prvih_imen = ['USD', 'EUR', 'CHF', 'USD', 'CHF', 'EUR',
                     'metrov', 'čevljev', 'kilometrov', 'milj', 'centimetrov', 'palcev',
                     'kilogramov', 'funtov', 'litrov', 'galonov', 'litrov', 'sodčkov',
                     'sekund', 'ur', 'ur', 'dni', 'mesecev', 'let']

seznam_drugih_imen = ['EUR', 'USD', 'USD', 'CHF', 'EUR', 'CHF',
                      'čevljev', 'metrov', 'milj', 'kilometrov', 'palcev', 'centimetrov',
                      'funtov', 'kilogramov', 'galonov', 'litrov', 'sodčkov', 'litrov',
                      'ur', 'sekund', 'dni', 'ur', 'let', 'mesecev']





def pretvori():
    output = round(seznam_konstant[v.get()] * vrednost.get(), 4)
    tk.Label(Frame1, text='                                  ').grid(row=5)
    tk.Label(Frame1, text=output).grid(row=5)
    tk.Label(Frame1, text='                                  ').grid(row=1)
    tk.Label(Frame1, text='{0}'.format(seznam_prvih_imen[v.get()])).grid(row=1)
    tk.Label(Frame1, text='                                  ').grid(row=4)
    tk.Label(Frame1, text='{0}'.format(seznam_drugih_imen[v.get()])).grid(row=4)



InputLabel = tk.Label(Frame1, text = ' ')
Input = tk.Entry(Frame1, textvariable=vrednost)
Output = tk.Label(Frame1, text=' ')
OutputLabel = tk.Label(Frame1, text=' ')
Button = tk.Button(Frame1, text='Pretvori',command=pretvori)


InputLabel.grid(row=1)
Input.grid(row=2)
Button.grid(row=3)
OutputLabel.grid(row=4)
Output.grid(row=5)

Frame1.grid(column = 1, row=1)

tk.Radiobutton(Frame2,text = 'USD/EUR', variable = v, value = 0).grid(row=2, column=1)
tk.Radiobutton(Frame2,text = 'EUR/USD', variable = v, value = 1).grid(row=3, column=1)
tk.Radiobutton(Frame2,text = 'CHF/USD', variable = v, value = 2).grid(row=4, column=1)
tk.Radiobutton(Frame2,text = 'USD/CHF', variable = v, value = 3).grid(row=5, column=1)
tk.Radiobutton(Frame2,text = 'CHF/EUR', variable = v, value = 4).grid(row=6, column=1)
tk.Radiobutton(Frame2,text = 'EUR/CHF', variable = v, value = 5).grid(row=7, column=1)

tk.Radiobutton(Frame2,text = 'meter/čevelj', variable = v, value = 6).grid(row=2, column=2)
tk.Radiobutton(Frame2,text = 'čevelj/meter', variable = v, value = 7).grid(row=3, column=2)
tk.Radiobutton(Frame2,text = 'kilometer/milja', variable = v, value = 8).grid(row=4, column=2)
tk.Radiobutton(Frame2,text = 'milja/kilometer', variable = v, value = 9).grid(row=5, column=2)
tk.Radiobutton(Frame2,text = 'centimeter/palec', variable = v, value = 10).grid(row=6, column=2)
tk.Radiobutton(Frame2,text = 'palec/centimeter', variable = v, value = 11).grid(row=7, column=2)

tk.Radiobutton(Frame2,text = 'kilogram/funt', variable = v, value = 12).grid(row=2, column=3)
tk.Radiobutton(Frame2,text = 'funt/kilogram', variable = v, value = 13).grid(row=3, column=3)
tk.Radiobutton(Frame2,text = 'liter/galon', variable = v, value = 14).grid(row=4, column=3)
tk.Radiobutton(Frame2,text = 'galon/liter', variable = v, value = 15).grid(row=5, column=3)
tk.Radiobutton(Frame2,text = 'liter/sodček', variable = v, value = 16).grid(row=6, column=3)
tk.Radiobutton(Frame2,text = 'sodček/liter', variable = v, value = 17).grid(row=7, column=3)

tk.Radiobutton(Frame2,text = 'sekudna/ura', variable = v, value = 18).grid(row=2, column=4)
tk.Radiobutton(Frame2,text = 'ura/sekunda', variable = v, value = 19).grid(row=3, column=4)
tk.Radiobutton(Frame2,text = 'ura/dan', variable = v, value = 20).grid(row=4, column=4)
tk.Radiobutton(Frame2,text = 'dan/ura', variable = v, value = 21).grid(row=5, column=4)
tk.Radiobutton(Frame2,text = 'mesec/leto', variable = v, value = 22).grid(row=6, column=4)
tk.Radiobutton(Frame2,text = 'leto/mesec', variable = v, value = 23).grid(row=7, column=4)

tk.Label(Frame2, text='Valute').grid(row=1, column=1)
tk.Label(Frame2, text='Dolžine').grid(row=1, column=2)
tk.Label(Frame2, text='Mase').grid(row=1, column=3)
tk.Label(Frame2, text='Čas').grid(row=1, column=4)

Frame2.grid(column=2, row=1, pady=20, padx=20)

okno.mainloop()