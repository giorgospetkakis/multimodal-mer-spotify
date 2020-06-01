import subprocess
import gdrive

gdrive.download_file_from_google_drive("0B_BScXpBMrN4V1k1OThWQ3dzZkk", "embeddings.zip")
subprocess.check_output("unzip embeddings.zip", shell=True)
subprocess.check_output("rm embeddings.zip", shell=True)
