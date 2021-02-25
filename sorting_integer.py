def counting_sort(numbers):
    min_int = int(min(numbers))
    max_int = int(max(numbers))
    range_of_nums = max_int - min_int + 1

    num_count = [0 for i in range(range_of_nums)]
    return_num = [0 for i in range(len(numbers))]

    for i in range(0, len(numbers)):
        num_count[numbers[i]-min_int] += 1

    for i in range(1, len(num_count)):
        num_count[i] += num_count[i-1]

    for i in range(len(numbers)-1, -1, -1):
        return_num[num_count[numbers[i] - min_int]-1] = numbers[i]
        num_count[numbers[i] - min_int] -= 1

    for i in range(0, len(numbers)):
        numbers[i] = return_num[i]
    
    return numbers


nums = [-3, 7, 13, 224, -49, 244, 589, -94, 0, 24]
answer = counting_sort(nums)
print("sorted array:  " + str(answer))


#     """Sort given numbers (integers) by counting occurrences of each number,
#     then looping over counts and copying that many numbers into output list.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Find range of given numbers (minimum and maximum integer values)✅
#     # TODO: Create list of counts with a slot for each number in input range✅
#     # TODO: Loop over given numbers and increment each number's count✅
#     # TODO: Loop over counts and append that many numbers into output list✅
#     # FIXME: Improve this to mutate input instead of creating new output list


# def bucket_sort(numbers, num_buckets=10):
#     """Sort given numbers by distributing into buckets representing subranges,
#     then sorting each bucket and concatenating all buckets in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Find range of given numbers (minimum and maximum values)
#     # TODO: Create list of buckets to store numbers in subranges of input range
#     # TODO: Loop over given numbers and place each item in appropriate bucket
#     # TODO: Sort each bucket using any sorting algorithm (recursive or another)
#     # TODO: Loop over buckets and append each bucket's numbers into output list
#     # FIXME: Improve this to mutate input instead of creating new output list