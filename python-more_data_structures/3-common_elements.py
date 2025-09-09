#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_c = set_1.copy()
    for i in set_2:
        set_c.add(i)
    return set_c
# Alternative:

# Tests
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
