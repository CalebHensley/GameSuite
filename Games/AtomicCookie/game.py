import tkinter as tk
import os
import math


def run_atomic_cookie():
    root = tk.Tk()
    root.title("Atomic Cookie")
    root.configure(background='#FED088')
    root.geometry("1280x720")

    # Initialize global variables
    global number, click_power, hands, hands_clicker, hands_clicker_started, hands_clicker_price, hands_clicker_multiplier
    global tools, tools_clicker, tools_clicker_started, tools_clicker_price, tools_clicker_multiplier, tools_auto_clicker
    global Peer, Peer_clicker, Peer_clicker_started, Peer_clicker_price, Peer_clicker_multiplier, Peer_auto_clicker
    global Research, Research_clicker, Research_clicker_started, Research_clicker_price, Research_clicker_multiplier, Research_auto_clicker
    global Scientist, Scientist_clicker, Scientist_clicker_started, Scientist_clicker_price, Scientist_clicker_multiplier, Scientist_auto_clicker
    global Funding, Funding_clicker, Funding_clicker_started, Funding_clicker_price, Funding_clicker_multiplier, Funding_auto_clicker
    global Collider, Collider_clicker, Collider_clicker_started, Collider_clicker_price, Collider_clicker_multiplier, Collider_auto_clicker

    number = 0
    click_power = 1

    hands = 0
    hands_clicker = 1
    hands_clicker_started = False
    hands_clicker_price = 20
    hands_clicker_multiplier = 1.5

    tools = 0
    tools_clicker = 10
    tools_clicker_started = False
    tools_clicker_price = 100
    tools_clicker_multiplier = 1.5

    Peer = 0
    Peer_clicker = 50
    Peer_clicker_started = False
    Peer_clicker_price = 1000
    Peer_clicker_multiplier = 1.5

    Research = 0
    Research_clicker = 1
    Research_clicker_started = False
    Research_clicker_price = 50
    Research_clicker_multiplier = 1.5

    Scientist = 0
    Scientist_clicker = 100
    Scientist_clicker_started = False
    Scientist_clicker_price = 500000
    Scientist_clicker_multiplier = 1.5

    Funding = 0
    Funding_clicker = 5000
    Funding_clicker_started = False
    Funding_clicker_price = 1000000
    Funding_clicker_multiplier = 1.5

    Collider = 0
    Collider_clicker = 1000
    Collider_clicker_started = False
    Collider_clicker_price = 10000000
    Collider_clicker_multiplier = 1.5


    img = tk.PhotoImage(file="Games/AtomicCookie/images/cookie.png")
    img = img.subsample(3, 3)

    def load_click_counts():
        global number
        if os.path.exists("clicks.txt"):
            with open("clicks.txt", "r") as f:
                number = int(f.read())
            ShowInfo["text"] = "You've Created " + str(number) + " Atoms!"

    def load_hands():
        global hands
        if os.path.exists("hands.txt"):
            with open("hands.txt", "r") as f:
                hands = int(f.read())
            HandsButton["text"] = f"Gain an Extra Hand    {hands_clicker_price} Atoms  (+{hands_clicker} Atoms/sec)"

    def load_tools():
        global tools
        if os.path.exists("tools.txt"):
            with open("tools.txt", "r") as f:
                tools = int(f.read())
            ToolsButton["text"] = f"Buy More Lab Tools    {tools_clicker_price} Atoms (+{tools_clicker} Atoms/sec)"
                        
    def save_click_counts():
        global number
        with open("clicks.txt", "w") as f:
            f.write(str(int(number)))

    def save_hands():
        global hands
        with open("hands.txt", "w") as f:
            f.write(str(hands))
            
    def save_Research():
        global tools
        with open("tools.txt", "w") as f:
            f.write(str(tools))
            
    def reset_clicks():
        global update_atoms_active
        update_atoms_active = False  # Stop all updates
        global number
        number = 0
        global hands
        hands = 0
        global hands_clicker
        hands_clicker = 1
        global hands_clicker_started
        hands_clicker_started = False
        global hands_clicker_price
        hands_clicker_price = 20
        global hands_clicker_multiplier
        hands_clicker_multiplier = 1.5
        global tools
        tools = 0
        global tools_clicker
        tools_clicker = 10
        global tools_clicker_started
        tools_clicker_started = False
        global tools_clicker_price
        tools_clicker_price = 100
        global tools_clicker_multiplier
        tools_clicker_multiplier = 1.5
        global Peer
        Peer = 0
        global Peer_clicker
        Peer_clicker = 50
        global Peer_clicker_started
        Peer_clicker_started = False
        global Peer_clicker_price
        Peer_clicker_price = 1000
        global Peer_clicker_multiplier
        Peer_clicker_multiplier = 1.5
        global Research
        Research = 0
        global Research_clicker
        Research_clicker = 1
        global Research_clicker_price
        Research_clicker_price = 50
        global Research_clicker_started
        Research_clicker_started = False
        global Research_clicker_multiplier
        Research_clicker_multiplier = 1.5
        global Scientist
        Scientist = 0
        global Scientist_clicker
        Scientist_clicker = 100
        global Scientist_clicker_price
        Scientist_clicker_price = 500000
        global Scientist_clicker_started
        Scientist_clicker_started = False
        global Scientist_clicker_multiplier
        Scientist_clicker_multiplier = 1.5
        global Funding
        Funding = 0
        global Funding_clicker
        Funding_clicker = 5000
        global Funding_clicker_price
        Funding_clicker_price = 1000000
        global Funding_clicker_started
        Funding_clicker_started = False
        global Funding_clicker_multiplier
        Funding_clicker_multiplier = 1.5
        global Collider
        Collider = 0
        global Collider_clicker
        Collider_clicker = 1000
        global Collider_clicker_started
        Collider_clicker_started = False
        global Collider_clicker_price
        Collider_clicker_price = 10000000
        global Collider_clicker_multiplier
        Collider_clicker_multiplier = 1.5
        
        AtomsPerSecondLabel["text"] = "Atoms per second: 0"
        
        with open("clicks.txt", "w") as file:
            file.write("0")
        ShowInfo["text"] = "Atoms reset to 0"
        
            
    def update_button_states():
        global number
        if number >= hands_clicker_price:
            HandsButton["state"] = "normal"
        else:
            HandsButton["state"] = "disabled"
        if number >= Research_clicker_price:
            ResearchButton["state"] = "normal"
        else:
            ResearchButton["state"] = "disabled"
        if number >= tools_clicker_price:
            ToolsButton["state"] = "normal"
        else:
            ToolsButton["state"] = "disabled"
        if number >= Peer_clicker_price:
            PeerButton["state"] = "normal"
        else:
            PeerButton["state"] = "disabled"
        if number >= Scientist_clicker_price:
            ScientistButton["state"] = "normal"
        else:
            ScientistButton["state"] = "disabled"
        if number >= Funding_clicker_price:
            FundingButton["state"] = "normal"
        else:
            FundingButton["state"] = "disabled"
        if number >= Collider_clicker_price:
            ColliderButton["state"] = "normal"
        else:
            ColliderButton["state"] = "disabled"
        root.after(100, update_button_states)

    def exit_to_main_menu():
            """Exit the game and return to the main menu."""
            root.quit()
            root.destroy()  # Close the tkinter window

    def ClickButton():
        global number, click_power
        number += click_power
        save_click_counts()
        ShowInfo["text"] = "You've Created " + str(int(number)) + " Atoms!"
        
    def BuyHands():
        global number, hands_clicker, hands_clicker_price, hands_clicker_started, click_power, hands
        if number >= hands_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            hands_clicker *= 2
            hands_clicker_price *= 4
            hands += 1
            click_power *= 1.5
            HandsButton["text"] = f"Gain an Extra Hand     {hands_clicker_price} Atoms  (+{hands_clicker} per click)"
            if not hands_clicker_started:
                hands_clicker_started = True

    def BuyResearch():
        global number, Research_clicker_started, Research_clicker_price, Research_clicker, Research_clicker_multiplier, Research
        if number >= Research_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            Research_clicker *= 2
            Research_clicker_price *= 4
            Research_clicker_multiplier *= 1.5
            Research += 1
            save_Research()
            ResearchButton["text"] = f"Publish a Research Paper    {Research_clicker_price} Atoms  (+{Research_clicker} Atoms/sec)"
            if not Research_clicker_started:
                Research_clicker_started = True
                Research_auto_clicker()
            if not tools_clicker_started:
                update_Atoms_per_second()
            if tools_clicker_started:
                update_Atoms_per_second2()
            if Peer_clicker_started:
                update_Atoms_per_second3()
            if Scientist_clicker_started:
                update_Atoms_per_second4()
            if Funding_clicker_started:
                update_Atoms_per_second5()
            if Collider_clicker_started:
                update_Atoms_per_second6()

            
                
    def BuyTools():
        global number, tools_clicker_started, tools_clicker_price, hands_clicker, tools_clicker_multiplier, tools_auto_clicker, tools_clicker, tools
        if number >= tools_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            tools_clicker *= 2
            tools_clicker_price *= 4
            tools_clicker_multiplier *= 1.5  # Multiply by 2
            tools += 1
            save_Research()
            ToolsButton["text"] = f"Buy More Lab Tools   {tools_clicker_price} Atoms (+{tools_clicker} Atoms/sec)"
            if not tools_clicker_started:
                tools_clicker_started = True
                tools_auto_clicker()
            if not Peer_clicker_started:
                update_Atoms_per_second2()
            if Peer_clicker_started:
                update_Atoms_per_second3()
            if Scientist_clicker_started:
                update_Atoms_per_second4()
            if Funding_clicker_started:
                update_Atoms_per_second5()
            if Collider_clicker_started:
                update_Atoms_per_second6()

            
    def BuyPeer():
        global number, Peer_clicker_started, Peer_clicker_price, Peer_clicker, Peer_clicker_multiplier, Peer
        if number >= Peer_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            Peer_clicker *= 2
            Peer_clicker_price *= 2
            Peer_clicker_multiplier *= 1.5  # Multiply by 2
            Peer += 1
            save_Research()
            PeerButton["text"] = f"Submit for Peer Review    {Peer_clicker_price} Atoms (+{Peer_clicker} Atoms/sec)"
            if not Peer_clicker_started:
                Peer_clicker_started = True
                Peer_auto_clicker()
            if not Scientist_clicker_started:
                update_Atoms_per_second3()
            if Scientist_clicker_started:
                update_Atoms_per_second4()
            if Funding_clicker_started:
                update_Atoms_per_second5()
            if Collider_clicker_started:
                update_Atoms_per_second6()

            
    def BuyScientist():
        global number, Scientist_clicker_started, Scientist_clicker_price, Scientist_clicker, Scientist_clicker_multiplier, Scientist
        if number >= Scientist_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            Scientist_clicker *= 2
            Scientist_clicker_price *= 2
            Scientist_clicker_multiplier *= 1.5  # Multiply by 2
            Scientist += 1
            save_Research()
            ScientistButton["text"] = f"Hire Another Scientist    {Scientist_clicker_price} Atoms (+{Scientist_clicker} Atoms/sec)"
            if not Scientist_clicker_started:
                Scientist_clicker_started = True
                Scientist_auto_clicker()
            if not Funding_clicker_started:
                update_Atoms_per_second4()
            if Funding_clicker_started:
                update_Atoms_per_second4()
            if Funding_clicker_started:
                update_Atoms_per_second6()
            
                
    def BuyFunding():
        global number, Funding_clicker_started, Funding_clicker_price, Funding_clicker, Funding_clicker_multiplier, Funding
        if number >= Funding_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            Funding_clicker *= 2
            Funding_clicker_price *= 2
            Funding_clicker_multiplier *= 1.5  # Multiply by 2
            Funding += 1
            save_Research()
            FundingButton["text"] = f"Receive Government Funding     {Funding_clicker_price} Atoms (+{Funding_clicker} Atoms/sec)"
            if not Funding_clicker_started:
                Funding_clicker_started = True
                Funding_auto_clicker()
            if not Collider_clicker_started:
                update_Atoms_per_second5()
            if Collider_clicker_started:
                update_Atoms_per_second6()


    def BuyCollider():
        global number, Collider_clicker_started, Collider_clicker_price, Collider_clicker, Collider_clicker_multiplier, Collider
        if number >= Collider_clicker_price:
            ShowInfo["text"] = "You Got " + str(int(number)) + " Atoms!"
            Collider_clicker *= 2
            Collider_clicker_price *= 2
            Collider_clicker_multiplier *= 1.5  # Multiply by 2
            Collider += 1
            save_Research()
            ColliderButton["text"] = f"Build A Particle Accelerator    {Collider_clicker_price} Atoms (+{Collider_clicker} Atoms/sec)"
            if not Collider_clicker_started:
                Collider_clicker_started = True
                Collider_auto_clicker()


    def Research_auto_clicker():
        global number, Research_clicker
        number += Research_clicker
        ShowInfo["text"] = "You've Got " + str(int(number)) + " Atoms!"
        root.after(100, Research_auto_clicker)
        
    def tools_auto_clicker():
        global number, tools_clicker
        number += tools_clicker
        ShowInfo["text"] = "You've Got " + str(int(number)) + " Atoms!"
        root.after(100, tools_auto_clicker)\

    def Peer_auto_clicker():
        global number, Peer_clicker
        number += Peer_clicker
        ShowInfo["text"] = "You've Got " + str(int(number)) + " Atoms!"
        root.after(100, Peer_auto_clicker)\
        
    def Scientist_auto_clicker():
        global number, Scientist_clicker
        number += Scientist_clicker
        ShowInfo["text"] = "You've Got " + str(int(number)) + " Atoms!"
        root.after(100, Scientist_auto_clicker)\
            
    def Funding_auto_clicker():
        global number, Funding_clicker
        number += Funding_clicker
        ShowInfo["text"] = "You've Got " + str(int(number)) + " Atoms!"
        root.after(100, Funding_auto_clicker)
        
    def Collider_auto_clicker():
        global number, Collider_clicker
        number += Collider_clicker
        ShowInfo["text"] = "You've Got " + str(int(number)) + " Atoms!"
        root.after(100, Collider_auto_clicker)

    global update_atoms_active
    update_atoms_active = True

    def update_Atoms_per_second():
        global hands_clicker, update_atoms_active
        if not update_atoms_active:
            return  # Stop updating if the flag is False
        Atoms_per_second = int(hands_clicker)
        AtomsPerSecondLabel["text"] = f"Atoms per second: {Atoms_per_second}"
        root.after(1000, update_Atoms_per_second)

    def update_Atoms_per_second2():
        global hands_clicker, tools_clicker, update_atoms_active
        if not update_atoms_active:
            return
        Atoms_per_second2 = int(hands_clicker + tools_clicker)
        AtomsPerSecondLabel["text"] = f"Atoms per second: {Atoms_per_second2}"
        root.after(1000, update_Atoms_per_second2)

    def update_Atoms_per_second3():
        global hands_clicker, tools_clicker, Peer_clicker, update_atoms_active
        if not update_atoms_active:
            return
        Atoms_per_second3 = int(hands_clicker + tools_clicker + Peer_clicker)
        AtomsPerSecondLabel["text"] = f"Atoms per second: {Atoms_per_second3}"
        root.after(1000, update_Atoms_per_second3)

    def update_Atoms_per_second4():
        global hands_clicker, tools_clicker, Peer_clicker, Scientist_clicker, update_atoms_active
        if not update_atoms_active:
            return
        Atoms_per_second4 = int(hands_clicker + tools_clicker + Peer_clicker + Scientist_clicker)
        AtomsPerSecondLabel["text"] = f"Atoms per second: {Atoms_per_second4}"
        root.after(1000, update_Atoms_per_second4)

    def update_Atoms_per_second5():
        global hands_clicker, tools_clicker, Peer_clicker, Scientist_clicker, Funding_clicker, update_atoms_active
        if not update_atoms_active:
            return
        Atoms_per_second5 = int(hands_clicker + tools_clicker + Peer_clicker + Scientist_clicker + Funding_clicker)
        AtomsPerSecondLabel["text"] = f"Atoms per second: {Atoms_per_second5}"
        root.after(1000, update_Atoms_per_second5)

    def update_Atoms_per_second6():
        global hands_clicker, tools_clicker, Peer_clicker, Scientist_clicker, Funding_clicker, Collider_clicker, update_atoms_active
        if not update_atoms_active:
            return
        Atoms_per_second6 = int(hands_clicker + tools_clicker + Peer_clicker + Scientist_clicker + Funding_clicker + Collider_clicker)
        AtomsPerSecondLabel["text"] = f"Atoms per second: {Atoms_per_second6}"
        root.after(1000, update_Atoms_per_second6) 


    root.after(1000, save_click_counts)
        
    ResetButton = tk.Button(root, text="Reset Atoms", background='#FED088', activebackground='#FED088', command=reset_clicks)

    ExitButton = tk.Button(root, text="Exit to Main Menu", background='#FED088', activebackground='#FED088', command=exit_to_main_menu)

    ClickingButton = tk.Button(root, image=img, background='#FED088', activebackground='#FED088', command=ClickButton)

    ShowInfo = tk.Label(root, text="Crush the Cookie Into Atoms!", background='#FED088', font=("Arial", 20), fg="purple", pady=20)

    HandsButton = tk.Button(root, text="Gain an Extra Hand    50 Atoms", background='#FED088', activebackground='#FED088', command=BuyHands)

    ResearchButton = tk.Button(root, text="Publish a Research Study   50 Atoms", background='#FED088', activebackground='#FED088', command=BuyResearch)

    ToolsButton = tk.Button(root, text="Buy More Lab Tools    500 Atoms", background='#FED088', activebackground='#FED088', command=BuyTools)

    PeerButton = tk.Button(root, text="Receive a Peer Review     1000 Atoms", background='#FED088', activebackground='#FED088', command=BuyPeer)

    ScientistButton = tk.Button(root, text="Hire A Scientist     500,000 Atoms", background='#FED088', activebackground='#FED088', command=BuyScientist)

    FundingButton = tk.Button(root, text="Get Government Funding     1,000,000 Atoms", background='#FED088', activebackground='#FED088', command=BuyFunding)

    ColliderButton = tk.Button(root, text="Build A Particle Accelerator     10,000,000 Atoms", background='#FED088', activebackground='#FED088', command=BuyCollider)

    AtomsPerSecondLabel = tk.Label(root, text="Atoms per second: 0", background='#FED088', font=("Arial", 16), fg="purple", pady=10)

    root.update_idletasks()

    ExitButton.pack()
    ResetButton.pack()
    ClickingButton.pack()
    ShowInfo.pack()
    AtomsPerSecondLabel.pack()
    HandsButton.pack()
    ResearchButton.pack()
    ToolsButton.pack()
    PeerButton.pack()
    ScientistButton.pack()
    FundingButton.pack()
    ColliderButton.pack()


    hands = 0
    hands_clicker = 1
    hands_clicker_started = False
    hands_clicker_price = 20
    hands_clicker_multiplier = 1.5
    tools = 0
    tools_clicker_started = False
    tools_clicker = 10
    tools_clicker_started = False
    tools_clicker_price = 100
    tools_clicker_multiplier = 1.5
    Peer = 0
    Peer_clicker = 50
    Peer_clicker_started = False
    Peer_clicker_price = 1000
    Peer_clicker_multiplier = 1.5
    Research = 0
    Research_clicker = 1
    Research_clicker_price = 50
    Research_clicker_started = False
    Research_clicker_multiplier = 1.5
    Scientist = 0
    Scientist_clicker = 100
    Scientist_clicker_started = False
    Scientist_clicker_price = 500000
    Scientist_clicker_multiplier = 1.5
    Funding = 0
    Funding_clicker = 5000
    Funding_clicker_started = False
    Funding_clicker_price = 1000000
    Funding_clicker_multiplier = 1.5
    Collider = 0
    Collider_clicker = 1000
    Collider_clicker_started = False
    Collider_clicker_price = 10000000
    Collider_clicker_multiplier = 1.5



    load_click_counts()
    load_hands()
    load_tools()
    update_button_states()

    root.mainloop()