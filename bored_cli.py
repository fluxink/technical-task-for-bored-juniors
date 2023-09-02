import argparse

from bored_api import get_activity
from bored_db import BoredDB


def main():
    parser = argparse.ArgumentParser(description="Bored API wrapper")

    parser.add_argument(
        "action",
        help="Action to perform",
        choices=["new", "list"],
    )

    parser.add_argument(
        "--type",
        help="Type of activity",
        choices=[
            "education",
            "recreational",
            "social",
            "diy",
            "charity",
            "cooking",
            "relaxation",
            "music",
            "busywork",
        ],
        default=None,
    )
    parser.add_argument(
        "--participants", help="Number of participants", type=int, default=None
    )
    parser.add_argument(
        "--price_min", help="Minimum price", type=float, default=None
    )
    parser.add_argument(
        "--price_max", help="Maximum price", type=float, default=None
    )
    parser.add_argument(
        "--accessability_min", help="Minimum accessability", type=float, default=None
    )
    parser.add_argument(
        "--accessability_max", help="Maximum accessability", type=float, default=None
    )

    args = parser.parse_args()

    if args.action == "new":
        activity = get_activity(
            type=args.type,
            participants=args.participants,
            price_min=args.price_min,
            price_max=args.price_max,
            accessability_min=args.accessability_min,
            accessability_max=args.accessability_max,
        )
        with BoredDB() as bored_db:
            bored_db.save_activity(activity)
        print(f"Activity '{activity['activity']}' saved!")
    elif args.action == "list":
        with BoredDB() as bored_db:
            activities = bored_db.get_last_activities(5)
        for activity in activities:
            print(activity)

if __name__ == "__main__":
    main()