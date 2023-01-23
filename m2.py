from collections import defaultdict
import math

points_source = defaultdict(list)
points_mea = defaultdict(list)
angles_src = defaultdict(list)
angles_mea = defaultdict(list)

f1 = open("../Milestone_Input/Milestone 2/Source.txt","r")
f0 = open("../Milestone_Input/Milestone 2/POI.txt","r")
f2 = open("m2_out.txt","w")

def slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return float('inf')
    return (y2-y1)/(x2-x1)

def angle(s1, s2): 
    return math.degrees(math.atan((s2-s1)/(1+(s2*s1))))


lines = f0.readlines()
end = 0
poly_num = 0
sze = 0

for line in lines:
    if "boundary" in line:
        end = 1
    elif end == 1:
        if "xy" in line:
            each_split = line.split("  ")
            sze = int(each_split[1])
            for i in range(0, len(each_split)):
                if i > 1:
                    temp_li = []
                    nums = each_split[i].split(" ")
                    temp_li.append(int(nums[0]))
                    temp_li.append(int(nums[1]))
                    points_mea[poly_num].append(temp_li)

        if "endel" in line:
            end = 0
            poly_num = poly_num + 1

sze = len(points_mea[0])

for i in range(0, sze):
    x1 = points_mea[0][i % sze][0]
    y1 = points_mea[0][(i % sze)][1]
    x2 = points_mea[0][((i+1) % sze)][0]
    y2 = points_mea[0][((i+1) % sze)][1]
    slope1 = slope(x1,y1,x2,y2)
    x1 = points_mea[0][((i+2) % sze)][0]
    y1 = points_mea[0][((i+2) % sze)][1]
    x2 = points_mea[0][((i+3) % sze)][0]
    y2 = points_mea[0][((i+3) % sze)][1]
    slope2 = slope(x1,y1,x2,y2)
    angles_mea[0].append(angle(slope1, slope2))

lines = f1.readlines()
end = 0
poly_num = 0

for line in lines:
    if "boundary" in line:
        end = 1
    elif end == 1:
        if "xy" in line:
            each_split = line.split("  ")
            for i in range(0, len(each_split)):
                if i > 1:
                    temp_li = []
                    nums = each_split[i].split(" ")

                    temp_li.append(int(nums[0]))
                    temp_li.append(int(nums[1]))
                    points_source[poly_num].append(temp_li)

        if "endel" in line:
            end = 0
            poly_num = poly_num + 1

count = []
angles_mea[0].sort()

for j in points_source.keys():
    if len(points_source[j]) == 7:
        for i in range(0, sze):
            x1 = points_source[j][(i % sze)][0]
            y1 = points_source[j][(i % sze)][1]
            x2 = points_source[j][((i+1) % sze)][0]
            y2 = points_source[j][((i+1) % sze)][1]
            slope1 = slope(x1,y1,x2,y2)
            x1 = points_source[j][((i+2) % sze)][0]
            y1 = points_source[j][((i+2) % sze)][1]
            x2 = points_source[j][((i+3) % sze)][0]
            y2 = points_source[j][((i+3) % sze)][1]
            slope2 = slope(x1,y1,x2,y2)
            angles_src[j].append(angle(slope1, slope2))
        angles_src[j].sort()
        if set(angles_src[j]) & set(angles_mea[0]):
            count.append(j)

end = 0
poly_num = 0
for line in lines:
    if "boundary" in line:
        if poly_num in count:
            f2.write(line)
        end = 1
    elif end == 1:
        if poly_num in count:
            f2.write(line)

        if "endel" in line:
            end = 0
            poly_num = poly_num + 1
    else:
        f2.write(line)