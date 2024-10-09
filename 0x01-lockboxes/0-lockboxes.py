#!/usr/bin/python3
"""Solves the lockboxes puzzle"""


def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for box in opened_boxes.values():
        if box['status'] == 'opened':
            box['status'] = 'opened/checked'
            return box['keys']
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List containing all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise False
    """
    if not boxes or len(boxes) == 1:
        return True

    opened_boxes = {0: {'status': 'opened', 'keys': boxes[0]}}

    while True:
        keys = look_next_opened_box(opened_boxes)
        if keys:
            for key in keys:
                if key < len(boxes) and key not in opened_boxes:
                    opened_boxes[key] = {
                            'status': 'opened',
                            'keys': boxes[key]
                    }
                else:
                    break

    return len(opened_boxes) == len(boxes)


def main():
    """Entry point for testing"""
    test_boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(test_boxes))


if __name__ == '__main__':
    main()
