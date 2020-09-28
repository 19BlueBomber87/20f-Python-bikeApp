#Chapters 1-8 Rob Mills
#_20f_bikeApp
import sys
import time
import pygame
import snaps
import os
import random

#from BTCInput import *  
#create empty lists
miles=[];moose=[];calf=[];hours=[];mins=[];dates=[];weather=[];notes=[];elevation_gain=[];elevation_loss=[];max_speed=[];average_speed=[];seconds=[];
# function 0
def analyze_stats():
    _t=True
    HUD_weather_date_time()
    snaps.display_image("fx/jpg/Atown.jpg")
    prompt='''          <@:D_Bike Stats_<@:D

    1: Enter Stats
    2: Print Stats
    3: Totals
    4: Elevation Gain/Loss
    5: Highest Indavidual 
    6: Averages
    7: Save Data
    8: Load Data
    9: Moose slide show
    10: Exit
    Enter your command: '''
    while _t == True:
        try:
            ride_number_text = snaps.get_string(prompt,color=(255,255,0),size=45,vert='bottom',horiz='left',max_line_length=3,margin=20)
            command = int(ride_number_text)
        except ValueError:
            continue
        if command==1:
            read_trips()
        elif command==2:
            print_bikeStats()
        elif command==3:
            total_stats()
        elif command==4:
            elevation_stats()
        elif command==5:
            highest_stats()
        elif command==6:
            average_stats()
        elif command==7:
            save_stats()
        elif command==8:
            load_stats()
        elif command==9:
            start_x()
        elif command ==10:
            HUD_weather_date_time()
            break
