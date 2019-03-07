from rnn_playground_data_processing import remove_nonstandard_aas, get_all_aa_word_list, get_int2aaword_aaword2int_dicts, get_overlapping_n_grams_list
from rnn_playground_data_processing import get_prot_id_seq_dict_from_fasta_fl, get_int_encodings_of_proteins_sequences, pad_encoded_features
from rnn_playground_data_processing import save_encoded_features
#print(get_aa_list())

# print(get_int2aa_aa2int_dicts())

# print(convert_aa_into_onehot("V"))

# print(convert_protein_sequence_into_onehot("ARN"))


# print(encode_protein_sequence("ARBNBZAXBAVAB"))
# print(get_prot_id_seq_dict_from_fasta_fl("test_targets.fasta")["P00519"])

# print(get_int_encodings_of_proteins_sequences("test_targets.fasta")["P00519"])

"""
prot_id_list, seq_encoding_list = get_int_encodings_of_proteins_sequences("test_targets.fasta")
features = pad_features(seq_encoding_list, 2000)
print(features[:100, :10])
"""

# print(len(get_all_aa_word_list(3)))

# print(get_int2aaword_aaword2int_dicts(3))

# print(get_overlapping_n_grams_list("ABSNC", 3))

# print(remove_nonstandard_aas("ABSNC"))

# print(get_prot_id_seq_dict_from_fasta_fl("dummy_test_targets.fasta"))

# _, encoded_features = get_int_encodings_of_proteins_sequences("dummy_test_targets.fasta", 3)
# print(encoded_features)
# print(pad_encoded_features(encoded_features, seq_length=20))


# save_encoded_features("idg_train_test.fasta", 3, 1000)


# print(get_overlapping_n_grams_list_by_skipping("ABCNSKABVGA", 3,3))
# _, encoded_features = get_int_encodings_of_proteins_sequences("dummy_test_targets.fasta", 3, 3)
# print(encoded_features)
# print(pad_encoded_features(encoded_features, seq_length=20))
#python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/trigramencodings100032_normalized.tsv
#save_encoded_features("idg_train_test.fasta", 3, 2, 1000)
#python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/trigramencodings1000_normalized.tsv
#save_encoded_features("idg_train_test.fasta", 3, 0, 1000)
