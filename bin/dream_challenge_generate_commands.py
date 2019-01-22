
from itertools import permutations, combinations

comp_feature_list = ["ecfp4", "fcfp4", "rdk5"]
tar_feature_list = ["k-sep-bigrams", "APAAC", "DDE", "pfam"]

comb_comp_feat_list = []
comb_tar_feat_list = []

for i in range(3):
    lst_cand_comp_list = list(combinations(comp_feature_list,i+1))

    for cand in lst_cand_comp_list:
        str_comp_feat = ""
        for feat in cand:
            str_comp_feat += "{}_".format(feat)
        str_comp_feat =str_comp_feat[:-1]

        comb_comp_feat_list.append(str_comp_feat)

for i in range(2):
    lst_cand_tar_list = list(combinations(tar_feature_list, i + 1))

    for cand in lst_cand_tar_list:
        str_tar_feat = ""
        for feat in cand:
            str_tar_feat += "{}_".format(feat)
        str_tar_feat = str_tar_feat[:-1]

        comb_tar_feat_list.append(str_tar_feat)


print(comb_comp_feat_list)
print(comb_tar_feat_list)
n_of_neuron_list_h = [4096, 2048, 1536, 1024, 512, 128]
n_of_neuron_list_fc = [1024, 512, 256, 64]

n_of_h_layers = 2
n_of_fc_layers = 2

lst_n_permutations = list(permutations(n_of_neuron_list_h, n_of_h_layers))

lst_decreasing_permutations = []
for perm in lst_n_permutations:
    is_decreasing = True
    perm_ind = 0

    while perm_ind+1<(len(perm)):
        if perm[perm_ind]<perm[perm_ind+1]:
            is_decreasing = False
            break
        perm_ind += 1

    if is_decreasing:
        lst_decreasing_permutations.append(perm)
for comp_feat in comb_comp_feat_list:
    for tar_feat in comb_tar_feat_list:
        for hidden in lst_decreasing_permutations:
            for fc in n_of_neuron_list_fc:
                print(comp_feat, tar_feat, hidden, fc )
#print(len(lst_decreasing_permutations))