# function 1
def read_trips(image_path="fx/jpg/Atown.jpg"):
    '''
    Reads in the miles values and stores them in
    the miles list.
    no_of_trips gives the number of miles values to store
    '''
    # remove all the previous values
    b_flag=True
    while b_flag==True:
        uac_answer_text=snaps.get_string(prompt="Any Unsaved Data Will Be Lost\n\nEnter Yes To Continue\n\nEnter No To Exit\n\nContinue?  ", vert='bottom',color=(255,255,0), max_line_length=3)
        uac_answer=uac_answer_text.upper()
        if uac_answer == 'NO':
            break
        elif uac_answer=='YES':
            miles.clear()
            moose.clear()
            calf.clear()
            hours.clear()
            mins.clear()
            dates.clear()
            elevation_gain.clear()
            elevation_loss.clear()
            max_speed.clear()
            average_speed.clear()
            snaps.display_image(image_path)
            try:
                sample_size_text=snaps.get_string(prompt="Enter The Sample Size: ", vert='bottom',color=(255,255,0), max_line_length=3)
                sample_size = int(sample_size_text)
            except ValueError:
                snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))

            # read in miles figures 
            for trip in range(1,sample_size+1):
                # assemble a prompt string
                prompt='Enter the date for trip ' + str(trip) + ': '
                prompt0='Enter the number of Calf Moose for trip ' + str(trip) + ': '
                prompt1='Enter the number of miles for trip ' + str(trip) + ': '
                prompt2='Enter the number of hours for trip ' + str(trip) + ': '
                prompt3='Enter the number of mins for trip' + str(trip) + ': '
                prompt4='Enter the number of Moose for trip ' + str(trip) + ': '
                prompt7='Enter the elevation gain for trip ' + str(trip) + ': '
                prompt8='Enter the elevation loss for trip ' + str(trip) + ': '
                prompt5='Enter the weather conditions for trip ' + str(trip) + ': '
                prompt6='Enter any extra notes for trip' + str(trip) + ': '
                prompt9='Enter the average speed per trip ' + str(trip) + ': '
                prompt10='Enter the max speed per trip' + str(trip) + ': '
                prompt11='Enter the number of seconds for trip ' + str(trip) + ': '
                _T=True
                while _T == True:
                    try:
                        date_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt, vert='bottom',color=(255,255,0), max_line_length=7)
                        if (date_number_text.upper()!='QUIT'):
                            _T=False
                            dates.append(date_number_text)
                        else:
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                    except ValueError:
                            snaps.display_message('A Problem Has Occured',vert='center')
                _T=True
                while _T == True:
                    try:
                        miles_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt1, vert='bottom', max_line_length=5,color=(255,255,0))
                        miles_number=float(miles_number_text) #float(str(1.1 + 0.1)[0:3])
                        if isinstance(miles_number, float):
                            _T=False
                            miles.append(miles_number)
                    except ValueError:
                        if miles_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:
                        hours_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt2, vert='bottom', max_line_length=5,color=(255,255,0))
                        hours_number = int(hours_number_text)
                        if isinstance(hours_number, int):
                            _T=False
                            hours.append(hours_number)
                    except ValueError:
                        if hours_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:    
                        mins_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt3, vert='bottom', max_line_length=5,color=(255,255,0))
                        mins_number=int(mins_number_text)
                        if isinstance(mins_number, int):
                            _T=False
                            mins.append(mins_number)
                    except ValueError:
                        if mins_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:    
                        second_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt11, vert='bottom', max_line_length=5,color=(255,255,0))
                        second_number=int(second_number_text)
                        if isinstance(second_number, int):
                            _T=False
                            seconds.append(second_number)
                    except ValueError:
                        if mins_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:
                        moose_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt4, vert='bottom', max_line_length=5,color=(255,255,0))
                        moose_number=int(moose_number_text)
                        if isinstance(moose_number,int):
                            moose.append(moose_number)
                            _T=False
                    except ValueError:
                        if moose_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:
                        moose_calf_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt0, vert='bottom', max_line_length=5,color=(255,255,0))
                        moose_calf_number=int(moose_calf_number_text)
                        if isinstance(moose_number,int):
                            calf.append(moose_calf_number)
                            _T=False
                    except ValueError:
                        if moose_calf_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:    
                        weather_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt5, vert='bottom', max_line_length=25,color=(255,255,0))
                        if (weather_number_text.upper()!='QUIT'):
                            _T=False
                            weather.append(weather_number_text)
                        else:
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                    except ValueError:
                            snaps.display_message('Something Went Wrong',vert='center')
                _T=True
                while _T == True:
                    try:
                        note_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt6, vert='bottom', max_line_length=25,color=(255,255,0))
                        if (note_number_text.upper()!='QUIT'):
                            _T=False
                            notes.append(date_number_text)
                        else:
                            snaps.display_message('Returning To Main Menu\nNo Data was saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                    except ValueError:
                            snaps.display_message('Somthing Went Wrong',vert='center')
                _T=True
                while _T == True:
                    try:
                        ev_gain_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt7, vert='bottom', max_line_length=5,color=(255,255,0))
                        ev_gain_number=int(ev_gain_number_text)
                        if isinstance(ev_gain_number,int):
                            elevation_gain.append(ev_gain_number)
                            _T=False
                    except ValueError:
                        if ev_gain_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:
                        ev_loss_number_text = snaps.get_string('Enter Quit To Exit\n'+prompt8, vert='bottom', max_line_length=5,color=(255,255,0))
                        ev_loss_number=int(ev_loss_number_text)
                        if isinstance(ev_loss_number,int):
                            _T=False
                            elevation_loss.append(ev_loss_number)
                    except ValueError:
                        if ev_loss_number_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data Was Saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:
                        average_speed_text = snaps.get_string('Enter Quit To Exit\n'+prompt9, vert='bottom', max_line_length=5,color=(255,255,0))
                        average_speed_number = float(average_speed_text)
                        if isinstance(average_speed_number, float):
                            _T=False
                            average_speed.append(average_speed_number)
                    except ValueError:
                        if average_speed_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data was saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')
                _T=True
                while _T == True:
                    try:
                        max_speed_text = snaps.get_string('Enter Quit To Exit\n'+prompt10, vert='bottom', max_line_length=5,color=(255,255,0))
                        max_speed_number = float(max_speed_text)
                        if isinstance(max_speed_number, float):
                            _T=False
                            max_speed.append(max_speed_number)
                    except ValueError:
                        if max_speed_text.upper()=='QUIT':
                            snaps.display_message('Returning To Main Menu\nNo Data was saved',vert='center',size=75,color=(255,255,0))
                            return time.sleep(2)
                        else:
                            snaps.display_message('Only Numbers',vert='center')# function 2
