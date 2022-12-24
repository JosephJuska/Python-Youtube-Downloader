from pytube import YouTube
from pytube import exceptions
import os
import tkinter
from tkinter import filedialog

PATH = ''
FORMAT = ''
def format():
    global FORMAT
    FORMAT = str(var.get())


def choose_path(l):
    global PATH
    PATH = filedialog.askdirectory()
    l.config(text=PATH)


def download():
    global PATH, FORMAT
    url = entry.get()
    if not entry.get():
        labelResult.config(text='Url is not entered')

    elif not PATH:
        labelResult.config(text='Path is not entered')
    
    elif not FORMAT:
        labelResult.config(text='Format is not chosen')

    else:
        try:
            yt = YouTube(url)
            destination = PATH
            if FORMAT == 'mp3':
                video = yt.streams.filter(only_audio = True).first()

            else:
                video = yt.streams.filter(only_audio = False).first()

            out_file = video.download(output_path = destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + f'.{FORMAT}'
            os.rename(out_file,new_file)
            labelResult.config(text=f'Success!!!')

        except exceptions.RegexMatchError:
            labelResult.config(text='Url has a mistake')
        
        except exceptions.AgeRestrictedError:
            labelResult.config(text='Video is age restricted')
        
        except exceptions.VideoPrivate:
            labelResult.config(text='Video is private')
        
        except exceptions.RecordingUnavailable:
            labelResult.config(text='Video is  unavaliable')
        
        except exceptions.LiveStreamError:
            labelResult.config(text='Video is a live stream')
        
        except exceptions.VideoUnavailable:
            labelResult.config(text='Video is  unavaliable')
        
        except exceptions.VideoRegionBlocked:
            labelResult.config(text='Video is not avaliale in your region')
        
        except exceptions.ExtractError:
            labelResult.config(text='Could not extract the video')

        except FileExistsError:
            labelResult.config(text='Done but file already exists')

        except Exception as e:
            labelResult.config(font=('monospace',10),text=e)


window = tkinter.Tk()
window.title('Youtube downloader')
window.config(bg = 'black')


var = tkinter.StringVar()

label = tkinter.Label(window,
foreground='green',
text='Youtube Downloader',
background='black',
font=('monospace',30))
label.pack(anchor='n')


labelFormat = tkinter.Label(window,
foreground='green',
background='black',
text='Choose the format:',
font=('monospace',20))
labelFormat.pack()


r1 = tkinter.Radiobutton(window,
text='MP4',
foreground='green',
background='black',
activebackground='black',
activeforeground='red',
variable=var,
value='mp4',
command=lambda: format(),
font=('monospace',20))
r1.pack()


r2 = tkinter.Radiobutton(window,
text='MP3',
foreground='green',
background='black',
activebackground='black',
activeforeground='red',
variable=var,
value='mp3',
command=lambda: format(),
font=('monospace',20))
r2.pack()


labelURL = tkinter.Label(window,
foreground='green',
background='black',
text='Enter the URL:',
font=('monospace',20))
labelURL.pack()


entry = tkinter.Entry(window,
foreground='green',
background='black',
relief='raised',
borderwidth=4,
width=40,
font=('monospace',20))
entry.pack(padx=20,pady=10)


btnPath = tkinter.Button(window,
text='Choose the path',
foreground='green',
background='black',
activebackground='black',
activeforeground='red',
borderwidth=3,
relief='raised',
font=('monospace',15),
command=lambda: choose_path(labelPath))
btnPath.pack()


labelPath = tkinter.Label(window,
foreground='green',
background='black',
text='Path of the directory',
font=('monospace',15))
labelPath.pack(pady=20)


btnDownload = tkinter.Button(window,
text='Download',
foreground='green',
background='black',
activebackground='black',
activeforeground='red',
borderwidth=3,
relief='raised',
font=('monospace',15),
command=lambda: download())
btnDownload.pack()


labelResult = tkinter.Label(window,
foreground='green',
background='black',
text='',
font=('monospace',20))
labelResult.pack(pady=20)


labelCreator = tkinter.Label(window,
foreground='green',
background='black',
text='Created by https://github.com/JosephJuska',
font=('monospace',20))
labelCreator.pack(pady=20)


window.mainloop()