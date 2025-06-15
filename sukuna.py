import pyjokes
def sukuna():
    print("Sukuna : hello brat I am sukuna the strongest of all time, if u dont wanna talk say 'bye'")
 #it keeps checkng unit i say bye or exit
    while True:                                     
        user_inp=input("you:").lower().strip()  
# strip() removes spaces  
        if user_inp in["bye", "exit"]:
            print("Sukuna:fine see you later brat ")
            break
        elif "hello" in user_inp or "hi" in user_inp:
            print("hi there")
        elif "joke pls" in user_inp :
            joke = pyjokes.get_joke()
            print(joke)  
        elif "how are you" in user_inp:
            print("as good as you")
        elif "your name" in user_inp:
            print("im sukuna but u can call me sir")
        else:
            print("idk what to say im spechless")

sukuna()
