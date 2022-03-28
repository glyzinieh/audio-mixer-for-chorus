import tkinter as tk
from tkinter import filedialog, ttk

#pageを遷移
def change_page(page):
    #pageを最前にする
    page.tkraise()

file_list = {}

def file_select_click(i):
    global file_list
    file_list[i] = {}
    file_list[i]["path"] = filedialog.askopenfilename()
    print(file_list)

def main():
    #windowを生成
    root=tk.Tk()
    root.title("合唱練習音源作成用ミックスツール")
    #root.geometry("x")
    #ウィンドウのグリッドを1x1にする
    root.grid_rowconfigure(0,weight=1)
    root.grid_columnconfigure(0,weight=1)
    
    #----------File Select----------
    file_select_page = ttk.Frame(root)
    file_select_widget = {}
    for i in range(4):
        file_select_widget[i] = {}
        file_select_widget[i]["frame"] = ttk.Frame(file_select_page)
        file_select_widget[i]["box"] = ttk.Entry(file_select_widget[i]["frame"])
        file_select_widget[i]["button"] = ttk.Button(file_select_widget[i]["frame"],text="参照",command=lambda:file_select_click(i))
        file_select_widget[i]["name"] = ttk.Entry(file_select_widget[i]["frame"])
        file_select_widget[i]["box"].pack(side=tk.LEFT)
        file_select_widget[i]["button"].pack(side=tk.LEFT)
        file_select_widget[i]["name"].pack(side=tk.LEFT)
        file_select_widget[i]["frame"].pack(side=tk.TOP)
        
    file_select_page.grid(row=0,column=0,sticky="nsew")

    #----------Select Mix----------
    select_mix_page = ttk.Frame(root)
    radio = ttk.Radiobutton(select_mix_page).pack()
    select_mix_page.grid(row=0,column=0,sticky="nsew")

    #実行
    file_select_page.tkraise()
    root.mainloop()

if __name__ == "__main__":
    main()
