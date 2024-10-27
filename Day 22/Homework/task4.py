#შექმენით ვენდინგ მანქანის თამაში პითონის მეშვეობით, როგორც გაკვეთილზე გავაკეთე, უნდა გქონდეთ პროდუქტები, მომხმარებელს უნდა შეეძლოს არჩევა რიცხვის მიხედვით, შემდეგ კი უნდა დაუპრინტოს ის პროდუქტი, რომელიც ამოირჩია, პროდუქტები შეინახეთ სიაში.



print ("You have £",round("TotalCredit",2),"credit " )       
    print ("")
    print ("Choose your item:")
    print ("")       
    print ("1.Coco-Cola")
    print ("2.Walkers Cheese & Onion")
    print ("3.Lucozade")
    print ("4.Wosits")
    print ("5.Water")
    print ("")
    FinalCredit = "TotalCredit"
    round (FinalCredit, 2)

    item = int (input ("Enter the number for your item: "))
    print ("")
    while item <1 or item >5:
        print ("This item is not available.")
        item = int (input ("Enter the number for your item: "))
    if item == 1:
        FinalCredit = :"TotalCredit" - 0.59
        print ("You now have a Coca-Cola can, costing £0.59.")
        print ("You have",round(FinalCredit,2),"credit remaning.") 
    elif item == 2:
        FinalCredit = "TotalCredit" - 0.69
        print ("You now have a Walkers crisp packet, costing £0.69.")
        print ("You have", round(FinalCredit,2),"credit remaning.")  
    elif item == 3:
        FinalCredit = "TotalCredit" - 0.99 
        print ("You now have a Lucozade drink, costing £0.99.")
        print ("You have" ,round(FinalCredit,2),"credit remaning.") 
    elif item == 4:
        FinalCredit = "TotalCredit" - 0.59
        print ("You now have a Wosits crisp packet, costing £0.59.")
        print ("You have",round(FinalCredit,2),"credit remaning.")   
    elif item == 5:
        FinalCredit = "TotalCredit" - 0.79
        print ("You now have a bottle of water, costing £0.79.")
        print ("You have",round(FinalCredit,2),"credit remaning.") 
    else:
        print ("This not an option.")
        print ("")
        print ("The rest of your money, £(0), has been "
    outputted.".format(round(FinalCredit,2)))       

 vendingMachine ()