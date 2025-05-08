import threading
import gdown

## here are my google drive file links used for testing, open to anyone with link
## https://drive.google.com/drive/folders/1C0TGU3VUWQs9bSjpMUUN57FksfDySSil?usp=sharing
## https://drive.google.com/drive/folders/1AkmkPUHsnhMZji94kaAlZj6jnOxL-Cne?usp=sharing
## https://drive.google.com/drive/folders/1nDKihZAa2AhEKOPMhCqGSFxne_eZq3Wj?usp=sharing

def extract_folder_id(folder_url):
    """
    Extracts the folder ID from a standard Google Drive folder URL.
    """
    if "drive.google.com" not in folder_url or "/folders/" not in folder_url:
        raise ValueError("Only full Google Drive folder links are accepted.")

    parts = folder_url.split("/folders/")
    if len(parts) < 2:
        raise ValueError("Invalid Google Drive folder link format.")

    folder_id = parts[1].split("?")[0]
    return folder_id

def download_folder(folder_id, output_dir):
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    print(f"[{threading.current_thread().name}] Downloading folder into '{output_dir}'...")
    gdown.download_folder(id=folder_id, output=output_dir, quiet=False, use_cookies=False)
    print(f"[{threading.current_thread().name}] Finished downloading folder.")

def main():
    try:
        count = int(input("How many folders do you want to download? "))
    except ValueError:
        print("Invalid number.")
        return

    downloads = []

    for i in range(count):
        print(f"\nFolder #{i+1}:")
        folder_url = input("Paste the full Google Drive folder URL: ").strip()
        try:
            folder_id = extract_folder_id(folder_url)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        output_name = input("Enter the name of the output directory: ").strip()
        downloads.append((folder_id, output_name))

    threads = []
    for i, (folder_id, output_dir) in enumerate(downloads):
        t = threading.Thread(
            target=download_folder,
            args=(folder_id, output_dir),
            name=f"Thread-{i+1}"
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll folder downloads completed.")

if __name__ == "__main__":
    main()
