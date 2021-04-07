def disk_img():
    image = [[" " * (2*n + 1)] * 3 for i in range(n)]
    for i, disk in enumerate(pegs):
        for j in range(len(disk)):
            image[-j-1][i] = " " * (n-disk[j]) + "█" * (2*disk[j]+1) + " " * (n-disk[j])
    for i in image:
        print(*i)
    
def move_disk(disk,source,destination):
    pegs[destination].append(pegs[source].pop())
    print(f"disk{disk}  {source} => {destination}")
    disk_img()

def move_tower(disk,source,destination):
    spare = 3 - source - destination
    if disk == 1:
        move_disk(disk,source,destination)
    else:
        move_tower(disk-1, source, spare)
        move_disk(disk, source, destination)
        move_tower(disk-1, spare, destination)

def hanoi(n):
    global pegs
    pegs = [[] for i in range(3)]
    pegs[0] = list(range(n-1,-1,-1))
    disk_img()
    move_tower(n,0,1)


if __name__ == "__main__":
    global n
    n = int(input("n = "))
    hanoi(n)