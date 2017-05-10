def data_type(something):
    if something is not None:
        is_type = type(something)
        if is_type == str:
            length = len(something)
            return length
        elif is_type == bool:
            return something
        elif is_type == int:
            if something < 100:
                return 'less than 100'
            elif something == 100:
                return 'equal to 100'
            else:
                return 'more than 100'
        elif is_type == list:
            if (len(something) < 3):
                return None
            return something[2]
        
    return 'no value'
