#!/usr/bin/python3.10
#Run on sandbox, committed for posterity
if __name__ == "__main__":
    import hidden_4 as hidden4
    names = dir(hidden4)
    for i in names:
        if i[0] != '_':
            print("{}".format(i))
