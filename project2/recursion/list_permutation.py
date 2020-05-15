import copy

def permutation(l):
    perms = []
    if len(l) == 0:
        perms.append([])
    else:
        first = l[0]
        sub_perms = permutation(l[1:])
        for p in sub_perms:
            for i in range(len(p) + 1):
                c = copy.deepcopy(p)
                c.insert(i, first)
                perms.append(c)

    return perms

print(len(list(1)))
#print(permutation([]))
#print(permutation([0]))
print(permutation([0,1,2]))
#[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]