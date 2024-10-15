import os
import zipfile
import kaggle

def download_kaggle_dataset(dataset_name, download_dir="./data/"):
    """Downloads and extracts a Kaggle dataset."""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    print(f"Downloading {dataset_name}...")

    kaggle.api.dataset_download_files(dataset_name, path=download_dir, unzip=True)

    print("Download complete.")

    for file in os.listdir(download_dir):
        if file.endswith(".zip"):
            file_path = os.path.join(download_dir, file)
            print(f"Extracting {file_path}...")
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)
            os.remove(file_path)
            print(f"Removed {file_path}.")

if __name__ == "__main__":
    dataset = "ebrahimelgazar/pixel-art"  
    download_kaggle_dataset(dataset)
