def in_used_collors(used_collors: dict, color: list[int,int,int]) ->  bool:
    result = False
    for name_of_block in used_collors:
        if color == used_collors[name_of_block]:
            result = True
            break
    return result
