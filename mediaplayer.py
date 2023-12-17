import os



from colorama import Fore

print(Fore.CYAN+"1.)Music"'\n'"2.)Videos"'\n'"3.)movies")
in1=input(Fore.LIGHTMAGENTA_EX+"Enter a content:")

if in1 =='1':
    
    musicdir="directry://filename"#Set Your Path
    songs=os.listdir(musicdir)
    len=len(songs)
    sum=0
    for s in songs:
        sum=sum+1
        print(Fore.WHITE+"",sum,'\t',s)
    d=0
    while d!=9:
        a=int(input(Fore.YELLOW+"Enter a Song Track NO:"))
        os.startfile(os.path.join(musicdir,songs[a-1]))
        print(Fore.BLUE+"Now playing....",Fore.GREEN+songs[a-1])
        
        
        print('\n')
    else:
        print(Fore.MAGENTA+"NO Songs Found!!")
        


elif in1 =='2':

    viddir="directry://filename"#Set Your Path"
    videos=os.listdir(viddir)
    len=len(videos)
    sum=0
    for v in videos:
        sum=sum+1
        print(Fore.WHITE+"",sum,'\t',v)
    d=0
    while d!=9:
        a=int(input(Fore.YELLOW+"Enter a Video Track NO:"))
        
        
        os.startfile(os.path.join(viddir,videos[a-1]))
    
        print(Fore.BLUE+"Now playing....",Fore.GREEN+videos[a-1])
        print('\n')

    else:
        print(Fore.MAGENTA+"NO Videos Found!!")
elif in1=='3':

        viddir="directry://filename"#Set Your Path
        videos=os.listdir(viddir)
        len=len(videos)
        sum=0
        for v in videos:
            sum=sum+1
            print(Fore.WHITE+"",sum,'\t',v)
        d=0
        while d!=9:
            a=int(input(Fore.YELLOW+"Enter a Movie Track NO:"))
            
            

            os.startfile(os.path.join(viddir,videos[a-1]))
            print(Fore.BLUE+"Now playing....",Fore.GREEN+videos[a-1])
            print('\n')
else:
    print(Fore.LIGHTRED_EX+"Input is Wrong Try Again")


  
