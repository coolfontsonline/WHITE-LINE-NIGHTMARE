# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mag = Character("Maggie", image="mag")
define mour = Character("Mourgan", image="mour")

image mag talk = "maggie-talksprite.png"
image mour talk = "mourgan-talksprite.png"

image side mag talk = "side-maggie-talksprite.png"
image side mour talk = "side-mourgan-talksprite.png"

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

    show mag talk
    show car:
        pos(50, 125)

    # These display lines of dialogue.

    mag "You've created a new Ren'Py game."

    show mour talk

    mour "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
