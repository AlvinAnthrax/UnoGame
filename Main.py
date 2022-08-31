import os
import random
import pygame
import sys

pygame.init()
# Define the background colour
# using RGB color coding.
background_colour = (0, 0, 0)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1920, 1080))

# Set the caption of the screen
pygame.display.set_caption("Uno")

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

#Global Variabel
#Game FPS
FPS = 60

#Card Size
Heigth = 300
Width = 200

#inisialisasi array yang akan digunakan pada permainan
player_1 = [] #Array dari pemain
bot_1 =[] #Array dari bot
played_deck = [] #Array dari deck yang sudah di gunakan


class card :
    def __init__(self):
        self.color #untuk warna / wild
        self.value #value kartu, angka / draw / reverse dsb
        self.asset #gambar kartu

    def __init__(self, color, value, asset):
        self.color = color
        self.value =value
        self.asset = asset

    def add (self, color, value, asset):
        self.color = color
        self.value = value
        self.asset = asset

    def setColor (self,color):
        self.color= color

    def setAsset (self, asset):
        self.asset = pygame.transform.scale(pygame.image.load(os.path.join('Asset',asset)),(Width,Heigth))
        ##
    def draw (self):
        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # button_col = (127, 127, 127)  # Abu-abu
        # hover_col = (255, 0, 0)  # Merah
        # click_col = (255, 255, 255)  # putih
        # text_col = (0, 0, 0)  # hitam
        # create pygame Rect obect for the button
        cards_rect = pygame.rect(self.x, self.y, Width, Heigth)

        # check mousehover and clicked conditions
        if cards_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, (255, 255, 255), cards_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, (255, 0, 0), cards_rect)
        else:
            pygame.draw.rect(screen, (127, 127, 127), cards_rect)

        # Button shading
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height),
                         2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                         2)