def print_bikeStats():
    '''
    Prints the miles figures on the screen with
    a heading. Each figure is numbered in seqeuence
    '''
    sample_size_text=snaps.get_string(prompt="Enter the sample trip size: ", vert='bottom', max_line_length=3,color=(255,255,0))
    lower_bound_text=snaps.get_string(prompt="Enter lower bound trip number: ", vert='bottom', max_line_length=3,color=(255,255,0))
    sample_size=int(sample_size_text)
    lower_bound=int(lower_bound_text)
    # start the trip counter
    try:
        for trip in range(1,sample_size+1):
            moose_value=moose[trip+lower_bound-2]#1,1 = 2-2 there index = 0 example: moose[0]
            calf_value=calf[trip+lower_bound-2]
            mile_value=miles[trip+lower_bound-2]
            hour_value=hours[trip+lower_bound-2]
            min_value=mins[trip+lower_bound-2]
            date_value=dates[trip+lower_bound-2]
            note_value=notes[trip+lower_bound-2]
            weather_value=weather[trip+lower_bound-2]
            ev_gain=elevation_gain[trip+lower_bound-2]
            ev_loss=elevation_loss[trip+lower_bound-2]
            mx_speed=max_speed[trip+lower_bound-2]
            avg_speed=average_speed[trip+lower_bound-2]
            # create date string
            date_value_text = ('Trip '+str(trip)+'\n'+date_value)
            # Create moose and calf strings
            moose_value_text=('\nMoose: '+str(moose_value))
            moose_calf_value_text=('\nMoose Calves: '+str(calf_value))
            # Create mile string
            mile_value_text=('\nMiles: '+str(mile_value))
            # Create hour string
            hour_value_text=('\nHours: '+str(hour_value))
            # Create minute string
            min_value_text=('\nminutes: '+str(min_value))
            # Create a weather string
            weather_value_text=('\nweather: '+weather_value)
            # Create a note string
            note_value_text=('\nnotes: '+note_value)
            elevation_gain_value_text=('\nelevation gain: '+str(ev_gain))
            elevation_loss_value_text=('\nelevation loss: '+str(ev_loss))
            max_speed_value_text=('\nmax speed: '+str(mx_speed))
            average_speed_value_text=('\naverage speed: '+str(avg_speed))
            snaps.display_image('fx/jpg/babymoose2.jpg')
            snaps.display_message(date_value_text+mile_value_text+hour_value_text+min_value_text+max_speed_value_text+average_speed_value_text+elevation_gain_value_text+elevation_loss_value_text+moose_value_text+moose_calf_value_text+weather_value_text+note_value_text,color=(0,0,0),size=30, horiz='left', vert='bottom')
            time.sleep(3)

    except IndexError:
            over_by=sample_size-len(dates)
            over_by_text=str(over_by)
            snaps.display_message('Invalid range by'+over_by_text,color=(255,255,255),size=25, horiz='left', vert='Top')
            time.sleep(3)
    snaps.display_image('fx/jpg/Atown.jpg')
