<<<<<<< Updated upstream
# A1 Submission – Forensic BIM

## Group Information
- **Group Number:** Group 22
- **Focus Area:** Structural analysis of walls in the model `25-08-D-STR.ifc`

---

## Claim Being Checked
- **Claim:** The consultant report states, that there are 23 walls in the building used for structural load-bearing.  
- **Source:** The given claim is found in the report: *D_Report_Team08_STR*, page 16.

---

## Script Description

### Analysts part for group 22
The script is called **`count_walls_rule`** and is written in Python using the **ifcopenshell** package to analyze an IFC model.  

- It loads every property for the walls, enabling further analysis.  
- It counts the number of walls on each floor.  
- Footings with wall properties are excluded from the count.  

This allows verification of whether the model matches the consultant report’s claim of 23 load-bearing walls.

---
### For Managers
All groups apart from 1 have been added as submodules. This group has not yet sent a link to be added.  

We have attempted to run through the different scripts made by other groups. For smoother collaboration, the following requirements have been identified:

- A dedicated folder should be added in the manager repository where IFC files can be stored and accessed directly by the scripts.  
- All groups should use **consistent file names** for the building to ensure compatibility across scripts.  
=======
 # BIMmanager group "Structural"
>>>>>>> Stashed changes
