import webbrowser
import time
import sys
import random
print('____________________________________________________________')
str001='''
Art Integrated Learning

Name: DEBANKO SINHA

Class: XII        Section: C      Roll No: 13

School: KENDRIYA VIDYALAYA BALLYGUNGE

Guided by   Mr. DEBJIT BISWAS'''

for i in str001:
    print(i,end='')
    time.sleep(.05)
    
print('''
____________________________________________________________''')

str3='''

Through this project, we will have a short tour of the city 
'''
for i in str3:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        print(i,end='')
        time.sleep(.05)

str2='''


██╗░░██╗░█████╗░██╗░░░░░██╗░░██╗░█████╗░████████╗░█████╗░
██║░██╔╝██╔══██╗██║░░░░░██║░██╔╝██╔══██╗╚══██╔══╝██╔══██╗
█████═╝░██║░░██║██║░░░░░█████═╝░███████║░░░██║░░░███████║
██╔═██╗░██║░░██║██║░░░░░██╔═██╗░██╔══██║░░░██║░░░██╔══██║
██║░╚██╗╚█████╔╝███████╗██║░╚██╗██║░░██║░░░██║░░░██║░░██║
╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝'''
str1='''

With almost 1.5 crore citizens, the City of Joy, Kolkata brims with culture unlike any other city.

Would you like to know about some entertainment/important/historical places? ☻
OR
Would you like to know more about Kolkata? ❤

'''
hipo={'Freedom fighters':['Subhas Chandra Bose','Sri Aurobindo','Benoy Basu','Khudiram Bose','Rash Behari Bose','Jogesh Chandra Chattopadhyay','Chittaranjan Das','Jatindra Nath Das','Bagha Jatin','Badal Gupta','Dinesh Gupta','Shyama Prasad Mukherjee','Bipin Chandra Pal','Sudhamoy Pramanick','Bidhan Chandra Roy','Ashoke Kumar Sen','Matangini Hazra','Maulana Abul Kalam Azad','Sisir Kumar Ghosh'],'Poets and Writers':['Rabindranath Tagore, Nobel Laureate.','Syed Mujtaba Ali','S. Wajid Ali','Sharadindu Bandyopadhyay','Suchitra Bhattacharya','Sukanta Bhattacharya','Buddhadev Bose','Amiya Chakravarty','Bankim Chandra Chattopadhyay','Sarat Chandra Chattopadhyay','Shakti Chattopadhyay','Nirad C. Chaudhuri','Pramatha Chowdhury','Upendrakishore Ray Chowdhury','Dinesh Das','Jibanananda Das','Henry Louis Vivian Derozio','Bishnu Dey','Michael Madhusudan Dutta','Satyendranath Dutta','Sudhindranath Dutta','Sunil Gangopadhyay','Joy Goswami','Kaji Nazrul Islam','Sisir Kumar Maitra','Arun Mukherjee, playwright and actor.','Binoy Majumdar','Mohitolal Majumdar','Samaresh Majumdar (b.1944)','Arun Mitra','Dinabandhu Mitra','Premendra Mitra','Dhan Gopal Mukerji','Subhas Mukhopadhyay','Purnendu Patri','Christopher Raja','Annada Shankar Ray','Dwijendralal Ray','Tarapada Ray','Sukumar Ray','Samar Sen','Badal Sircar, dramatist and theatre director.','Husne Chand Sultana','Srijato','Jaydeep Sarangi, English poet (also writes in Bangla) with eight collections.'],'Directors':['Satyajit Ray','Utpal Dutta','Nitin Bose','Buddhadeb Dasgupta','Anik Dutta','Kaushik Ganguly','Kishore Kumar','Ritwik Ghatak','Gautam Ghose','Rituparno Ghosh','Hrishikesh Mukherjee','Srijit Mukherji','Shiboprosad Mukherjee','Aniruddha Roy Chowdhury','Tapan Sinha','Aparna Sen','Mrinal Sen','Manick Sorcar',],'Cinema actors':['Uttam Kumar','Kishore Kumar','Utpal Dutt','Soumitra Chatterjee','Sabyasachi Chakrabarty','Dhritiman Chaterji','Tapen Chatterjee','Rabi Ghosh','Barun Chanda','Pahari Sanyal','N. Viswanathan','Chhabi Biswas','Karuna Bannerjee','Anil Chatterjee','Subir Banerjee','Roopa Ganguly','Uma Dasgupta','Saswata Chatterjee','Tarun Kumar','Anup Kumar','Ashok Kumar','Bhanu Bandopadhyay','Biswajit Chatterjee','Prosenjit Chatterjee','Jahor Roy','Kanan Devi','Swastika Mukherjee','Razzak','Dev','Jeet','Ruma Guha Thakurta','Ranjit Mallick','Mirza Abbas Ali','Suchitra Sen','Moonmoon Sen','Riya Sen','Raima Sen','Reema Sen','Omar Sani','Victor Banerjee','Parambrata Chatterjee','Konkona Sen Sharma','Varsha Ashwathi','Abhishek Chatterjee','Tathagata Mukherjee'] }
ffax=['Calcutta Polo Club is a polo club located in Kolkata, West Bengal, India. It was established in 1862 and is considered as the oldest polo club of the world in existence','M.P. Birla Planetarium is the largest planetarium in Asia and the second largest planetarium in the world.',"Asia's oldest electric running tram is not in Mumbai or Delhi, but only in Calcutta operating across the City of Joy since 1902.",'Kolkata Has The Oldest And The Only Riverine Port in India','Howrah Railway station is India’s busiest railway station. It handles the largest number of unique trains on a daily basis.','Kolkata is the only city in India where hand-pulled rickshaws are still prevalent.','Calcutta(now Kolkata) was the capital of India from 1858–1911',"The Kolkata Book Fair is the most awaited annual cultural event of the city of Calcutta(now Kolkata). It is Asia's biggest and the world's largest non-trade book fair",'The city has earned the nickname "City of Joy" for its soulful embodiment of culture, love, mystery, respect, enthusiasm and definitely some amazing sweet delicacies. Kolkata, as it is now referred to as, is a city that upholds a perfect juxtaposition between the old world and the modern one.','The football club "Mohunbagan" was established in 1889 by Bhupendra Nath Bose and is the oldest existing football club in India.']
for i in str2:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        print(i,end='')
        time.sleep(.001)
