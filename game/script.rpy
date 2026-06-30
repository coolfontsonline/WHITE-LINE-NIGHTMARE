# The script of the game goes in this file.

image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(1)

    play sound "audio/splash.wav"

    show splash with dissolve
    with Pause(3)

    scene black with dissolve
    with Pause(1)

    return

init python:
#TEXT BLIPS
    def magtext(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/mablip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")

    def mourtext(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/moblip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")


define mag = Character("Maggie", image="mag", who_color="#228047", callback=magtext)
define magthink = Character("Maggie", image="mag", who_color="#228047", what_color="#2D50C4",)
define mour = Character("Mourgan", image="mour" , who_color="#733294", callback=mourtext)
define rot = Character("Rotwife383927", image="rot", who_color="#228047")
define kit = Character("kittysockz", image="kit", who_color="#733294")
define trucker =Character("Trucker", image="", who_color="#3727c0")

image mag talk = "maggie-talksprite.png"
image mour talk = "mourgan-talksprite.png"
image rot pfp = "maggie-talksprite.png"
image kit pfp = "mourgan-talksprite.png"

image side mag talk = im.Scale("side-maggie-talksprite.png", 256, 256)
image side mour talk = im.Scale("side-mourgan-talksprite.png", 256, 256)
image side rot pfp = im.Scale("side-maggie-pfp.png", 256, 256)
image side kit pfp = im.Scale("side-mourgan-pfp.png", 256, 256)

image bg road = Tile("bg-road.jpg")
image car = "bg-car"
image door = "bg-mourgan-door"
image trunk = "img-car-trunk"
image backroad = "bg-car-interior-backroad"
image wow1 = "bg-wow-memory"
image wow2 = "bg-wow-steamy"
image raymond1 ="img-raymond-normal"

# The game starts here.

label start:

    scene bg road

    play music "driving.ogg"

    show backroad:
        pos (130,130)
    with dissolve

    # OPENING MONOLOGUE

    "Maggie's hatchback rushes down a Too Clean suburban stroad. Tacky houses and trees unsuited for this dry, humid climate pass her by."
    "All these lawns and freshly planted oaks. Artificial life supported supping from misappropriated mana."
    "This is not kind territory. The plastic facade of white-fence ignorance stapled over seething hatred of the incompatible."
    "All Maggie needs to do is pick up Mourgan, load all her stuff in this tiny 3 door shitbox and fuck off."
    "...And try not to think about all the ways she's gonna turn her girlfriend into soaking wet pleasuremush between now and the time they get home."
    "Her mind swirls with rage. Roiling against the soybean and hog infected Southern Illinois New Home Developments."
    "\"Minnow Creek - A Safe, Stable Community\"\n For you, maybe."
    "This place isn't meant for city seasoned girlfreaks like her, and it isn't for Mourgan either. She deserves so much more."
    "Well-to-do WASPS kissing their wives with eyes wide open before bed every night. Dead ends for suburbanites who never wanted anything more than nothing."
    "Maggie white knuckles the steering wheel, studded armbands tighten around her wrists."
    "Eight hours and we'll be back in Pittsburgh."
    "538. This is it."
    "Maggie picks up the phone sitting in her lap."

    #MAGGIE ARRIVES AT MOURGAN'S HOUSE

    play music "outside.ogg"

    show rot pfp

    show door:
        pos(970, 200)

    play sound "dooropen.wav"

    rot "I'm here, beautiful. wya?"

    show kit pfp

    kit "sdlkjjfhweui hold on holdon holdon AaaAA"

    rot "Alright, we gotta be quick about this though."

    rot "I'll help load your stuff in, but I know how you're gonna be."

    "..."

    "A soft pitter pattering rapidly approaches the orate glass and oak wood door."

    show mour talk

    mour "MAGGIIIIEEEE!!!"

    "The short woman flings herself into Maggie's soft arms. Maggie catches her easily, holding Mourgan tightly against her leather jacket."

    "The two settle and recede into quiet joy, holding eachother for a momentary eternity."

    show mag talk

    mag "I know you're excited but we gotta pack up."

    magthink "If we get held up too long im gonna pass the fuck out. Way too early for me right now."

    mour "don't worry, i got all my stuff ready by the door."



    # THEY PACK INTO THE CAR

    hide backroad

    mag "Shit, is that really all your stuff?"

    mour "just my computer, clothes, bag, some odds and ends."

    mag "Your whole life fits in less than half the trunk size of my car?"

    mour "I don't {i}get{/i} to live as myself. Until today."

    mag "God, i'm so glad you're here."

    mour "mwee heee c'mere."

    "The two girls embrace roundside the rear of the stout car."

    "Mourgan's buries herself in Maggie's leather jacket"

    mour "I'm so excited. I can't believe this is happening."

    mag "Feels pretty good to get away from all this right?"

    "Mourgan gives an enthusiastic nod, still pressed into Maggie's jacket, slightly smudging her makeup."

    mour "mmm, you smell like cigarettes and leather."

    mag "Is that a good thing?"

    mour "everything is good about you."

    "She gives Maggie a peck on the cheek. Maggie reciporicates with another. The two hug tightly before making a break, shuffling past one another to load Mourgan's life into the small gray hatchback."

    mag "Lets get out of here."

    play sound "doorclose.wav"

    "Maggie slams the doors shut, jacks the phone into the holster, and with the push of a button they set the engine alight."

    "Maggie places her hand over the shifter, ready to set the car to Drive. Mourgan places her hand on top of Maggie's. Fingers interlocking atop the mechanism that binds them."

    magthink "You hear that, motherfuckers? She's all mine now."

    hide trunk
    with dissolve
    hide door
    with dissolve

    show car:
        pos(50, 125)
    with dissolve

    #MAGGIE AND MOURGAN DRIVING, REMINISCING.

    play music "driving.ogg"

    mour "yknow, its still unbelievable to me that we're here now. finally in the same car."

    mag "Yeah. Im glad I logged in that day. You are as pretty as your character, too."

    mour "eeeeeeee. yayayay I've heard you say it before, hehe."

    mour "go on, go on."

    mag "All I'm saying is its hard to beat a night elf in looks and you are an all star hottie."

    mour "vvvvvuh"

    "Mourgan lets out a puff of air, looks at her lap, and gazes out the window."

    mag "Someone can't handle a compliment. Come onnn."

    play sound "thud.ogg"

    "Mourgan winces and jabs Maggie in the side with her elbow"

    mag "Hey!"

    mag "..."

    show wow1: 
        pos (820,300)

    mag "Really though, what are the odds of striking up a conversation with someone advertising a goth party in main chat like that though?"

    mag "They were hazing you, girl!"

    mag "What did they say? \"Feel the sweat drip down your spine as demons take over The Cheryl Club. Drink, chat and dance the night away with the hottest vampie goth baddies in Stormrage?\" Lmao."

    mour "listennnn, It was my turn. i don't normally do things like that."

    mour " i don't normally talk to people in MMOs like i did with you."

    mag "Sluttt."

    mour "you wanna talk about sluts, look to the people playing final fantasy."

    mag "Lol, yeah its a den of e-whores and casuals. Gimmie the number crunching and glorious gratification of a grind over being handed treats."

    mour "you would say that."

    mour "what a miracle it is i got you looking up from your spreadsheets at all."

    mag "Motherfucker. Whatever, yeah the Hearts of Iron Player likes numbers and schematics. Go fuck yourself."

    "Mourgan smirks and eeks out a whisper."

    mour "am i gonna have to write a callout post?"

    "Maggie scowls, Mourgan leans back and winces"

    mour "shit!"

    mour "aaa sorry, sorry. i'm not very good with first impressions. Sorry."

    mag "This isn't our first impression, it's been eight months, Mourgan."

    mour "right, right."

    "Mourgan twiddles with a pastel plush keychain between her soft fingers."

    mour "you know i love you."

    "Maggie softens, arms releasing tension-linkage between the wheel and her shoulders."

    mag "You're right, I do. I love you too, Mourgan."

    mag "You're lucky I was already mid jerk-off when I was courting you."

    "Mourgan stifles a laugh, covering her face for a moment before regaining her composure."

    mour "you're even luckier I'm so good at ERP. a lifetime reading fanfiction will do that to you."

    mour "an alignment of stars brought us together. maybe that's how it always is when two people meet amongst net-circumstances. It always feels special."

    mag "Yeah the world and its conditions is making me feel real special right now. Feels real nice having everyone else suffer like me for once."

    mag ""

    "Mourgan swallows a pill nonexistent."

    hide wow1
    with dissolve

    "Maggie looks away from the road for a second and shoots a confident glance to Mourgan."

    mag "Hey at least this shit got us the money to get you out of your parents place."

    mour "you ruined my perfect towwwwn!"

    mag "Who cares about the stupid cat island, there's no fucking shot that shitass villager was actually worth $700"

    show raymond1:
        pos(500,100)

    mag "You seize the moment and capitalize on it. I'm worth more than a bunch of pixels right?"

    mour "mmm"

    mag "Listen, we can buy the character card and get whatshisface back. That'll be easy"

    mour "it's not about that. The whole balance is off. Guh. I'm hitting Hazel as much as I can."

    mour "ankha, bob, monique, tom, cranky, mitzi, kid cat, purrl, lolly and HAZEL??? lkdfjgevc"

    mour "kys kys kys"

    mag "Jesus Christ you're serious about this shit."

    mour "yeah im a gremlin, you're bringing a twisted gender gremlin into your home."

    mag "Looking forward to it"

    "Maggie rolls her eyes"

    # DINER SCENE


    # FLASHBACKS


    # DINER SCENE 2


    #SECOND ROAD CONVERSATION


    #ARGUEMENT


    #FLASHBACK


    #THIRD ROAD CONVERSATION


    #GAS STATION SCENE


    #PRELUDE TO ROAD HEAD


    #ROAD HEAD


    #AFTERMATH OF ROAD HEAD


    #FINAL ARGUEMENT


    #MAGGIE CRASHES THE CAR
    label crash:
        mag "STOP FUCKING HITTING ME."
    mour  "I HATE YOU I HATE YOU I HATE YOU I HATE YOU."
    mag "SHIT!"
    mour "I HATE- {cps=1} {/cps}{nw}"
        play sound "squeal.ogg"
    "For a moment it was bathed in light. {w=2.0}"
    "Animal bone colliding with aluminum and glass, the heaven-sent ungulate craters into the engine bay."
    "The horns breach the windshield, muscles streak the hood. Parts of the animal ski flightedly past the vehicle on all sides."
    "............"
    "................................."
    "......................................................."
    mag "Mmm."
    "A jostling. Leaf springs creak metal on metal."
    "The two are in the back of another car. Adrenalinedly maneuvering through the post-crash motions. They fell into a daze some time ago."
    trucker "............."
    mag ".............."
    mour " ............."
    trucker "Yknow it was good timing when you called me. There usually aren't any other cars for miles on this road this late. Heck, Im only here because there was another crash about two hours off my usual route."
    trucker "Bit of a pain to go out that far, but you don't get to complain about those sorts of things in this line of work y'know?"
    mag ".............."
    mour "............."
    trucker "............."
    trucker "It might not be any of my business, but yall wouldnt happen to be tra-"
    mag "Do you have to talk to us the whole way there?"
    trucker "Sorry, brother."
    "It's just after 10:00 PM."
    mag "......."

    #ENDING

    "The two are taken to a nearby auto shop, and take a lengthy uber back home. Despite the strain and coordination of moving Mourgan's stuff to a new car, the two don't speak a word to eachother."
    mag "It's the apartment right there."
    "Mourgan rouses from deep thought."
    mour "....huh?"
    mag "My place? It's on the second floor all the way down."
    mour "Oh.. right."
    play sound "dooropen.wav"
    "The two lazily breach the car, each carrying Mourgan's stuff out of the van."
    "It doesn't take much effort between the two of them."
    play sound "doorclose.wav"
    "They make their way to the shadowy apartment door. Maggie fishes for her keys for while before opening the lock."
    "Before turning the tumbler she stares at Mourgan. She's staring at the ground."
    "Mourgan grits her teeth. She winces. Each step up Maggie's stairs pushing inward on her lungs, her brain, her muscles. Her computer counterbalances heavy on her spine."
    "The two open the shabby white door into Maggie's apartment."
    "The home is sparsely decorated. A dim plastic floor lamp reveals yellowed mounting tape, dusty floors, and crackling paint."
    mag "I guess you can just put your stuff wherever for now. The bedroom is on the left."
    mour "Maggie?"
    mag "Yeah?"
    mour "Im gonna sleep on the couch tonight if thats alright."
    mag "Oh... okay."
    mag "...."
    "Maggie grimaces. She looks up at Mourgans face. Seeking remnant affection."
    "Maggie grimaces again. Now turning away. She stares at the plastic laminate flooring."
    mag "Im sorry..."
    "Mourgan stares up at Maggie with a look of pure scorn."
    mag "Fine. be that way, fuck you."
    "Maggie walks into her bedroom and slams the door."
    "Mourgan sets her pillow on the couch."
    "And stands above the long gray loveseat."
    "........"
    "She makes her way out of the house and slams the door shut behind her. Into the hilly dilapidated streets."

    hide road
    with dissolve

    return
