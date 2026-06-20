# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mag = Character("Maggie", image="mag", who_color="#228047")
define magthink = Character("Maggie", image="mag", who_color="#228047", what_color="#2D50C4")
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

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg road

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Maggie's hatchback rushes down a Too Clean suburban stroad. Tacky houses and trees unsuited for this dry, humid climate pass her by."
    "All these lawns and freshly planted oaks. Artificial life supported supping from misappropriated mana."
    "This is not kind territory. The plastic facade of white-fence ignorance stapled over seething hatred of the incompatible."
    "All Maggie needs to do is pick up Mourgan, load all her stuff in this tiny 3 door shitbox and fuck off before her parents wake up."
    "...And try not to think about all the ways she's gonna turn her girlfriend into soaking wet pleasuremush between now and the time they get home."
    "Her mind swirls with rage. Roiling against the soybean and hog infected Southern Illinois New Home Developments."
    "\"Minnow Creek - A Safe, Stable Community\"\n For you, maybe."
    "This place isn't meant for city seasoned girlfreaks like her, and it isn't for Mourgan either. She deserves so much more."
    "Well-to-do WASPS kissing their wives with eyes wide open before bed every night. Dead ends for suburbanites who never wanted anything more than nothing."
    "Maggie white knuckles the steering wheel, studded armbands tighten around her wrists."
    "Eight hours and we'll be back in Pittsburgh."
    "538. This is it."
    "Maggie picks up the phone sitting in her lap."

    show rot pfp

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

    mag "What, just like that?"

    mour "my computer, my clothes, my backpack filled with necessities, that's it."

    mag "Shit, you really do live light. Alright let's pack it in and go."

    mour "ok, love."

    "She gives Maggie a peck on the cheek. Maggie reciporicates with another. The two hold eachother before making a break, shuffling past one another to load Mourgan's life into the small gray hatchback."

    "Slam the trunk shut, both hands shifting into Drive."

    magthink "You hear that, motherfuckers? She's all mine now."

    show car:
        pos(50, 125)

    # These display lines of dialogue.

    mag "You've created a new Ren'Py game."

    mour "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
