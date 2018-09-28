a = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2]
n = len(a)
m = 3

#Function to accept reference string and frame size.
def accept():
    global a,n,m
    a = []
    n = input("\n Enter the size of reference string : ")
    for i in range(n):
        a.append(input(" Enter [%2d] : " % (i+1)))
    m = input("\n Enter page frame size : ")

#First In First Out Page Replacement Algorithm
def __fifo():
    global a,n,m
    f = -1
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)
		
    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%m
            page[f] = a[i]
            page_faults+=1
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            
    print "\n Total page faults : %d." % (page_faults)

#Least Recently Used Page Replacement Algorithm
def __lru():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                min = 999
                for k in range(m):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == a[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = a[i]
            x=(x+1)%m
            page_faults+=1
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            
    print "\n Total page faults : %d." % (page_faults)

#Least Frequently Used Page Replacement Algorithm
def __lfu():
	
	global a,n,m
	x = 0
	page_faults = 0
	page = []
	time={}
	b=list(a)
	
	for i in range(m):
		page.append(-1)

	for i in a:
		time[i]=0

	for i in range(n):
		flag = 0
		for j in range(m):
			if(page[j] == a[i]):
				flag = 1
				time[a[i]]+=1
				break
			
		if flag == 0:
			rpage = -1
			if page[x] != -1:
				
				t=[]
				for k in page:
					t.append(time[k])
				
				minis=min(t)
				
				gpage=[]
				for k in page:
					if time[k] == minis:
						gpage.append(k)		
						
				maxi = -1
				flag = 0
				
				for k in gpage:
					for n in range(0,i):
						if(k == b[n]):
							if maxi == -1:
								maxi = n
								rpage = k
							elif n < maxi:
								maxi = n 
								rpage = k	
					flag = 1
							
				if (flag == 1):
					b[maxi]=-1
					x = page.index(rpage)
						
			if rpage != -1:
				time[rpage]=0
				
			page[x] = a[i]
			x=(x+1)%m
			time[a[i]]+=1
			page_faults+=1
			print "\n%d ->" % (a[i]),
			for j in range(m):
				if page[j] != -1:
					print page[j],
				else:
					print "-",
		else:
			print "\n%d -> No Page Fault" % (a[i]),
			
	print "\n Total page faults : %d." % (page_faults)
	print "\n Frequencies of pages: ", time

#Optimal Page Replacement Algorithm
def __optimal():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    FREE = -1
    for i in range(m):
        page.append(FREE)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            # look for an empty one
            faulted = False
            new_slot = FREE
            for q in range(m):
                if page[q] == FREE:
                    faulted = True
                    new_slot = q
            
            if not faulted:
                # find next use farthest in future
                max_future = 0
                max_future_q = FREE
                for q in range(m):
                    if page[q] != FREE:
                        found = False
                        for ii in range(i, n):
                            if a[ii] == page[q]:
                                found = True
                                if ii > max_future:
                                    # print "\n\tFound what will be used last: a[%d] = %d" % (ii, a[ii]),
                                    max_future = ii
                                    max_future_q = q

                                break
                        
                        if not found:
                            # print "\n\t%d isn't used again." % (page[q]),
                            max_future_q = q
                            break

                faulted = True
                new_slot = max_future_q
            
            page_faults += 1
            page[new_slot] = a[i]
            print "\n%d ->" % (a[i]),
            for j in range(m-1,-1,-1):
                if page[j] != FREE:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            
    print "\n Total page faults : %d." % (page_faults)

#Displaying the menu and calling the functions.    
while True:
    print "\n SIMULATION OF PAGE REPLACEMENT ALGORITHM"
    print " Menu:"
    print " 0. Accept."
    print " 1. FIFO."
    print " 2. LRU."
    print " 3. LFU."
    print " 4. Optimal."
    print " 5. Exit."
    ch = input(" Select : ")

    if ch == 0:
        accept()
    if ch == 1:
        __fifo()
    if ch == 2:
        __lru()
    if ch == 3:
		__lfu()
    if ch == 4:
        __optimal()
    if ch == 5:
        break