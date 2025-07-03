def flat_generator(list_of_lists):
    outer_index = 0
    while outer_index < len(list_of_lists):
        current_list = list_of_lists[outer_index]
        outer_index += 1
        inner_index = 0
        while inner_index < len(current_list):
            # print(outer_index, inner_index)
            item = current_list[inner_index]
            inner_index += 1
            yield item
