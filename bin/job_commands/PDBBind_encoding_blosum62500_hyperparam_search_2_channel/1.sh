mkdir ../../../log_files/PDBBind_encoding_blosum62500_hyperparam_search_2_channel
python ../../cnn_playground.py 512_512 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.2
sleep 1
python ../../cnn_playground.py 512_512 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.3
sleep 1
python ../../cnn_playground.py 512_512 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.5
sleep 1
python ../../cnn_playground.py 1024_512 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.2
sleep 1
python ../../cnn_playground.py 1024_512 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.3
sleep 1
python ../../cnn_playground.py 1024_512 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.5
sleep 1
python ../../cnn_playground.py 1024_256 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.2
sleep 1
python ../../cnn_playground.py 1024_256 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.3
sleep 1
python ../../cnn_playground.py 1024_256 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.5
sleep 1
python ../../cnn_playground.py 1024_1024 128 128_64 0.0001 16 PDBBind ecfp4 sequencematrix500_blosum62500 1 CompFCNNTarCNN2 0.2
sleep 1
