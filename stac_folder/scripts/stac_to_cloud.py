import pathlib
import sys

# make modules importable when running this file as script
# sys.path.append(str(pathlib.Path(__file__).parent.parent))

# import coclicodata functionalities (TODO: import as package when ETL is decoupled from CoCliCo STAC; Etiënne & Floris now whereabouts)
sys.path.append(
    str(pathlib.Path().home().joinpath("Documents", "GitHub", "coclicodata"))
)  # import functionality from local clone of coclicodata (make sure you pull the latest version)

from etl.cloud_services import dir_to_google_cloud
from etl.keys import load_google_credentials
from etl import p_drive, rel_root

if __name__ == "__main__":
    # hard-coded input params
    GCS_PROJECT = "DGDS - I1000482-002"
    BUCKET_NAME = "dgds-data-public"
    BUCKET_PROJ = "gca"
    STAC_NAME = "gca-stac"
    IN_DIRNAME = "current"

    # hard-coded input params at project level
    coclico_data_dir = pathlib.Path(p_drive, "11205479-coclico", "FASTTRACK_DATA")

    # upload dir to gcs from local drive
    source_dir_fp = str(pathlib.Path(__file__).parent.parent.joinpath(IN_DIRNAME))

    load_google_credentials(
        google_token_fp=coclico_data_dir.joinpath("google_credentials.json")
    )

    dir_to_google_cloud(
        dir_path=source_dir_fp,
        gcs_project=GCS_PROJECT,
        bucket_name=BUCKET_NAME,
        bucket_proj=BUCKET_PROJ,
        dir_name=STAC_NAME,
    )