# function 3
def total_stats():
    '''
    Print out the total values
    '''
    
    total=0
    total0=0
    total1=0
    total2=0
    total3=0
    total4=0
    for miles_value in miles:
        total=total+miles_value
    for moose_value in moose:
        total1=total1+moose_value
    for calf_value in calf:
        total0=total0+calf_value
    for hour_value in hours:
        total2 = total2+hour_value
    for min_value in mins:
        total3 = total3+min_value
    for second_value in seconds:
        total4 = total4+second_value
    total_x=(total3/60)
    total_y=total_x+total2
    grand_hour=int(total_y)
    grand_min_decimal=total_y-grand_hour
    grand_min=int((grand_min_decimal*60)+(total4/60))
    if grand_min>=2:
        minute_v='Minutes'
    else:
        minute_v='Minute'
    if grand_hour>=2:
        hour_v='Hours'
    else:
        hour_v='Hour'
    snaps.display_image('fx/jpg/aquamoose.jpg')
    total_string=snaps.get_string('\nTotal Moose Seen: '+str(total1)+'\n\nTotal Miles Biked: '+str(round(total,2))+'\n\nTotal Time Spent Biking: '+str(grand_hour)+hour_v+' and '+str(grand_min)+minute_v+'\n\nPRESS THE ENTER KEY TO EXIT', vert='bottom',horiz='left',color=(0,0,0))
    cwd = os.getcwd()
    if total > 7000:
        snaps.display_image('fx/jpg/omg.jpg')
        snaps.display_message("Congrats On Biking Over 7,000 Miles \n\tIn\nAnchorage Alaska!\nEnjoy The Secret Movie_<@:D",color=(255,255,0),size=50,vert='top',horiz='left')
        snaps.play_sound('fx/siren.wav')
        time.sleep(5)
        snaps.display_image("fx/jpg/Atown.jpg")
        time.sleep(1)       
        os.startfile(cwd+"fx/secret_folder/7k.mp4")
        time.sleep(360)
        os.system('powershell.exe Stop-Process (Get-Process -ProcessName *video*);exit')
        snaps.display_image("fx/jpg/Atown.jpg")
    else:
        snaps.display_image('fx/jpg/Atown.jpg')
        snaps.display_message('<@:D_Log More Miles To Unlock A Secret_<@:D',size=77,vert='top',horiz='left',color=(1,36,86))
        time.sleep(7)
# function 4
def elevation_stats():
    '''
    Print out a total elevation gain and loss
    '''
    total=0
    total1=0
    for gain_value in elevation_gain:
        gain_value_number=float(gain_value)
        total=total+gain_value_number
    for loss_value in elevation_loss:
        loss_value_number=float(loss_value)
        total1=total1+loss_value_number
    tl_string=str(int(total))
    tl_string1=str(int(total1))
    snaps.display_image('fx/jpg/babywithmom2.jpg')
    total_string=snaps.get_string('\nTotal Elevation Gain Was: '+tl_string+' Vertical Feet\n'+'\nTotal Elevation Loss Was: '+tl_string1+' Vertical feet\n'+'\nPRESS THE ENTER KEY TO EXIT', vert='top',color=(0,0,0))
    snaps.display_image('fx/jpg/Atown.jpg')
# function 5=
def highest_stats():
    '''
    Print out the highest miles values
    '''
    try:
        highest=miles[0]
        highest0=calf[0]
        highest2=moose[0]
        highest3=max_speed[0]
        highest4=hours[0]


    except IndexError:
        highest=0
        highest0=0
        highest2=0
        highest3=0
        highest4=0

    for miles_value in miles:
        if miles_value>highest:
            highest=miles_value
    for moose_value in moose:
        if moose_value>highest2:
            highest2=moose_value
    for calf_value in calf:
        if calf_value>highest0:
            highest0=calf_value
    for hour_value in hours:
        if hour_value>highest4:
            highest4=hour_value
    for max_value in max_speed:
        if max_value>highest3:
            highest3=max_value
    highest_text=str(highest)
    highest0_text= str(highest0)
    highest2_text = str(highest2)
    highest3_text = str(highest3)
    highest4_text=str(highest4)
    snaps.display_image('fx/jpg/sunset1.jpg')
    if highest4>1:
        hour_v="Hours"
    else:
        hour_v="Hour"
    total_string=('\nMost Moose Seen In One Trip: '+str(highest2_text)+'\nMost Moose Calves Seen In One Trip: '+(highest0_text)+'\nThe Most Miles Biked In One Trip: '+str(highest_text)+'\nTop Speed In One Trip: '+str(highest3_text)+'mph'+'\nLongest Ride Time was over : '+str(highest4_text)+hour_v+'\nPRESS THE ENTER TO EXIT')
    snaps.get_string(total_string,size=40,vert='bottom',horiz='left',color=(255,255,0))
    snaps.display_image('fx/jpg/Atown.jpg')
