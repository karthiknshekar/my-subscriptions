import itertools

def weeklyExpenses(input):
# Mapping weekly cost of papers to its name in a dictionary
    expenses = {
    26:"TOI",
    20.5:"Hindu",
    34: "ET",
    10.5:"BM",
    16.4:"HT",
    };
    prices=[26,20.5,34,10.5,16.4]
    papers=[]
# storing all possible combinations to a variable
    combination=list(itertools.combinations(prices, 2))
    for i in combination:
        if sum(i)<=input: #Fitering out the combinations based on the weekly budget
            papers.append(i)
    
    np=[]
    for i in range(len(papers)):
        val1=papers[i][0]
        val2=papers[i][1]
        np.append((expenses[val1],expenses[val2])) # Getting values for keys
    print(np)


input=int(input())
weeklyExpenses(input)



