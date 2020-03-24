A=[1/x for x in range(1,11)] # 1,2,3,4,5,6,7,8,9,10

B=[2**i for i in range(1,11)] # 1,2,3,4,5,6,7,8,9,10

C=[i for i in B if i %4==0] # Looks at uneven values in A and uses those. so, it would be 1,3,5,7,9

print(A)
print(B)
print(C)