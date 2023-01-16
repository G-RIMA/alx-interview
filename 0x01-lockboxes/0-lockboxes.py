#!/usr/bin/python3
'''lockboxes task '''

def canUnlockAll(boxes):
    '''method that detamines if all the boxes can be opened'''
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
