from pyrogram.types import InlineKeyboardButton



class Data:
    # Start Message
    START = """
Hey {}
Thanks for using {}
I can help you in many things regarding to fixed games. Am smart but you can still contact the **UFM administration** for farther help.
ADMIN [ADMIN 1](t.me/talktotegs) or [ADMIN 2](t.me/talktotegs2)
**So now can I know your need ?**
Use below buttons for simplicity!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ JOIN MAIN CHANNEL ✨", url="https://t.me/ugfixedmatches")],
        [
        [
            InlineKeyboardButton("BOOK NOW", callback_data="help"),
            InlineKeyboardButton("ABOUT US", callback_data="about")
        ],
       ]
    # Help Message
    HELP = """
**PLEASE CONTACT**

[ADMIN1](t.me/talktotegs)    [ADMIN2](t.me/talktotegs2)
    """

    # About Message
    ABOUT = """
**About This Bot** 

THS IS AN OFFICIAL UFM ASSISTANT BOT

It was developed for UFM clients who inbox UFM admins when offline. It replies instantly.
Guides you through aquiring fixed matches and free matches.

SUPPOSED BY : UFM MANAGEMENT
Main channel : [Click Here](t.me/ugfixedmatches)

Group : [Click Here](t.me/UFMfreematches)

Language : [ADMIN1](t.me/talktotegs) [ADMIN2](t.me/talktotegs2)

Developer : UFM MANAGEMENT
Version : 0.1.3.1
    """
