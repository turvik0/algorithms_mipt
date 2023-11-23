import numpy as np
def transformshorted(p, q):
    newanwrdt(p)
    all_p_chain = []
    now_p = []
    for i in range(len(p)):
        now_p.append(p[i])

    red_cuttsii = briktnd(p)
    blue_cuttsii = briktnd(q)
    all_cuttsii = []
    sdertblue_cuttsii = []
    sdertred_cuttsii = []
    all_p_chain.append(red_cuttsii)

    for i in range(len(red_cuttsii)):
        all_cuttsii.append(red_cuttsii[i])
        sdertred_cuttsii.append(red_cuttsii[i])
    for i in range(len(blue_cuttsii)):
        all_cuttsii.append(blue_cuttsii[i])
        sdertblue_cuttsii.append(blue_cuttsii[i])

    while (graph_hascirclsds_notrivial(all_cuttsii) == 1):
        cycle = findcirclsd(all_cuttsii)
        first_cuttsii = []
        ind_1 = 0
        if (cycle[0] not in sdertred_cuttsii):
            ind_1 = 1

        first_cuttsii.append(cycle[ind_1])
        if (ind_1 + 2 < len(cycle)):
            first_cuttsii.append(cycle[ind_1 + 2])
        else:
            first_cuttsii.append(cycle[-len(cycle) + ind_1 + 2])
        i_4 = first_cuttsii[1][1]
        i_1 = first_cuttsii[0][0]
        i_3 = first_cuttsii[1][0]
        i_2 = first_cuttsii[0][1]

        p_new = tofight(now_p, [i_1, i_2, i_3, i_4])
        now_p = p_new

        if ([i_1, i_2] in sdertred_cuttsii):
            sdertred_cuttsii.remove([i_1, i_2])
            all_cuttsii.remove([i_1, i_2])
        else:
            sdertred_cuttsii.remove([i_2, i_1])
            all_cuttsii.remove([i_2, i_1])

        if ([i_3, i_4] in sdertred_cuttsii):
            sdertred_cuttsii.remove([i_3, i_4])
            all_cuttsii.remove([i_3, i_4])
        else:
            sdertred_cuttsii.remove([i_4, i_3])
            all_cuttsii.remove([i_4, i_3])

        sdertred_cuttsii.append([i_1, i_4])
        sdertred_cuttsii.append([i_2, i_3])

        newanwrdt(now_p)

        all_cuttsii.append([i_1, i_4])
        all_cuttsii.append([i_2, i_3])


def roundgtckl(genom):
    darkdgk = []
    itemsd = []
    for chrom in genom:
        itemsd = np.zeros(2 * len(chrom))
        for j in range(len(chrom)):
            i = chrom[j]
            if (i > 0):
                itemsd[2 * j] = 2 * i - 1
                itemsd[2 * j + 1] = 2 * i
                darkdgk.append([2 * i - 1, 2 * i])
            else:
                itemsd[2 * j] = (-2) * i
                itemsd[2 * j + 1] = (-2) * i - 1
                darkdgk.append([2 * abs(i), 2 * abs(i) - 1])
    return itemsd, darkdgk


def briktnd(p):
    cuttsii = []
    for i in p:
        itemsd = roundchromd(i)[0]
        for j in range(len(i) - 1):
            cuttsii.append([itemsd[2 * j + 1], itemsd[2 * j + 2]])
        last_j = 2 * len(i) - 1
        cuttsii.append([itemsd[last_j], itemsd[0]])
    return cuttsii


def clechrmo(itemsd):
    chrom = np.zeros(int(len(itemsd) / 2))
    for j in range(int(len(itemsd) / 2)):
        if (itemsd[2 * j] < itemsd[2 * j + 1]):
            chrom[j] = itemsd[2 * j + 1] / 2
        else:
            chrom[j] = - itemsd[2 * j] / 2
    return chrom


def otparg(graph, darkdgk):
    p = []
    now_chrom = []
    smalds = []
    sdertcuttsii = []
    for i in range(len(graph)):
        sdertcuttsii.append(graph[i])
    sdertdarkdgk = []
    for i in range(len(darkdgk)):
        sdertdarkdgk.append(darkdgk[i])

    while(len(sdertcuttsii) > 0):
        start_i = sdertdarkdgk[0][0]
        now_i = sdertdarkdgk[0][1]
        now_chrom.append([start_i, now_i])
        sdertdarkdgk.remove([start_i, now_i])
        sdertcuttsii.remove([start_i, now_i])
        while(now_i != start_i):
            for j in range(len(sdertcuttsii)):
                if (sdertcuttsii[j][0] == now_i):
                    now_i = sdertcuttsii[j][1]
                    now_chrom.append(sdertcuttsii[j])
                    if (sdertcuttsii[j] in sdertdarkdgk):
                        sdertdarkdgk.remove(sdertcuttsii[j])
                    gettwo = sdertcuttsii[j]
                    sdertcuttsii.remove(gettwo)
                    break
                if (sdertcuttsii[j][1] == now_i):
                    now_i = sdertcuttsii[j][0]
                    now_chrom.append(sdertcuttsii[j])
                    if (sdertcuttsii[j] in sdertdarkdgk):
                        sdertdarkdgk.remove(sdertcuttsii[j])
                    gettwo = sdertcuttsii[j]
                    sdertcuttsii.remove(gettwo)
                    break

        smalds.append(now_chrom)
        now_chrom = []

    for chr in smalds:
        now_els = []
        for edg in chr:
            if (edg[0] not in now_els):
                now_els.append(edg[0])
            if (edg[1] not in now_els):
                now_els.append(edg[1])
        p_now = clechrmo(now_els)
        p.append(p_now)
    return p


