import sys

STAT_START_COL = {"letter": 'F', "number": 6}

def get_time():
    TIME_FORMAT = "%Y-%m-%d"
    get_time()
    return strftime(TIME_FORMAT, gmtime())

def initialize_metadata():
    METADATA["comics sent"] = METADATA["comics sent"].format(*letters)
    STAT_START_COL
    METADATA["MRCN"] = scrape_utils.most_recent_comic_num()
    call_important()

def run_setup():
    # CREATE SHEETS].value = md_items[i][1]
    reset()
    initialize_metadata()

def reset():
    wb = db_client.wb
    get_time

# NOTE: Doesn't run if not specifically running setup - file should only be run once.
if __name__ == "__main__":
    print("dummy")
    reset()
