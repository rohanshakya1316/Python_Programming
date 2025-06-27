# Various set operations 

print("----------- Set Operations -----------")

# Initial sets
set1 = {1, 2, 3, 4}
set2 = {6, 3, 5, 4}

print("Set A:", set1)
print("Set b:", set2)

# Built - in functions 

print("len(s):", len(set1))         # 4
print("sorted(s) List:", sorted(set2))   # returns list [3, 4, 5, 6]
print("sum(s):", sum(set1))         # 10
print("min(s):", min(set2))         # 3
print("max(s):", max(set1))         # 4

# 1. union() = joins all items from both sets excluding duplicates 
union_set = set1.union(set2) 
print("union():", union_set)
print("Using | union:", set1 | set2)

# 2. intersection() = set of duplicates only, elements present in both sets 
intersect_set = set1.intersection(set2)
print("intersection():", intersect_set)
print("& intersection:", set1 & set2)

a = {True, False, 3, 6}
b = {0, 1, 32, 36}

bool_match_intersect = a & b        # treats True as 1 and False as 0
print("1 = True, 0 = False:", bool_match_intersect)

# 3. difference() = Returns a set containing the difference between two or more sets
diff = set1.difference(set2)
print("difference():", diff)
print("- difference:", set1 - set2)

# 4. symmetric_difference() = Returns a set with the symmetric differences of two sets
sym_diff = set1.symmetric_difference(set2)
print("symmetric_difference():",sym_diff)
print("^ symmetric_difference():", set1 ^ set2)

# In - place set operation i.e., modifying the original set

print("========= _update() Methods and Their Shorthands =========\n")

# Original sets
a = {1, 2, 3}
b = {3, 4, 5}

print("Set A:", a)
print("Set B:", b)

# union_update() or update() – In-place union
a1 = a.copy()
a1.update(b)          # same as a1 |= b
print("\nupdate() / |= : A ∪ B =", a1)

# intersection_update()
a2 = a.copy()
a2.intersection_update(b)  # same as a2 &= b
print("intersection_update() / &= : A ∩ B =", a2)

# difference_update()
a3 = a.copy()
a3.difference_update(b)    # same as a3 -= b
print("difference_update() / -= : A - B =", a3)

# symmetric_difference_update()
a4 = a.copy()
a4.symmetric_difference_update(b)  # same as a4 ^= b
print("symmetric_difference_update() / ^= : A Δ B =", a4)

# Sets Relationship tests 

print("\n========= Subset / Superset / Disjoint =========")

x = {1, 2}
y = {1, 2, 3}

print("x.issubset(y):", x.issubset(y))           # True
print("y.issuperset(x):", y.issuperset(x))       # True
print("x.isdisjoint({4, 5}):", x.isdisjoint({4, 5}))  # True