def average_stats():
    '''
    Print out the average miles value
    '''
    total=0
    total1=0
    total2=0
    total3=0
    try:
        for miles_value in miles:
            total = total+miles_value
        average_miles=total/len(miles)
    except ZeroDivisionError:
        average_miles=0

    for speed_value in average_speed:
        speed_value_number=float(speed_value)
        total3 = total3+speed_value_number
    try:
        average_speed_per_trip=total3/len(average_speed)
    except ZeroDivisionError:
        average_speed_per_trip=0
    snaps.display_image('fx/jpg/sealion.jpeg')
    total_string='Average Miles Per Trip: '+(str(round(average_miles,2)))+'\n'+'\nAverage Speed Was '+str(round(average_speed_per_trip,2))+'Miles Per Hour\n'+'\nPRESS THE KEY TO EXIT'
    snaps.get_string(total_string,vert='bottom',size=40,color=(0,0,0))
    snaps.display_image('fx/jpg/Atown.jpg')
# function 7
def save_stats(file_path="_output"):
    '''
    Saves the contents of the sales list in a file
    file_path gives he path to the file to save
    Raises file exceptions if the save fail
    ''' 
    save_name_text = snaps.get_string('Enter Save Name',color=(255,255,0))
    save_name='/'+save_name_text
    try:
        os.mkdir(file_path+save_name)
    except FileExistsError:
        snaps.display_message('File Already Exsits\nTry A Different Save Name\n[Returning to main menu]',color=(255,255,0),size=70, horiz='left', vert='bottom')
        time.sleep(4)
        return
    #pg 248
    try:
        # Open the output file
        output_file=open(file_path+save_name+'/miles.txt', 'w')
        output_file0=open(file_path+save_name+'/calf.txt', 'w')
        output_file2=open(file_path+save_name+'/moose.txt', 'w')
        output_file3=open(file_path+save_name+'/hours.txt', 'w')
        output_file4=open(file_path+save_name+'/mins.txt', 'w')
        output_file5=open(file_path+save_name+'/dates.txt', 'w')
        output_file6=open(file_path+save_name+'/weather.txt', 'w')
        output_file7=open(file_path+save_name+'/notes.txt', 'w')
        output_file8=open(file_path+save_name+'/ev_gain.txt', 'w')
        output_file9=open(file_path+save_name+'/ev_loss.txt', 'w')
        output_file10=open(file_path+save_name+'/max_speed.txt', 'w')
        output_file11=open(file_path+save_name+'/average_speed.txt', 'w')
        output_file12=open(file_path+save_name+'/seconds.txt', 'w')

        #Work through the sales values in the list
        for mile_value in miles:
            # write out the sale as a string
            output_file.write(str(mile_value)+'\n')
            #print('file Written Successfully to: ',file_path+'miles.txt')
        for moose_value in moose:
            output_file2.write(str(moose_value)+'\n')
            #print('file Written Successfully',file_path+'moose.txt')
        for calf_value in calf:
            output_file0.write(str(calf_value)+'\n')
            #print('file Written Successfully',file_path+'moose.txt')
        for hour_value in hours:
            output_file3.write(str(hour_value)+'\n')
            #print('file Written Successfully',file_path+'hours.txt')
        for min_value in mins:
            output_file4.write(str(min_value)+'\n')
            #print('file Written Successfully',file_path+'mins.txt')
        for date_value in dates:
            output_file5.write(date_value+'\n')
            #print('file Written Successfully',file_path+'mins.txt')
        for weather_value in weather:
            output_file6.write(weather_value+'\n')
            #print('file Written Successfully',file_path+'mins.txt')
        for note_value in notes:
            output_file7.write(note_value+'\n')
            #print('file Written Successfully',file_path+'mins.txt')
        for ev_gain_value in elevation_gain:
            output_file8.write(str(ev_gain_value)+'\n')
            #print('file Written Successfully',file_path+'mins.txt')
        for ev_loss_value in elevation_loss:
            output_file9.write(str(ev_loss_value)+'\n')            
            #print('file Written Successfully',file_path+'mins.txt')
        for max_value in max_speed:
            output_file10.write(str(max_value)+'\n')            
            #print('file Written Successfully',file_path+'mins.txt')
        for avg_value in average_speed:
            output_file11.write(str(avg_value)+'\n')            
            #print('file Written Successfully',file_path+'mins.txt')
        for second_value in second_speed:
            output_file12.write(str(second_value)+'\n')            
            #print('file Written Successfully',file_path+'mins.txt')
    except:
        print('Something went wrong <@:(')
    finally:
        output_file.close()
        output_file0.close()
        output_file2.close()
        output_file3.close()
        output_file4.close()
        output_file5.close()
        output_file6.close()
        output_file7.close()
        output_file8.close()
        output_file9.close()
        output_file10.close()
        output_file11.close()
        output_file12.close()
    snaps.display_message('Save Path: '+file_path+save_name,color=(255,255,0),size=70,vert='bottom',horiz='left')
    time.sleep(4)
