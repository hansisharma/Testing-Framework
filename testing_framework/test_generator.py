import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from database import db


def generate_tests():

    tests = []

    departments = db.execute_query(
        "SELECT DISTINCT department FROM precalculated_demand"
    )

    locations = db.execute_query(
        "SELECT DISTINCT base_location_code as location FROM precalculated_demand"
    )

    months = db.execute_query(
        "SELECT DISTINCT issuance_month as month FROM precalculated_demand LIMIT 6"
    )

    genders = ["Male", "Female"]

    for dept in departments:
        for gender in genders:
            for loc in locations:
                for month in months:

                    tests.append({
                        "department": dept["department"],
                        "gender": gender,
                        "location": loc["location"],
                        "month": month["month"]
                    })

    return tests