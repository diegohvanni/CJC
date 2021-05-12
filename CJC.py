#Content JSON Composer (CJC) by Diego H. Vanni - dvanni@paypal.com

#Imports
import os.path
import tkinter as tk

#declaring global variables
jsonData = {} #defining Empty Dictionary Object
label = {}
entry1 = {}
entry2 = {}
entry3 = {}
entry4 = {}

# GUI STARTS
window = tk.Tk()

window.title("CONTENT JSON Composer (CJC)")
canvas = tk.Canvas(window, width = 1000, height = 1000,  relief = 'raised')
canvas.pack()

title = tk.Label(window, text='CONTENT JSON Composer (CJC)')
title.config(font=('helvetica', 22))
canvas.create_window(500, 25, window=title)

label00 = tk.Label(window, text='Enter the number of custom contents (Max 20)')
label00.config(font=('helvetica', 12))
canvas.create_window(390, 100, window=label00)

entry00 = tk.Entry(window)
canvas.create_window(610, 100, window=entry00)

signature = tk.Label(window, text='by Diego H. Vanni - dvanni@paypal.com')
signature.config(font=('helvetica', 12))
canvas.create_window(900, 990, window=signature)

def createJSON():

#creating output file using "UTF-8+BOM" encoding to avoid issues with special char
    o = open(os.getcwd()+"/Content.json", "w+", 1, "utf-8-sig", "Save File Error!") #generating UTF-8+BOM
    o.write("{\"smartling\" : {\"placeholder_format_custom\" : [\"\\\{.*\\\}|@.*?@\"],\"translate_paths\" : [{\"path\" : \"/content/*\",\"exclude_path\" : \"*/keyName\"},{\"path\" : \"/content/*\",\"exclude_path\" : \"*/type\"},{\"path\" : \"/content/*\",\"exclude_path\" : \"*/description\"}]},\"walletNumber\" : 3450004,\"channel\" : \"consumer\",\"content\" : [")

    #variables dictionary
    keyname = {}
    type = {}
    description = {}
    content = {}

    #iterate through entries populating file
    for y in range(int(entry00.get())):

        keyname[y] = entry1[y].get()
        type[y] = entry2[y].get()
        description[y] = entry3[y].get()
        content[y] = entry4[y].get()

    for w in range(len(keyname)):

        if w < len(keyname)-1:
            o.write("{\"keyName\" : \""+keyname[w]+"\",\"type\" : \""+type[w]+"\",\"description\" : \""+description[w]+"\",\"content\" : \""+content[w]+"\"},")
        else:
            o.write("{\"keyName\" : \""+keyname[w]+"\",\"type\" : \""+type[w]+"\",\"description\" : \""+description[w]+"\",\"content\" : \""+content[w]+"\"}")

    #add trailling piece
    o.write("]}")

    #closing output file
    o.close()


    #throwing completion message to the GUI
    conclusionLabel = tk.Label(window, text='Done!')
    conclusionLabel.config(font=('helvetica', 12))
    canvas.create_window(500, 980, window=conclusionLabel)

def cjc():

    #set Y position
    y_distance = 180

    if int(entry00.get()) <= 20:

        #GUI compose extra labels
        fieldLabel1 = tk.Label(window, text='KEYNAME(S)')
        fieldLabel1.config(font=('helvetica', 12))
        canvas.create_window(155, y_distance, window=fieldLabel1)

        fieldLabel2 = tk.Label(window, text='TYPE(S)')
        fieldLabel2.config(font=('helvetica', 12))
        canvas.create_window(355, y_distance, window=fieldLabel2)

        fieldLabel3 = tk.Label(window, text='DESCRIPTION(S)')
        fieldLabel3.config(font=('helvetica', 12))
        canvas.create_window(550, y_distance, window=fieldLabel3)

        fieldLabel4 = tk.Label(window, text='CONTENT(S')
        fieldLabel4.config(font=('helvetica', 12))
        canvas.create_window(740, y_distance, window=fieldLabel4)

        #iterate through values creating multiple entry lines
        for x in range(int(entry00.get())):

            y_distance = y_distance + 30

            label[x] = tk.Label(window, text=str(x+1))
            label[x].config(font=('helvetica', 12))
            canvas.create_window(40, y_distance, window=label[x])

            entry1[x] = tk.Entry(window)
            canvas.create_window(150, y_distance, window=entry1[x])

            entry2[x] = tk.Entry(window)
            canvas.create_window(350, y_distance, window=entry2[x])

            entry3[x] = tk.Entry(window)
            canvas.create_window(550, y_distance, window=entry3[x])

            entry4[x] = tk.Entry(window)
            canvas.create_window(750, y_distance, window=entry4[x])


            #declaring GUI (Compose) button + action
        composeButton = tk.Button(text='Compose JSON file!', command=createJSON, bg='black', fg='black', font=('helvetica', 12, 'bold'))
        canvas.create_window(500, 950, window=composeButton)

#declaring GUI (Next) button + action
button = tk.Button(text='Next', command=cjc, bg='black', fg='black', font=('helvetica', 12, 'bold'))
canvas.create_window(500, 130, window=button)

window.mainloop()