def make_two_break(cuttsii, two_break):
    res = []
    for i in range(len(cuttsii)):
        res.append(cuttsii[i])
    idx_1 = -1

    if ([two_break[0], two_break[1]] in cuttsii):
        idx_1 = cuttsii.index([two_break[0], two_break[1]])
    else:
        idx_1 = cuttsii.index([two_break[1], two_break[0]])

    idx_2 = -1
    if ([two_break[2], two_break[3]] in cuttsii):
        idx_2 = cuttsii.index([two_break[2], two_break[3]])
    else:
        idx_2 = cuttsii.index([two_break[3], two_break[2]])

    res[idx_1][0] = two_break[0]
    res[idx_1][1] = two_break[3]
    res[idx_2][1] = two_break[1]
    res[idx_2][0] = two_break[2]
    return res

def findcirclsd(cuttsii):
    sdertcuttsii = []
    for i in range(len(cuttsii)):
        sdertcuttsii.append(cuttsii[i])
    while (len(sdertcuttsii) > 0):
        cycle = []
        start_i = sdertcuttsii[0][0]
        now_i = sdertcuttsii[0][1]
        cyc_len = 0
        cycle.append([start_i, now_i])
        sdertcuttsii.remove([start_i, now_i])
        sdvrtd = []
        sdvrtd.append(start_i)
        while (now_i != start_i):
            sdvrtd.append(now_i)
            for j in range(len(sdertcuttsii)):
                if (sdertcuttsii[j][0] == now_i):
                    now_i = sdertcuttsii[j][1]
                    gettwo = sdertcuttsii[j]
                    cycle.append(gettwo)
                    sdertcuttsii.remove(gettwo)
                    cyc_len += 1
                    break
                else:
                    if (sdertcuttsii[j][1] == now_i):
                        now_i = sdertcuttsii[j][0]
                        gettwo = sdertcuttsii[j]
                        cycle.append([sdertcuttsii[j][1], sdertcuttsii[j][0]])
                        sdertcuttsii.remove(gettwo)
                        cyc_len += 1
                        break
        if (cyc_len > 1):
            return cycle
    return []

def tofight(p, two_break):
    darkdgk = roundgtckl(p)[1]
    bretndcuttsii = briktnd(p)

    all_cuttsii = []
    for i in range(len(darkdgk)):
        all_cuttsii.append(darkdgk[i])
    for j in range(len(bretndcuttsii)):
        all_cuttsii.append(bretndcuttsii[j])

    all_new_cuttsii = make_two_break(all_cuttsii, two_break)
    pr = otparg(all_new_cuttsii, darkdgk)
    return pr


def newanwrdt(p):
    st_res = ""
    for res_i in p:
        st_res += "("
        for i in range(len(res_i)):
            if (res_i[i] > 0):
                st_res += "+"
            st_res += str(int(res_i[i]))
            st_res += " "
        st_res = st_res[:-1]
        st_res += ")"
    print(st_res)
    return st_res


def graph_hascirclsds_notrivial(cuttsii):
    res = 0
    sdertcuttsii = []
    for i in range(len(cuttsii)):
        sdertcuttsii.append(cuttsii[i])

    while (len(sdertcuttsii) > 0):
        start_i = sdertcuttsii[0][0]
        now_i = sdertcuttsii[0][1]
        cyc_len = 0
        sdertcuttsii.remove([start_i, now_i])
        while (now_i != start_i):
            has_edge = 0
            for j in range(len(sdertcuttsii)):
                if (sdertcuttsii[j][0] == now_i):
                    now_i = sdertcuttsii[j][1]
                    gettwo = sdertcuttsii[j]
                    sdertcuttsii.remove(gettwo)
                    has_edge = 1
                    cyc_len += 1
                    break
                if (sdertcuttsii[j][1] == now_i):
                    now_i = sdertcuttsii[j][0]
                    gettwo = sdertcuttsii[j]
                    sdertcuttsii.remove(gettwo)
                    has_edge = 1
                    cyc_len += 1
                    break
            if (has_edge == 0):
                break
        if (now_i == start_i and cyc_len > 1):
            res = 1
    return res

def roundchromd(chrom):
    itemsd = np.zeros(2 * len(chrom))
    darkdgk = []
    for j in range(len(chrom)):
        i = chrom[j]
        if (i > 0):
            itemsd[2 * j] = 2 * i - 1
            itemsd[2 * j + 1] = 2 * i
            darkdgk.append([2 * i - 1, 2 * i])
        else:
            itemsd[2 * j] = (-2) * i
            itemsd[2 * j + 1] =(-2) * i - 1
            darkdgk.append([2 * abs(i), 2 * abs(i) - 1])
    return itemsd, darkdgk

if __name__ == '__main__':
    with open('data.txt') as f:
        lineinput = f.readline()
        lineinput2 = f.readline()
    itemnumns = []
    now_itemnum = []
    now = ''
    for i in range(1, len(lineinput)):
        if (lineinput[i] == " " or lineinput[i] == ")"):
            now_itemnum.append(int(now))
            now = ""
        else:
            now += lineinput[i]
        if (lineinput[i] == ")"):
            itemnumns.append(now_itemnum)
            now_itemnum = []
        if (lineinput[i] == "("):
            now = ""
    now = ''
    itemnumns2 = []
    now_itemnum = []
    for i in range(1, len(lineinput2)):
        if (lineinput2[i] == " " or lineinput2[i] == ")"):
            now_itemnum.append(int(now))
            now = ""
        else:
            now += lineinput2[i]
        if (lineinput2[i] == ")"):
            itemnumns2.append(now_itemnum)
            now_itemnum = []
        if (lineinput2[i] == "("):
            now = ""
    transformshorted(itemnumns, itemnumns2)