import requests

def download(url: str, filename: str) -> None:

    with requests.get(url, stream=True) as r:
        r.raise_for_status() 
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  
                    f.write(chunk)


filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/medical_insurance_dataset.csv'
download(filepath, "insurance.csv")
