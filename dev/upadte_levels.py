def update_level(current_levels, new_level):
    """
    Parameters
    ==========
    current_levels: list
        e.g., [0,0,0,0]
    new_level: int
        e.g., 1

    Return
    ======
    list: [1,0,0,0]

    Example
    =======
    update_level([0,0,0,0], 1): [1, 0, 0, 0]
    update_level([0,1,2,3], 2): [0, 2, 2, 3]
    """
    try:
        idx = current_levels.index(new_level-1)
        current_levels[idx] = new_level
    except ValueError:
        # new_level-1 is not in the current_levels
        pass
    return current_levels

## input
now = {'mortar':[1,1,1,0],'cannon':[0,0,0,0]}
working = [('mortar',2,0), ('camp',1, 0), ('mortar',2,3), ('cannon',1,0), ('camp', 1, 5)]
 
## expected output
# new_now = {'mortar':[2,1,1,0],'cannon':[1,0,0,0], 'camp': [1]}
# new_working = [('mortar',2,3), ('camp',1,5)]

if __name__ == '__main__':

    # copy the previous states
    new_now = dict(now)
    new_working = list(working)

    # update `new_now` values
    for name, level, remaining in filter(lambda x:x[2] == 0, working):

        # create value
        if name not in now:
            new_now[name] = [level]
        # update value
        else:
            new_now[name] = update_level(current_levels=now[name], new_level=level)

    # update `new_working` values
    new_working = filter(lambda x:x[2] > 0, working)

    print '\n','='*30, 'previous', '='*30
    print 'now:',now
    print 'working:',working

    print '\n','='*30, 'current', '='*30
    print 'new_now:',new_now
    print 'new_working:',new_working