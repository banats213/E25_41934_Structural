<<<<<<< Updated upstream
# A3 Submission – Tool

## 01 The tool - python script

The main.py file will include all relevant functions and scripts from the analyst groups. The goal is for the combined script to smoothly incorporate every analyst script, to work effortsly on a given ifc-model.

# A4: External BIManalyst Tools – A3 Context

This document summarizes the external BIManalyst tools in the `external/` folder and relates them to the A3 "Tool" assignment requirements. It serves as preparation and background for A4, where we teach and communicate how our own structural tool fits into the broader pattern.

---
## 1. Overview of External Groups

- `BIManalyst_g_20`  
	- `main.py` opens an IFC model and runs two rule modules: `windowRule` and `doorRule`.  
	- Demonstrates a simple manager script that delegates specific checks to separate rule files in a `rules/` subfolder.

- `BIManalyst_g_22`  
	- README describes structural analysis of walls and a claim about **23 structural load-bearing walls**.  
	- Script `count_walls_rule.py` (under `rules/`) uses `ifcopenshell` to count walls per floor and exclude footings with wall-like properties.  
	- Good example of: clear focus area, concrete claim, explicit report reference, and a single, focused rule script.

- `BIManalyst_g_23`  
	- `main.py` opens an IFC file and extracts all `IfcBeam` instances, their property sets and associated materials.  
	- README explains the claim that beams have programmatically accessible property sets and materials.  
	- Demonstrates IFC traversal via `IsDefinedBy` (property sets) and `HasAssociations` (materials).

- `BIManalyst_g_24`  
	- README clearly states group members, focus area (structure), claim (number and type of storeys), and report reference.  
	- `check_storey.py` counts `IfcBuildingStorey` elements, prints names and elevations, and tests whether the reported claim holds.  
	- Strong template for separating **analyst notes** (technical details) from **manager notes** (how and why the script is used).

- `BIManalyst_g_29`  
	- README is minimal; the main work is in `rules/` (beam dimension and classification checks) and `samples/` (IFC models).  
	- Includes multiple specialized scripts (`BeamClassifications.py`, `Dimensions.py`, `max_UDL.py`, etc.) that together check beam sizing, materials, and utilization.  
	- Illustrates a more extensive rule library rather than a single script.

---
## 2. Relation to A3 Assignment Requirements

Using the public A3 description (main script, markdown, IDS, BPMN, etc.), we can see how these external tools align and where our own structural tool extends them.

### 2.1 Main Python Script (`main.py`)
- External groups usually implement a small orchestration script (`main.py`) that:
	- Opens a specific IFC file inside the repo.
	- Imports one or more rule modules from a `rules/` folder.
	- Prints results directly to the console.
- Our A3 `main.py` follows this pattern but on a larger, manager/analyst scale:
	- Integrates functions and claims from multiple analyst groups (GR20, GR22, GR23, GR24, GR29).
	- Provides a single structural "manager" entry point, which is exactly what A3 asks for.

### 2.2 IFC Model Handling
- Many external scripts hardcode IFC file names, such as `25-06-D-STR.ifc` or `25-16-D-STR (2).ifc`, and store them in the repository.
- A3 requires that the **IFC model is not part of the submission**; instead, `main.py` should refer to a local path on the user’s machine.
- Our tool adapts this by using a configurable `model_path` variable (e.g. via `pathlib.Path`) instead of committing IFC files with the code.

### 2.3 Markdown / Documentation
- External READMEs typically cover:
	- Group number and focus area.
	- A specific claim from an Advanced Building Design report.
	- A short description of the script and what it checks.
- Our `A3_structural_tool.md` extends this pattern to fit the A3 markdown specification by also describing:
	- The broader use case (generalized structural validation, not a single claim).
	- Which Advanced Building Design stages (B/C/D) the tool supports.
	- Which subjects and users the tool is aimed at.
	- What information must be present in the IFC model.

### 2.4 IDS (Input Data Specification)
- External tools mostly describe their input implicitly through code: they access walls, beams, storeys, etc., but do not formally define an IDS file.
- A3 explicitly requires an IDS that checks whether a model contains the data needed by the tool.
- Our structural tool introduces `script_requirements.ids`, which:
	- Lists required IFC classes (e.g. `IfcWall`, `IfcBeam`, `IfcColumn`, `IfcSlab`).
	- Ensures key properties like dimensions, IDs and fire ratings are present.
	- Produces `ids_report.html` to document which requirements are met or missing.

### 2.5 BPMN and Workflow (Peer Presentation)
- External examples tend to explain workflows in text form, not as explicit BPMN diagrams.
- For A3 (and in preparation for A4 teaching), we add:
	- `A3_as_is.bpmn` – current structural tool workflow.
	- `A3_to_be.bpmn` – proposed, more integrated future workflow.
- These diagrams make it easier to explain, in A4, how scripts from different analyst groups fit together.

---
## 3. How Our Structural Tool Builds on These Examples

- **From Single Checks to an Integrated Pipeline**  
	External groups usually validate **one** claim (wall count, storey count, beam properties). Our structural tool combines multiple claim types into one pipeline: slab → beam → column utilization, and wall fire/load-bearing checks, all feeding into a unified report.

- **From Ad-Hoc Scripts to a Manager/Analyst Structure**  
	The external pattern of `main.py + rules/` is preserved, but we strengthen the manager/analyst distinction: `main.py` acts as the manager coordinating several analyst functions, which is directly aligned with the course’s manager/analyst concept.

- **From Hardcoded Files to Configurable Paths + IDS**  
	Rather than assuming a specific IFC model in the repo, our tool expects the user to set `model_path` locally and uses the IDS to ensure that any chosen model is suitable for the analysis.

---
## 4. Using This Comparison in A4 (Teach)

In A4, when presenting or teaching our tool, we can:

- Show how it generalizes and integrates patterns from earlier BIManalyst groups (external examples).
- Emphasize the improvements that respond to updated A3 requirements: no IFC in repo, explicit IDS, clear BPMN diagrams, and richer markdown documentation.
- Use specific external groups as examples when explaining:
	- Simple claim checking (e.g. wall count – g_22, storey count – g_24).
	- Property and material extraction (g_23).
	- Building a library of beam rules (g_29).
- Then position our structural `main.py` as the next step: a manager script that coordinates and scales these ideas.

This README in `A4/` is therefore both a comparison to external work and a teaching aid for explaining our own A3 tool.


(to be done)

---
=======
 # BIMmanager group "Structural"

