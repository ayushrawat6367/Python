def count_occurrences(stringList, queries):
    # result = []
    # for query in queries:
    #     count = 0
    #     for string in stringList:
    #         if string == query:
    #             count += 1
    #     result.append(count)  # Append the count for the current query
    
    # return result

    count_dict = {}
    for string in stringList:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1
    
    result = []
    for query in queries:
        result.append(count_dict.get(query, 0))

    return result


# Example usage
stringList = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
output = count_occurrences(stringList, queries)
print(output)
