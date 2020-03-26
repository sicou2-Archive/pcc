visit = ["iceland", "alaska", "tdf", "pbp", "colorado"]

print(visit)


#temp sorted
print(sorted(visit))
print(visit)

#temp reverserd
print(sorted(visit, reverse = True))
print(visit)

#perm reversed
visit.reverse()
print(visit)

#reversed back to original 
visit.reverse()
print(visit)

#perm sort 
visit.sort()
print(visit)

#reverse alpha
visit.sort(reverse = True)
print(visit)

