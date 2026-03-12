import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from tools.combined_sku_demand import combined_sku_demand_mcp


def validate_combined_demand(filters):

    result = combined_sku_demand_mcp({
        "metric": "sku_demand",
        "filters": filters
    })

    summary = result.get("summary", {})

    existing = summary.get("total_existing_demand", 0)
    future = summary.get("total_future_demand", 0)
    combined = summary.get("total_combined_demand", 0)

    return {
        "department": filters["department"],
        "existing_demand": existing,
        "future_demand": future,
        "combined_demand": combined
    }