# function 8
def load_stats(file_path="_output"):
    '''
    Loads the miles list in a file from a file
    file_path gives the path to the file to load
    Raises file exceptions if the load fails.  
    '''
    load_name_text = snaps.get_string('Press The Enter Key To Load Test Data:\nOr\nEnter Data Set Name To Load: ', size=50,color=(255,255,0))
    load_name = '/'+load_name_text
    miles.clear()
    moose.clear()
    calf.clear()
    hours.clear()
    mins.clear()
    seconds.clear()
    dates.clear()
    weather.clear()
    notes.clear()
    elevation_gain.clear()
    elevation_loss.clear()
    max_speed.clear()
    average_speed.clear()
    try:
        m_file='Miles Data Missing'
        input_file = open(file_path+load_name+'/miles.txt','r')
        for line in input_file:
            miles.append(float(line.strip('\n')))
        input_file.close()
        m_file='Moose Data Missing'
        input_file2 = open(file_path+load_name+'/moose.txt','r')
        for line in input_file2:
            moose.append(int(line.strip('\n')))
        input_file2.close()
        m_file='Calf Data Missing'
        input_file0 = open(file_path+load_name+'/calf.txt','r')
        for line in input_file0:
            calf.append(int(line.strip('\n')))
        input_file0.close()
        m_file='Hours Data Missing'
        input_file3 = open(file_path+load_name+'/hours.txt','r')
        for line in input_file3:
            hours.append(float(line.strip('\n')))
        input_file3.close()
        m_file='Minute Data Missing'
        input_file4 = open(file_path+load_name+'/mins.txt','r')
        for line in input_file4:
            mins.append(float(line.strip('\n')))
        input_file4.close()
        m_file='Date Data Missing'
        input_file5 = open(file_path+load_name+'/dates.txt','r')
        for line in input_file5:
            dates.append(line.strip('\n'))
        input_file5.close()
        m_file='Weather Data Missing'
        input_file6 = open(file_path+load_name+'/weather.txt','r')
        for line in input_file6:
            weather.append(line.strip('\n'))
        input_file6.close()
        m_file='Note Data Missing'
        input_file7 = open(file_path+load_name+'/notes.txt','r')
        for line in input_file7:
            notes.append(line.strip('\n'))
        input_file7.close()
        m_file='ev_gain Data Missing'
        input_file8 = open(file_path+load_name+'/ev_gain.txt','r')
        for line in input_file8:
            elevation_gain.append(float(line.strip('\n')))
        input_file8.close()
        m_file='ev_loss Data Missing'
        input_file9 = open(file_path+load_name+'/ev_loss.txt','r')
        for line in input_file9:
            elevation_loss.append(float(line.strip('\n')))
        input_file9.close()
        m_file='Max Speed Data Missing'
        input_file10 = open(file_path+load_name+'/max_speed.txt','r')
        for line in input_file10:
            max_speed.append(float(line.strip('\n')))
        input_file10.close()
        m_file='Average Speed Data Missing'
        input_file11 = open(file_path+load_name+'/average_speed.txt','r')
        for line in input_file11:
            average_speed.append(float(line.strip('\n')))
        input_file11.close
        m_file='Seconds Data Missing'
        input_file12 = open(file_path+load_name+'/seconds.txt','r')
        for line in input_file12:
            seconds.append(float(line.strip('\n')))
        input_file11.close
    except FileNotFoundError:
        snaps.display_message('Data Corrupted: '+m_file,color=(255,255,0),size=70,vert='bottom',horiz='left')
        time.sleep(4)
    finally:
        snaps.display_message('Loaded From:\n'+file_path+'/'+load_name_text,color=(255,255,0),size=35,vert='bottom',horiz='left')
        time.sleep(4)

