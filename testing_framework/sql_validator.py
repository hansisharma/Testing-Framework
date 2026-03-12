import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from database import db


def get_expected_demand(department):

    # Existing employee demand
    existing_query = """
    SELECT SUM(total_quantity_needed) AS existing_demand
    FROM precalculated_demand
    WHERE department = :department
    """

    existing_result = db.execute_query(existing_query, {"department": department})

    existing_demand = 0
    if existing_result and existing_result[0]["existing_demand"]:
        existing_demand = existing_result[0]["existing_demand"]


    # Future hire demand
    future_query = """
    SELECT SUM(new_joiners) AS future_demand
    FROM projected_hc_for_new_joiner_s_projected_hc_for_new_joiners
    WHERE department_name = :department
    """

    future_result = db.execute_query(future_query, {"department": department})

    future_demand = 0
    if future_result and future_result[0]["future_demand"]:
        future_demand = future_result[0]["future_demand"]


    combined_demand = existing_demand + future_demand

    return combined_demand