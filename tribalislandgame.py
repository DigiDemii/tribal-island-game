import sys, time, os 



def start_game():
    start_message = """
Welcome to Tribal Island!"""
    for i in start_message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    print(r"""
                   _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   \
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---""  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~  
              ~        ~~       ~~~       ~
""")
    message = "You wake up and find yourself on a beach."
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    message_two = """
You're dazed and confused, how did you get here?"""
    for i in message_two:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.09)
    message_three = """
You look around and realise that you're alone with no sign of civilization."""
    for i in message_three:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.08)
    message_four = """
You pick yourself up and make the decision to explore your surroundings."""
    for i in message_four:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06)
    message_five = """
Where would you like to go, the jungle, the coast or try and swim?"""
    for i in message_five:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""

Please press: 

1 - for jungle
2 - for coast
3 - for swim

Enter here:  """)
    if response == "1":
        jungle()
    elif response == "2":
        coast()
    elif response == "3":
        swim()
    else:
        print("""
Response not recognised, please try again.""")
        start_game()

def jungle():
    print(r"""
                   ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
jgs \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
""")
    message = """
You step into the jungle.
Aside from the rustling of the trees above you, you hear no other sounds.
You can see the sun through the branches above you, but you know you don't have much daylight left.
As you walk deeper into the jungle you find yourself at an impass.
To the left you see a bear.
To the right is a tribesman gesturing you to follow him.
Where would you like to go, to the bear, the tribesman or try to run away?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - for bear
2 - for tribesman
3 - for run

Enter here:  """)
    if response.capitalize() == "1":
        bear()
    elif response.capitalize() == "2":
        tribesman()
    elif response.capitalize() == "3":
        run()
    else:
        print("""
Response not recognised, please try again.""")
        jungle()

def coast():
    print(r"""
                  ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
""")
    message = """
You decide to walk along the coast to see if you can see anything of use.
The hot sand burns your feet a little, however the breeze from the ocean is very welcome.
You start to feel like you have been walking for a long time, your legs are aching and you are starting to feel weak.
There is still no sign of civilisation, however the jungle is still to the side of you and could provide some well needed shade.
Do you choose to continue along the coast or risk the dangers of the jungle for some shade?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - for jungle
2 - for coast

Enter here:  """)
    if response == "1":
        jungle()
    elif response == "2":
        coast_continue()
    else:
        print("""
Response not recognised, please try again.""")
        coast()


def swim():
    print(r"""
                ___
          /`  _\
          |  / 0|--.
     -   / \_|0`/ /.`'._/)
 - ~ -^_| /-_~ ^- ~_` - -~ _
 -  ~  -| |   - ~ -  ~  -
jgs     \ \, ~   -   ~
         \_|
""")
    message = """
After deciding the jungle looked too dangerous you turn to look at the sea.
It looks cool and inviting, but it could also be your way off the island.
Do you take a paddle in the water to cool off whilst you think of a game plan or do you swim deeper into the ocean hoping to find help?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response_one = input("""
Please press: 

1 - for paddle
2 - for swim

Enter here:  """)
    if response_one == "1":
        message = """
You choose to cool off in the water whilst you gather your thoughts.
As you relax in the gentle waves with the sun on your skin, you feel what you think is seaweed wrapping around your leg.
You look into the water and find yourself surrounded by jellyfish.
One by one they sting you, the pain is unbearable."""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_two = """
You feel your life slipping away.
Your legs weaken and you collapse into the water.
You lose consiousness."""
        for i in message_two:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_three = """
and fade
slowly
away.
"""
        for i in message_three:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.3)
    if response_one == "2":
        message_five = """
You decided to brave the ocean waves and swim into them.
After a few minutes your start to tire, why did you think this was a good decision when you haven't ate for a while?
As you continue you feel something brush against your leg.
Thinking it's possibly just seaweed, you ignore it and continue swimming.
You feel it brush against you again, what could that be?
Suddenly you feel an explosion of pain.
You look down to see a shark has your leg in it's mouth.
It drags you under the water."""
        for i in message_five:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_six = """
You feel your life slipping away.
The water surrounds you and your eyes start to close.
You lose consiousness."""
        for i in message_six:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_seven = """
and fade
slowly
away.
"""
        for i in message_seven:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.3)
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)

