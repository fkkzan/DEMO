class CCA:
    def calAvgHeight(totalheight, totalcount):
        avgHeight = totalheight / totalcount
        print("The average height are "," {:.2f}".format(round(avgHeight, 2)) , "for" , totalcount, "members")
names = []
heights = []

totalheight = float(0)
totalcount = int(0)

txtfile = open("membersheights", 'r')

for line in txtfile:
    name, height = line.split()
    names.append(name)
    heights.append(height)
    totalcount = totalcount + 1

txtfile.close()

print("The name of the members are:", names)
print("The heights of the members are:", heights)

for i in heights:
    totalheight = totalheight + float(i)

CCA.calAvgHeight(totalheight, totalcount)

name = input("Please enter your name:")
names.append(name)
print("The names of the members are:", names)
totalcount = int(0)
totalheight = float(0)


while True:
    try:
        height = (input("Please enter your height in numbers:"))
    except ValueError:
        print("Please enter your height")
        continue
    else:
        break

for i in heights:
  totalcount = totalcount + 1
  totalheight = totalheight + float(i)

heights.append(height)
print("The height of the members are:", heights)
CCA.calAvgHeight(totalheight, totalcount)
