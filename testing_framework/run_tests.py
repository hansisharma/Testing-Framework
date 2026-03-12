import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from test_generator import generate_tests
from validators.combined_demand_validator import validate_combined_demand
from report_generator import generate_report
from ui_validator import get_ui_combined_demand
from browser_driver import start_browser, close_browser
from ui_validator import get_ui_combined_demand

def run_tests():

    print("\n===== DASHBOARD VALIDATION STARTED =====\n")
    MAX_TESTS = 30
    tests = generate_tests()[:MAX_TESTS]
    print(f"\nTotal Test Cases Generated: {len(tests)}")

    results = []

    total_tests = len(tests)
    passed = 0
    failed = 0

    driver = start_browser()

    driver.get("http://localhost:8080")
    for i, test in enumerate(tests, start=1):

        print(f"\nRunning Test {i}/{len(tests)}")
        print(f"Department: {test['department']} | Gender: {test['gender']}")
        try:

            result = validate_combined_demand(test)

            existing = result["existing_demand"]
            future = result["future_demand"]
            combined = result["combined_demand"]

            # expected combined demand
            expected = existing + future

            ui_value = get_ui_combined_demand(driver)
            print("UI VALUE:", ui_value)
            if ui_value == combined:
                status = "PASS"
                passed += 1
            else:
                status = "FAIL"
                failed += 1

            row = {
                "department": test["department"],
                "gender": test["gender"],
                "location": test["location"],
                "month": test["month"],
                "existing_demand": existing,
                "future_demand": future,
                "backend_combined": combined,
                "ui_combined": ui_value,
                "expected_combined": expected,
                "status": status
            }

            results.append(row)

            print("Result:", row)

        except Exception as e:

            failed += 1
            print("Test failed:", e)

    accuracy = (passed / total_tests) * 100

    print("\n========== TEST SUMMARY ==========")
    print("Total Tests :", total_tests)
    print("Passed      :", passed)
    print("Failed      :", failed)
    print(f"Accuracy    : {accuracy:.2f}%")

    generate_report(results)

    print("\n===== TESTING COMPLETED =====\n")


if __name__ == "__main__":
    run_tests()