from spy_database import spy_details_dict, spy_friend_dict, friends_list, spy_chat, status_list  #dictionaries and lists
from steganography.steganography import Steganography   # for encode and decode a msg
from datetime import datetime      # for date and time

def menu_choices(spy_name):    # spy choices from main menu
    while True:
        spy_choice = spy_menu(spy_name)     # spy menu
        if spy_choice == 1:      # add status
            type_of_status = int(raw_input("1.Existing status \n2.New status"))
            if type_of_status == 1:   # set default status from a list
                spy_status = int(raw_input("1.Buzy \n2.Good morning \n3.At meeting \n4.feeling sad \n5.feeling happy"))
                spy_status = status_list[spy_status - 1]
                spy_details_dict[spy_name]['status'] = spy_status
                print "your new status " + spy_status
            elif type_of_status == 2:    # set new status
                spy_status = raw_input("enter your status")
                spy_details_dict[spy_name]['status'] = spy_status
                print "your new status " + spy_status
            else:
                print "wrong choice"
        elif spy_choice == 2:  # add a friend
            spy_rating = spy_details_dict[spy_name]['rating']
            add_a_friend(spy_name, spy_rating)
            print spy_friend_dict[spy_name]

        elif spy_choice == 3:   # select a friend and send message
            send_a_secret_msg(spy_name)  # calling function for encoding msg

        elif spy_choice == 4:    #read a secret message
            friend = select_friend() # calling function to select a friend
            msg = decode_msg(spy_name, friend) # calling function to decode msg
            if msg != None:
                print msg

        elif spy_choice == 5:     #read chat from user
            friend = select_friend()  # calling function to select a friend
            msg = decode_msg(spy_name, friend)
            time = spy_chat[spy_name][friend]['time']
            print friend + ":" + msg + " time : " + time

        elif spy_choice == 6:      #exit
            exit()


def decode_msg(spy_name, friend):   # function for decoding msg
    p = None
    if friend in spy_chat[spy_name]:  # does friend exists in list
        read_msg = spy_chat[spy_name][friend]['secret_msg']
        p = Steganography.decode(read_msg)  # decoding msg
    else:
        print "        No Conversation Found       "
    return p


def send_a_secret_msg(spy_name):   # function for encoding msg
    friend = select_friend()     # calling function to select a friend from friend list
    image_path = raw_input("enter image path : ")
    image_name = raw_input("enter image name with extension : ")
    secret_msg = raw_input("enter secret message you want to send")
    output_image = image_path + "\secret_image.jpg"
    Steganography.encode(image_path + "\\" + image_name, output_image, secret_msg) # encoding msg
    date_time = date()
    spy_chat[spy_name] = {
        friend: {
            'secret_msg': output_image,
            'time': date_time}}


def date():   # function for date and time
    date = datetime.today()
    date = date.strftime('%d %B %Y %I %p: %M')
    return date


def select_friend():  # function to select a friend
    i = 0
    for name in spy_friend_dict[spy_name]:  # pick friends name from the dictionary
        i = i + 1
        print str(i) + ". " + name
    spy_select = int(raw_input("select a friend"))
    friend = friends_list[spy_select - 1]
    return friend


def check_age_valid():   # function to check validity of age
    age_true = True
    while age_true:
        age = int(raw_input("enter age say in between 12 and 50\n"))
        if age >= 12 and age <= 50:
            age_true = False
        else:
            print '\ntry again\n'
    return age


def add_a_friend(spy_name, spy_rating):  # function to add a friend
    spy_friend_name = raw_input("enter your friend name")
    if len(spy_friend_name) > 0:
        spy_friend_age = check_age_valid()  # calling function of age validity
        spy_friend_rating = float(raw_input("enter friend's rating"))
        if spy_rating > spy_friend_rating:
            print "friend rating should greater than your rating"

        else:
            spy_friend_dict[spy_name] = {spy_friend_name: {
                'age': spy_friend_age,
                'rating': spy_friend_rating
            }}
        friends_list.append(spy_friend_name)  # adding new friend to friend list
    else:
        print "invalid friend name"


def spy_menu(spy_name):  #function only display spy menu
    print"WELCOME TO THE SPY CHAT"
    print spy_details_dict[spy_name]['salutation'] \
          + " " \
          + spy_name + "\nrating: " + str(spy_details_dict[spy_name]['rating']) \
          + "\nage : " + str(spy_details_dict[spy_name]['age'])
    spy_choice = int(raw_input("\n1.Add status update\n2.Add a friend \n3.Send a secret message\n"
                               "4.Read a secret message\n5.Read chat from a user\n6.close application \nselect : "))
    return spy_choice

# ==============================================================================================

spy_name = raw_input("enter the name")  # enter spy name
spy_check = spy_name in spy_details_dict # check if spy name already exits
if spy_check:
    menu_choices(spy_name)  # calling function to only display spy menu
elif len(spy_name) > 0:  # spy name validity
    spy_salutation = raw_input("enter salutation : \n")
    spy_age = check_age_valid()
    spy_rating = float(raw_input("enter rating .say in 1-5\n"))

    # update spy_details to dictionary
    spy_details_dict[spy_name] = {
        "salutation": spy_salutation,
        "age": spy_age,
        "rating": spy_rating
    }
    print spy_details_dict
    menu_choices(spy_name)  # calling function to only display spy menu
else:
    print"spy name is invalid"
    # ==============================================================================================================
