#!/usr/bin/python3
"""
Lock boxes
"""

def canUnlockAll(boxes):
    unlocked_boxes = [0]
    for bid, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes \
               and key != bid:
                unlocked_boxes.append(key)

    if len(unlocked_boxes) == len(boxes):
        return True
    return False
