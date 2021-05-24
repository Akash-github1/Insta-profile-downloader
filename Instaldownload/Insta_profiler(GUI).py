import instaloader
import tkinter as tk

root = tk.Tk()
root.title("Profile Pic Downloader")
root.geometry("600x200+600+200")

def download():
    img = instaloader.Instaloader()
    img.download_profile(user_entry.get(), profile_pic_only=True)
user_var = tk.StringVar()
down_frame = tk.Frame(root, background = 'black',width=600,height=200).place(x=0,y=0)

user_label = tk.Label(root,text='insta id', font=("times new roman",15,"bold"),bg="grey",fg="white")
user_label.grid(row=0,column=1,padx=145,pady=10)

user_entry = tk.Entry(root,bd=2,width=30,textvariable=user_var,relief='sunken',font=("times new roman",15))
user_entry.grid(row=1,column=1,padx=145,pady=10)

download_button = tk.Button(root,text="Download",command=download,width=10,font=("times new roman",14,"bold"),bg="grey",fg="navyblue")
download_button.grid(row=2,column=1)

root.mainloop()