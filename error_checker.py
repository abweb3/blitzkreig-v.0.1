import os
import importlib
import traceback


def check_imports(directory):
    errors = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "error_checker.py":
                module_path = os.path.join(root, file)
                module_name = os.path.splitext(module_path)[0].replace(os.path.sep, ".")
                try:
                    importlib.import_module(module_name)
                except Exception as e:
                    error_message = (
                        f"Error in {module_path}:\n{traceback.format_exc()}\n"
                    )
                    if "No module named" in str(e):
                        missing_module = (
                            str(e).split("No module named ")[-1].replace("'", "")
                        )
                        error_message += f"Try installing the missing module: pip install {missing_module}\n"
                    errors.append(error_message)

    return errors


if __name__ == "__main__":
    project_root = (
        "vertex_trading_bot"  # Change this to the actual root of your project
    )
    all_errors = check_imports(project_root)

    if all_errors:
        print("Errors found:")
        for error in all_errors:
            print(error)
    else:
        print("No errors found.")
