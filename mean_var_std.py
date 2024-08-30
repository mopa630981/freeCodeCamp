import numpy as np
def calculate(input_list):
    my_mat=np.array(input_list).reshape(3,3)
    output={
        'mean':[np.mean(my_mat,axis=0).tolist(),np.mean(my_mat,axis=1).tolist(),np.mean(my_mat).tolist()],
        'variance':[np.var(my_mat,axis=0).tolist(),np.var(my_mat,axis=1).tolist(),np.var(my_mat).tolist()],
        'standard deviation':[np.std(my_mat,axis=0).tolist(),np.std(my_mat,axis=1).tolist(),np.std(my_mat).tolist()],
        'max':[np.max(my_mat,axis=0).tolist(),np.max(my_mat,axis=1).tolist(),np.max(my_mat).tolist()],
        'min':[np.min(my_mat,axis=0).tolist(),np.min(my_mat,axis=1).tolist(),np.min(my_mat).tolist()],
        'sum':[np.sum(my_mat,axis=0).tolist(),np.sum(my_mat,axis=1).tolist(),np.sum(my_mat).tolist()]}
    return output

