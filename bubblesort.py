bubble_sort_list = [19,30,15,12,10,2,9,22,26,7]
bsl = bubble_sort_list

for i in range(0 , len(bsl)):

    for j in range(0,len(bsl)-1):

        if bsl[j+1] < bsl[j]:
            bsl[j] , bsl[j+1] = bsl[j+1] , bsl[j]

print(bsl)