def coast_continue():
    print(r"""
             |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
jgs =- =- -=.--"
""")
    message = """
You continue to walk along the coast hoping to find something that can help you.
After walking for a while longer you hear a rumblling in the distance.
Is the heat getting to you or is the rumbling sound real?
You look to the source of the sound and see a huge wave in the distance, this can't be a tsunami surely?
The wave gets closer and the sound is getting louder.
Do you run inland to escape the tsunami or climb up a nearby tree?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - for inland
2 - for tree

Enter here:  """)
    if response == "1":
        message = """
You run inland to try and escape the incoming wave.
Running as fast as you can, you narrowly miss the low hanging branches and felled trees on the ground.
You can hear the rumbling sound getting close, why did you think you could outrun a tsunami?
As you continue running you notice your feet getting wet, the wave is getting closer.
You see the exit of the jungle ahead of you, you're so close!
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_two = """
Your legs are swept from underneath you.
The world around you gets flipped upside down as the monstrous wave envelops you.
You find yourself deep inside the wave, no light can enter and you struggle to breathe.
You feel your eyes starting to close as your mind becomes foggy.
"""
        for i in message_two:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_three = """
You fade
slowly
away.
"""
        for i in message_three:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.3)
    elif response == "2":
        message_four = """
You see that a nearby tree is climbable and take the chance with it.
You get as high as you can and watch as the tsunami consumes the world below you.
You narrowly escaped.
Once everything seems to have calmed down you climb down the tree and walk into the jungle."""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        jungle()
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("""
Response not recognised, please try again.""")
        coast_continue()

def bear():
    print(r"""
    .--.              .--.
   : (\ ". _......_ ." /) :
    '.    `        `    .'
     /'   _        _   `\
    /     0}      {0     \
   |       /      \       |
   |     /'        `\     |
    \   | .  .==.  . |   /
     '._ \.' \__/ './ _.'
jgs  /  ``'._-''-_.'``  \
    """)
    message = """
You decide the bear looks friendly and could protect you from the tribesman.
The bear smiles at you, you definitely made the right decision!
He stands behind you and wraps his arms around you, how kind of him to protect you.
"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    message_two = """
The air around you becomes warm and slightly moist.
You look up to find your head surrounded by the bears mouth, it's teeth sharp and ready to bite down.
"""
    for i in message_two:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.09)
    message_three = """
Crunch.
"""
    for i in message_three:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("""
