#start
soccer_points = 0
basketball_points = 0

#middle
answer = input ("Do you like A) Soccer, or B) basketball?")
if answer == "A":
    soccer_points += 1
elif answer == "B":
    basketball_points += 1



answer = input ("Would you rather A) Play in the NBA, or B) play in the the champions league?")
if answer == "B":
    soccer_points += 1
elif answer == "A":
    basketball_points += 1



answer = input ("Would you rather? Option A) meet Ronaldo, or B) Lebron?")
if answer == "A":
    soccer_points += 1
elif answer == "B":
    basketball_points += 1



answer = input ("Would you rather A) be outside, or B) be indoors?")
if answer == "A":
    soccer_points += 1
elif answer == "B":
    basketball_points += 1



answer = input ("Would you rather play A) Fifa25, or B) 2K25?")
if answer == "A":
    soccer_points += 1
elif answer == "B":
    basketball_points += 1


#end
if soccer_points > basketball_points:
    print("Your weird cus you like soccer")
elif basketball_points > soccer_points:
    print ("Your a pretty chill person cus you know basketball is better")
elif soccer_points == basketball_points:
    print ("You think that soccer and basketball are the same you sheep")