from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import calendar
class Structure:
    def __init__(self,root):
        self.root = root
        self.root.title("Structure_of_college")
        self.root.geometry("1550x800+0+0")
        frame = Frame(self.root, bg="#e4f7fd")
        frame.place(x=0, y=0, relwidth=1, height=134, )


        # ======================= logo of college ==========================
        self.collegeImage = ImageTk.PhotoImage(file="images/es1.png")
        collegeImage = Label(frame, image=self.collegeImage, bg="#e4f7fd", padx=10,pady=20).place(x=10,y=10,width=250,height=124)


        # ======================= Title of the college =====================

        title = Label(frame, text="Eshan College Of Engineering ", font=("Bookman Old Style", 35 ,"bold"),bg="#e4f7fd",)
        title.place(x=320,y=40)


        # login_btn = Button(frame,text="Sign Up", font=("times new roman", 12, "bold"),bg="#280050", fg="white", cursor="hand2").place(x=1340,y=10,width=80)
        login_btn = Button(frame,text="Log Out", font=("times new roman", 12, "bold"), bg="#280050", fg="white", cursor="hand2").place(x=1350,y=10,width=160)

        # ============================ Maker Name =========================
        maker_name = Label(frame,text="Shishupal Singh", font=("Brush Script MT", 15, ),bg="#e4f7fd").place(x=1400,y=100)

        # ============================ for border in frame of college name =======================

        border_s = Label(frame,bg="black").place(x=0,y=131,width=1530,height=2)

        # ========================== create frame1 to college management =========================

        frame1 = Frame(self.root, bg="#215b8f")
        frame1.place(x=0,y=134,width=500,height=660)

        # ========================== Structure of college management System =====================

        title_1 = Label(frame1,text="College Management System",font=("times new roman", 28, "bold"), bg="yellow", fg="red", bd=10, relief=RIDGE, padx=14,pady=10).grid(row=1,column=1,columnspan=1)
        self.staff =ImageTk.PhotoImage(file="images/icons8-staff-50.png")
        label2 = Button(frame1,image=self.staff,text="Staff Management",font=("times new roman",20,"bold"),bg="gray",bd=5,relief=GROOVE, command=self.data,compound=LEFT,padx=82).place(x=50,y=100,width=380)
        self.student =ImageTk.PhotoImage(file="images/icons8-staff-50.png")

        label3 = Button(frame1,image=self.student,text="Student Management",font=("times new roman",20,"bold"),bg="gray",bd=5,relief=GROOVE, command=self.student_1,compound=LEFT,padx=60).place(x=50,y=180,width=380)
        self.financial =ImageTk.PhotoImage(file="images/icons8-staff-50.png")

        label4 = Button(frame1,image=self.financial, text="Fees Management", font=("times new roman", 20, "bold"), bg="gray", bd=5,relief=GROOVE, command=self.fees1, compound=LEFT, padx=90).place(x=50, y=260, width=380)


        label5 = Button(frame1,image=self.staff,text="Attendance Management",font=("times new roman",20,"bold"),bg="gray",bd=5,relief=GROOVE, command=self.data,compound=LEFT,padx=20).place(x=50,y=340,width=380)
        label6 = Button(frame1,image=self.staff,text="Exam Management",font=("times new roman",20,"bold"),bg="gray",bd=2,relief=GROOVE, command=self.data,compound=LEFT,padx=80).place(x=50,y=420,width=380)
        label6 = Button(frame1,image=self.staff,text="More->",font=("times new roman",20,"bold"),bg="gray",bd=2,relief=GROOVE, command=self.data,compound=LEFT,padx=80).place(x=50,y=500,width=380)
        lebel7 = Label(bg="red").place(x=500,y=132,width=3,height=665)

        frame4 = Frame(self.root,bg="#14D683",bd="2",relief=GROOVE)
        frame4.place(x=502,y=132,width=1050,height=665)


        # use of the naming in frame 4
        lab_stfname = Label(frame4,text="First Name",bg="#14D683",fg="#270C6C",font=("timew new roman",13)).place(x=50, y=30)
        stfname =Entry(frame4, font=("times new roman",)).place(x=170,y=30,width=200,height=25)

        lab_stlname = Label(frame4, text="Last Name", bg="#14D683", fg="#270C6C",font=("timew new roman", 13)).place(x=400, y=30)
        stlname = Entry(frame4, font=("times new roman", 13)).place(x=520, y=30, width=200, height=25)

        lab_stfname = Label(frame4, text="Qualification", bg="#14D683", fg="#270C6C",font=("timew new roman", 13)).place(x=50, y=90)
        stfname = Entry(frame4, font=("times new roman", 13)).place(x=170, y=90, width=200, height=25)

        lab_stlname = Label(frame4, text="Your Email", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(x=400, y=90)
        stlname = Entry(frame4, font=("times new roman", 13)).place(x=520, y=90, width=200, height=25)

        lab_stfname = Label(frame4, text="Subject", bg="#14D683", fg="#270C6C",font=("times new roman", 13)).place(x=50, y=150)
        combo_subject = ttk.Combobox(frame4,font=("times new roman",11),state="readonly")
        combo_subject['values'] = ("Data Structure", "COA","Mathematics 1V")
        combo_subject.place(x=170, y=150, width=200, height=25)

        lab_stsalary = Label(frame4, text="Salary", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(x=400, y=150)
        stsalary = Entry(frame4, font=("times new roman", 13)).place(x=520, y=150, width=200, height=25)

        lab_stdob = Label(frame4, text="DOB", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(x=50, y=210)
        stdob     =  Entry(frame4, font=("times new roman", 13)).place(x=170, y=210, width=200, height=25)

        lab_stgender = Label(frame4, text="Gender", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(x=400, y=210)
        stgner_combo = ttk.Combobox(frame4,font=("times new roman",11),state="readonly")
        stgner_combo['values'] = ("Male", "Female","Other")
        stgner_combo.place(x=520, y=210, width=200, height=25)

        lab_stcourse  = Label(frame4, text="Course", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(x=50, y=270)
        st_course = ttk.Combobox(frame4,font=("times new roman",11),state="readonly")
        st_course['values'] = ("BTech","Diploma","ITI")
        st_course.place(x=170, y=270, width=200, height=25)

        lab_stphone = Label(frame4, text="Phone", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(x=400, y=270)
        stphone = Entry(frame4, font=("times new roman", 13)).place(x=520, y=270, width=200, height=25)
        las_address = Label(frame4, text="Address", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(x=50, y=330)
        st_address =  Text(frame4, font=("times new roman", 13)).place(x=50, y=370, width=690, height=100)



        st_save = Button(frame4,text="Save Data",font=("times new roman", 20,"bold"),bg="#14D683", fg="#270C6C",bd=5)
        st_save.place(x=80,y=490,width=180,height=50)
        btn_info = Button(frame4, text="Info", font=("times new roman", 20,"bold"), bg="#14D683", bd=5,fg="#270C6C").place(x=300, y=490, width=180,height=50)
        btn_search = Button(frame4, text="Search", font=("times new roman", 20,"bold"), bg="#14D683", bd=5,fg="#270C6C").place(x=520, y=490, width=180,height=50)


    def data(self):
        # ========================================== this is creating the manage the data ===============================
        frame4 = Frame(self.root, bg="#14D683", bd="2", relief=GROOVE)
        frame4.place(x=502, y=132, width=1050, height=665)

        # use of the naming in frame 4
        lab_stfname = Label(frame4, text="First Name", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(
            x=50, y=30)
        stfname = Entry(frame4, font=("times new roman", 13)).place(x=170, y=30, width=150, height=25)

        lab_stlname = Label(frame4, text="Last Name", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(
            x=400, y=30)
        stlname = Entry(frame4, font=("times new roman", 13)).place(x=520, y=30, width=200, height=25)

        lab_stfname = Label(frame4, text="Qualification", bg="#14D683", fg="#270C6C",
                            font=("timew new roman", 13)).place(x=50, y=90)
        stfname = Entry(frame4, font=("times new roman", 13)).place(x=170, y=90, width=200, height=25)

        lab_stlname = Label(frame4, text="Your Email", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(
            x=400, y=90)
        stlname = Entry(frame4, font=("times new roman", 13)).place(x=520, y=90, width=200, height=25)

        lab_stfname = Label(frame4, text="Subject", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(
            x=50, y=150)
        combo_subject = ttk.Combobox(frame4, font=("times new roman", 11), state="readonly")
        combo_subject['values'] = ("Data Structure", "COA", "Mathematics 1V")
        combo_subject.place(x=170, y=150, width=200, height=25)

        lab_stsalary = Label(frame4, text="Salary", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(
            x=400, y=150)
        stsalary = Entry(frame4, font=("times new roman", 13)).place(x=520, y=150, width=200, height=25)

        lab_stdob = Label(frame4, text="DOB", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(x=50,
                                                                                                              y=210)
        stdob = Entry(frame4, font=("times new roman", 13)).place(x=170, y=210, width=200, height=25)

        lab_stgender = Label(frame4, text="Gender", bg="#14D683", fg="#270C6C", font=("timew new roman", 13)).place(
            x=400, y=210)
        stgner_combo = ttk.Combobox(frame4, font=("times new roman", 11), state="readonly")
        stgner_combo['values'] = ("Male", "Female", "Other")
        stgner_combo.place(x=520, y=210, width=200, height=25)

        lab_stcourse = Label(frame4, text="Course", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(
            x=50, y=270)
        st_course = ttk.Combobox(frame4, font=("times new roman", 11), state="readonly")
        st_course['values'] = ("BTech", "Diploma", "ITI")
        st_course.place(x=170, y=270, width=200, height=25)

        lab_stphone = Label(frame4, text="Phone", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(x=400,
                                                                                                                  y=270)
        stphone = Entry(frame4, font=("times new roman", 13)).place(x=520, y=270, width=200, height=25)
        las_address = Label(frame4, text="Address", bg="#14D683", fg="#270C6C", font=("times new roman", 13)).place(
            x=50, y=330)
        st_address = Text(frame4, font=("times new roman", 13)).place(x=50, y=370, width=690, height=100)

        st_save = Button(frame4, text="Save Data", font=("times new roman", 20, "bold"), bg="#14D683", fg="#270C6C",
                         bd=5)
        st_save.place(x=190, y=490, width=390, height=50)
    def student_1(self):
        frame3 = Frame(self.root, bg="#656565", bd="2", relief=GROOVE)
        frame3.place(x=502, y=132, width=1050, height=665)
        label1 = Label(frame3,text="new", bg="white").place(x=0,y=0)
    def fees1(self):
        frame3 = Frame(self.root, bg="#125475", bd="2", relief=GROOVE)
        frame3.place(x=502, y=132, width=1050, height=665)


root = Tk()
obj = Structure(root)
root.mainloop()