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

    show rot pfp

    rot "I'm here, beautiful. wya?"

    show kit pfp

    kit "sdlkjjfhweui hold on holdon holdon AaaAA"

    rot "Alright, we gotta be quick about this though."

    rot "I'll help load your stuff in, but I know how you're gonna be."

    "..."

    show mag talk
    show car:
        pos(50, 125)

    # These display lines of dialogue.

    mag "You've created a new Ren'Py game."

    show mour talk

    mour "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
