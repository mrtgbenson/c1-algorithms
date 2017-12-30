"""Birthstone chooser program"""

print("This program will tell you which is your birthstone")

month = input("What month were you born in? :   ") #the user inputs their birht month

#The banks of statements below compares the entered alue with different ways to they could enter the month.
#If none match, it will tell them there is no match.

if month == "January" or month == "january" or month =="jan" or month == "Jan":
  stone = "garnet"
  
elif month == "February" or month == "february" or month =="feb" or month == "Feb":
  stone = "amethyst"

elif month == "March" or month == "march" or month =="mar" or month == "Mar":
  stone = "bloodstone"

elif month == "April" or month == "april" or month =="apr" or month == "Apr":
  stone = "diamond"

elif month == "May" or month == "may":
  stone = "emerald"

elif month == "June" or month == "june" or month =="jun" or month == "Jun":
  stone = "agate"

elif month == "July" or month == "july" or month =="jul" or month == "Jul":
  stone = "ruby"

elif month == "August" or month == "august" or month =="aug" or month == "Aug":
  stone = "sardonyx"
  
elif month == "September" or month == "september" or month =="sep" or month == "Sep":
  stone = "sapphire"

elif month == "October" or month == "october" or month =="oct" or month == "Oct":
  stone = "sapphire"
  
elif month == "November" or month == "november" or month =="nov" or month == "Nov":
  stone = "topaz"
  
elif month == "December" or month == "december" or month =="Dec" or month == "dec":
  stone = "turquoise"
  
print("Your birthstone is: {}".format(stone))
