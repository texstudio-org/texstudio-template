import json
from pathlib import Path

for json_path in Path(".").glob("**/*.json"):
    json_path_str = str(json_path)
    if json_path_str.startswith("."):
        continue
    print(f"Validating {json_path_str}")
    with open(json_path_str) as f:
        template_data = json.load(f)

    template_name = template_data["Name"]
    print(f"\tName field in JSON: {template_name}")
    expected_path = json_path.parent / f"template_{template_name}.json"
    print(f"\tExpected .json path: {expected_path}")
    print(f"\tActual .json path:   {json_path_str}")
    print("\tChecking whether .json path matches name")
    assert json_path == expected_path

    png_path = expected_path.with_suffix(".png")
    print(f"\tChecking whether .png exists: {png_path}")
    assert png_path.is_file()

    tex_path = expected_path.with_suffix(".tex")
    zip_path = expected_path.with_suffix(".zip")
    print(f"\tChecking whether .tex ({tex_path}) or .zip ({zip_path}) exists")
    assert (
        expected_path.with_suffix(".tex").is_file()
        or expected_path.with_suffix(".zip").is_file()
    )
    print()
