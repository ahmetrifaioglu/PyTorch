from torch.utils.data.dataset import Dataset
from torchvision import transforms
import pandas as pd
import numpy as np
import torch

class CustomDatasetFromCSV(Dataset):
    def __init__(self, csv_path):
        """
        Args:
            csv_path (string): path to csv file
            height (int): image height
            width (int): image width
            transform: pytorch transforms for transforms and tensor conversion
        """
        self.data = pd.read_csv(csv_path)

        self.labels = np.asarray(self.data.iloc[:, 0])
        self.data = np.asarray(self.data.iloc[:, 2:]).astype('float')
        print(len(self.labels), len(self.data))
        print(self.data.shape)


    def __getitem__(self, index):
        single_image_label = self.labels[index]
        #print(single_image_label)

        # Read each 784 pixels and reshape the 1D array ([784]) to 2D array ([28,28])
        #print(self.data[1])
        #img_as_np = np.asarray(self.data.iloc[index][1:])
        # Transform image to tensor
        #if self.transforms is not None:
        img_as_tensor = torch.tensor(self.data)
        # Return image and the label
        #print(img_as_tensor)
        return (img_as_tensor, single_image_label)


    def __len__(self):
        return len(self.data)


if __name__ == "__main__":
    # Define transforms
    #transformations = transforms.Compose([transforms.ToTensor()])
    # Define custom dataset
    custom_mnist_from_csv = \
        CustomDatasetFromCSV('./data/kc_house_data.csv')
    # Define data loader
    mn_dataset_loader = torch.utils.data.DataLoader(dataset=custom_mnist_from_csv,
                                                    batch_size=1,
                                                    shuffle=False)



    for images, labels in mn_dataset_loader:
        print(images.shape, labels.shape)
