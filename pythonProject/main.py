class CF2104Q:
 def calavgheight(totalheight, totalstudents):
    avgheight = totalheight/totalstudents

names = []
heights = []
totalheight = float(0)
totalstudents = int(0)

file = open("heights.txt", 'r')
for line in file:
    name, height = line.split()
    names.append(name)
    heights.append(height)
    totalstudents = totalstudents + 1
file.close()
print("The names of the students are", names)
print("The heights of the students are", heights)
for i in heights:
    totalheight = totalheight + float(i)
    CF2104Q.calavgheight(totalheight,totalstudents)


