numbers = [1,2,3,2,4,5,3,6,7,5,1]
def find_duplicates(numbers):
    counts={}
    for number in numbers:
        counts[number]=counts.get(number,0)+1
    duplicates = [number for number, count in counts.items() if count>1]
    return duplicates

results = find_duplicates(numbers)
print(results)