# isi deck
deck = []
Sleeve = card("Deck","Deck",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Deck.png')),(Width,Heigth)))

#Red Card
deck.append(card("red",0,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_0.png')),(Width,Heigth))))
deck.append(card("red",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_1.png')),(Width,Heigth))))
deck.append(card("red",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_2.png')),(Width,Heigth))))
deck.append(card("red",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_3.png')),(Width,Heigth))))
deck.append(card("red",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_4.png')),(Width,Heigth))))
deck.append(card("red",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_5.png')),(Width,Heigth))))
deck.append(card("red",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_6.png')),(Width,Heigth))))
deck.append(card("red",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_7.png')),(Width,Heigth))))
deck.append(card("red",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_8.png')),(Width,Heigth))))
deck.append(card("red",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_9.png')),(Width,Heigth))))
deck.append(card("red",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_1.png')),(Width,Heigth))))
deck.append(card("red",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_2.png')),(Width,Heigth))))
deck.append(card("red",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_3.png')),(Width,Heigth))))
deck.append(card("red",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_4.png')),(Width,Heigth))))
deck.append(card("red",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_5.png')),(Width,Heigth))))
deck.append(card("red",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_6.png')),(Width,Heigth))))
deck.append(card("red",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_7.png')),(Width,Heigth))))
deck.append(card("red",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_8.png')),(Width,Heigth))))
deck.append(card("red",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_9.png')),(Width,Heigth))))
deck.append(card("red","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_Draw.png')),(Width,Heigth))))
deck.append(card("red","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_Draw.png')),(Width,Heigth))))
deck.append(card("red","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_Skip.png')),(Width,Heigth))))
deck.append(card("red","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_Skip.png')),(Width,Heigth))))
deck.append(card("red","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_Reverse.png')),(Width,Heigth))))
deck.append(card("red","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Red_Reverse.png')),(Width,Heigth))))

# Blue
deck.append(card("blue",0,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_0.png')),(Width,Heigth))))
deck.append(card("blue",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_1.png')),(Width,Heigth))))
deck.append(card("blue",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_2.png')),(Width,Heigth))))
deck.append(card("blue",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_3.png')),(Width,Heigth))))
deck.append(card("blue",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_4.png')),(Width,Heigth))))
deck.append(card("blue",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_5.png')),(Width,Heigth))))
deck.append(card("blue",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_6.png')),(Width,Heigth))))
deck.append(card("blue",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_7.png')),(Width,Heigth))))
deck.append(card("blue",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_8.png')),(Width,Heigth))))
deck.append(card("blue",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_9.png')),(Width,Heigth))))
deck.append(card("blue",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_1.png')),(Width,Heigth))))
deck.append(card("blue",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_2.png')),(Width,Heigth))))
deck.append(card("blue",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_3.png')),(Width,Heigth))))
deck.append(card("blue",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_4.png')),(Width,Heigth))))
deck.append(card("blue",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_5.png')),(Width,Heigth))))
deck.append(card("blue",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_6.png')),(Width,Heigth))))
deck.append(card("blue",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_7.png')),(Width,Heigth))))
deck.append(card("blue",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_8.png')),(Width,Heigth))))
deck.append(card("blue",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_9.png')),(Width,Heigth))))
deck.append(card("blue","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_Draw.png')),(Width,Heigth))))
deck.append(card("blue","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_Draw.png')),(Width,Heigth))))
deck.append(card("blue","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','BLue_Skip.png')),(Width,Heigth))))
deck.append(card("blue","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_Skip.png')),(Width,Heigth))))
deck.append(card("blue","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_Reverse.png')),(Width,Heigth))))
deck.append(card("blue","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Blue_Reverse.png')),(Width,Heigth))))


#Yellow
deck.append(card("green",0,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_0.png')),(Width,Heigth))))
deck.append(card("green",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_1.png')),(Width,Heigth))))
deck.append(card("green",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_2.png')),(Width,Heigth))))
deck.append(card("green",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_3.png')),(Width,Heigth))))
deck.append(card("green",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_4.png')),(Width,Heigth))))
deck.append(card("green",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_5.png')),(Width,Heigth))))
deck.append(card("green",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_6.png')),(Width,Heigth))))
deck.append(card("green",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_7.png')),(Width,Heigth))))
deck.append(card("green",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_8.png')),(Width,Heigth))))
deck.append(card("green",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_9.png')),(Width,Heigth))))
deck.append(card("green",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_1.png')),(Width,Heigth))))
deck.append(card("green",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_2.png')),(Width,Heigth))))
deck.append(card("green",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_3.png')),(Width,Heigth))))
deck.append(card("green",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_4.png')),(Width,Heigth))))
deck.append(card("green",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_5.png')),(Width,Heigth))))
deck.append(card("green",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_6.png')),(Width,Heigth))))
deck.append(card("green",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_7.png')),(Width,Heigth))))
deck.append(card("green",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_8.png')),(Width,Heigth))))
deck.append(card("green",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_9.png')),(Width,Heigth))))
deck.append(card("green","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_Draw.png')),(Width,Heigth))))
deck.append(card("green","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_Draw.png')),(Width,Heigth))))
deck.append(card("green","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_Skip.png')),(Width,Heigth))))
deck.append(card("green","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_Skip.png')),(Width,Heigth))))
deck.append(card("green","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_Reverse.png')),(Width,Heigth))))
deck.append(card("green","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Yellow_Reverse.png')),(Width,Heigth))))



#Green
deck.append(card("yellow",0,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_0.png')),(Width,Heigth))))
deck.append(card("yellow",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_1.png')),(Width,Heigth))))
deck.append(card("yellow",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_2.png')),(Width,Heigth))))
deck.append(card("yellow",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_3.png')),(Width,Heigth))))
deck.append(card("yellow",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_4.png')),(Width,Heigth))))
deck.append(card("yellow",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_5.png')),(Width,Heigth))))
deck.append(card("yellow",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_6.png')),(Width,Heigth))))
deck.append(card("yellow",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_7.png')),(Width,Heigth))))
deck.append(card("yellow",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_8.png')),(Width,Heigth))))
deck.append(card("yellow",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_9.png')),(Width,Heigth))))
deck.append(card("yellow",1,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_1.png')),(Width,Heigth))))
deck.append(card("yellow",2,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_2.png')),(Width,Heigth))))
deck.append(card("yellow",3,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_3.png')),(Width,Heigth))))
deck.append(card("yellow",4,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_4.png')),(Width,Heigth))))
deck.append(card("yellow",5,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_5.png')),(Width,Heigth))))
deck.append(card("yellow",6,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_6.png')),(Width,Heigth))))
deck.append(card("yellow",7,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_7.png')),(Width,Heigth))))
deck.append(card("yellow",8,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_8.png')),(Width,Heigth))))
deck.append(card("yellow",9,pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_9.png')),(Width,Heigth))))
deck.append(card("yellow","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_Draw.png')),(Width,Heigth))))
deck.append(card("yellow","Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_Draw.png')),(Width,Heigth))))
deck.append(card("yellow","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_Skip.png')),(Width,Heigth))))
deck.append(card("yellow","Skip",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_Skip.png')),(Width,Heigth))))
deck.append(card("yellow","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_Reverse.png')),(Width,Heigth))))
deck.append(card("yellow","Reverse",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Green_Reverse.png')),(Width,Heigth))))

#Wild Card
deck.append(card("wild","wild",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild.png')),(Width,Heigth))))
deck.append(card("wild","wild",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild.png')),(Width,Heigth))))
deck.append(card("wild","wild",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild.png')),(Width,Heigth))))
deck.append(card("wild","wild",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild.png')),(Width,Heigth))))
deck.append(card("wild","wild_Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Draw.png')),(Width,Heigth))))
deck.append(card("wild","wild_Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Draw.png')),(Width,Heigth))))
deck.append(card("wild","wild_Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Draw.png')),(Width,Heigth))))
deck.append(card("wild","wild_Draw",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Draw.png')),(Width,Heigth))))
deck.append(card("wild","wild_Reload",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Reload.png')),(Width,Heigth))))
deck.append(card("wild","wild_Reload",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Reload.png')),(Width,Heigth))))
deck.append(card("wild","wild_Reload",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Reload.png')),(Width,Heigth))))
deck.append(card("wild","wild_Reload",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Reload.png')),(Width,Heigth))))
deck.append(card("wild","wild_Restart",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Restart.png')),(Width,Heigth))))
deck.append(card("wild","wild_Restart",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Restart.png')),(Width,Heigth))))
deck.append(card("wild","wild_Restart",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Restart.png')),(Width,Heigth))))
deck.append(card("wild","wild_Restart",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Restart.png')),(Width,Heigth))))
deck.append(card("wild","wild_Shuffle",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Shuffle.png')),(Width,Heigth))))
deck.append(card("wild","wild_Shuffle",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Shuffle.png')),(Width,Heigth))))
deck.append(card("wild","wild_Shuffle",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Shuffle.png')),(Width,Heigth))))
deck.append(card("wild","wild_Shuffle",pygame.transform.scale(pygame.image.load(os.path.join('Asset','Wild_Shuffle.png')),(Width,Heigth))))



def main():
    #Fungsi memindahkan kartu yang terbuka ke deck
    def shuffle ():
        #loop untuk mengembalikan value wild yang sudah berubah warna menjadi wild lagi
        for i in range (len(played_deck)):
            if (played_deck[i].value == "wild" and played_deck[i].color != "wild"):
                played_deck[i].setColor("wild")
                played_deck[i].setAsset('Wild.png')
                deck.append(played_deck[i])
            elif(played_deck[i].value == "wild_Restart" and played_deck[i].color != "wild"):
                played_deck[i].setColor("wild")
                played_deck[i].setAsset('Wild_Restart.png')
                deck.append(played_deck[i])
            elif (played_deck[i].value == "wild_Shuffle" and played_deck[i].color != "wild"):
                played_deck[i].setColor("wild")
                played_deck[i].setAsset('Wild_Shuffle.png')
                deck.append(played_deck[i])
            elif (played_deck[i].value == "wild_Draw" and played_deck[i].color != "wild"):
                played_deck[i].setColor("wild")
                played_deck[i].setAsset('Wild_Draw.png')
                deck.append(played_deck[i])
            elif (played_deck[i].value == "wild_Reload" and played_deck[i].color != "wild"):
                played_deck[i].setColor("wild")
                played_deck[i].setAsset('Wild_Reload.png')
                deck.append(played_deck[i])
            else:
                played_deck.append(deck[i])
        random.shuffle(deck)
        temp = played_deck[-1]
        played_deck.clear()
        played_deck.append(temp)

    def reStart ():
        shuffle()
        for i in range (len(player_1)):
            deck.append(player_1[i])
        player_1.clear()
        for i in range (len (bot_1)):
            deck.append(bot_1[i])
        bot_1.clear()

        for i in range (7):
            player_1.append(deck.pop())
            bot_1.append(deck.pop())

    #Rule based untuk gerakan yang akan dilakukan bot, pengecekan dimulai dari warna, angka lalu value
    def move(color,turn, value):
        for i in range(len(bot_1)):
            #Untuk Pengecekan warna dan pemasukan value
            if (bot_1[i].color == color and bot_1[i].value == 0):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 1):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 2):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 3):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 4):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 5):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 6):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 7):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 8):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == 9):
                played_deck.append(bot_1.pop(i))
                turn += 1
                break
            elif (bot_1[i].color == color and bot_1[i].value == "Draw"):
                played_deck.append(bot_1.pop(i))
                player_1.append(deck.pop())
                player_1.append(deck.pop())
                turn += 2
                drawWindow()
                break
            elif (bot_1[i].color == color and bot_1[i].value == "Reverse"):
                played_deck.append(bot_1.pop(i))
                turn += 2
                drawWindow()
                break
            elif (bot_1[i].color == color and bot_1[i].value == "Skip"):
                played_deck.append(bot_1.pop(i))
                turn += 2
                drawWindow()
                break

        return turn

    def drawWindow():
        screen.fill(background_colour)
        # random.shuffle(deck)
        # screen.blit(deck[0].asset,(0,0 ))

        # pygame.draw.rect(screen,(255,255,255),(150,150,Width,Heigth),1)
        x1 = 200
        y1 = 780

        # loop untuk menggambar / render kartu pemain
        for i in range(len(player_1)):
            screen.blit(player_1[i].asset, (x1, y1))
            if (len(player_1) <= 7):
                x1 += 225
            elif (len(player_1) > 7):
                x1 += 175
        x2 = 50
        y2 = 50

        # loop untuk menggambar / render kartu bot
        for i in range(len(bot_1)):
            screen.blit(bot_1[i].asset, (x2, y2))
            if (len(player_1) <= 7):
                x2 += 225
            elif (len(player_1) > 7):
                x2 += 175

        screen.blit(played_deck[-1].asset,(660, 420))  # Menggambar / render kartu terakhir yang dijadikan patokan oleh pemain
        screen.blit(Sleeve.asset, (960, 420))  # Mengambbar deck untuk draw
        # for i in range (len(deck)-1) :
        #
        #     if ( i!=0 and i % 25 == 0):
        #         x=0
        #         y+=200
        #     screen.blit(deck[i+1].asset,(x,y))
        #     x += 60

        pygame.display.update()


    #Asset untuk bagian belakang kartu

    clock = pygame.time.Clock()

    # Variable to keep our game loop running
    running = True

    #Untuk mengacak deck pertama kali
    random.shuffle(deck)

    #inisialisasi array yang akan digunakan pada permainan
    player_1 = [] #Array dari pemain
    bot_1 =[] #Array dari bot
    played_deck = [] #Array dari deck yang sudah di gunakan

    #Loop untuk memastikan played deck bukanlah kartu wild
    Wild = True

    while Wild:
        played_deck.append(deck.pop())
        if (played_deck[-1].color != "wild"):
            Wild = False


    for i in range (7):
        player_1.append(deck.pop())
        bot_1.append(deck.pop())

    turn = 1

    # game loop
    while running:
        if (turn %2 ==1):
            print()

            # if (played_deck[i].color == player_1[i].color or player_1[i].color == "wild"):
            #     if (player_1[i].value == "Skip" or player_1[i].value == "Reverse"):
            #         played_deck.append(player_1.pop(i))
            #         turn += 2
            #         break
            #     elif (player_1[i].value == "Draw"):
            #         played_deck.append(bot_1.pop(i))
            #         bot_1.append(deck.pop())
            #         bot_1.append(deck.pop())
            #         turn += 2
            #         break
            #     elif (player_1[i].value == "wild"):
            #         print("player choose :"
            #               "1.red"
            #               "2.blue"
            #               "3.yellow"
            #               "4.green")
            #         played_deck.append(bot_1.pop(i))
            #         x = input()
            #         if (x == 1):
            #             player_1[i].setColor("red")
            #         elif (x == 2):
            #             player_1[i].setColor("blue")
            #         elif (x == 3):
            #             player_1[i].setColor("yellow")
            #         elif (x == 4):
            #             player_1[i].setColor("green")
            #     elif (player_1[i].value == "wild_Draw"):
            #
            #         bot_1.append(deck.pop())
            #         bot_1.append(deck.pop())
            #         bot_1.append(deck.pop())
            #         bot_1.append(deck.pop())
            #         if (x == 1):
            #             player_1[i].setColor("red")
            #         elif (x == 2):
            #             player_1[i].setColor("blue")
            #         elif (x == 3):
            #             player_1[i].setColor("yellow")
            #         elif (x == 4):
            #             player_1[i].setColor("green")
            #         played_deck.append(player_1.pop(i))
            #         turn += 2
            #
            #         break
            #     elif (player_1[i].value == "wild_Reload"):
            #         print("player choose :"
            #               "1.red"
            #               "2.blue"
            #               "3.yellow"
            #               "4.green")
            #         played_deck.append(bot_1.pop(i))
            #         x = input()
            #         if (x == 1):
            #             player_1[i].setColor("red")
            #             player_1[i].setAsset('Wild_Reload_Red.png')
            #         elif (x == 2):
            #             player_1[i].setColor("blue")
            #             player_1[i].setAsset('Wild_Reload_Blue.png')
            #         elif (x == 3):
            #             player_1[i].setColor("yellow")
            #             player_1[i].setAsset('Wild_Reload_Yellow.png')
            #         elif (x == 4):
            #             player_1[i].setColor("green")
            #             player_1[i].setAsset('Wild_Reload_Green.png')
            #         played_deck.append(player_1.pop(i))
            #         cards = len(player_1)
            #         for i in range(len(player_1)):
            #             deck.append(player_1[i])
            #         player_1[i].clear
            #         random.shuffle(deck)
            #
            #         for i in range(cards):
            #             player_1.append(deck.pop())
            #         turn += 1
            #         break
            #     elif (player_1[i].value == "wild_Shuffle"):
            #         if (x == 1):
            #             player_1[i].setColor("red")
            #             player_1[i].setAsset('Wild_Reload_Red.png')
            #         elif (x == 2):
            #             player_1[i].setColor("blue")
            #             player_1[i].setAsset('Wild_Reload_Blue.png')
            #         elif (x == 3):
            #             player_1[i].setColor("yellow")
            #             player_1[i].setAsset('Wild_Reload_Yellow.png')
            #         elif (x == 4):
            #             player_1[i].setColor("green")
            #             player_1[i].setAsset('Wild_Reload_Green.png')
            #         played_deck.append(player_1.pop(i))
            #         cards = len(bot_1)
            #         for i in range(len(bot_1)):
            #             deck.append(bot_1[i])
            #         bot_1[i].clear
            #         random.shuffle(deck)
            #         for i in range(cards):
            #             bot_1.append(deck.pop())
            #         turn += 1
            #         break
            #     elif (player_1[i].value == "wild_Restart"):
            #         played_deck.append(player_1.pop(i))
            #         if (x == 1):
            #             player_1[i].setColor("red")
            #             player_1[i].setAsset('Wild_Restart_Red.png')
            #         elif (x == 2):
            #             player_1[i].setColor("blue")
            #             player_1[i].setAsset('Wild_Restart_Blue.png')
            #         elif (x == 3):
            #             player_1[i].setColor("yellow")
            #             player_1[i].setAsset('Wild_Restart_Yellow.png')
            #         elif (x == 4):
            #             player_1[i].setColor("green")
            #             player_1[i].setAsset('Wild_Restart_Green.png')
            #         reStart()
            #         turn += 1
            #     else:
            #         played_deck.append(player_1.pop(i))
            # elif (player_1[i].value == "Skip" or player_1 - 1[i].value == "Reverse"):
            #     played_deck.append(player_1.pop(i))
            #     turn += 2
            #     break
            # elif (player_1[i].value == "Draw"):
            #     played_deck.append(bot_1.pop(i))
            #     bot_1.append(deck.pop())
            #     bot_1.append(deck.pop())
            #     turn += 2
            #     break
            # elif (player_1[i].value <= 9):
            #     played_deck.append(player_1.pop(i))
        elif (turn % 2 == 0):

            #variabel untuk mengecek langkah yang akan digunakan saat menggunakan kartu wild
            greenCounter=0
            redCounter=0
            yellowCounter=0
            blueCounter=0
            wildCounter =0
            sameValue = False

            #Loop untuk menghitung total warna di deck bot, sekaligus mengecek keberadaannya
            for i in range (len(bot_1)):
                if (bot_1[i].color == "green"):
                    greenCounter+=1
                elif(bot_1[i].color == "red"):
                    redCounter+=1
                elif(bot_1[i].color == "blue"):
                    blueCounter+=1
                elif(bot_1[i].color == "yellow"):
                    yellowCounter+=1
                elif(bot_1[i].color == "wild"):
                    wildCounter +=1
                if (bot_1[i].value == played_deck[-1].value):
                    sameValue = True

            #Variabel pengecekan apakah kartu telah di keluarkan dari tangan bot atau tidak
            temp = turn

            # Pengecekan bila kartu played teratas adalah Merah
            if (played_deck[-1].color == "red" and redCounter >0 ):
                color = "red"
                value = played_deck[-1].value
                turn = move(color,turn,value)
                if (turn != temp) :
                    redCounter-=1

                # Pengecekan bila kartu played teratas adalah hijau
            elif (played_deck[-1].color == "green" and greenCounter> 0):
                color = "green"
                value = played_deck[-1].value
                turn = move(color, turn, value)
                if (turn != temp):
                    greenCounter -= 1

            # Pengecekan bila kartu played teratas adalah Biru
            elif (played_deck[-1].color == "blue" and blueCounter>0):
                color = "blue"
                value = played_deck[-1].value
                turn = move(color,turn,value)
                if (turn != temp):
                    blueCounter-=1

                # Pengecekan bila kartu played teratas adalah Kuning
            elif (played_deck[-1].color == "yellow" and yellowCounter>0):
                color = "yellow"
                value = played_deck[-1].value
                turn = move(color, turn, value)
                if (turn != temp):
                    yellowCounter -= 1
            # Pengecekan lanjutan bila tidak ada warna yang sama selama ada value yang sama maka akan di inputkan
            elif (sameValue == True):
                for i in  range(len(bot_1)):

                    if (bot_1[i].value == played_deck[-1].value):
                        if (bot_1[i].color == "red" ):
                            redCounter -=1
                        elif (bot_1[i].color == "green"):
                            greenCounter -=1
                        elif (bot_1[i].color == "blue"):
                            blueCounter -=1
                        elif (bot_1[i].color == "yellow"):
                            yellowCounter -=1
                        played_deck.append(bot_1.pop(i))
                        turn += 1
                        break
                    #pengecekan untuk value khusus seperti Draw / Skip / Reverse
                    elif (bot_1[i].value == played_deck[-1].value and value == "Draw"):
                        if (bot_1[i].color == "red" ):
                            redCounter -=1
                        elif (bot_1[i].color == "green"):
                            greenCounter -=1
                        elif (bot_1[i].color == "blue"):
                            blueCounter -=1
                        elif (bot_1[i].color == "yellow"):
                            yellowCounter -=1
                        played_deck.append(bot_1.pop(i))
                        player_1.append(deck.pop())
                        player_1.append(deck.pop())
                        turn += 2
                        drawWindow()
                        break
                    elif (bot_1[i].value == played_deck[-1].value and value == "Skip"):
                        if (bot_1[i].color == "red" ):
                            redCounter -=1
                        elif (bot_1[i].color == "green"):
                            greenCounter -=1
                        elif (bot_1[i].color == "blue"):
                            blueCounter -=1
                        elif (bot_1[i].color == "yellow"):
                            yellowCounter -=1
                        played_deck.append(bot_1.pop(i))
                        turn += 2
                        drawWindow()
                        break
                    elif (bot_1[i].value == played_deck[-1].value and value == "Reverse"):
                        if (bot_1[i].color == "red" ):
                            redCounter -=1
                        elif (bot_1[i].color == "green"):
                            greenCounter -=1
                        elif (bot_1[i].color == "blue"):
                            blueCounter -=1
                        elif (bot_1[i].color == "yellow"):
                            yellowCounter -=1
                        played_deck.append(bot_1.pop(i))
                        turn += 2
                        drawWindow()
                        break
            #pilihan terakhir untuk menggunakan kartu wild
            elif(wildCounter > 0 ):
                for i in range (len (bot_1)):

                    #untuk kartu wild biasa
                    if (bot_1[i].value == "wild"):
                        if (redCounter>greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                            bot_1[i].setColor("red")
                            bot_1[i].setAsset('Wild_Red.png')
                            played_deck.append(bot_1.pop(i))
                            wildCounter-=1
                            turn+=1
                            break
                        elif (greenCounter>redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                            bot_1[i].setColor("green")
                            bot_1[i].setAsset('Wild_Green.png')
                            played_deck.append(bot_1.pop(i))
                            wildCounter-=1
                            turn += 1
                            break
                        elif (blueCounter>redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                            bot_1[i].setColor("blue")
                            bot_1[i].setAsset('Wild_Blue.png')
                            played_deck.append(bot_1.pop(i))
                            wildCounter-=1
                            turn += 1
                            break
                        else:
                            bot_1[i].setColor("yellow")
                            bot_1[i].setAsset('Wild_Yellow.png')
                            played_deck.append(bot_1.pop(i))
                            wildCounter-=1
                            turn += 1
                            break

                    #shuffle untuk mengacak kartu musuh
                    elif (bot_1[i].value == "wild_Shuffle"):
                        if (redCounter>greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                            bot_1[i].setColor("red")
                            bot_1[i].setAsset('Wild_Shuffle_Red.png')
                            played_deck.append(bot_1.pop(i))

                            cards = len(player_1)
                            for i in range (len(player_1)):
                                deck.append(player_1[i])
                            player_1.clear()
                            random.shuffle(deck)

                            for i in range (cards):
                                player_1.append(deck.pop())
                            wildCounter-=1
                            turn += 1
                            break
                        elif (greenCounter>redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                            bot_1[i].setColor("green")
                            bot_1[i].setAsset('Wild_Shuffle_Green.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(player_1)
                            for i in range(len(player_1)):
                                deck.append(player_1[i])
                            player_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                player_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 1
                            break
                        elif (blueCounter>redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                            bot_1[i].setColor("blue")
                            bot_1[i].setAsset('Wild_Shuffle_Blue.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(player_1)
                            for i in range(len(player_1)):
                                deck.append(player_1[i])
                            player_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                player_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 1
                            break
                        else :
                            bot_1[i].setColor("yellow")
                            bot_1[i].setAsset('Wild_Shuffle_Yellow.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(player_1)
                            for i in range(len(player_1)):
                                deck.append(player_1[i])
                            player_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                player_1.append(deck.pop())
                            wildCounter -= 1
                            turn +=2
                            drawWindow()
                            break
                    elif (bot_1[i].value == "wild_Draw"):
                        if (redCounter>greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                            bot_1[i].setColor("red")
                            bot_1[i].setAsset('Wild_Draw_Red.png')
                            played_deck.append(bot_1.pop(i))
                            for i in range (4):
                                player_1.append(deck.pop())
                            wildCounter-=1
                            turn += 2
                            drawWindow()
                            break
                        elif (greenCounter>redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                            bot_1[i].setColor("green")
                            bot_1[i].setAsset('Wild_Draw_Green.png')
                            played_deck.append(bot_1.pop(i))
                            for i in range(4):
                                player_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 2
                            drawWindow()
                            break
                        elif (blueCounter>redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                            bot_1[i].setColor("blue")
                            bot_1[i].setAsset('Wild_Draw_Blue.png')
                            played_deck.append(bot_1.pop(i))
                            for i in range(4):
                                player_1.append(deck.pop())
                            wildCounter -= 1
                            turn+=2
                            drawWindow()
                            break
                        else:
                            bot_1[i].setColor("yellow")
                            bot_1[i].setAsset('Wild_Draw_Yellow.png')
                            played_deck.append(bot_1.pop(i))
                            for i in range(4):
                                player_1.append(deck.pop())
                            wildCounter -= 1
                            turn+=2
                            drawWindow()
                            break

                            # Reload untuk kartu di tangan sendiri
                    elif (bot_1[i].value == "wild_Reload"):
                        if (redCounter > greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                            bot_1[i].setColor("red")
                            bot_1[i].setAsset('Wild_Reload_Red.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(bot_1)
                            for i in range(len(bot_1)):
                                deck.append(bot_1[i])
                            bot_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                bot_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 1
                            break
                        elif (greenCounter>redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                            bot_1[i].setColor("green")
                            bot_1[i].setAsset('Wild_Reload_Green.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(bot_1)
                            for i in range(len(bot_1)):
                                deck.append(bot_1[i])
                            bot_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                bot_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 1
                            break
                        elif (blueCounter>redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                            bot_1[i].setColor("blue")
                            bot_1[i].setAsset('Wild_Reload_Blue.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(bot_1)
                            for i in range(len(bot_1)):
                                deck.append(bot_1[i])
                            bot_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                bot_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 1
                            break
                        else :
                            bot_1[i].setColor("yellow")
                            bot_1[i].setAsset('Wild_Reload_Yellow.png')
                            played_deck.append(bot_1.pop(i))
                            cards = len(bot_1)
                            for i in range(len(bot_1)):
                                deck.append(bot_1[i])
                            bot_1.clear()
                            random.shuffle(deck)

                            for i in range(cards):
                                bot_1.append(deck.pop())
                            wildCounter -= 1
                            turn += 1
                            break



                    elif (bot_1[i].value == "wild_Restart"):
                        if (redCounter>greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                            bot_1[i].setColor("red")
                            bot_1[i].setAsset('Wild_Restart_Red.png')
                            played_deck.append(bot_1.pop(i))
                            reStart()
                            wildCounter-=1
                            turn +=1
                            drawWindow()
                            break
                        elif (greenCounter>redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                            bot_1[i].setColor("green")
                            bot_1[i].setAsset('Wild_Restart_Green.png')
                            played_deck.append(bot_1.pop(i))
                            reStart()
                            wildCounter-=1
                            drawWindow()
                            break
                        elif (blueCounter>redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                            bot_1[i].setColor("blue")
                            bot_1[i].setAsset('Wild_Restart_Blue.png')
                            played_deck.append(bot_1.pop(i))
                            reStart()
                            wildCounter-=1
                            drawWindow()
                            break
                        else:
                            bot_1[i].setColor("yellow")
                            bot_1[i].setAsset('Wild_Restart_Yellow.png')
                            played_deck.append(bot_1.pop(i))
                            reStart()
                            wildCounter-=1
                            drawWindow()
                            break

            #apabila tidak memiliki kartu sama sekali yang dimainkan maka draw
            else :

                if (deck[-1].color == played_deck[-1].color or deck[-1].value == played_deck[-1].value):
                    played_deck.append(deck.pop())
                    turn+=1
                elif (deck[-1].color== "wild"):
                    for i in range(len(bot_1)):

                        # untuk kartu wild biasa
                        if (bot_1[i].value == "wild"):
                            if (redCounter > greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                                bot_1[i].setColor("red")
                                bot_1[i].setAsset('Wild_Red.png')
                                played_deck.append(bot_1.pop(i))
                                wildCounter -= 1
                                turn += 1
                                break
                            elif (
                                    greenCounter > redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                                bot_1[i].setColor("green")
                                bot_1[i].setAsset('Wild_Green.png')
                                played_deck.append(bot_1.pop(i))
                                wildCounter -= 1
                                turn += 1
                                break
                            elif (
                                    blueCounter > redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                                bot_1[i].setColor("blue")
                                bot_1[i].setAsset('Wild_Blue.png')
                                played_deck.append(bot_1.pop(i))
                                wildCounter -= 1
                                turn += 1
                                break
                            else:
                                bot_1[i].setColor("yellow")
                                bot_1[i].setAsset('Wild_Yellow.png')
                                played_deck.append(bot_1.pop(i))
                                wildCounter -= 1
                                turn += 1
                                break

                        # shuffle untuk mengacak kartu musuh
                        elif (bot_1[i].value == "wild_Shuffle"):
                            if (redCounter > greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                                bot_1[i].setColor("red")
                                bot_1[i].setAsset('Wild_Shuffle_Red.png')
                                played_deck.append(bot_1.pop(i))

                                cards = len(player_1)
                                for i in range(len(player_1)):
                                    deck.append(player_1[i])
                                player_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break
                            elif (
                                    greenCounter > redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                                bot_1[i].setColor("green")
                                bot_1[i].setAsset('Wild_Shuffle_Green.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(player_1)
                                for i in range(len(player_1)):
                                    deck.append(player_1[i])
                                player_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break
                            elif (
                                    blueCounter > redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                                bot_1[i].setColor("blue")
                                bot_1[i].setAsset('Wild_Shuffle_Blue.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(player_1)
                                for i in range(len(player_1)):
                                    deck.append(player_1[i])
                                player_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break
                            else:
                                bot_1[i].setColor("yellow")
                                bot_1[i].setAsset('Wild_Shuffle_Yellow.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(player_1)
                                for i in range(len(player_1)):
                                    deck.append(player_1[i])
                                player_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 2
                                drawWindow()
                                break
                        elif (bot_1[i].value == "wild_Draw"):
                            if (redCounter > greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                                bot_1[i].setColor("red")
                                bot_1[i].setAsset('Wild_Draw_Red.png')
                                played_deck.append(bot_1.pop(i))
                                for i in range(4):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 2
                                drawWindow()
                                break
                            elif (
                                    greenCounter > redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                                bot_1[i].setColor("green")
                                bot_1[i].setAsset('Wild_Draw_Green.png')
                                played_deck.append(bot_1.pop(i))
                                for i in range(4):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 2
                                drawWindow()
                                break
                            elif (
                                    blueCounter > redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                                bot_1[i].setColor("blue")
                                bot_1[i].setAsset('Wild_Draw_Blue.png')
                                played_deck.append(bot_1.pop(i))
                                for i in range(4):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 2
                                drawWindow()
                                break
                            else:
                                bot_1[i].setColor("yellow")
                                bot_1[i].setAsset('Wild_Draw_Yellow.png')
                                played_deck.append(bot_1.pop(i))
                                for i in range(4):
                                    player_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 2
                                drawWindow()
                                break

                                # Reload untuk kartu di tangan sendiri
                        elif (bot_1[i].value == "wild_Reload"):
                            if (redCounter > greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                                bot_1[i].setColor("red")
                                bot_1[i].setAsset('Wild_Reload_Red.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(bot_1)
                                for i in range(len(bot_1)):
                                    deck.append(bot_1[i])
                                bot_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    bot_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break
                            elif (
                                    greenCounter > redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                                bot_1[i].setColor("green")
                                bot_1[i].setAsset('Wild_Reload_Green.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(bot_1)
                                for i in range(len(bot_1)):
                                    deck.append(bot_1[i])
                                bot_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    bot_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break
                            elif (
                                    blueCounter > redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                                bot_1[i].setColor("blue")
                                bot_1[i].setAsset('Wild_Reload_Blue.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(bot_1)
                                for i in range(len(bot_1)):
                                    deck.append(bot_1[i])
                                bot_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    bot_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break
                            else:
                                bot_1[i].setColor("yellow")
                                bot_1[i].setAsset('Wild_Reload_Yellow.png')
                                played_deck.append(bot_1.pop(i))
                                cards = len(bot_1)
                                for i in range(len(bot_1)):
                                    deck.append(bot_1[i])
                                bot_1.clear()
                                random.shuffle(deck)

                                for i in range(cards):
                                    bot_1.append(deck.pop())
                                wildCounter -= 1
                                turn += 1
                                break



                        elif (bot_1[i].value == "wild_Restart"):
                            if (redCounter > greenCounter and redCounter > blueCounter and redCounter > yellowCounter):
                                bot_1[i].setColor("red")
                                bot_1[i].setAsset('Wild_Restart_Red.png')
                                played_deck.append(bot_1.pop(i))
                                reStart()
                                wildCounter -= 1
                                turn += 1
                                drawWindow()
                                break
                            elif (
                                    greenCounter > redCounter and greenCounter > blueCounter and greenCounter > yellowCounter):
                                bot_1[i].setColor("green")
                                bot_1[i].setAsset('Wild_Restart_Green.png')
                                played_deck.append(bot_1.pop(i))
                                reStart()
                                wildCounter -= 1
                                drawWindow()
                                break
                            elif (
                                    blueCounter > redCounter and blueCounter > greenCounter and blueCounter > yellowCounter):
                                bot_1[i].setColor("blue")
                                bot_1[i].setAsset('Wild_Restart_Blue.png')
                                played_deck.append(bot_1.pop(i))
                                reStart()
                                wildCounter -= 1
                                drawWindow()
                                break
                            else:
                                bot_1[i].setColor("yellow")
                                bot_1[i].setAsset('Wild_Restart_Yellow.png')
                                played_deck.append(bot_1.pop(i))
                                reStart()
                                wildCounter -= 1
                                drawWindow()
                                break
                else :
                    if (deck[-1].color == "red"):
                        redCounter += 1
                    elif (deck[-1].color == "green"):
                        greenCounter += 1
                    elif (deck[-1].color == "blue"):
                        blueCounter += 1
                    elif (deck[-1].color == "yellow"):
                        yellowCounter += 1
                    bot_1.append(deck.pop())


        #FPS dari game
        clock.tick(FPS)
        # loop untuk inputan (keyboard / mouse)
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                turn+=1

        if (len(deck)<10):
            shuffle()
        if (len (bot_1) == 0):
            print("Bot win")
            running = False
        elif(len(player_1)==0) :
            print("Player 1 Win")
            running = False
        #untuk menggambar / render Background
        drawWindow()





if __name__ == '__main__':
    main()



