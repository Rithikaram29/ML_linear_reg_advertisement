import kagglehub
import os

def download_dataset():
    # Define project data folder
    project_data_path = os.path.join(os.getcwd(), "data")

    # Create folder if it doesn't exist
    os.makedirs(project_data_path, exist_ok=True)

    resolved_path = kagglehub.dataset_download(
        "harrimansaragih/dummy-advertising-and-sales-data",
        output_dir=project_data_path,
        force_download=False,
    )

    print("Dataset downloaded to:", resolved_path)
    return resolved_path

# download_dataset()
if __name__ == "__main__":
    download_dataset()