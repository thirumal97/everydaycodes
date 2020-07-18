# python3


def max_pairwise_product(n,numbers):
    #n = len(numbers)
    #max_product = 0
    numbers.sort()
    return numbers[n-1] * numbers[n-2]
    
"""    index_one = -1
    for i in range(n):
        
        if index_one == -1 or numbers[i] > numbers[index_one] :
            index_one = i
          #  print(index_one)
    index_two = -1
    for j in range(1,n):
        if (j != index_one ) and (index_two == -1 or numbers[j]>numbers[index_two]):
            index_two = j
           # print(index_two)
    return numbers[index_one]   *numbers[index_two]

    for first in range(n):
          for second in range(first + 1, n):
              max_product = max(max_product,
                   numbers[first] * numbers[second])

     return max_product

"""
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_n,input_numbers))
