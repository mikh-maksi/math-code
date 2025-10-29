from gen_functions import gen_VRP_data

A_ij,b_i,Xbasis_i,c_i = gen_VRP_data(4)
phi_i = [0,0,0,0]
Z_0 = 0
delta_i = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(b_i)

def simplex_out_fnc(file_name,A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,phi_i,base_i,base_j):
    str_out_ci = "&"
    for el in c_i:
        out_el = round(el, 2)
        str_out_ci += "& \\tiny{"+str(out_el)+"} "
    str_out_ci += "\\\\"

    str_out_x =" \\tiny{C_b}&\\tiny{ X_b}"
    for i in range(len(c_i)):
        str_out_x+="&  \\tiny{x_{"+str(i+1)+"}}"
    str_out_x +="&\\tiny{b_{i}}&\\tiny{\phi_{i}}\\\\"

    i=0
    str_matrix_out = ""
    for i in range(len(A_ij)):
        str_matrix_out += "\\tiny{"+str(round(c_i[i],2))+"}&\\tiny{x_{"+str(Xbasis_i[i][0])+"}}"
        for j in range(len(A_ij[0])):
            if (i==base_i)and(j==base_j):
                str_matrix_out += "&\\boxed{\\tiny{"+str(round(A_ij[i][j],2))+"}}"
            else:
                str_matrix_out += "&\\tiny{"+str(round(A_ij[i][j],2))+"}"
        str_matrix_out+="&\\tiny{"+str(b_i[i][0])+"}&\\tiny{"+str(round(phi_i[i],2))+"}\\\\"
        str_matrix_out+="\hline \n"

    str_last_out = "& "
    for d in delta_i:
        str_last_out += "&\\tiny{"+str(round(d,2))+"}"
    str_last_out+="&\\tiny{"+str(Z_0)+"}& \\\\"


    fl = open(f"c:/Work/repo/math-code/simplex/vrp-generation_minus/out/{file_name}.MD", "a+")
    fl.write('\r\n$$') 
    str_c=""
    for i in range(len(A_ij[0])):
        str_c+="c"
    fl.write("\\begin{array}{|c|c|"+str_c+"|c|c|}\n")
    fl.write('\hline')

    fl.write(str_out_ci)
    fl.write(''' \hline''')
    fl.write(str_out_x)
    fl.write(''' \hline''')
    fl.write(str_matrix_out)
    fl.write(str_last_out)

    fl.write('''
    \hline
    \end{array}
            
            $$\r\n\r\n
            ''')
    fl.close()