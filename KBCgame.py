
# ------------------------  KON BANYEGA CRORE PATI---------------"
print(""" -----KON BANYEGA CRORE PATI-----

        ENTER "A" or "a" FOR OPTION 1
        ENTER "B" or "b" FOR OPTION 2
        ENTER "C" or "c" FOR OPTION 3
        ENTER "D" or "d "FOR OPTION 4""")

print(input("press enter to play game\t"))
amounts=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
reverse_amm=amounts[::-1]



questions = ["The International Literacy Day is observed on \nA.	Sep 8\nB.	Nov 28\nC.	May 2\nD.Sep 22",
             "The language of Lakshadweep. a Union Territory of India, is \nA.Tamil\nB.Hindi\nC.Malayalam\nD. Telugu",
             "In which group of places the Kumbha Mela is held every twelve years?\nA.	Ujjain. Purl; Prayag. Haridwar\nB.	Prayag. Haridwar, Ujjain,. Nasik\nC.	Rameshwaram. Purl, Badrinath. Dwarika\nD.	Chittakoot, Ujjain, Prayag,Haridwar",
             "Bahubali festival is related to\nA.Islam\nB.Hinduism\n C. Buddhism\nD. Jainism",
             "Which day is observed as the World Standards  Day? \n A.June 26 \nB.Oct 14\n C.Nov 15\n D.Dec 2",
             "Which of the following was the theme of the World Red Cross and Red Crescent Day?\nA.	'Dignity for all - focus on women'\nB.	Dignity for all - focus on Children'\nC.	Focus on health for all \nD. Nourishment for all-focus on children",
             "September 27 is celebrated every year as\n A. Teachers' Day \nB. National Integration Day \nC. World Tourism Day\n D. International Literacy Day",
             "Who is the author of 'Manas Ka-Hans' ?\n A. Khushwant Singh\n B. Prem Chand \nC.Jayashankar Prasad\n D. Amrit Lal Nagar"

             ]
ANSWERS = ["A", "C", "B", "D", "B", "B", "C", "D"]

amount = 0
count = 0
for i in questions:
    print(f"\n\t Your balance: {amount:} RS")
    print(i)
#     github : NOOB-MUKESH
    print("----------------------------------")
    x = input("enter ur answer?\t")
    print(x)
    if ANSWERS[count].lower() == x.lower():
        print(f"Correct Answer ---------- AAP JIT CHUKE🎉🎉✨🎆 {amount:} RS")
        count += 1
        amount += reverse_amm.pop()
    else:
        exit(
            f"\n \t  AB AAP GHAR JA SAKTE HO \n \t AAP JIT CHUKE🎉🎉✨🎆 {amount:} RS")
