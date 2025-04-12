

if __name__=='__main__':
    N = int(input())
 
    customers = []
    
    for i in range(N):
        group_size, pay_amount = [int(k) for k in input().split()]
        customers.append((pay_amount, group_size, i))
    
    customers = sorted(customers, key=lambda x: -x[0])
    
    K = int(input())
    
    tables = sorted(enumerate([int(k) for k in input().split()]), key=lambda x:x[1])
    ans = 0
    taken = [0 for x in range(K)]
    
    records = []
    for pay_amount, group_size, customer_idx in customers:
    # find first empty table from small to large
        for table_index, table_size in tables:
            if taken[table_index] == 0 and group_size <= table_size:
                ans += pay_amount
    
                records.append((customer_idx+1, table_index+1))
                taken[table_index] = 1
                break
 
 
    print(len(records), ans)
    records_sorted = sorted(records)
    
    for i in range(len(records_sorted)):
        print(records_sorted[i][0],records_sorted[i][1])

   