#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.2
#  in conjunction with Tcl version 8.6
#    May 10, 2020 12:55:32 PM IST  platform: Windows NT
import os
import shutil
import sys
from tkinter import END
from tkinter import filedialog
from tkinter import messagebox
from time import sleep

import cv2
from cv2 import VideoCapture

from GUICommunication import GUICommunication

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import gui_support

print(os.getcwd())


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    gui_support.init(root, top)
    # root.mainloop()
    while True:
        msgs = guiCommunicator.getListOfMessages()
        top.listbox_CameraList.delete(0, tk.END)
        for i in range(len(msgs)):
            # update camera messages
            top.listbox_CameraList.insert(i, msgs[i])
        root.update_idletasks()
        root.update()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("725x613+815+219")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Home Surveillance System")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.main_frame = tk.Frame(top)
        self.main_frame.place(relx=0.014, rely=0.082, relheight=0.904
                              , relwidth=0.971)
        self.main_frame.configure(relief='groove')
        self.main_frame.configure(borderwidth="2")
        self.main_frame.configure(relief="groove")
        self.main_frame.configure(background="#d9d9d9")
        self.main_frame.configure(highlightbackground="#d9d9d9")
        self.main_frame.configure(highlightcolor="black")

        self.frame_register = tk.Frame(self.main_frame)
        self.frame_register.place(relx=0.0, rely=0.0, relheight=1.002
                                  , relwidth=1.0)
        self.frame_register.configure(relief='groove')
        self.frame_register.configure(borderwidth="2")
        self.frame_register.configure(relief="groove")
        self.frame_register.configure(background="#d0d0e8")
        self.frame_register.configure(highlightbackground="#d9d9d9")
        self.frame_register.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.frame_register)
        self.Frame1.place(relx=0.014, rely=0.414, relheight=0.351
                          , relwidth=0.307)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d0d0e8")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1_3 = tk.Label(self.Frame1)
        self.Label1_3.place(relx=0.046, rely=0.041, height=20, width=150)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d0d0e8")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Image count (Default 50)''')

        self.textbox_photoCount = tk.Entry(self.Frame1)
        self.textbox_photoCount.place(relx=0.046, rely=0.205, height=20
                                      , relwidth=0.898)
        self.textbox_photoCount.configure(background="white")
        self.textbox_photoCount.configure(disabledforeground="#a3a3a3")
        self.textbox_photoCount.configure(font="TkFixedFont")
        self.textbox_photoCount.configure(foreground="#000000")
        self.textbox_photoCount.configure(highlightbackground="#d9d9d9")
        self.textbox_photoCount.configure(highlightcolor="black")
        self.textbox_photoCount.configure(insertbackground="black")
        self.textbox_photoCount.configure(selectbackground="#c4c4c4")
        self.textbox_photoCount.configure(selectforeground="black")

        self.btn_takePhoto = tk.Button(self.Frame1, command=self.takePhotos)
        self.btn_takePhoto.place(relx=0.324, rely=0.41, height=24, width=77)
        self.btn_takePhoto.configure(activebackground="#ececec")
        self.btn_takePhoto.configure(activeforeground="#000000")
        self.btn_takePhoto.configure(background="#b3b3d9")
        self.btn_takePhoto.configure(disabledforeground="#a3a3a3")
        self.btn_takePhoto.configure(foreground="#000000")
        self.btn_takePhoto.configure(highlightbackground="#d9d9d9")
        self.btn_takePhoto.configure(highlightcolor="black")
        self.btn_takePhoto.configure(pady="0")
        self.btn_takePhoto.configure(text='''Take Photos''')
        self.btn_takePhoto.configure(state="disabled")

        self.Label1 = tk.Label(self.frame_register)
        self.Label1.place(relx=0.27, rely=0.378, height=21, width=33)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#b3b3d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''2''')

        self.Frame2 = tk.Frame(self.frame_register)
        self.Frame2.place(relx=0.014, rely=0.054, relheight=0.297
                          , relwidth=0.307)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d0d0e8")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        # ============================================================
        # Add owner
        self.Frame3 = tk.Frame(self.frame_register)
        self.Frame3.place(relx=0.35, rely=0.054, relheight=0.71
                          , relwidth=0.62)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d0d0e8")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.lbl_addOwner = tk.Label(self.Frame3)
        self.lbl_addOwner.place(relx=0.03, rely=0.025, height=21, width=80)
        self.lbl_addOwner.configure(activebackground="#f9f9f9")
        self.lbl_addOwner.configure(activeforeground="black")
        self.lbl_addOwner.configure(background="#d0d0e8")
        self.lbl_addOwner.configure(disabledforeground="#a3a3a3")
        self.lbl_addOwner.configure(foreground="#000000")
        self.lbl_addOwner.configure(highlightbackground="#d9d9d9")
        self.lbl_addOwner.configure(highlightcolor="black")
        self.lbl_addOwner.configure(text='''Owner's Name''')

        self.textbox_addOwner = tk.Entry(self.Frame3)
        self.textbox_addOwner.place(relx=0.03, rely=0.075, height=20
                                    , relwidth=0.5)
        self.textbox_addOwner.configure(background="white")
        self.textbox_addOwner.configure(disabledforeground="#a3a3a3")
        self.textbox_addOwner.configure(font="TkFixedFont")
        self.textbox_addOwner.configure(foreground="#000000")
        self.textbox_addOwner.configure(highlightbackground="#d9d9d9")
        self.textbox_addOwner.configure(highlightcolor="black")
        self.textbox_addOwner.configure(insertbackground="black")
        self.textbox_addOwner.configure(selectbackground="#c4c4c4")
        self.textbox_addOwner.configure(selectforeground="black")

        self.btn_addOwner = tk.Button(self.Frame3, command=self.addOwner2TxtFile)
        self.btn_addOwner.place(relx=0.55, rely=0.07, height=24
                                , width=87)
        self.btn_addOwner.configure(activebackground="#ececec")
        self.btn_addOwner.configure(activeforeground="#000000")
        self.btn_addOwner.configure(background="#b3b3d9")
        self.btn_addOwner.configure(disabledforeground="#a3a3a3")
        self.btn_addOwner.configure(foreground="#000000")
        self.btn_addOwner.configure(highlightbackground="#d9d9d9")
        self.btn_addOwner.configure(highlightcolor="black")
        self.btn_addOwner.configure(pady="0")
        self.btn_addOwner.configure(text='''Add Owner''')

        self.btn_delOwner = tk.Button(self.Frame3, command=self.delOwnerFromTxtFile)
        self.btn_delOwner.place(relx=0.3, rely=0.67, height=24
                                , width=87)
        self.btn_delOwner.configure(activebackground="#ececec")
        self.btn_delOwner.configure(activeforeground="#000000")
        self.btn_delOwner.configure(background="#b3b3d9")
        self.btn_delOwner.configure(disabledforeground="#a3a3a3")
        self.btn_delOwner.configure(foreground="#000000")
        self.btn_delOwner.configure(highlightbackground="#d9d9d9")
        self.btn_delOwner.configure(highlightcolor="black")
        self.btn_delOwner.configure(pady="0")
        self.btn_delOwner.configure(text='''Delete Owner''')

        self.listbox_OwnerList = ScrolledListBox(self.Frame3)
        self.listbox_OwnerList.place(relx=0.03, rely=0.15, relheight=0.5
                                     , relwidth=0.725)
        self.listbox_OwnerList.configure(background="white")
        self.listbox_OwnerList.configure(cursor="xterm")
        self.listbox_OwnerList.configure(disabledforeground="#a3a3a3")
        self.listbox_OwnerList.configure(font="TkFixedFont")
        self.listbox_OwnerList.configure(foreground="black")
        self.listbox_OwnerList.configure(highlightbackground="#d9d9d9")
        self.listbox_OwnerList.configure(highlightcolor="#d9d9d9")
        self.listbox_OwnerList.configure(selectbackground="#c4c4c4")
        self.listbox_OwnerList.configure(selectforeground="black")
        # ============================================================
        self.textbox_fname = tk.Entry(self.Frame2)
        self.textbox_fname.place(relx=0.046, rely=0.182, height=20
                                 , relwidth=0.898)
        self.textbox_fname.configure(background="white")
        self.textbox_fname.configure(disabledforeground="#a3a3a3")
        self.textbox_fname.configure(font="TkFixedFont")
        self.textbox_fname.configure(foreground="#000000")
        self.textbox_fname.configure(highlightbackground="#d9d9d9")
        self.textbox_fname.configure(highlightcolor="black")
        self.textbox_fname.configure(insertbackground="black")
        self.textbox_fname.configure(selectbackground="#c4c4c4")
        self.textbox_fname.configure(selectforeground="black")

        self.textbox_lname = tk.Entry(self.Frame2)
        self.textbox_lname.place(relx=0.046, rely=0.545, height=20
                                 , relwidth=0.898)
        self.textbox_lname.configure(background="white")
        self.textbox_lname.configure(disabledforeground="#a3a3a3")
        self.textbox_lname.configure(font="TkFixedFont")
        self.textbox_lname.configure(foreground="#000000")
        self.textbox_lname.configure(highlightbackground="#d9d9d9")
        self.textbox_lname.configure(highlightcolor="black")
        self.textbox_lname.configure(insertbackground="black")
        self.textbox_lname.configure(selectbackground="#c4c4c4")
        self.textbox_lname.configure(selectforeground="black")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.046, rely=0.061, height=21, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d0d0e8")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''First name''')

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.046, rely=0.424, height=21, width=64)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d0d0e8")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Last name''')

        self.btn_personRegister = tk.Button(self.Frame2, command=self.addNewAuthorized)
        self.btn_personRegister.place(relx=0.278, rely=0.727, height=24
                                      , width=87)
        self.btn_personRegister.configure(activebackground="#ececec")
        self.btn_personRegister.configure(activeforeground="#000000")
        self.btn_personRegister.configure(background="#b3b3d9")
        self.btn_personRegister.configure(disabledforeground="#a3a3a3")
        self.btn_personRegister.configure(foreground="#000000")
        self.btn_personRegister.configure(highlightbackground="#d9d9d9")
        self.btn_personRegister.configure(highlightcolor="black")
        self.btn_personRegister.configure(pady="0")
        self.btn_personRegister.configure(text='''Register''')

        self.btn_datasetRefresh = tk.Button(self.frame_register, command=self.refreshDataset)
        self.btn_datasetRefresh.place(relx=0.1, rely=0.8, height=24
                                      , width=87)
        self.btn_datasetRefresh.configure(activebackground="#ececec")
        self.btn_datasetRefresh.configure(activeforeground="#000000")
        self.btn_datasetRefresh.configure(background="#b3b3d9")
        self.btn_datasetRefresh.configure(disabledforeground="#a3a3a3")
        self.btn_datasetRefresh.configure(foreground="#000000")
        self.btn_datasetRefresh.configure(highlightbackground="#d9d9d9")
        self.btn_datasetRefresh.configure(highlightcolor="black")
        self.btn_datasetRefresh.configure(pady="0")
        self.btn_datasetRefresh.configure(text='''Dataset refresh''')

        self.Label2 = tk.Label(self.frame_register)
        self.Label2.place(relx=0.27, rely=0.018, height=21, width=34)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#b3b3d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''1''')

        self.frame_manage = tk.Frame(self.main_frame)
        self.frame_manage.place(relx=0.0, rely=0.0, relheight=1.002
                                , relwidth=0.996)
        self.frame_manage.configure(relief='groove')
        self.frame_manage.configure(borderwidth="2")
        self.frame_manage.configure(relief="groove")
        self.frame_manage.configure(background="#dbdbee")
        self.frame_manage.configure(highlightbackground="#d9d9d9")
        self.frame_manage.configure(highlightcolor="black")

        self.TSeparator1 = ttk.Separator(self.frame_manage)
        self.TSeparator1.place(relx=0.26, rely=-0.004, relheight=1.009)
        self.TSeparator1.configure(orient="vertical")

        self.listbox_PersonList = ScrolledListBox(self.frame_manage)
        self.listbox_PersonList.place(relx=0.014, rely=0.018, relheight=0.964
                                      , relwidth=0.225)
        self.listbox_PersonList.configure(background="white")
        self.listbox_PersonList.configure(cursor="xterm")
        self.listbox_PersonList.configure(disabledforeground="#a3a3a3")
        self.listbox_PersonList.configure(font="TkFixedFont")
        self.listbox_PersonList.configure(foreground="black")
        self.listbox_PersonList.configure(highlightbackground="#d9d9d9")
        self.listbox_PersonList.configure(highlightcolor="#d9d9d9")
        self.listbox_PersonList.configure(selectbackground="#c4c4c4")
        self.listbox_PersonList.configure(selectforeground="black")

        self.listbox_photoList = ScrolledListBox(self.frame_manage)
        self.listbox_photoList.place(relx=0.28, rely=0.018, relheight=0.964
                                     , relwidth=0.579)
        self.listbox_photoList.configure(background="white")
        self.listbox_photoList.configure(cursor="xterm")
        self.listbox_photoList.configure(disabledforeground="#a3a3a3")
        self.listbox_photoList.configure(font="TkFixedFont")
        self.listbox_photoList.configure(foreground="black")
        self.listbox_photoList.configure(highlightbackground="#d9d9d9")
        self.listbox_photoList.configure(highlightcolor="#d9d9d9")
        self.listbox_photoList.configure(selectbackground="#c4c4c4")
        self.listbox_photoList.configure(selectforeground="black")

        self.btn_deleteUser = tk.Button(self.frame_manage, command=self.deleteUser)
        self.btn_deleteUser.place(relx=0.884, rely=0.180, height=24, width=67)
        self.btn_deleteUser.configure(activebackground="#ececec")
        self.btn_deleteUser.configure(activeforeground="#000000")
        self.btn_deleteUser.configure(background="#b3b3d9")
        self.btn_deleteUser.configure(disabledforeground="#a3a3a3")
        self.btn_deleteUser.configure(foreground="#000000")
        self.btn_deleteUser.configure(highlightbackground="#d9d9d9")
        self.btn_deleteUser.configure(highlightcolor="black")
        self.btn_deleteUser.configure(pady="0")
        self.btn_deleteUser.configure(text='''Delete User''')

        self.btn_deletePhotos = tk.Button(self.frame_manage, command=self.deletePhoto)
        self.btn_deletePhotos.place(relx=0.884, rely=0.108, height=24, width=67)
        self.btn_deletePhotos.configure(activebackground="#ececec")
        self.btn_deletePhotos.configure(activeforeground="#000000")
        self.btn_deletePhotos.configure(background="#b3b3d9")
        self.btn_deletePhotos.configure(disabledforeground="#a3a3a3")
        self.btn_deletePhotos.configure(foreground="#000000")
        self.btn_deletePhotos.configure(highlightbackground="#d9d9d9")
        self.btn_deletePhotos.configure(highlightcolor="black")
        self.btn_deletePhotos.configure(pady="0")
        self.btn_deletePhotos.configure(text='''Delete''')

        self.btn_Addphotos = tk.Button(self.frame_manage, command=self.addNewPhoto)
        self.btn_Addphotos.place(relx=0.884, rely=0.036, height=24, width=67)
        self.btn_Addphotos.configure(activebackground="#ececec")
        self.btn_Addphotos.configure(activeforeground="#000000")
        self.btn_Addphotos.configure(background="#b3b3d9")
        self.btn_Addphotos.configure(disabledforeground="#a3a3a3")
        self.btn_Addphotos.configure(foreground="#000000")
        self.btn_Addphotos.configure(highlightbackground="#d9d9d9")
        self.btn_Addphotos.configure(highlightcolor="black")
        self.btn_Addphotos.configure(pady="0")
        self.btn_Addphotos.configure(text='''Add''')

        self.frame_detectLog = tk.Frame(self.main_frame)
        self.frame_detectLog.place(relx=0.0, rely=0.0, relheight=1.002
                                   , relwidth=1.0)
        self.frame_detectLog.configure(relief='groove')
        self.frame_detectLog.configure(borderwidth="2")
        self.frame_detectLog.configure(relief="groove")
        self.frame_detectLog.configure(background="#d0d0e8")
        self.frame_detectLog.configure(highlightbackground="#d9d9d9")
        self.frame_detectLog.configure(highlightcolor="black")

        self.textbox_facelog = ScrolledText(self.frame_detectLog)
        try:
            open("detectionlog.txt", "r").close()
        except:
            open("detectionlog.txt", "w").close()
        logfile = open('detectionlog.txt', 'r')
        for entry in logfile:
            self.textbox_facelog.insert(tk.INSERT, entry)
        logfile.close()
        self.textbox_facelog.place(relx=0.0, rely=0.0, relheight=1.0
                                   , relwidth=0.5)
        self.textbox_facelog.configure(background="white")
        self.textbox_facelog.configure(font="TkTextFont")
        self.textbox_facelog.configure(foreground="black")
        self.textbox_facelog.configure(highlightbackground="#d9d9d9")
        self.textbox_facelog.configure(highlightcolor="black")
        self.textbox_facelog.configure(insertbackground="black")
        self.textbox_facelog.configure(insertborderwidth="3")
        self.textbox_facelog.configure(selectbackground="#c4c4c4")
        self.textbox_facelog.configure(selectforeground="black")
        self.textbox_facelog.configure(wrap="none")
        self.textbox_facelog.configure(state="disabled")

        self.btn_clrLog = tk.Button(self.frame_detectLog, command=self.clearlog)
        self.btn_clrLog.place(relx=0.68, rely=0.018, height=30, width=100)
        self.btn_clrLog.configure(activebackground="#ececec")
        self.btn_clrLog.configure(activeforeground="#000000")
        self.btn_clrLog.configure(background="#b3b3d9")
        self.btn_clrLog.configure(disabledforeground="#a3a3a3")
        self.btn_clrLog.configure(foreground="#000000")
        self.btn_clrLog.configure(highlightbackground="#d9d9d9")
        self.btn_clrLog.configure(highlightcolor="black")
        self.btn_clrLog.configure(pady="0")
        self.btn_clrLog.configure(text='''Clear Log''')

        self.listbox_CameraList = ScrolledListBox(self.frame_detectLog,height=20)
        self.listbox_CameraList.place(relx=0.52, rely=0.1, relheight=0.83, relwidth=0.46)
        self.listbox_CameraList.configure(background="white")
        self.listbox_CameraList.configure(cursor="xterm")
        self.listbox_CameraList.configure(disabledforeground="#a3a3a3")
        self.listbox_CameraList.configure(font="TkFixedFont")
        self.listbox_CameraList.configure(foreground="black")
        self.listbox_CameraList.configure(highlightbackground="#d9d9d9")
        self.listbox_CameraList.configure(highlightcolor="#d9d9d9")
        self.listbox_CameraList.configure(selectbackground="#c4c4c4")
        self.listbox_CameraList.configure(selectforeground="black")

        self.btn_register = tk.Button(top, command=self.show_registerPanel)
        self.btn_register.place(relx=0.014, rely=0.016, height=34, width=100)
        self.btn_register.configure(activebackground="#ececec")
        self.btn_register.configure(activeforeground="#000000")
        self.btn_register.configure(background="#b3b3d9")
        self.btn_register.configure(disabledforeground="#a3a3a3")
        self.btn_register.configure(foreground="#000000")
        self.btn_register.configure(highlightbackground="#d9d9d9")
        self.btn_register.configure(highlightcolor="black")
        self.btn_register.configure(pady="0")
        self.btn_register.configure(text='''Register Face''')

        self.btn_ManageFaces = tk.Button(top, command=self.show_managePanel)
        self.btn_ManageFaces.place(relx=0.152, rely=0.016, height=34, width=110)
        self.btn_ManageFaces.configure(activebackground="#ececec")
        self.btn_ManageFaces.configure(activeforeground="#000000")
        self.btn_ManageFaces.configure(background="#b3b3d9")
        self.btn_ManageFaces.configure(disabledforeground="#a3a3a3")
        self.btn_ManageFaces.configure(foreground="#000000")
        self.btn_ManageFaces.configure(highlightbackground="#d9d9d9")
        self.btn_ManageFaces.configure(highlightcolor="black")
        self.btn_ManageFaces.configure(pady="0")
        self.btn_ManageFaces.configure(text='''Manage Faces''')

        self.btn_facelog = tk.Button(top, command=self.show_detectLogPanel)
        self.btn_facelog.place(relx=0.303, rely=0.016, height=34, width=110)
        self.btn_facelog.configure(activebackground="#ececec")
        self.btn_facelog.configure(activeforeground="#000000")
        self.btn_facelog.configure(background="#b3b3d9")
        self.btn_facelog.configure(disabledforeground="#a3a3a3")
        self.btn_facelog.configure(foreground="#000000")
        self.btn_facelog.configure(highlightbackground="#d9d9d9")
        self.btn_facelog.configure(highlightcolor="black")
        self.btn_facelog.configure(pady="0")
        self.btn_facelog.configure(text='''Detection Log''')

        #     event listeners
        self.listbox_PersonList.bind('<Double-Button-1>', self.getPicsByDirName)
        self.listbox_photoList.bind('<Double-Button-1>', self.displayPhoto)

    # user defined event triggers------------
    def show_registerPanel(self):
        self.frame_manage.place_forget()
        self.frame_detectLog.place_forget()
        self.frame_register.place(relx=0.0, rely=0.0, relheight=1.002
                                  , relwidth=1.0)
        if not os.path.exists("owner_email.txt"):
            open("owner_email.txt", 'w').close()
        mailIdFile = open("owner_email.txt", 'r')
        mailIds = mailIdFile.readlines()
        self.listbox_OwnerList.delete(0, tk.END)
        for i in range(len(mailIds)):
            self.listbox_OwnerList.insert(i, mailIds[i])
        mailIdFile.close()

    def show_managePanel(self):
        self.frame_detectLog.place_forget()
        self.frame_register.place_forget()
        self.frame_manage.place(relx=0.0, rely=0.0, relheight=1.002
                                , relwidth=0.996)

        personNames = self.getAllAuthorizedNames()
        self.listbox_PersonList.delete(0, tk.END)
        for i in range(len(personNames)):
            self.listbox_PersonList.insert(i, personNames[i])

    def show_detectLogPanel(self):
        self.frame_manage.place_forget()
        self.frame_register.place_forget()
        self.frame_detectLog.place(relx=0.0, rely=0.0, relheight=1.002
                                   , relwidth=1.0)

    def clearlog(self):
        open('detectionlog.txt', 'w').close()
        self.textbox_facelog.configure(state="normal")
        self.textbox_facelog.delete(1.0, tk.END)
        self.textbox_facelog.update()
        self.textbox_facelog.configure(state="disabled")

    def addNewPhoto(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image File", '.jpg'), ("Image File", '.png'), ("Image File", '.jpeg')])
        try:
            shutil.copy(filepath, "dataset/" + self.listbox_PersonList.get(tk.ACTIVE))
        except(Exception):
            return
        self.getPicsByDirName()
        messagebox.showinfo(title="Refreshing Dataset",
                            message="Adding photo to dataset, this may take 2-10mins depending on the computer.\n Please do not quit the application!")
        os.system("python encode_faces.py")
        messagebox.showinfo(title="Refreshing Dataset", message="Dataset is refreshed, please press ok to continue! ")

    def deletePhoto(self):
        if (messagebox.askokcancel("Delete photo",
                                   "Are you sure you want to delete this photo?\n" + self.listbox_photoList.get(
                                       tk.ACTIVE))):
            os.remove('dataset/' + self.listbox_PersonList.get(tk.ACTIVE) + "/" + self.listbox_photoList.get(tk.ACTIVE))
            self.getPicsByDirName()
            messagebox.showinfo(title="photo Deleted", message="Dataset is needs to be refreshed to apply the changes.")

    def deleteUser(self):
        if (messagebox.askokcancel("Delete photo",
                                   "Are you sure you want to delete this user?\n" + self.listbox_PersonList.get(
                                       tk.ACTIVE))):
            shutil.rmtree('dataset/' + self.listbox_PersonList.get(tk.ACTIVE))
            self.listbox_photoList.delete(0, tk.END)
            self.show_managePanel()
            messagebox.showinfo(title="User Deleted", message="Dataset is needs to be refreshed to apply the changes.")

    def getAllAuthorizedNames(self):
        return os.listdir("dataset")

    def getPicsByDirName(self, evt=None):
        dirname = self.listbox_PersonList.get(tk.ACTIVE)
        photo_name = os.listdir("dataset/" + dirname)
        self.listbox_photoList.delete(0, tk.END)
        for i in range(len(photo_name)):
            self.listbox_photoList.insert(i, photo_name[i])

    def addNewAuthorized(self):
        if (self.textbox_fname.get() != "" and self.textbox_lname.get() != ""):
            name = self.textbox_fname.get() + "_" + self.textbox_lname.get()
            try:
                os.mkdir("dataset/" + name)
            except(Exception):
                messagebox.showerror(title="User creation", message="User " + name + " already exists!")
                return
            self.btn_takePhoto.configure(state="normal")
        else:
            messagebox.showerror(title="User creation",
                                 message="First name or Last name cant be empty, Please try again!")

    def displayPhoto(self, evt):
        os.system(
            'start dataset/' + self.listbox_PersonList.get(tk.ACTIVE) + "/" + self.listbox_photoList.get(tk.ACTIVE))

    def takePhotos(self):
        if (messagebox.askokcancel("Register face",
                                   "Please move your face slowly from right to left.\n Please click okay to start taking photos!")):
            cam = VideoCapture(0)
            count = 50
            if (self.textbox_photoCount.get() != ""):
                try:
                    count = int(self.textbox_photoCount.get())
                except(Exception):
                    messagebox.showerror(title="Taking Photo",
                                         message="Photo count only excepts numbers(0-9), Please try again!")
                    return
            for i in range(count):
                success, image = cam.read()
                cv2.imwrite(
                    'dataset/' + self.textbox_fname.get() + "_" + self.textbox_lname.get() + "/" + str(i) + ".jpg",
                    image)
                sleep(0.1)
                print(i + 1, end="\t")
                self.btn_takePhoto.configure(text=str(i + 1) + "/" + str(count))
                self.btn_takePhoto.update()
            self.btn_takePhoto.configure(text="Take Photos")
            messagebox.showinfo(title="Refreshing Dataset",
                                message="Adding person to dataset, this may take 2-10mins depending on the computer.\n Please do not quit the application!")
            os.system("python encode_faces.py")
            messagebox.showinfo(title="Refreshing Dataset",
                                message="Dataset is refreshed, please press ok to continue! ")
        else:
            os.rmdir("dataset/" + self.textbox_fname.get() + "_" + self.textbox_lname.get())
        self.btn_takePhoto.configure(state='disabled')

    def refreshDataset(self):
        if os.path.exists("encodings.pickle"):
            os.remove("encodings.pickle")
        open("images.txt", 'w').close()
        waitMessageBox = messagebox.askokcancel("Refreshing Dataset",
                                                "Please wait patiently, this may take 2-20 mins depending on the computer.\n Please do not quit the application!")
        if (waitMessageBox):
            os.system("python encode_faces.py")
            messagebox.showinfo(title="Refreshing Dataset",
                                message="Dataset is refreshed, please press ok to continue! ")

    def addOwner2TxtFile(self):
        emailId = self.textbox_addOwner.get()

        if emailId != "":
            mailIdFile = open("owner_email.txt", 'a')
            mailIdFile.write(emailId + "\n")
            mailIdFile.close()

            # refresh
            self.listbox_OwnerList.delete(0, tk.END)
            mailIdFile = open("owner_email.txt", 'r')
            mailIds = mailIdFile.readlines()
            for i in range(len(mailIds)):
                self.listbox_OwnerList.insert(i, mailIds[i])
            mailIdFile.close()
        else:
            messagebox.showerror(title="Recipient List", message="Blank email id cannot be added, Please try again!")

    def delOwnerFromTxtFile(self):
        delId = self.listbox_OwnerList.get(tk.ACTIVE)
        self.listbox_OwnerList.delete(0, tk.END)
        mailIdFile = open("owner_email.txt", 'r')
        mailIds = mailIdFile.readlines()
        mailIds.remove(delId)
        mailIdFile.close()

        open("owner_email.txt", 'w').close()
        mailIdFile = open("owner_email.txt", 'a')
        for mailId in mailIds:
            mailIdFile.write(mailId)
        mailIdFile.close()

        # refresh
        self.listbox_OwnerList.delete(0, tk.END)
        mailIdFile = open("owner_email.txt", 'r')
        mailIds = mailIdFile.readlines()
        for i in range(len(mailIds)):
            self.listbox_OwnerList.insert(i, mailIds[i])
        mailIdFile.close()


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

    def size_(self):
        sz = tk.Listbox.size(self)
        return sz


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    guiCommunicator = GUICommunication()
    vp_start_gui()
