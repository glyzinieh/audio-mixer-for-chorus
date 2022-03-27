import tkinter as tk
from tkinter import filedialog, ttk


#pageを遷移
def change_page(page):
    #pageを最前にする
    page.tkraise()

def select_mix(root_frame):
    select_mix_page = ttk.Frame(root_frame)

def file_select(root_frame):
    file_select_page = ttk.Frame(root_frame)

def main():
    #windowを作成
    root=tk.Tk()
    root.title("合唱練習音源作成用ミックスツール")
    #root.geometry("x")
    #file_selecteを読み込み
    file_select(root)
    #select_mixを読み込み
    select_mix(root)
    #実行
    root.mainloop()

if __name__ == "__main__":
    main()
