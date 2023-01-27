import pygame

def export_Mat(matriz, name):
    t = "saved_anim/" + name + ".txt"
    with open(t,"w") as f:
        for third_d in matriz:
            for second_d in third_d:
                for firt_d in second_d:
                    f.write("(" + ', '.join(map(str,firt_d)) + ")-")
                f.write("\n")
            f.write("# new Layer\n")

def import_Mat(name):
    t = "saved_anim/" + name + ".txt"
    with open(t,"r") as f:
        list = f.readlines()
        list = "".join(list[:-1]).split("# new Layer\n")
        for third_d in range(len(list)):
            list[third_d] = "".join(list[third_d][:-1]).split("\n")
            for second_d in range(len(list[third_d])):
                list[third_d][second_d] = "".join(list[third_d][second_d][:-1]).split("-")
                for first_d in range(len(list[third_d][second_d])):
                    list[third_d][second_d][first_d] = tuple(map(int,list[third_d][second_d][first_d][1:-1].split(",")))
    return list