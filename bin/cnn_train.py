import argparse



parser = argparse.ArgumentParser(description='')
parser.add_argument(
    '--comp-hidden-layer-neurons',
    type=str,
    default="512_512",
    metavar='CHLN',
    help='number of neurons in compound hidden layers (default: 512_512)')
parser.add_argument(
    '--target-layer-neurons-after-flattened',
    type=int,
    default=512,
    metavar='TFFLAF',
    help='number of neurons after flattening target conv layers (default: 512)')
parser.add_argument(
    '--last-two-hidden-layer-neurons',
    type=str,
    default="256_256",
    metavar='CHLN',
    help='number of neurons in last two hidden layers before output layer (default: 256_256)')
parser.add_argument(
    '--lr',
    type=float,
    default=0.01,
    metavar='LR',
    help='learning rate (default: 0.01)')
parser.add_argument(
    '--batch-size',
    type=int,
    default=32,
    metavar='BS',
    help='batch size (default: 32)')

parser.add_argument(
    '--training-data',
    type=str,
    default="PDBBind",
    metavar='TD',
    help='the name of the training dataset (default: PDBBind)')


args = parser.parse_args()
training_data= args.training_data

"""
comp_hidden_layer_neurons = [int(num) for num in sys.argv[1].split("_")]
after_flattened_conv_layer_neurons = sys.argv[2]
last_2_hidden_layer_list = sys.argv[3].split("_")
learn_rate = sys.argv[4]
batch_size = sys.argv[5]
training_dataset = sys.argv[6]
"""