file = open("day5.txt", "r")

seeds = ""

tline = file.readline().strip("\n")
seeds = tline.split(": ")
seeds = seeds[1].split(" ")
seeds = [int(seed) for seed in seeds]
print(seeds)
rng = range(0, len(seeds), 2)
nseeds = []
for i in range(0, len(seeds), 2):
    print(seeds[i], seeds[i + 1])

    for x in range(seeds[i], seeds[i] + seeds[i + 1]):
        nseeds.append(x)
seeds = nseeds
print(seeds)

gseed = 0
for seed in seeds:
    if seed > gseed: gseed = seed

maps = [[i] * 3 for i in seeds]
newSet = False
sets = 0

for i, line in enumerate(file.readlines()):
    if i == 0:
        continue
    if line[len(line) - 2] == ":":
        newSet = True
        continue
    if newSet:
        print("Set " + str(sets) + " DONE")
        newSet = False
        for j, v in enumerate(seeds):
            maps[j][1] = maps[j][2]
        sets += 1

    if line == "\n": continue

    idx = [int(x) for x in line.split("\n")[0].split(" ")]
    start = idx[0]
    end = idx[1]
    delta = start - end
    count = idx[2]
    Map = [maps[k][1] for k in range(len(seeds))]

    if not any(x in Map for x in range(end, end + count)):
        print("Skipped line " + str(i))
        continue

    In = [e for e in Map if end <= e < end + count]
    for j in In:
        for k in range(len(maps)):
            if maps[k][1] == j:
                maps[k][2] += delta
                break
        print("Completed " + str(j))

    # for j in range(count):
    #     if not ((end + j) in Map): continue
    #     print(j, start, end)
    #     for k, v in enumerate(maps):
    #         if maps[k][1] == end + j:
    #             maps[k][2] = start + j
    #             break
    #     print("Completed " + str(j))
    print("Line " + str(i) + " DONE")
print([[seeds[k], maps[k][2]] for k in range(len(seeds))])

smallest = 10 ** 15
for i in maps:
    if i[2] < smallest: smallest = i[2]
print(smallest)
