import pandas as pd
from datetime import datetime


def generate_report(results):

    df = pd.DataFrame(results)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"testing_framework/test_report_{timestamp}.xlsx"

    df.to_excel(output_file, index=False)

    print(f"\nTest report generated: {output_file}")