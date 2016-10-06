#listy i krotki
#krotki sa statyczne - jedyna roznica

l=[1,2,'el',3.14]
print l

k=(1,2,'el',3.14)
print k

print l[1]
print k[1]

print l[1:3]
print k[:-2]

print 1 in l

l[0]=3
print l
#
# k[0]=3
# print k

l[1:3] = ['a','b']
print l
