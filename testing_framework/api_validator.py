import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools.combined_sku_demand import combined_sku_demand_mcp


def get_dashboard_demand(filters):

    result = combined_sku_demand_mcp(filters)

    if "total_demand_quantity" in result:
        return result["total_demand_quantity"]

    return result