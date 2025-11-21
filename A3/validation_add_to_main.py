import subprocess
import sys
from pathlib import Path
import ifcopenshell

## Add the following function to your existing script "main.py"
## It runs IDS validation using IfcTester before proceeding with the rest of the script.

# ---------- IDS Validation ----------
def validate_ifc_with_ids(ifc_path: str, ids_path: str, report_path: str = "ids_report.html") -> bool:
    """Run IDS validation using IfcTester."""
    print("🔍 Running IDS validation...")
    result = subprocess.run(
        ["ifctester", "-i", ifc_path, "-s", ids_path, "-r", report_path],
        check=False, capture_output=True, text=True
    )

    if result.returncode == 0:
        print("✅ IDS validation passed.")
        return True
    else:
        print("❌ IDS validation failed. See:", report_path)
        print(result.stdout)
        print(result.stderr)
        return False


# ---------- Main Script ----------
def main():
    ifc_file = Path("models/sample.ifc")
    ids_file = Path("script_requirements.ids")

    if not ifc_file.exists():
        print(f"⚠️ IFC file not found: {ifc_file}")
        sys.exit(1)

    # Step 1: Run IDS validation
    if not validate_ifc_with_ids(str(ifc_file), str(ids_file)):
        print("Aborting: IFC model did not meet IDS requirements.")
        sys.exit(1)

    # Step 2: Continue with your IFC logic
    print("📦 Loading IFC model...")
    model = ifcopenshell.open(ifc_file)

    walls = model.by_type("IfcWall")
    print(f"Found {len(walls)} walls.")

    # ... add Bonsai / IfcOpenShell logic here ...


if __name__ == "__main__":
    main()