Response not recognised, please try again.""")
        jungle()

def tribesman():
    print(r"""
                      __               
                 /  \  _.-----._        /`\ _   _
              __/   _\_. ':. ' :'.           \,/
             /__       \,`. `: ':'.                    _
            /        ___\_`.'.':.`:        /'\        /
          _/___           \ .: ' `:                  /
        _/               __\__.`:':               __/
__- _--/      ;               \;':   \  |    /   /
            `~`~`            ~~`~~   \\ || // __/__
  ;        ~~`~~`~~        `~~`~`~~`  \\||//_/   \__
`~~`~     ~`~~`~~`~         ~`~~`~`~   \\//          \
~`~~`      ~~~|~~~        ~`~~`~~`~~~  /  \
`~~`~     `~~~`~~~`  __ -   ~`~||~~`  /====\
~~|~~`     ~~`|~~~__       ~~~`~`~~~~/\/\/\/\
~~`~~~__  _   |_-    `|' ~~`~~~||~~~/,____   \
__|_--  -     |   \( )/    ~~`~||~~/ |/(__)\\ \
  |           |    | |         || /    /\/\    \
  |               // \\        ||/\/\/\/\/\/\/\/\
                ;;.---.;;      |/================\
               ;; () () ;;     /O=O=O=O=O=O=O=O=O=\
               ;;-() ()-;;    /======X|\===========\
               ; \() ()/ ;   /       X| \           \
    ,,;,,         () ()     /        X|  \           \
 ,;,  / ,,;,,     .===.    /         X|   |   _       \
   \,|,,/         |   |   / ( *      X|   |  ====      \
,,;,,|            |   |  /   )       X|     /- \\|      
  \  /,,;,, /^|   |   |\/___( )___O___|o /o }  (@)______
 ,,\|__/  <(- /   |||||    /=/\=\       / \ `/  ()
           / |     |||    /((__))\   []/|  \/   ()
         \(__,\    (|)  _/_) *(* _\_    /       /|\
                       ( )_)(_))(_)_) _/         |
                        Ż _________  (__\________/
               \|/        |)\{'}/(|            __
                          |\     /|            )(
 \|/                      |-|   |-|       _   /XX\    __
      .-'- .              |/ ___ \|\      )( (____)___ - 
  ,;;'       ' . - ' ';,  |)/___\(| \    (__) -__- ~~~~~
 ~;);'               ;;;~      \|/         __-__~~~~~~~~
 )(;; '    )     (   ;);;,    \|| |/    -___-~~~~~~~ ~~~
;;;); /  '  - - - \  (;;),;~   ||/ __ _(_)-~~~~~~~~ ~~~~
~;;`;/  '          \ ;);;;;,   \||(__)~~~ ~~~~~~~~~ ~~~~
(~;;/ .'            \';(;;>;>  __--~~~~~~~~ ~~~____~~~~
\||/.       /    __  \\ \ -;; -~~~~~~~ ~~~ ~ _/    \___/
 |||/     \||  _(__) _\\ \ _|~~~~~~~ ~~~~~~/      /
\||/    .:|||.(_____)_)~~ (_)~~~ ~~~~~~~__~/_~~~ ~|__~~~
 \||_ -- _|||_ ~~~~ ~~~~~ ~~ ~~~~~ ~~~~/    \~~~~~~~
- ~~ ~~~ ~~~~ ~~~~ ~~~~ ~~~~  ~~~~~~~~(~~~~~~|~~~~ ~~~~
~~ ~~ ~~ ~~~ ~~~~ ~~~~ ~~~ ~~~ ~~~~~~~ ~~~~~~~~~~~~~~~~
""")
    message = """
You follow the tribesman to a campsite where you find a group of people gathered around a fire.
They smile at you and ask if you'd like to sit with them.
You sit beside them and enjoy the feeling of no longer being on your feet.
A tribesman asks you if you would like to eat a plate of vegetables and herbs he has gathered.
Do you accept the food?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - yes
2 - no

Enter here:  """)
    if response == "1":
        message = """
You enjoy the tasty plate of food that has been gifted to you.
Not realising just how hungry you were, you devour the food and fall asleep.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        massage()
    elif response == "2":
        message = """
Not knowing the motives of the people around you, you choose to reject the plate of food.
The tribesman seem insulted by this and start to turn on you.
Fearing for your life, you make a run for it.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        leave_campsite()
    else:
        print("""
Response not recognised, please try again.""")
        tribesman()

def massage():
    message = """
As you wake up you find a tribesman stood over you.
He asks if you would like to have a massage to help relieve your aching muscles.
Do you take the massage?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print(r"""
   ,--,
   )""(
  .%nn%.
 /%%%%%%\
.%%%%%%%%.
|"*%%%%*"|
|        |
| Garlic |
| Butter |
|8n....n8|
|%%%%%%%%|
|%%%%%%%%|
 "*%%%%*" 
 """)
    response = input("""
Please press: 

1 - yes
2 - no

Enter here:  """)
    if response == "1":
        message = """
You accept the offer and lay back to enjoy the massage.
The oil smells suspiciously like butter mixed with garlic, but you put it to the back of your mind.
After all, what else are they going to use as massage oil around here?
You feel yourself drifting into a peaceful sleep.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_two = """
When you start to wake you feel an uncomfortable feeling.
It feels like you are slowly spinning.
You notice how hot you feel, almost as if you're close to a flame.
As you open your eyes you realise where you are.
"""
        for i in message_two:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_three = """
You are slowly being turned on the spitroast in the camp.
You are their next meal.
"""
        for i in message_three:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.3)
        print("""
Would you like to start again?""")
        response_two = input("""
1 - yes
2 - no

Enter here:  """)
        if response_two == "1":
            start_game()
        elif response_two == "2":
            message_four = """
Thank you for playing!"""
            for i in message_four:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.05)
        else:
            print("""
Response not recognised, please try again.""")
            massage()
    elif response == "2":
        message = """
You reject the massage, you don't even know these people, why would you let them massage you? 
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        leave_campsite()
    else:
        print("""
Response not recognised, please try again.""")
        massage()


def leave_campsite():
    print(r"""
                     .e$c"*eee...                      
                z$$$$$$.  "*$$$$$$$$$.                    
            .z$$$$$$$$$$$e. "$$$$$$$$$$c.                 
         .e$$P""  $$  ""*$$$bc."$$$$$$$$$$$e.             
     .e$*""       $$         "**be$$$***$   3             
     $            $F              $    4$r  'F            
     $           4$F              $    4$F   $            
    4P   \       4$F              $     $$   3r           
    $"    r      4$F              3     $$r   $           
    $     '.     $$F              4F    4$$   'b          
   dF      3     $$    ^           b     $$L   "L         
   $        .    $$   %            $     ^$$r   "c        
  JF             $$  %             4r     '$$.   3L       
 .$              $$ "               $      ^$$r""         
 $%              $$P                3r  .e*"              
'*=*********************************$$P"     
""" )
    message = """
You run as fast as you can, leaving the campsite behind you.
Eventually you come to a crossroads, do you turn left or right?"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - left
2 - right

Enter here:  """)
    if response == "1":
        message = """
You run through the jungle hoping to find somewhere to hide.
A large felled tree is to the side of you.
You hide behind it and wait for a while so the tribesman lose track of you.
The silence of the jungle feels almost peaceful.
Behind you there is a snapping sound as if someone has walked across a branch.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_two = """
You turn around to see a pack of wolves staring at you.
They stand angrily, bearing their teeth.
The leader charges for you and the rest follow.
"""
        for i in message_two:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_three = """
They tear at your flesh
slowly.
"""
        for i in message_three:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.3)
    elif response == "2":
        message_four = """
You run to your right away from the campsite and the jungle.
The ocean is to your left, perhaps you could find a way back onto the beach where it was safer?
As you are running you feel the earth at your feet crumbling.
"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_five = """
The earth collapses below you.
As it does you realise just how high up you are.
There is a very large drop from where you are to the beach below.
"""
        for i in message_five:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_six = """
The air whooshes past you as you fall
very swiftly
to your death.
"""
        for i in message_six:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.2)
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("""
Response not recognised, please try again.""")
        leave_campsite()

def run():
    print(r"""
           _( }
   -=  _  <<  \
      `.\__/`/\\
 -=     '--'\\  `
      -=    //
