# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mag = Character("Maggie", image="mag", who_color="#228047")
define mour = Character("Mourgan", image="mour" , who_color="#733294")
define rot = Character("Rotwife383927", image="rot", who_color="#228047")
define kit = Character("kittysockz", image="kit", who_color="#733294")

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

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg road

    play music "Driving.ogg"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show backroad:
        pos (130,130)
    with dissolve

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

    play music "Outside.ogg"

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

    hide backroad
    with dissolve
    
    show trunk:
        pos(650, 450)
    with dissolve

    show mag talk

    mag "Shit, is that really all your stuff?"

    show mour talk

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

    "Maggie blushes, and grips Mourgan harder."

    "The two kiss."

    mag "Lets get out of here."

    "They load into the car, jack the phone into the holster, and with the push of a button they set the engine alight."

    "Maggie places her hand over the shifter, ready to set the car to Drive. Mourgan places her hand on top of Maggie's. Fingers interlocking atop the mechanism that binds them."

    mag "Let's go."

    hide trunk
    with dissolve
    hide door
    with dissolve

    show car:
        pos(50, 125)
    with dissolve

    mour "yknow, its still unbelievable to me that we're here now. finally in the same car."

    mag "Yeah. Im glad I logged in that day. You are as pretty as your character, too."

    mour "eeeeeeee. yayayay I've heard you say it before, hehe."

    mour "go on, go on."

    mag "All I'm saying is its hard to beat a night elf in looks and you are an all star hottie."

    mour "vvvvvuh"

    "Mourgan lets out a puff of air, looks at her lap, and gazes out the window."

    mag "Someone can't handle a compliment. Come onnn."

    "Mourgan winces and jabs Maggie in the side with her elbow"

    mag "Hey!"

    mag "..."

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

    "mour twiddles with a pastel plush keychain between her soft fingers."

    mour "you know i love you."

    "Maggie softens, arms lessening their linkage between the wheel and her shoulders."

    mag "You're right, I do. I love you too, Mourgan."

    mag "You're lucky I was already mid jerk-off when I was courting you."

    "Mourgan stifles a laugh, covering her face for a moment before regaining her composure."

    mour "you're even luckier I'm so good at ERP. a lifetime reading fanfiction will do that to you."

    mour "an alignment of stars brought us together. maybe that's how it always is when two people meet amongst net-circumstances. It always feels special."

    mag "Yeah the world and its conditions is making me feel real special right now. Feels real nice having everyone else suffer like me for once."

    "Mourgan swallows a pill nonexistent."

    "Maggie looks away from the road for a second and shoots a confident glance to Mourgan."

    mag "Hey at least this shit got us the money to get you out of your parents place."

    mour "you ruined my perfect towwwwn!"

    mag "Who cares about the stupid cat island, there's no fucking shot that shitass villager was actually worth $700"

    mag "You seize the moment and capitalize on it. I'm worth more than a bunch of pixels right?"

    mour "mmm"

    mag "Listen, we can buy the character card and get whatshisface back. That'll be easy"

    mour "it's not about that. The whole balance is off. Guh. I'm hitting Hazel as much as I can."

    mour "ankha, bob, monique, tom, cranky, mitzi, kid cat, purrl, lolly and HAZEL??? Lkdfjgevc"

    mour "kys kys kys"

    mag "Jesus Christ you're serious about this shit."

    mour "Yeah im a gremlin, you're bringing a twisted gender gremlin into your home."

    mag "Looking forward to it"

    "Maggie rolls her eyes"

    # This ends the game.

    return
