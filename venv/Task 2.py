
def grade(percent):
    x = 0
    while x == 0:
        if percent <=49:
            print("you have an F")
            x = x + 1
        if percent >= 50 and percent <= 59:
            print("you have a C-")
            x = x + 1
        if percent >= 60 and percent <=70:
            print("you have a C")
            x = x + 1
        if percent >= 71 and percent <=80:
            print("you have a B")
            x = x + 1
        if percent >= 81 and percent <= 85:
            print("you have a A-")
            x = x + 1
        if percent >= 86 and percent <= 90:
            print("you have A")
            x = x + 1
        if percent >=91 and percent <= 100:
            print("you have an A+")
            x = x + 1
        if percent >100:
            print("you cant have an average over 100% silly!")
            percent = int(input("what is your average?"))


percent = int(input("what is your average?"))
grade(percent)
