def data_input_f():
    import pandas as pd
    import csv
    import numpy as np

    # Шлях до CSV-файлу
    file_path = "c:/Work/repo/math-code/simplex/vrp-generation/input/data.csv"
    file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out.csv"

    # Читання CSV
    df = pd.read_csv(file_path,sep=";")
    cols = len(df.columns)-1
    rows = len(df)-1

    cols_name = []
    cols_name.append("C_i")
    cols_name.append("Xbase_i")

    for ii in range(cols):
        i = ii+1
        x_n_name="x"+str(i)
        cols_name.append(x_n_name)

    for i in range(rows):
        x_n = i+cols+1
        x_n_name = "x"+str(x_n)
        cols_name.append(x_n_name)
        df.loc[i+1,"Xbase_i"]=x_n
        df.loc[i+1,"C_i"]=0
        df.loc[0,x_n_name]=0
        for jj in range(rows):
            j=jj+1
            n_out =0
            if i == jj:
                n_out=1
            df.loc[j,x_n_name]=n_out

    cols_name.append("bi")
    df = df[cols_name]
    # print(df)

    A = np.array([df["x1"][1:].to_numpy(), df["x2"][1:].to_numpy(), df["x3"][1:].to_numpy(), df["x4"][1:].to_numpy(), df["x5"][1:].to_numpy()])
    A_t = np.transpose(A)

    bi_num = df["bi"][1:].to_numpy()
    bi_num_shape =  bi_num.reshape(-1, 1)

    c_i_arr=[]
    c_i_arr.append(df['x1'][0])
    c_i_arr.append(df['x2'][0])
    c_i_arr.append(df['x3'][0])
    c_i_arr.append(df['x4'][0])
    c_i_arr.append(df['x5'][0])

    c_i_num=np.array(c_i_arr)

    A_ij = A_t
    b_i = bi_num_shape
    c_i = c_i_num
    Xbasis_i_a = df["Xbase_i"][1:].to_numpy()
    Xbasis_i = Xbasis_i_a.reshape(-1, 1)
    # print(Xbasis_i)
    return [A_ij,b_i,c_i,Xbasis_i]


# print(data_input_f())
# df.to_csv(file_path_out ,mode='a',sep=";")
def to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0):
    import pandas as pd
    import numpy as np
    data = {}
    df = pd.DataFrame(data)
    df.loc[0,'x1']="0"
    for i in range(len(Xbasis_i)):
        ii = i+1
        df.loc[ii,'Xbase_i']=Xbasis_i[i][0]
        df.loc[ii,'C_i']=Cbasis_i[i]
        df.loc[ii,'b_i']=b_i[i]
        df.loc[ii,'fi_i']=fi_i[i]

    A_T_ij=np.transpose(A_ij)

    for i in range(len(A_T_ij)):
        ii = i+1
        # print()
        col_name = "x"+str(ii)
        df.loc[0,col_name]=c_i[i]
        df.loc[4,col_name]=delta_i[i]
        for j in range(len(A_T_ij[0])):
            jj = j+1
            # print(A_T_ij[i][j])
            df.loc[jj,col_name]=A_T_ij[i][j]
                            

    line_plus = len(Xbasis_i)+1

    df.loc[line_plus,"b_i"] = Z_0[0]
    # delta =  | "x1", "x2","x3","x4","x5"
    # Z = | b_i

    df = df[["C_i","Xbase_i", "x1", "x2","x3","x4","x5", "b_i","fi_i"]]

    print(df)
    return df