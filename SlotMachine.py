
import random
My_Money=0
Bank_Account=0
My_Answer =input('''Welcome to the Digital Slot Machine! Are you ready to take a risk? Will you strike it rich 💰🤑? Or, will you leave broke😥? Type "Yes" to play.\n''')
while (My_Answer=="Yes") or (My_Answer=="Transfer") or (My_Answer=="Bank") or (My_Answer=="Reset") or (My_Answer=="Withdraw"):
    if (My_Answer=="Yes"):
        num=random.randint(1,4)
        if num==1:
            My_Money= My_Money+50
            print("Oh-Yeah😁! You win $50💵!")
            print('You have $%s.' % My_Money)

        elif num==2:
            My_Money= My_Money-50
            print("Sorry😢! You lost $50💵!")
            print('You have $%s.' % My_Money)

        elif num==3:
            My_Money= My_Money+100
            print("You won the Grand Prize🎰! You win $100💰🤑! Ka-ching!")
            print('You have $%s.' % My_Money)

        elif num==4:
            My_Money= My_Money-100
            print("You lose BIG😭! You lost $100💵! Oof, tough break😬!")
            print('You have $%s.' % My_Money)
    My_Answer =input('''Type "Yes" to play and "Done" to stop. Type "Transfer" to transfer money and "Bank" to show money you can also type "Withdraw" to withdraw your money🏦. Type "Reset" to reset.\n''')
    if (My_Answer=="Transfer"):
        if My_Money<1:
                print("You have no money to transfer.")
                My_Answer =input('''Type "Yes" to play and "Done" to stop. Type "Transfer" to transfer money and "Bank" to show money you can also type "Withdraw" to withdraw your money🏦. Type "Reset" to reset.\n''')

        if My_Money>0:
            Bank_Account=Bank_Account+My_Money
            print("Transferring $%s to your bank account..." % My_Money)
            My_Answer =input('''Type "Yes" to play and "Done" to stop. Type "Transfer" to transfer money and "Bank" to show money you can also type "Withdraw" to withdraw your money🏦. Type "Reset" to reset.\n''')
            My_Money=0

    if (My_Answer=="Bank"):
        print("You Have $%s in your bank account🏧" % Bank_Account)
        My_Answer =input('''Type "Yes" to play and "Done" to stop. Type "Transfer" to transfer money and "Bank" to show money you can also type "Withdraw" to withdraw your money🏦. Type "Reset" to reset.\n''')

    if (My_Answer=="Reset"):
        My_Money=0
        Bank_Account=0
        print("Reset complete.")
        My_Answer =input('''Type "Yes" to play and "Done" to stop. Type "Transfer" to transfer money and "Bank" to show money you can also type "Withdraw" to withdraw your money🏦. Type "Reset" to reset.\n''')
    
    if (My_Answer=="Withdraw"):
        My_Money= My_Money + Bank_Account
        Bank_Account=0
        My_Answer =input('''Type "Yes" to play and "Done" to stop. Type "Transfer" to transfer money and "Bank" to show money you can also type "Withdraw" to withdraw your money🏦. Type "Reset" to reset.\n''')
    
    if (My_Answer=="Done"):
        sum= Bank_Account + My_Money
        if (sum>0) and (sum<250):
            print("You gained $%s!😁" %sum)
            break
        if (sum>0) and (sum > -200):
            print("You lost $%s.😞" %sum)
        if (sum>249):
            print("You earned $%s! Ka-ching!🚛💰💵 🤑 📈" % sum)
        if (sum<-199):
            print("Oof. You got %s dollars, so you're dead broke.😭 💸📉"%sum)