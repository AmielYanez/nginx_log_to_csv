import os
import csv

from libs import *


def export_data(input_file, output_file):
    if not os.path.isfile(input_file):
        raise Exception("Input File does not exists: {}".format(input_file))
    columns = [
        constants.COL_IP_ADDRESS,
        constants.COL_LOG_TIME,
        constants.COL_LOG_PATH,
        constants.COL_LOG_STATUS,
        constants.COL_LOG_BW,
        constants.COL_LOG_REFERER,
        constants.COL_USER_AGENT,
        constants.COL_COUNTRY,
        constants.COL_STATE,
        constants.COL_DEVICE_TYPE,
        constants.COL_BROWSER
    ]
    with open(input_file) as f:
        with open(output_file, 'ab') as csv_file:
            wtr = csv.writer(csv_file)
            wtr.writerow(columns)
            for line in read_file(f):
                datum = process_line(line)
                if not datum:
                    continue
                wtr.writerow([datum[col_name] for col_name in columns])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help="Log file location", required=True)
    parser.add_argument('--output', help="Log file location", required=True)
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output

    export_data(input_file, output_file)
