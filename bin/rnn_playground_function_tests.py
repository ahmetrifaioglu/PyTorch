from dream_challenge_data_processing import remove_nonstandard_aas, get_all_aa_word_list, get_int2aaword_aaword2int_dicts, get_overlapping_n_grams_list
from dream_challenge_data_processing import get_prot_id_seq_dict_from_fasta_fl, get_int_encodings_of_proteins_sequences, pad_encoded_features
from dream_challenge_data_processing import save_encoded_features, get_aa_match_encodings, get_sequence_matrix, get_prot_seq_lengths_given_fasta
from dream_challenge_data_processing import get_training_validation_data_loaders_for_cnn, save_all_flattened_sequence_matrices
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


# print(get_overlapping_n_grams_list("ABCNSKABVGA", 2,0))
# _, encoded_features = get_int_encodings_of_proteins_sequences("dummy_test_targets.fasta", 2, 0)
#print(encoded_features)
# _, encoded_features = get_int_encodings_of_proteins_sequences("dummy_test_targets.fasta", 3, 3)
# print(encoded_features)
# print(pad_encoded_features(encoded_features, seq_length=20))
#python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/trigramencodings100032_normalized.tsv
#save_encoded_features("idg_train_test.fasta", 3, 2, 1000)
#python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/trigramencodings1000_normalized.tsv
#save_encoded_features("idg_train_test.fasta", 3, 0, 1000)

# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/bigramencodings100022_normalized.tsv
# save_encoded_features("idg_train_test.fasta", 2, 2, 1000)

# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/bigramencodings100020_normalized.tsv
# save_encoded_features("idg_train_test.fasta", 2, 0, 1000)


# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/trigramencodings50032_normalized.tsv
# save_encoded_features("idg_train_test.fasta", 3, 2, 500)

#python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/trigramencodings50030_normalized.tsv
# save_encoded_features("idg_train_test.fasta", 3, 0, 500)


# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/bigramencodings50022_normalized.tsv
# save_encoded_features("idg_train_test.fasta", 2, 2, 500)

# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/bigramencodings50020_normalized.tsv
# save_encoded_features("idg_train_test.fasta", 2, 0, 500)

# print(get_aa_match_encodings())
# get_sequence_matrix("ARNT", 10)

# create_sequence_matrix("ARN")


# get_training_validation_dataloaders_for_cnn(batch_size, comp_feature_list, comp_target_pair_dataset, "idg_train_test.fasta", "1500", "r")
# get_training_validation_data_loaders_for_cnn(1, 32, ["ecfp4"], "idg_comp_targ_uniq_inter_filtered.csv", "idg_train_test.fasta", 1500, "r" )

# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/sequencematrix500_normalized.tsv
# save_all_flattened_sequence_matrices("idg_train_test.fasta", 500)
# python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/sequencematrix1000_normalized.tsv
# save_all_flattened_sequence_matrices("idg_train_test.fasta", 1000)
#python rnn_playground_function_tests.py > ../trainingFiles/IDGDreamChallenge/protein_feature_vectors/sequencematrix1000_normalized.tsv
#save_all_flattened_sequence_matrices("idg_train_test.fasta", 1500)


# python rnn_playground_function_tests.py > ../trainingFiles/DeepDTA/protein_feature_vectors/sequencematrix500_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA/helper_files/davis_prots.fasta", 500)

# python rnn_playground_function_tests.py > ../trainingFiles/DeepDTA/protein_feature_vectors/sequencematrix1000_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA/helper_files/davis_prots.fasta", 1000)

# python rnn_playground_function_tests.py > ../trainingFiles/DeepDTA/protein_feature_vectors/sequencematrix1500_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA/helper_files/davis_prots.fasta", 1500)


# get_prot_seq_lengths_given_fasta("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA/helper_files/davis_prots.fasta")

# davis_prot_fl_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA/helper_files/davis_prots.fasta"

# get_training_validation_data_loaders_for_cnn(1, 32, ["ecfp4"], ["sequencematrix500"], "davis_comp_targ_affinity.csv", davis_prot_fl_path, "r")




# python rnn_playground_function_tests.py > /Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_kiba/target_feature_vectors/sequencematrix500_normalized.tsv
#save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_kiba/helper_files/targets.fasta", 500)

# python rnn_playground_function_tests.py > /Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_kiba/target_feature_vectors/sequencematrix1000_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_kiba/helper_files/targets.fasta", 1000)

# python rnn_playground_function_tests.py > /Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_kiba/target_feature_vectors/sequencematrix1500_normalized.tsv
save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_kiba/helper_files/targets.fasta", 1500)