for i in str1:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        print(i,end='')
        time.sleep(.05)
        
while True:
    
    x=int(input('''Enter
    <1> For Kolkata
    <2> For entertainment/important/historical places
    <3> To quit

    =>'''))
    if x==1:
        while True:
            str6='''What would you like to know about Kolkata?'''
            for i in str6:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                print(i,end='')
                time.sleep(.05)
                

                
            x1=int(input('''

        
Enter
        <1> Famous Bengali personalities 
        <2> Interesting Facts
        <3> Everything about Kolkata
        <4> Go Back
        
        
        =>'''))
            if x1==1:
                    for i in hipo:
                            l=list(i)
                            print('________________________________'+('_')*len(i))
                            print()
                            print('                ',end='')
                            for abcd in l:
                                    print(abcd,end='')
                                    time.sleep(.1)
                            print()    
                            print('________________________________'+('_')*len(i))
                            print('''


        ''')
                            for j in range(len(hipo[i])):
                                    print('        '+hipo[i][j])
                                    time.sleep(.06)

                            print('''


        ''')
            elif x1==2:
                print('''
Here's a random interesting fact about Kolkata

                      ''')
                time.sleep(1)

                str78='>>>'+ffax[random.randint(0,len(ffax)-1)]+'''

'''
                for i in str78:
                    print(i,end='')
                    time.sleep(.05) 
                time.sleep(1)
            elif x1==3:
                webbrowser.open('https://en.wikipedia.org/wiki/Kolkata')
            elif x1==4:
                print('''
Back to Menu
''')
                time.sleep(1)
                break
            else:
                print('''
Wrong input... TRY AGAIN!''')    
    elif x==2:
        while True:
            
            print('''

Which place would you like to know about?
''')
            place=input('''Enter

1>Victoria Memorial
2>Howrah Bridge
3>Belur Math
4>St. Paul's Cathedral Kolkata
5>Nakhoda Masjid
6>Nicco Park, Kolkata
7>Science City Kolkata
8>South Park Cemetery, Kolkata
9>M.P.Birla Planetarium
10>Indian Museum
11>Eden Gardens
12>Prinsep Ghat
13>Return to Menu

=>''')
            if place=='1':
                webbrowser.open('https://en.wikipedia.org/wiki/Victoria_Memorial,_Kolkata')
            elif place=='2':
                webbrowser.open('https://en.wikipedia.org/wiki/Howrah_Bridge')
            elif place=='3':
                webbrowser.open('https://en.wikipedia.org/wiki/Belur_Math')
            elif place=='4':
                webbrowser.open('https://en.wikipedia.org/wiki/St._Paul%27s_Cathedral,_Kolkata')
            elif place=='5':
                webbrowser.open('https://en.wikipedia.org/wiki/Nakhoda_Masjid')
            elif place=='6':
                webbrowser.open('https://en.wikipedia.org/wiki/Nicco_Park')
            elif place=='7':
                webbrowser.open('https://en.wikipedia.org/wiki/Science_City_Kolkata')
            elif place=='8':
                webbrowser.open('https://en.wikipedia.org/wiki/South_Park_Street_Cemetery')
            elif place=='9':
                webbrowser.open('https://en.wikipedia.org/wiki/Birla_Planetarium,_Kolkata')
            elif place=='10':
                webbrowser.open('https://en.wikipedia.org/wiki/Indian_Museum,_Kolkata')
            elif place=='11':
                webbrowser.open('https://en.wikipedia.org/wiki/Eden_Gardens')
            elif place=='12':
                webbrowser.open('https://en.wikipedia.org/wiki/Prinsep_Ghat')
            elif place=='13':
                break
            else:
                print('''
Wrong input... TRY AGAIN!''')        
    elif x==3:
        break
    else:
        print('''
Wrong input... TRY AGAIN!''')
print('''

      Have a nice day...''')
