import json
import os

curDir = os.path.dirname(__file__)
a_list = {"A": []}
b_list = {"B": []}
c_list = {"C": []}
d_list = {"D": []}
e_list = {"E": []}
f_list = {"F": []}
g_list = {"G": []}
h_list = {"H": []}
i_list = {"I": []}
j_list = {"J": []}
k_list = {"K": []}
l_list = {"L": []}
m_list = {"M": []}
n_list = {"N": []}
o_list = {"O": []}
p_list = {"P": []}
q_list = {"Q": []}
r_list = {"R": []}
s_list = {"S": []}
t_list = {"T": []}
u_list = {"U": []}
v_list = {"V": []}
w_list = {"W": []}
x_list = {"X": []}
y_list = {"Y": []}
z_list = {"Z": []}
all_lists = [a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list, i_list, j_list, k_list, l_list, m_list, n_list, o_list, p_list, q_list, r_list, s_list, t_list, u_list, v_list, w_list, x_list, y_list, z_list]

word = ""
with open(f"{curDir}/engWords.txt", "r") as engWordsTxt, open(f"{curDir}/engWords.json", "w") as engWordsJson:
    words = engWordsTxt.readlines()
    for line in words:
        word = line.strip()
        if word.lower().startswith("a"):
            a_list["A"].insert(-1, word)
        elif word.lower().startswith("b"):
            b_list["B"].insert(-1, word)
        elif word.lower().startswith("c"):
            c_list["C"].insert(-1, word)
        elif word.lower().startswith("d"):
            d_list["D"].insert(-1, word)
        elif word.lower().startswith("e"):
            e_list["E"].insert(-1, word)
        elif word.lower().startswith("f"):
            f_list["F"].insert(-1, word)
        elif word.lower().startswith("g"):
            g_list["G"].insert(-1, word)
        elif word.lower().startswith("h"):
            h_list["H"].insert(-1, word)
        elif word.lower().startswith("i"):
            i_list["I"].insert(-1, word)
        elif word.lower().startswith("j"):
            j_list["J"].insert(-1, word)
        elif word.lower().startswith("k"):
            k_list["K"].insert(-1, word)
        elif word.lower().startswith("l"):
            l_list["L"].insert(-1, word)
        elif word.lower().startswith("m"):
            m_list["M"].insert(-1, word)
        elif word.lower().startswith("n"):
            n_list["N"].insert(-1, word)
        elif word.lower().startswith("o"):
            o_list["O"].insert(-1, word)
        elif word.lower().startswith("p"):
            p_list["P"].insert(-1, word)
        elif word.lower().startswith("q"):
            q_list["Q"].insert(-1, word)
        elif word.lower().startswith("r"):
            r_list["R"].insert(-1, word)
        elif word.lower().startswith("s"):
            s_list["S"].insert(-1, word)
        elif word.lower().startswith("t"):
            t_list["T"].insert(-1, word)
        elif word.lower().startswith("u"):
            u_list["U"].insert(-1, word)
        elif word.lower().startswith("v"):
            v_list["V"].insert(-1, word)
        elif word.lower().startswith("w"):
            w_list["W"].insert(-1, word)
        elif word.lower().startswith("x"):
            x_list["X"].insert(-1, word)
        elif word.lower().startswith("y"):
            y_list["Y"].insert(-1, word)
        elif word.lower().startswith("z"):
            z_list["Z"].insert(-1, word)
        else:
            print(f"Term '{word}' is not a valid entry!")
    
    json.dump(all_lists, engWordsJson, indent = 4)