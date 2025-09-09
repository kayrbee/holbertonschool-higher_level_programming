#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1_diff = set_1.difference(set_2)
    set_2_diff = set_2.difference(set_1)
    set_c = set_2_diff.union(set_1_diff)
    return set_c
# Alternative:

# Tests
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))