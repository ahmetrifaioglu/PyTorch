mkdir ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel
python ../../cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.2"
sleep 1
python ../../cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.2"
sleep 1
python ../../cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.3"
sleep 1
python ../../cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.3"
sleep 1
python ../../cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.5"
sleep 1
python ../../cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.5"
sleep 1
python ../../cnn_playground.py 512_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.2"
sleep 1
python ../../cnn_playground.py 512_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.2"
sleep 1
python ../../cnn_playground.py 512_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.3"
sleep 1
python ../../cnn_playground.py 512_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.3"
sleep 1
