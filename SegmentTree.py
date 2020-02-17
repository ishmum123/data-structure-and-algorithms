from Utils import get_random_numbers, measure


def construct_segment_tree(marr, seg_tree=None, si=0, ei=None, ci=0):
    if not marr:
        return

    if ei is None:
        ei = len(marr) - 1

    if not seg_tree:
        seg_tree = [0] * len(marr) * 4

    if si == ei:
        seg_tree[ci] = (si, ei, marr[si])
    else:
        mid = (si + ei) // 2
        lidx = ci * 2 + 1
        ridx = ci * 2 + 2
        construct_segment_tree(marr, seg_tree, si, mid, lidx)
        construct_segment_tree(marr, seg_tree, mid + 1, ei, ridx)
        seg_tree[ci] = (si, ei, seg_tree[lidx][2] + seg_tree[ridx][2])

    return seg_tree


def get_sum_of_range(seg_tree, si, ei, ci=0):
    crv = seg_tree[ci]
    if si <= crv[0] and crv[1] <= ei:
        return crv[2]
    if crv[0] > ei or crv[1] < si:
        return 0
    return get_sum_of_range(seg_tree, si, ei, ci * 2 + 1) + get_sum_of_range(seg_tree, si, ei, ci * 2 + 2)


def update_index(seg_tree, idx, value, ci=0):
    crv = seg_tree[ci]
    if crv[0] <= idx <= crv[1]:
        if crv[0] == crv[1]:
            seg_tree[ci] = (crv[0], crv[1], value)
        else:
            lidx = ci * 2 + 1
            update_index(seg_tree, idx, value, lidx)
            ridx = ci * 2 + 2
            update_index(seg_tree, idx, value, ridx)
            seg_tree[ci] = (crv[0], crv[1], seg_tree[lidx][2] + seg_tree[ridx][2])
    else:
        return


def perform_seg_tree_ops(arr):
    st = construct_segment_tree(arr)
    print(get_sum_of_range(st, 0, 900))
    print(get_sum_of_range(st, 0, 5000))
    print(get_sum_of_range(st, 1774, 9881))
    print(get_sum_of_range(st, 2932, 5771))
    print(get_sum_of_range(st, 0, 9999))
    update_index(st, 2, 5)
    print('----------------After Update-------------')
    print(get_sum_of_range(st, 0, 900))
    print(get_sum_of_range(st, 0, 5000))
    print(get_sum_of_range(st, 1774, 9881))
    print(get_sum_of_range(st, 2932, 5771))
    print(get_sum_of_range(st, 0, 9999))


if __name__ == '__main__':
    arr = get_random_numbers(10 ** 5)

    measure(lambda: perform_seg_tree_ops(arr))
