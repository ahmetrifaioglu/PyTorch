import sys

#def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs)


def get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path):
    prot_id_seq_dict = dict()

    prot_id = ""
    with open("{}".format(fasta_fl_path)) as f:
        for line in f:
            line = line.split("\n")[0]
            if line.startswith(">"):
                prot_id = line.split("|")[1]
                prot_id_seq_dict[prot_id] = ""
            else:
                prot_id_seq_dict[prot_id] = prot_id_seq_dict[prot_id] + line

    return prot_id_seq_dict


