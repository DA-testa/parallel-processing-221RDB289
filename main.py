# python3
# Autors: Gundars Pelle 6. grupa

def parallel_processing(n, m, data):
    output = []
    # function for simulating parallel tasks,
    # creates the output pairs

    threads = [(i, 0) for i in range(n)]

    for job in range(m):
        thread = 0
        for i in range(0, n):
            if threads[i][1] < threads[thread][1]:
                thread = i
        
        index, time = threads[thread]
        output.append(threads[thread])
        threads[thread] = (index, time + data[job])


    return output

def main():
    # input from keyboard
    # input consists of two lines

    # first line - n and m
    # n - thread count 
    # m - job count
    first_line = input().split()
    n = int(first_line[0])
    m = int(first_line[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # runs the parallel processing function
    result = parallel_processing(n,m,data)
    
    # print out the results, each pair in it's own line (seperated by 2 spaces)
    for t1, t2 in result:
        print(str(t1)+' '+str(t2))


if __name__ == "__main__":
    main()
