def flat_generator(input_list):
    for element in input_list:
        if isinstance(element, list):
            for item in flat_generator(element):
                yield item
        else:
            yield element








