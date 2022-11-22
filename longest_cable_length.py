from math import sqrt


def is_in_range(x):
    if len(x) <= 50:
        for y in x:
            if 1 <= y <= 100:
                return True
    return False


def find_longest_cable_length(dist, heights):
    cable_length = 0
    if is_in_range(heights):
        n = 0
        change_to_min = False
        for height in heights:
            n += 1
            if n < len(heights):
                if change_to_min:
                    if heights[n] > 1:
                        cable_length += sqrt((heights[n] - 1)**2 + dist**2)
                    else:
                        cable_length += dist
                    change_to_min = False
                else:
                    change_length = sqrt((1 - height)**2 + dist**2)
                    cur_length = sqrt((heights[n] - height)**2 + dist**2)
                    if change_length > cur_length:
                        change_to_min = True
                        cable_length += change_length
                    else:
                        cable_length += cur_length
    return cable_length



