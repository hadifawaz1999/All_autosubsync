import autosubsync as ass
import os
from tkinter import *
from tkinter import filedialog
from tkinter import font

class sync:

    def __init__(self):
        self.gui=Tk()
        self.gui.title("All_autosubsync")
        self.gui.geometry("690x440")

        self.my_font=font.Font(size=15)

        self.vids_path=StringVar()
        self.subs_path=StringVar()
        self.vids_dir=""
        self.subs_dir=""

        self.vids_label=Label(self.gui,text="Path to videos directory")
        self.vids_label['font']=self.my_font
        self.vids_label.grid(row=1,column=1)

        self.vids_entry=Entry(self.gui,textvariable=self.vids_path)
        self.vids_entry['font']=self.my_font
        self.vids_entry.grid(row=1,column=2)

        self.vids_browse_button=Button(self.gui,text="Browse",command=self.browse_vids_directory_button)
        self.vids_browse_button['font']=self.my_font
        self.vids_browse_button.grid(row=1,column=3)

        self.subs_label=Label(self.gui,text="Path to subtitles directory")
        self.subs_label['font']=self.my_font
        self.subs_label.grid(row=2,column=1,padx=20,pady=100)

        self.subs_entry=Entry(self.gui,textvariable=self.subs_path)
        self.subs_entry['font']=self.my_font
        self.subs_entry.grid(row=2,column=2)

        self.subs_browse_button=Button(self.gui,text="Browse",command=self.browse_subs_directory_button)
        self.subs_browse_button['font']=self.my_font
        self.subs_browse_button.grid(row=2,column=3)

        self.start_button=Button(self.gui,text="Start syncing",command=self.start_syncing)
        self.start_button.grid(row=3,column=1)

        self.close_button=Button(self.gui,text="Close",command=self.close_app)
        self.close_button.grid(row=3,column=2)

        self.Verbose1=""
        self.verbose1=StringVar()
        self.label1=Label(self.gui,textvariable=self.verbose1)
        self.label1.grid(row=4,column=1)

        self.END_strvar=StringVar()
        self.label2=Label(self.gui,textvariable=self.END_strvar)
        self.label2.grid(row=5,column=1)

    def browse_vids_directory_button(self):
        self.vids_dir=filedialog.askdirectory()
        self.vids_path.set(self.vids_dir)
        print(self.vids_dir)
    
    def browse_subs_directory_button(self):
        self.subs_dir=filedialog.askdirectory()
        self.subs_path.set(self.subs_dir)
        print(self.subs_dir)

    def start_syncing(self):
        for rootv, dirsv, vids in os.walk(self.vids_dir):
            vids.sort()
            for roots, dirss, subs in os.walk(self.subs_dir):
                subs.sort()
                for i in range(len(vids)):
                    self.vid_path = self.vids_dir+'/'+vids[i]
                    self.sub_path=self.subs_dir+'/'+subs[i]
                    self.out_path=self.vids_dir+'/'+vids[i][:-3]+'srt'
                    
                    print(self.vid_path)
                    print(self.sub_path)
                    print(self.out_path)

                    ass.synchronize(self.vid_path,self.sub_path,self.out_path,verbose=True)

                    self.Verbose1=self.out_path[len(self.vids_dir)+1:]+" Sync Success !!!"
                    self.verbose1.set(self.Verbose1)
                    self.gui.update()
        self.END_strvar.set("END of sync enjoy !!!")
        self.gui.update()

    def start_app(self):
        self.gui.mainloop()

    def close_app(self):
        self.gui.destroy()
'''
vids_path = '/media/hadi/torrents/saved/Two and a half men/Two and a Half Men Season 3 720p MaRS/'
subs_path = '/media/hadi/torrents/subs/twoandahalfmen_s03/'
outs_path = '/media/hadi/torrents/saved/Two and a half men/Two and a Half Men Season 3 720p MaRS/'

for rootv, dirsv, vids in os.walk(vids_path):
    vids.sort()

    for roots, dirss, subs in os.walk(subs_path):
        subs.sort()
        for i in range(len(vids)):
            vid_path = vids_path+vids[i]
            sub_path=subs_path+subs[i]
            out_path=outs_path+vids[i][:-3]+'srt'
            print(vid_path,sub_path,out_path,sep='\n')
            ass.synchronize(vid_path,sub_path,out_path,verbose=True)
'''

if __name__ == '__main__':
    my_sync=sync()
    my_sync.start_app()