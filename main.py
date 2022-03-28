import tkinter as tk
from tkinter import filedialog, ttk

#pageを遷移
def change_page(page):
    #pageを最前にする
    page.tkraise()

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
    button = {}
    for i in range(4):
        button[i] = ttk.Button(file_select_page,text="send",command=lambda:change_page(select_mix_page))
        button[i].pack()
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