jgs         \)
""")
    message = """
You run as fast as you can.
Good job, the bear hadn't eaten in weeks, nor had the tribesman!
Whilst walking through the jungle you make a decision, do you explore further into the jungle or do you climb 
a tall tree to better see your surroundings?
"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - explore jungle
2 - climb tree

Enter here:  """)
    if response == "1":
        message = """
You decide to explore deeper in the jungle.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        jungle_exploration()
    elif response == "2":
        message = """
You decide to climb a tall tree to get a better look around you.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        climb_tall_tree()
    else:
        print("""
Response not recognised, please try again.""")
        run()

def jungle_exploration():
    print(r"""
                .        +          .      .          .
     .            _        .                    .
  ,              /;-._,-.____        ,-----.__
 ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
  `                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /           .
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              +
   .                 `.:.  /:'  }      .
           .           ):_(:;   \           .
                      /:. _/ ,  |
                   . (|::.     ,`                  .
     .                |::.    {\
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
dew   ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~
""")
    message = """
You continue to explore the forest to look for a way off the island.
As you are navigating the forest you hear a haunting sound; the crunching of branches behind you.
As you turn your head to glance in the direction of the sound, you are
met by warm breath and the sight of a gaping mouth with large teeth.
You know you are done for and accept your fate.
You pay the bear a visit as he looks friendly and welcoming.
He smiles as you walk closer towards him.
With each step his smile grows larger; the sun glints off the teeth
he is now bearing at you.
"Im so lucky to have stumbled upon you, I havent ate in weeks!", said
the bear.
"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    message_two = """
You close your eyes and accept your fate.
"""
    for i in message_two:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.07)
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("""
Response not recognised, please try again.""")
        jungle_exploration()

def climb_tall_tree():
    print(r"""
                  * *    
           *    *  *
      *  *    *     *  *
     *     *    *  *    *
 * *   *    *    *    *   *
 *     *  *    * * .#  *   *
 *   *     * #.  .# *   *
  *     "#.  #: #" * *    *
 *   * * "#. ##"       *
   *       "###
             "##
              ##.
              .##:
              :###
              ;###
            ,####.
/\/\/\/\/\/.######.\/\/\/\/\
""")
    message = """
Once you reach the top of the tree you can see everywhere around you.
You notice out in the ocean is a boat, could this be your way off the island?
Do you run to the beach in hopes the boat will see you or do you decide it's too far?
"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    response = input("""
Please press: 

1 - run for boat
2 - ignore the boat

Enter here:  """)  
    if response == "1":
        message = """
You decide to run towards the beach to flag down the boat.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        boat()
    elif response == "2":
        message = """
With your confidence beaten down and your spirits low, you accept that the boat is too 
far and instead decide to continue exploring the jungle.
As you are walking you hear a slight hissing sound, could this be a snake or is this your imagination running wild?
You take a few steps and are greated by a very large python.
It loops around you for a while, rendering you unable to function.
"""
        for i in message:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        message_two = """
As it prints itself into your body, it bites your leg before swallowing you whole.
You calculate all the different results that could've come from your day and realise"""
        for i in message_two:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09)
        message_three = """
you were doomed from the beginning.
"""
        for i in message_three:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.3)
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("""
Response not recognised, please try again.""")
        climb_tall_tree()

def boat():
    print(r"""
                 ____
              ---|
  \/            /|     \/
               / |\
              /  | \        \/
             /   || \
            /    | | \
           /     | |  \
          /      | |   \
         /       ||     \
        /        /       \
       /________/         \
       ________/__________--/
 ~~~   \___________________/
         ~~~~~~~~~~       ~~~~~~~~
~~~~~~~~~~~~~     ~~~~~~~~~
                               ~~~~~~~~~
""")
    message = """
Your feet hurt from running across the broken branches on the jungle floor, but the
sweet relief of the soft sand soon eases the pain.
You wave your hands to the boat to signal that you are in need of help.
After a few minutes of watching the boat tackle the waves, it finally lands on the beach.
The sailors hoist you into the boat and greet you with a blanket to keep you warm.
You sit back as the slight rocking of the boat lulls you into a peaceful sleep.
"""
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    message_two = """
You're safe now, you'll be back home soon.
"""
    for i in message_two:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    print("""
Would you like to start again?""")
    response_two = input("""
1 - yes
2 - no

Enter here:  """)
    if response_two == "1":
        start_game()
    elif response_two == "2":
        message_four = """
Thank you for playing!"""
        for i in message_four:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("""
Response not recognised, please try again.""")
        boat()

start_game()