# <@:D <@:D <@:D <@:D <@:D <@:D
#  function <@:D
def teletype_print(text='<@:D<@:D<@:D<@:D<@:D\n<@:D<@:D<@:D<@:D<@:D<@:D<@:D''', delay=.1):
    for ch in text:
        print(ch, sep=' ', end = ' ', flush=True)
        time.sleep(delay)

# function X
def start_x():
    '''
    <@:D
    '''
    try:
        path = "fx/jpg/"
        directories = os.listdir(path)
        for file in directories:
            display_text=(path+file)
            print(display_text)
            snaps.display_image(display_text)
            time.sleep(2)
    except pygame.error:
        file_text=str(file)
        snaps.display_image('fx/jpg/omg.jpg')
        error_prompt='['+file_text+']'+' Caused A Problem <@:(\nRemove: ['+file_text+']'+'\nFrom: '+path+'\nAnd Restart The Slide Show'
        x=snaps.get_string(error_prompt+'\nPress the Enter key to return to the main menu',size=30,margin=20,vert='top',horiz='left',color=(255,255,0))
        if x:
            return
    finally:
        snaps.display_image('fx/jpg/Atown.jpg')
# function_pgm_11 [date/weather/tme]
def HUD_weather_date_time(_t1=True):
    count = 1
    snaps.display_image("fx/jpg/Atown.jpg")
    while _t1 == True: #Loop that never ends <@:D###
        current_time = time.localtime()
        if current_time.tm_hour >= 13:
            print(current_time.tm_hour-12)
            hour_int=int(current_time.tm_hour)
            hour_string=str(hour_int-12)
        else:
            hour_string = str(current_time.tm_hour)
        if current_time.tm_min <10:
            minute_string='0'+str(current_time.tm_min)
        else:
            minute_string = str(current_time.tm_min)
        if current_time.tm_hour >= 12:
            ampm='PM'
        else:
            ampm='AM'
        weather_desc = str(snaps.get_weather_desciption(latitude=61.217381, longitude=-149.863129))
        weather_tmp = str(snaps.get_weather_temp(latitude=61.217381, longitude=-149.863129))
        month_text=str(current_time.tm_mon)
        day_text=str(current_time.tm_mday)
        year_text=str(current_time.tm_year)
        date_text=(month_text+'-'+day_text+'-'+year_text)
        time_string = ('\t'+date_text+'\n'+hour_string+':'+minute_string+':'+ampm+'\n'+'The Conditons in Anchorage are: '+weather_desc+"_<@:D"'\n'\
        +'The tempearture is: '+weather_tmp+'F')
        snaps.display_message(time_string,color=(0,0,0),size=30, horiz='left', vert='top')
        time.sleep(1)
        count += 1#incrmets after the continue
        if count<=2:
            count_string = str(count)
            print(count_string+"<@:D")
            continue
        elif count>=4:
            _t1=False 
            print('clock ends')
##############Start###################
#_<@:D                              #
##_<@:D                             #                            
####_<@:D                           #
#####_<@:D                          #
analyze_stats()######################
#####_<@:D                          #
####_<@:D                           #
###_<@:D                            #
##_<@:D                             #
#_<@:D        _bikeApp:[8-23-20]#V1
###############END####################

##############Start#################################Start###################
