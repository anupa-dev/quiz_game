import random
from prettytable import PrettyTable

quiz_data={
    'BOOKS':[{'q':"Who wrote 'Harry Potter'?",'a':'J.K. Rowling','b':'Tolkien','c':'C.S. Lewis','ans':'a'},
             {'q':"Which book is about Middle Earth?",'a':'Harry Potter','b':'Lord of the Rings','c':'Narnia','ans':'b'},
             {'q':"Who wrote 'Pride and Prejudice'?",'a':'Charlotte Bronte','b':'Jane Austen','c':'Emily Bronte','ans':'b'},
             {'q':"Which book features Sherlock Holmes?",'a':'Sherlock Holmes series','b':'Agatha Christie','c':'Hercule Poirot','ans':'a'},
             {'q':"Who wrote 'The Great Gatsby'?",'a':'F. Scott Fitzgerald','b':'Ernest Hemingway','c':'Mark Twain','ans':'a'},
             {'q':"What is the first book of Narnia series?",'a':'The Lion, the Witch and the Wardrobe','b':'Prince Caspian','c':'The Horse and His Boy','ans':'a'},
             {'q':"Who wrote 'To Kill a Mockingbird'?",'a':'Harper Lee','b':'J.D. Salinger','c':'John Steinbeck','ans':'a'},
             {'q':"Which book is set in dystopian society of Panem?",'a':'Divergent','b':'The Hunger Games','c':'Maze Runner','ans':'b'},
             {'q':"Who wrote 'Moby Dick'?",'a':'Herman Melville','b':'Nathaniel Hawthorne','c':'Mark Twain','ans':'a'},
             {'q':"Which book series features Katniss Everdeen?",'a':'The Hunger Games','b':'Divergent','c':'Twilight','ans':'a'}],
    'MOVIES':[{'q':"Who directed 'Inception'?",'a':'Nolan','b':'Spielberg','c':'Tarantino','ans':'a'},
              {'q':"Which movie won Best Picture in 2020?",'a':'1917','b':'Parasite','c':'Joker','ans':'b'},
              {'q':"Who played Jack in 'Titanic'?",'a':'Leonardo DiCaprio','b':'Brad Pitt','c':'Tom Cruise','ans':'a'},
              {'q':"Which movie features 'May the Force be with you'?",'a':'Star Wars','b':'Star Trek','c':'Guardians of the Galaxy','ans':'a'},
              {'q':"Who directed 'Pulp Fiction'?",'a':'Steven Spielberg','b':'Quentin Tarantino','c':'Christopher Nolan','ans':'b'},
              {'q':"Which movie is about dreams within dreams?",'a':'Inception','b':'Shutter Island','c':'The Matrix','ans':'a'},
              {'q':"Who played Iron Man?",'a':'Chris Evans','b':'Robert Downey Jr.','c':'Chris Hemsworth','ans':'b'},
              {'q':"Which movie features a ring that must be destroyed?",'a':'The Hobbit','b':'The Lord of the Rings','c':'Harry Potter','ans':'b'},
              {'q':"Who directed 'Avatar'?",'a':'James Cameron','b':'Peter Jackson','c':'Ridley Scott','ans':'a'},
              {'q':"Which movie is about a boxing underdog called Rocky?",'a':'Creed','b':'Rocky','c':'Million Dollar Baby','ans':'b'}],
    'MUSIC':[{'q':"Who sang 'Shape of You'?",'a':'Ed Sheeran','b':'Justin Bieber','c':'Shawn Mendes','ans':'a'},
             {'q':"Which band sang 'Bohemian Rhapsody'?",'a':'Queen','b':'The Beatles','c':'Pink Floyd','ans':'a'},
             {'q':"Who is the King of Pop?",'a':'Elvis Presley','b':'Michael Jackson','c':'Prince','ans':'b'},
             {'q':"Who released 'Rolling in the Deep'?",'a':'Adele','b':'Beyonce','c':'Rihanna','ans':'a'},
             {'q':"Who sang 'Blinding Lights'?",'a':'The Weeknd','b':'Drake','c':'Post Malone','ans':'a'},
             {'q':"Which band sang 'Hey Jude'?",'a':'The Beatles','b':'Queen','c':'Pink Floyd','ans':'a'},
             {'q':"Who sang 'Bad Guy'?",'a':'Billie Eilish','b':'Dua Lipa','c':'Ariana Grande','ans':'a'},
             {'q':"Lead singer of Coldplay?",'a':'Chris Martin','b':'Bono','c':'Brandon Flowers','ans':'a'},
             {'q':"Who released 'Thriller'?",'a':'Michael Jackson','b':'Prince','c':'Justin Timberlake','ans':'a'},
             {'q':"Who sang 'Someone Like You'?",'a':'Adele','b':'Taylor Swift','c':'Katy Perry','ans':'a'}]
}

users={}
scoreboard={}

def displayquiz(user):
    print("\nLet us begin the game!!!\n")
    while True:
        topics=list(quiz_data.keys())
        print("Topics:",topics)
        choice=input('Choose your topic: ').upper()
        if choice not in topics:
            print("Invalid topic.")
            continue
        data=quiz_data[choice].copy()
        realscore=0
        answers_list=[]
        for i in range(10):
            x=random.choice(data)
            data.remove(x)
            answers_list.append((x['q'],x[x['ans']]))
            print("\nQ:",x['q'])
            print("A:",x['a'],"B:",x['b'],"C:",x['c'])
            ans=input("Answer(a,b,c): ").lower()
            if ans==x['ans']:
                realscore+=1
        scoreboard[user]['score']+=realscore
        scoreboard[user]['ngames']+=1
        avg_score=scoreboard[user]['score']/scoreboard[user]['ngames']
        print(f"\nYou scored {realscore}/10\n")
        if avg_score>7:
            print("CONGRATS!! LEVEL ONE ACE!")
        elif avg_score>5:
            print("KEEP IT UP!! LEVEL TWO KNOCKOUT KING!")
        elif avg_score>3:
            print("YAY!! LEVEL THREE REIGNING QUEEN!")
        else:
            print("GREAT!! LEVEL FOUR THRIVING JACK!")
        if input("See correct answers? (y/n): ").lower()=='y':
            t=PrettyTable()
            t.field_names=['Q','Ans']
            for q,a in answers_list:
                t.add_row([q,a])
            print(t)
        if input("Continue? (y/n): ").lower()=='n':
            if input("Exit? (y/n): ").lower()=='y':
                print("Thanks for playing!")
                break

def signup():
    global users
    while True:
        user=input('Username: ')
        pwd=input('Password: ')
        if user in users:
            print("Username taken")
        elif 'admin' in user.lower():
            print("Invalid username")
        else:
            users[user]=pwd
            scoreboard[user]={'score':0,'ngames':0}
            print("Sign-up done\n")
            displayquiz(user)
            break

def login():
    global users
    while True:
        user=input('Username: ')
        pwd=input('Password: ')
        if user in users and users[user]==pwd:
            print("Login success")
            displayquiz(user)
            break
        else:
            if input("Retry? (y/n): ").lower()=='n':
                break

def intro():
    print("\n"+"-"*120)
    print(' '*48,'WELCOME TO\n',' '*47,'QUIZZLER')
    print("-"*120+"\n")
    c=input('Sign up/Login?(1/2): ')
    if c=='1':
        signup()
    elif c=='2':
        login()
    else:
        print("Invalid choice")
        intro()

intro()
