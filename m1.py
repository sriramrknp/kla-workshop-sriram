from collections import defaultdict

polygon = defaultdict(list)
points = defaultdict(list)

f1 = open("../Milestone_Input/Milestone 1/Format_Source.txt","r")
f2 = open("m1_out.txt","w")
lines = f1.readlines()

end = 0
poly_num = 0

for line in lines:
    if "boundary" in line:
        end = 1
        if(poly_num < 2):
            polygon[poly_num].append(line)
            f2.write(line)
    elif end == 1:
        if(poly_num < 2):
            polygon[poly_num].append(line)
            if "xy" in line:
                each_split = line.split("  ")
                print(each_split)
                for i in range(0, len(each_split)):
                    if i > 1:
                        temp_li = []
                        nums = each_split[i].split(" ")

                        temp_li.append(int(nums[0]))
                        temp_li.append(int(nums[1]))
                        points[poly_num].append(temp_li)

            f2.write(line)
        if "endel" in line:
            end = 0
            poly_num = poly_num + 1
    else:
        f2.write(line)

print(points)