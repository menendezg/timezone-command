from datetime import datetime
import pytz
import sys
import os
import time
import argparse


def process_time(args):
    if args.get == "live-time":
        try:
            while True:
                print_time_table(args.timezones)
                time.sleep(1)  # Update every second
        except KeyboardInterrupt:
            print("Exiting...")
    if args.get == "timezones":
        all_timezones = pytz.all_timezones
        for timezone in all_timezones:
            print(timezone)


def get_time_by_tz(time_zone):
    try:
        tz = pytz.timezone(time_zone)
        time_in_tz = datetime.now(tz)
        return time_in_tz.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except Exception as e:
        return str(e)


def print_time_table(time_zones):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n{'Time Zone':<30} | {'Current Time'}")
    print(f"{'-'*30} | {'-'*25}")
    for zone in time_zones:
        time_str = get_time_by_tz(zone)
        print(f"{zone:<30} | {time_str}")
    print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple get time app")

    # Arguments
    parser.add_argument(
        "--get",
        type=str,
        choices=["live-time", "timezones"],
        default="live-time",
        help="The operation to perform, picture will be \
                        a picture of the moment, live will be a loop showing time all the time like a tail",
    )
    parser.add_argument(
        "--timezones", type=str, nargs="+", help="a list of timezones to display"
    )

    args = parser.parse_args()
    process_time(args)
