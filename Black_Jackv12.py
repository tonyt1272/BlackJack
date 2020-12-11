#  import sys
import time
import random
import os
#  from PIL import Image
from tkinter import *
#  from flask import Flask, request, redirect, render_template, session, flash #Imports for Flask server
#  from datetime import datetime


class MainWindow:

    def __init__(self, main, money):
        """Define variables for logic flow and game play.  Also import playing card images"""
        decks_in_boot = 6  # sets number of decks in the dealer's boot 1= one deck, 4= four decks
        deck_new = decks_in_boot * list(range(52))  # creates the virtual decks of cards.  Ace=1, King=13
        random.shuffle(deck_new)  # suit order is spade,club,diamond, heart.
        print(deck_new)
        # random.shuffle(deck_new)
        # print(deck_new)
        self.deck = deck_new  # Card 1 is Ace of spades.  Card 52 is King of hearts
        #  newList = [round(x / 10) for x in deck_new]      ####Testing
        #  self.deck = newList                             ####Testing
        #  self.deck[0] = 1                                 ##Testing
        #  self.deck[1] = 2                                 ##Testing
        #  self.deck[2] = 8                                 #Testing
        #  self.deck[3] = 2                                 #Testing
        #  self.deck[4] = 0                                 #Testing
        self.dealer_total = 0  # Black Jack hand dealer score variable
        self.player_total = 0  # Black Jack hand player score variable
        self.split_player_total = 0
        self.split_hand_alive = False
        self.no_more_bets = False
        self.double_check = False
        self.split_check = False
        self.split_build = False
        self.bust = False  #
        self.let_deal = True  # Game logic booleans
        self.let_shuffle = True  #
        self.player_stay = False  #
        self.split_check = False  #
        self.split_lock_on_secondary = False
        self.split_lock_on_primary = False
        self.money = money  # Player's current cash value
        self.dealer_ace_total = 0
        self.stay_clicks = 0
        self.clicks = 1
        self.bet1 = 5  # Initializing player bet
        self.win = StringVar()  #
        self.win.set("")  #
        self.lose = StringVar()  # Initializing announcements string variables
        self.lose.set("")  #
        self.split_win = StringVar()
        self.split_win.set("")
        self.split_lose = StringVar()
        self.split_win.set("")
        self.hand_bet = StringVar()  #
        self.hand_bet.set("Bet: $5")  #
        self.pot = StringVar()  # String variable for displaying player's current pot
        self.pot.set("$"+str(money))  #
        self.toolbar = Frame(main, bg="green")  # Creating a toolbar below the menu
        self.toolbar.grid(row=0)  # applying the toolbar with the pack method
        self.dealer_label = Label(self.toolbar, text="DEALER")
        self.dealer_label.grid(row=0, column=2)
        self.player_hand = []
        self.dealer_hand = []

        # ####Dealer Frames#### #
        self.dealer_frameLL = Frame(main, bg="green", width=90, height=120)
        self.dealer_frameLL.grid(row=1, column=1)
        self.dealer_frameL = Frame(main, bg="green", width=90, height=120)
        self.dealer_frameL.grid(row=1, column=2)
        self.dealer_frameLC = Frame(main, bg="green", width=90, height=120)
        self.dealer_frameLC.grid(row=1, column=3)
        self.dealer_frameRC = Frame(main, bg="green", width=90, height=120)
        self.dealer_frameRC.grid(row=1, column=4)
        self.dealer_frameR = Frame(main, bg="green", width=90, height=120)
        self.dealer_frameR.grid(row=1, column=5)
        self.dealer_frameRR = Frame(main, bg="green", width=90, height=120)
        self.dealer_frameRR.grid(row=1, column=6)
        # ########################## #

        # #### Result Frames#### #
        self.result_frame1 = Frame(main, bg="green")
        self.result_frame1.grid(row=2, column=2)
        self.result_frame2 = Frame(main, bg="green")
        self.result_frame2.grid(row=3, column=4)
        self.result_frame3 = Frame(main, bg="green")
        self.result_frame3.grid(row=4, column=4)
        self.result_frame4 = Frame(main, bg="green")
        self.result_frame4.grid(row=5, column=0)
        # self.result_frame4 = Frame(main, bg="green")
        # self.result_frame4.grid(row=5, column=0)
        # ######################## #

        # #### Player Frames#### #
        self.player_frameLL = Frame(main, bg="green", width=90, height=115)
        self.player_frameLL.grid(row=7, column=1)
        self.player_frameL = Frame(main, bg="green", width=90, height=115)
        self.player_frameL.grid(row=7, column=2)
        self.player_frameLC = Frame(main, bg="green", width=90, height=115)
        self.player_frameLC.grid(row=7, column=3)
        self.player_frameRC = Frame(main, bg="green", width=90, height=115)
        self.player_frameRC.grid(row=7, column=4)
        self.player_frameR = Frame(main, bg="green", width=90, height=115)
        self.player_frameR.grid(row=7, column=5)
        self.player_frameRR = Frame(main, bg="green", width=90, height=115)
        self.player_frameRR.grid(row=7, column=6)
        # ####################### #

        # ####  BUTTON FRAMES #### #
        self.button_frameLL = Frame(main, bg="green")
        self.button_frameLL.grid(row=8, column=0)
        self.button_frameL = Frame(main, bg="green")
        self.button_frameL.grid(row=8, column=1)

        self.button_frameL_lower = Frame(main, bg="green")
        self.button_frameL_lower.grid(row=9, column=1)

        self.button_frameLC = Frame(main, bg="green")
        self.button_frameLC.grid(row=8, column=2)

        self.button_frameLC_lower = Frame(main, bg="green")
        self.button_frameLC_lower.grid(row=9, column=2)

        self.button_frameRC = Frame(main, bg="green")
        self.button_frameRC.grid(row=8, column=3)
        self.button_frameR = Frame(main, bg="green")
        self.button_frameR.grid(row=8, column=4)
        self.button_frameRR = Frame(main, bg="green")
        self.button_frameRR.grid(row=8, column=5)
        self.button_frameRRE = Frame(main, bg="green")
        self.button_frameRRE.grid(row=8, column=6)
        # ###################### #

        # #### Get Card Images ####
        self.owd = os.getcwd()  # save the original working directory
        os.chdir('Cards')  # change directory to where the cards are

        self.my_cards = []
        for f in os.listdir('.'):  # loading the card images for game play.  '.' gets all files in current directory
            if f.endswith('.png'):
                fn, fext = os.path.splitext(f)
                print(fn + '  ' + fext)
                self.my_cards.append(PhotoImage(file=f))
        os.chdir(self.owd)
        #########################

        # #### DEALER CARDS #####
        self.canvasdLL = Canvas(self.dealer_frameLL, width=90, height=120, bg='green')
        self.canvasdLL.pack()
        self.dealercardLL = self.canvasdLL.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvasdL = Canvas(self.dealer_frameL, width=90, height=120, bg='green')
        self.canvasdL.pack()
        self.dealercardL = self.canvasdL.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvasdLC = Canvas(self.dealer_frameLC, width=90, height=120, bg='green')
        self.canvasdLC.pack()
        self.dealercardLC = self.canvasdLC.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvasdRC = Canvas(self.dealer_frameRC, width=90, height=120, bg='green')
        self.canvasdRC.pack()
        self.dealercardRC = self.canvasdRC.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvasdR = Canvas(self.dealer_frameR, width=90, height=120, bg='green')
        self.canvasdR.pack()
        self.dealercardR = self.canvasdR.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvasdRR = Canvas(self.dealer_frameRR, width=90, height=120, bg='green')
        self.canvasdRR.pack()
        self.dealercardRR = self.canvasdRR.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        #########################

        # #### Results Labels##########

        self.label_result1 = Label(self.result_frame2, textvariable=self.lose, bg="green", fg="red")
        self.label_result1.pack()

        self.label_result2 = Label(self.result_frame3, textvariable=self.win, bg="green", fg="white")
        self.label_result2.pack()

        self.label_result3 = Label(self.result_frame4, text="PLAYER")
        self.label_result3.pack()

        ################################

        # #### PLAYER CARDS #####

        self.canvaspLL = Canvas(self.player_frameLL, width=90, height=120, bg='green')
        self.canvaspLL.pack(side=LEFT)
        self.playercardLL = self.canvaspLL.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvaspL = Canvas(self.player_frameL, width=90, height=120, bg='green')
        self.canvaspL.pack(side=LEFT)
        self.playercardL = self.canvaspL.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvaspLC = Canvas(self.player_frameLC, width=90, height=120, bg='green')
        self.canvaspLC.pack(side=LEFT)
        self.playercardLC = self.canvaspLC.create_image(0, 0, anchor=SW, image=self.my_cards[53])
        self.canvaspRC = Canvas(self.player_frameRC, width=90, height=120, bg='green')
        self.canvaspRC.pack(side=LEFT)
        self.playercardRC = self.canvaspRC.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvaspR = Canvas(self.player_frameR, width=90, height=120, bg='green')
        self.canvaspR.pack(side=LEFT)
        self.playercardR = self.canvaspR.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.canvaspRR = Canvas(self.player_frameRR, width=90, height=120, bg='green')
        self.canvaspRR.pack(side=LEFT)
        self.playercardRR = self.canvaspRR.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        #####################
        # #### Player Split Cards

        # #### Buttons #########
        self.bet_Button = Button(self.button_frameL, textvariable=self.hand_bet, bg="yellow",
                                 command=lambda: self.bet(self.hand_bet))  #lambda function uses self.bet(self.hand_bet)
        self.bet_Button.pack()                                          #to assign the result of the function to the
                                                                        #textvariable to be displayed

        # ##### Hit button #####
        self.hitbutton = Button(self.button_frameR, text="HIT", command=self.hit_func)
        self.hitbutton.pack(side=TOP)

        # ####Stay Button#####
        self.stayButton = Button(self.button_frameRR, text="STAY",
                                 command=self.stay)  # creating a button on the toolbar
        self.stayButton.pack(side=TOP, padx=4, pady=2)

        # #####Cash Display#####
        # self.cash = Label(self.button_frameLL, text="$" + str(self.pot), bg="white")
        self.cash = Label(self.button_frameLL, textvariable=self.pot, bg="white")
        self.cash.pack(side=LEFT)

        # ####New_Shuffle#####
        self.new_shuffle_Button = Button(self.button_frameRRE, text="New Shuffle", bg = "yellow",
                                         command=self.new_shuffle)  # creating a button on the toolbar
        self.new_shuffle_Button.pack(side=BOTTOM, padx=4, pady=2)

        # ####Deal#####
        self.deal_Button = Button(self.button_frameLC, text="DEAL", command=self.deal, bg="yellow")
        self.deal_Button.pack(side=BOTTOM, padx=4, pady=2)

    # ---------------------------- #
    #Define function for game play

    def new_window(self, money):
        MainWindow(root, money)

    def clear_table(self):

        if self.split_build:
            self.player_sframeLL.destroy()
            self.player_sframeL.destroy()
            self.player_sframeLC.destroy()
            self.player_sframeRC.destroy()
            self.player_sframeR.destroy()
            self.player_sframeRR.destroy()
            self.split_hitbutton.destroy()
            self.split_stayButton.destroy()
            self.split_result_label.destroy()
            self.split_build = False
            self.split_hand_alive = False

        self.split_win.set("")
        self.split_lose.set("")
        self.bust = False
        self.lose.set("")
        self.win.set("")

        if self.double_check:
            self.double_Button.destroy()
            self.double_check = False

        if self.split_check:
            self.split_Button.destroy()
            self.split_check = False

        self.canvaspLL.delete(all)
        self.playercardLL = self.canvaspLL.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvaspL.delete(all)
        self.playercardL = self.canvaspL.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvaspLC.delete(all)
        self.playercardLC = self.canvaspLC.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvaspRC.delete(all)
        self.playercardRC = self.canvaspRC.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvaspR.delete(all)
        self.playercardR = self.canvaspR.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvaspRR.delete(all)
        self.playercardRR = self.canvaspRR.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvasdLL.delete(all)
        self.dealercardLL = self.canvasdLL.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvasdL.delete(all)
        self.dealercardL = self.canvasdL.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvasdLC.delete(all)
        self.dealercardLC = self.canvasdLC.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvasdRC.delete(all)
        self.dealercardRC = self.canvasdRC.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvasdR.delete(all)
        self.dealercardR = self.canvasdR.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.canvaspRR.delete(all)
        self.dealercardRR = self.canvasdRR.create_image(0, 0, anchor=NW, image=self.my_cards[53])

    def double_down_option(self):
        self.double_Button = Button(self.button_frameL_lower,bg="yellow", text="Dub D", command=self.double_down_action)
        self.double_Button.pack()
        return

    def double_down_action(self):
        self.double_Button.destroy()
        self.double_check = False
        if self.bust is False and self.let_deal is False:
            if not self.player_stay:
                self.canvaspLC.itemconfig(self.playercardLC, image=self.my_cards[self.deck[0]])
                self.player_hand.append((self.deck[0] % 13) + 1)
                self.card_score_adjust(self.player_hand)
                print(self.player_hand, "Player hand")
                self.deck.pop(0)
                a = self.bet1
                self.bet1 = 2*a
                self.stay()
                self.bet1 = a
            else:
                return

    def split_stay(self):
        self.hitbutton["bg"] = "yellow"
        self.stayButton["bg"] = "yellow"
        self.split_lock_on_primary = False
        self.split_hitbutton.destroy()
        self.split_stayButton.destroy()
        print('split stay')
        if self.split_lock_on_secondary is False:
            self.split_lock_on_primary = False
            self.hit_card = 0
            self.split_hand_alive = True
            self.splayer_total = sum(self.splayer_hand)
            if 1 in self.splayer_hand:
                splayer_ace_total = sum(self.splayer_hand) + 10
                if (splayer_ace_total <= 21) and (splayer_ace_total > self.splayer_total):
                    self.splayer_total = splayer_ace_total
            print(self.splayer_total, " split Player total")

    def split_hit_func(self):
        if self.split_lock_on_secondary is False:
            self.hit_card += 1
            self.split_lock_on_primary = True
            if self.hit_card == 1:  # and self.split_check == False
                self.scanvaspLC.itemconfig(self.splayercardLC, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

            elif self.hit_card == 2:  # and self.split_check == False:
                self.scanvaspRC.itemconfig(self.splayercardRC, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

            elif self.hit_card == 3:  # and self.split_check == False:
                self.scanvaspR.itemconfig(self.splayercardR, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

            elif self.hit_card == 4:  # and self.split_check == False:
                self.scanvaspRR.itemconfig(self.splayercardRR, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

            elif self.hit_card == 5:  # and self.split_check == False:
                self.scanvaspRR.itemconfig(self.splayercardRR, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

            elif self.hit_card == 6:  # and self.split_check == False:
                self.scanvaspRR.itemconfig(self.splayercardRR, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

            elif self.hit_card == 7:  # and self.split_check == False:
                self.scanvaspRR.itemconfig(self.splayercardRR, image=self.my_cards[self.deck[0]])
                self.splayer_hit()

    def split_option(self):
        self.split_Button = Button(self.button_frameLC_lower, text="split", command=self.split_action, bg="yellow")
        self.split_Button.pack()
        return

    def split_action(self):
        self.split_lock_on_primary = True
        self.split_Button.destroy()
        self.split_check = True
        self.split_build = True
        self.hitbutton["bg"] = "white"
        self.stayButton["bg"] = "white"

        ##### Split Player Frames #####
        self.player_sframeLL = Frame(root, bg="green", width=90, height=115)
        self.player_sframeLL.grid(row=9, column=1)
        self.player_sframeL = Frame(root, bg="green", width=90, height=115)
        self.player_sframeL.grid(row=9, column=2)
        self.player_sframeLC = Frame(root, bg="green", width=90, height=115)
        self.player_sframeLC.grid(row=9, column=3)
        self.player_sframeRC = Frame(root, bg="green", width=90, height=115)
        self.player_sframeRC.grid(row=9, column=4)
        self.player_sframeR = Frame(root, bg="green", width=90, height=115)
        self.player_sframeR.grid(row=9, column=5)
        self.player_sframeRR = Frame(root, bg="green", width=90, height=115)
        self.player_sframeRR.grid(row=9, column=6)
        self.split_result_frame = Frame(root, bg="green")
        self.split_result_frame.grid(row=10, column=4)
        self.split_result_frameb = Frame(root, bg="green")
        self.split_result_frameb.grid(row=11, column=4)

        # #### Split_hitButton #####
        self.split_hitbutton = Button(self.button_frameR, text="HIT",fg="green",bg="yellow",highlightbackground="red", command=self.split_hit_func)
        self.split_hitbutton.pack(side=BOTTOM)

        # #### Split stay Button #####
        self.split_stayButton = Button(self.button_frameRR, text="STAY",bg="yellow",
                                       command=self.split_stay)  # creating a button on the toolbar
        self.split_stayButton.pack(side=BOTTOM, padx=4, pady=2)

        # #### Split Result Label #####
        self.split_result_label = Label(self.split_result_frame, textvariable=self.split_win, bg="green", fg="white")
        self.split_result_label.pack()

        self.split_result_labelb = Label(self.split_result_frameb, textvariable=self.split_lose, bg="green", fg="red")
        self.split_result_labelb.pack()


        # #### Player Split Cards
        self.scanvaspLL = Canvas(self.player_sframeLL, width=90, height=120, bg='green')
        self.scanvaspLL.pack(side=LEFT)
        self.splayercardLL = self.scanvaspLL.create_image(0, 0, anchor=NW, image=self.my_cards[self.card_b_face])
        self.scanvaspL = Canvas(self.player_sframeL, width=90, height=120, bg='green')
        self.scanvaspL.pack(side=LEFT)
        self.splayercardL = self.scanvaspL.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.scanvaspLC = Canvas(self.player_sframeLC, width=90, height=120, bg='green')
        self.scanvaspLC.pack(side=LEFT)
        self.splayercardLC = self.scanvaspLC.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.scanvaspRC = Canvas(self.player_sframeRC, width=90, height=120, bg='green')
        self.scanvaspRC.pack(side=LEFT)
        self.splayercardRC = self.scanvaspRC.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.scanvaspR = Canvas(self.player_sframeR, width=90, height=120, bg='green')
        self.scanvaspR.pack(side=LEFT)
        self.splayercardR = self.scanvaspR.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.scanvaspRR = Canvas(self.player_sframeRR, width=90, height=120, bg='green')
        self.scanvaspRR.pack(side=LEFT)
        self.splayercardRR = self.scanvaspRR.create_image(0, 0, anchor=NW, image=self.my_cards[53])

        self.playercardL = self.canvaspL.create_image(0, 0, anchor=NW, image=self.my_cards[53])
        self.splayer_hand = [self.card_b]
        self.card_score_adjust(self.splayer_hand)
        self.player_hand.pop(1)
        print(self.player_hand, "player hand")
        print(self.splayer_hand, "split player hand")

        root.update()
        time.sleep(.5)

        self.canvaspL.itemconfig(self.playercardL, image=self.my_cards[self.deck[0]])  # deal first split card
        self.player_hand.append((self.deck[0] % 13) + 1)
        self.card_score_adjust(self.player_hand)
        print(self.player_hand, "Player hand")
        self.deck.pop(0)

        root.update()
        time.sleep(.5)

        self.scanvaspL.itemconfig(self.splayercardL, image=self.my_cards[self.deck[0]])  # deal second split card
        self.splayer_hand.append((self.deck[0] % 13) + 1)
        self.card_score_adjust(self.splayer_hand)
        print(self.splayer_hand, "split Player hand")
        self.deck.pop(0)

    def dealer_hit(self):

        self.dealer_hand.append((self.deck[0] % 13) + 1)
        self.card_score_adjust(self.dealer_hand)
        self.dealer_total = sum(self.dealer_hand)
        self.deck.pop(0)
        print(self.dealer_hand, "Dealer hand")
        return

    def player_hit(self):
        self.player_hand.append((self.deck[0] % 13) + 1)
        self.card_score_adjust(self.player_hand)
        if sum(self.player_hand) > 21:
            self.canvasdL.itemconfig(self.dealercardL,
                                     image=self.my_cards[self.dealer_down_card])  # show dealer down card
            print(self.player_hand, "Player hand")
            self.split_lock_on_primary = False
            self.player_stay = True
            self.bust = True
            self.you_lose_player()

        else:
            print(self.player_hand, "Player hand")
            self.deck.pop(0)

    def split_player_check(self):
        if self.split_hand_alive:

            self.dealer_takes_cards()

            if (self.dealer_total > 21) and (self.splayer_total <= 21):
                self.money = self.cash_update_win(self.pot.get(), self.bet1)
                self.pot.set("$" + str(self.money))
                self.split_win.set("YOU WIN !!!")
                print(self.money, "Player cash split player check")
                self.let_deal = True
                self.no_more_bets = False
                self.cash['bg'] = "yellow"
                root.update()
                time.sleep(1)
                self.cash['bg'] = "white"

            elif (self.dealer_total > self.splayer_total) and (self.dealer_total <= 21):
                self.money = self.cash_update_lose(self.pot.get(), self.bet1)
                self.pot.set("$" + str(self.money))
                self.split_lose.set("YOU LOSE!!!")
                print(self.money, "Player cash split player check")
                self.let_deal = True
                self.no_more_bets = False
                self.cash['bg'] = "red"
                root.update()
                time.sleep(.5)
                self.cash['bg'] = "white"

            elif (self.dealer_total < self.splayer_total) and (self.splayer_total <= 21):
                self.money = self.cash_update_win(self.pot.get(), self.bet1)
                self.pot.set("$" + str(self.money))
                self.split_win.set("YOU WIN!!!")
                print(self.money, "Player cash split player check")
                self.let_deal = True
                self.no_more_bets = False
                self.cash['bg'] = "yellow"
                root.update()
                time.sleep(1)
                self.cash['bg'] = "white"

            elif self.dealer_total == self.splayer_total and self.dealer_total <= 21:
                self.split_win.set("PUSH!!!")
                print(self.money)
                self.let_deal = True
                self.no_more_bets = False

    def you_win_player(self):
        self.money = self.cash_update_win(self.pot.get(), self.bet1)
        self.pot.set("$" + str(self.money))
        self.win.set("YOU WIN!!!")
        self.let_deal = True
        self.no_more_bets = False
        print(self.money, "Player Cash")
        self.split_player_check()
        self.cash['bg'] = "yellow"
        root.update()
        time.sleep(1)
        self.cash['bg'] = "white"
        self.deal_Button['bg'] = "yellow"
        self.bet_Button['bg'] = "yellow"
        self.new_shuffle_Button['bg'] = "yellow"
        return

    def you_push_player(self):
        self.win.set("PUSH!!!")
        self.let_deal = True
        self.no_more_bets = False
        print(self.money, "Player Cash")
        self.split_player_check()
        self.deal_Button['bg'] = "yellow"
        self.bet_Button['bg'] = "yellow"
        self.new_shuffle_Button['bg'] = "yellow"

    def you_lose_player(self):
        self.money = self.cash_update_lose(self.pot.get(), self.bet1)
        self.pot.set("$" + str(self.money))
        self.lose.set("YOU LOSE!!!")
        self.let_deal = True
        self.no_more_bets = False
        print(self.money, "Player cash")
        self.split_player_check()
        self.cash['bg'] = "red"
        root.update()
        time.sleep(.5)
        self.cash['bg'] = "white"
        self.deal_Button['bg'] = "yellow"
        self.bet_Button['bg'] = "yellow"
        self.new_shuffle_Button['bg'] = "yellow"
        self.hitbutton['bg'] = "white"
        self.stayButton['bg'] = "white"
        return

    def splayer_hit(self):
        self.splayer_hand.append((self.deck[0] % 13) + 1)
        self.card_score_adjust(self.splayer_hand)
        if sum(self.splayer_hand) > 21:
            self.hitbutton["bg"] = "yellow"
            self.stayButton["bg"] = "yellow"
            self.split_lock_on_primary = False
            self.hit_card = 0
            self.split_stayButton.destroy()
            self.split_hitbutton.destroy()
            print(self.splayer_hand, "split Player hand")
            print(sum(self.splayer_hand), "split Player total")
            self.money = self.cash_update_lose(self.pot.get(), self.bet1)
            self.pot.set("$" + str(self.money))
            self.split_lose.set("YOU LOSE!!!")
            print(self.money, "split Player Cash")
            self.split_hand_alive = False
            self.cash['bg'] = "red"
            root.update()
            time.sleep(.5)
            self.cash['bg'] = "white"
        else:
            self.split_hand_alive = True
            print(self.splayer_hand, "split Player hand")
            self.deck.pop(0)

    def cash_update_lose(self, pot, bet):
        a = pot
        a_split = int(a.split("$")[1])
        b = a_split - bet
        return b

    def cash_update_win(self, pot, bet):

        a = pot
        a_split = int(a.split("$")[1])
        b = a_split + bet
        return b

    def card_score_adjust(self, face):
        for i in range(len(face)):
            if face[i] > 10:
                face[i] = 10

    def new_shuffle(self):
        if self.let_deal == True or len(self.deck) < 16:
            self.clear_table()
            money = self.money
            self.new_window(money)
            print("New Shuffle")

    def deal(self):

        if len(self.deck) < 16:
            self.let_deal = False
            self.deal_Button["bg"] = "white"
            self.win.set("Empty Boot\nNew Shuffle")
        else:
            self.split_hand_alive = False
            self.no_more_bets = True
            self.bet_Button["bg"] = "white"
            self.new_shuffle_Button["bg"] = "white"
            self.deal_Button["bg"] = "white"
            self.hitbutton["bg"] = "yellow"
            self.stayButton["bg"] = "yellow"

        if self.let_deal:
            self.stay_clicks = 0
            print(self.money, "Player cash")
            self.let_deal = False
            self.player_stay = False
            # self.let_shuffle = False
            self.hit_card = 0
            self.clear_table()
            self.player_hand = []
            self.dealer_hand = []

            self.canvaspLL.itemconfig(self.playercardLL, image=self.my_cards[self.deck[0]])
            self.player_hand.append((self.deck[0] % 13) + 1)
            card_a = (self.deck[0] % 13) + 1        # saving card for split check
            self.card_score_adjust(self.player_hand)

            self.deck.pop(0)

            self.canvasdLL.itemconfig(self.dealercardLL, image=self.my_cards[self.deck[0]])
            self.dealer_hand.append((self.deck[0] % 13) + 1)
            self.card_score_adjust(self.dealer_hand)

            self.deck.pop(0)

            self.canvaspL.itemconfig(self.playercardL, image=self.my_cards[self.deck[0]])
            self.player_hand.append((self.deck[0] % 13) + 1)
            self.card_b = (self.deck[0] % 13) + 1    # saving card for split check
            self.card_b_face = self.deck[0]  # saving for face of split card

            self.card_score_adjust(self.player_hand)
            print(self.player_hand, "Player hand")
            self.deck.pop(0)

            self.canvasdL.itemconfig(self.dealercardL, image=self.my_cards[52])  # displaying back of card for dealer
            self.dealer_down_card = self.deck[0]  # recording dealer's down card
            self.dealer_hand.append((self.deck[0] % 13) + 1)
            self.card_score_adjust(self.dealer_hand)
            self.deck.pop(0)

            if sum(self.player_hand) == 11 and 1 not in self.player_hand:
                self.double_check = True
                self.double_down_option()

            if card_a == self.card_b:
                self.split_check = True
                self.split_option()

    def dealer_ace_check(self):

        pass

    def dealer_takes_cards(self):

        root.update()
        time.sleep(.5)
        self.canvasdL.itemconfig(self.dealercardL,
                                 image=self.my_cards[self.dealer_down_card])  # show dealer down card
        self.dealer_total = sum(self.dealer_hand)
        dealer_ace_total = 0
        print(self.dealer_hand, "Dealer hand")

        # ##### TODO: Move dealer Hit Logic 1 to 8 into a single function that takes an int numberDealerHit
        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if dealer_ace_total <= 17 and self.dealer_total < 17:  # dealer must hit a soft 17
            root.update()
            time.sleep(.5)
            self.canvasdLC.itemconfig(self.dealercardLC, image=self.my_cards[self.deck[0]])  # dealer hit 1
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdRC.itemconfig(self.dealercardRC, image=self.my_cards[self.deck[0]])  # dealer hit 2
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdR.itemconfig(self.dealercardR, image=self.my_cards[self.deck[0]])  # dealer hit 3
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdRR.itemconfig(self.dealercardRR, image=self.my_cards[self.deck[0]])  # dealer hit 4
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdRR.itemconfig(self.dealercardRR, image=self.my_cards[self.deck[0]])  # dealer hit 5
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdRR.itemconfig(self.dealercardRR, image=self.my_cards[self.deck[0]])  # dealer hit 6
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdRR.itemconfig(self.dealercardRR, image=self.my_cards[self.deck[0]])  # dealer hit 7
            self.dealer_hit()

        if 1 in self.dealer_hand:
            dealer_ace_total = self.dealer_total + 10
        if (dealer_ace_total <= 17 or dealer_ace_total > 21) and self.dealer_total < 17:
            root.update()
            time.sleep(.5)
            self.canvasdRR.itemconfig(self.dealercardRR, image=self.my_cards[self.deck[0]])  # dealer hit 8
            self.dealer_hit()

        if (dealer_ace_total <= 21) and (dealer_ace_total > self.dealer_total):
            self.dealer_total = dealer_ace_total

        print(self.dealer_total, "Dealer total")

    def stay(self):
        self.hitbutton["bg"] = "white"
        self.stayButton["bg"] = "white"
        if self.split_lock_on_primary is False and self.let_deal is False:
            self.player_stay = True
            self.stay_clicks += 1
            if self.split_check:
                self.split_Button.destroy()
            if self.double_check:
                self.double_Button.destroy()

            if self.bust and self.stay_clicks == 1:
                self.you_lose_player()

                self.canvasdL.itemconfig(self.dealercardL,
                                         image=self.my_cards[self.dealer_down_card])  # show dealer down car

            if self.stay_clicks < 2:
                if self.bust is False or self.split_hand_alive:

                    self.player_total = sum(self.player_hand)
                    if 1 in self.player_hand:
                        player_ace_total = sum(self.player_hand) + 10
                        if (player_ace_total <= 21) and player_ace_total > self.player_total:
                            self.player_total = player_ace_total
                    print(self.player_total, "Player total")

                    if (self.player_total <= 21) or self.split_hand_alive:
                        self.dealer_takes_cards()

                        # ################### END DEALER HITS ######################## #
                        if self.dealer_total > self.player_total and (self.dealer_total <= 21):
                            self.you_lose_player()

                        elif self.dealer_total < self.player_total and (self.player_total <= 21):
                            self.you_win_player()

                        elif (self.dealer_total > 21) and (self.player_total <= 21):
                            self.you_win_player()

                        elif self.dealer_total == self.player_total and (self.dealer_total <= 21):
                            self.you_push_player()

    def bet(self, x):
        """function to define the bet amount.  This has a minimum bet
        of 5 and a maximum of 25, uses the mod method to cycle through
        bet ammounts"""

        # TODO: Modify bet buttons, change to two buttons labeled +bet and -bet, same basic logic wrap around at max bet
        #  and zero.  Change logic so that self.bet1 = clicks *5, get rid of the elifs

        if self.no_more_bets is not True:
            self.clicks = self.clicks + 1
            clicks = (self.clicks % 10)
            if clicks == 1:
                x.set("Bet: $5")
                self.bet1 = 5
            elif clicks == 2:
                x.set("Bet: $10")
                self.bet1 = 10
            elif clicks == 3:
                x.set("Bet: $15")
                self.bet1 = 15
            elif clicks == 4:
                x.set("Bet: $20")
                self.bet1 = 20
            elif clicks == 5:
                x.set("Bet: $25")
                self.bet1 = 25
            elif clicks == 6:
                x.set("Bet: $30")
                self.bet1 = 30
            elif clicks == 7:
                x.set("Bet: $35")
                self.bet1 = 35
            elif clicks == 8:
                x.set("Bet: $40")
                self.bet1 = 40
            elif clicks == 9:
                x.set("Bet: $45")
                self.bet1 = 45
            elif clicks == 0:
                x.set("Bet: $50")
                self.bet1 = 50

    def hit_func(self):
        if self.split_check:
            self.split_Button.destroy()
        if self.double_check:
            self.double_Button.destroy()

        if self.split_lock_on_primary is False:
            if self.bust is False and self.let_deal is False:

                if not self.player_stay:
                    self.hit_card += 1

                    if self.hit_card == 1:  # and self.split_check == False
                        self.canvaspLC.itemconfig(self.playercardLC, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 2:  # and self.split_check == False:
                        self.canvaspRC.itemconfig(self.playercardRC, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 3:  # and self.split_check == False:
                        self.canvaspR.itemconfig(self.playercardR, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 4:  # and self.split_check == False:
                        self.canvaspRR.itemconfig(self.playercardRR, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 5:  # and self.split_check == False:
                        self.canvaspRR.itemconfig(self.playercardRR, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 6:  # and self.split_check == False:
                        self.canvaspRR.itemconfig(self.playercardRR, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 7:  # and self.split_check == False:
                        self.canvaspRR.itemconfig(self.playercardRR, image=self.my_cards[self.deck[0]])
                        self.player_hit()

                    elif self.hit_card == 8:  # and self.split_check == False:
                        self.canvaspRR.itemconfig(self.playercardRR, image=self.my_cards[self.deck[0]])
                        self.player_hit()


root = Tk()
root.title("                                                                                "
           "      Tony's Black Jack")
root.configure(background='green')
root.geometry('660x600+500+200')  # changes size of the window opened +x position and +y position on monitor
root.iconbitmap(r'forge.ico')
root.resizable(width=False, height=False)

MainWindow(root, 300)

root.mainloop()

