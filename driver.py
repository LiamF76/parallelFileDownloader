## Liam Fogarty
## Parallel Final
## Parallel File Downloader

import threading
import gdown
import time

def download_file(file_id, output_name):
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"[{threading.current_thread().name}] Downloading {output_name}...")
    gdown.download(url, output_name, quiet=False)
    print(f"[{threading.current_thread().name}] Finished downloading {output_name}")

def main():
    try:
        count = int(input("How many files do you want to download? "))
    except ValueError:
        print("Invalid number.")
        return

    file_ids = []
    output_names = []

    for i in range(count):
        print(f"\nFile #{i+1}:")
        file_id = input("Enter the Google Drive file ID: ").strip()
        output_name = input("Enter the desired output filename (e.g., file.txt): ").strip()
        file_ids.append(file_id)
        output_names.append(output_name)

    threads = []
    for i in range(count):
        t = threading.Thread(
            target=download_file,
            args=(file_ids[i], output_names[i]),
            name=f"Thread-{i+1}"
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll downloads completed.")

if __name__ == "__main__":
    main()