<<<<<<< Updated upstream
# A3 Submission – Tool

## 01 The tool - python script

The main.py file will include all relevant functions and scripts from the analyst groups. The goal is for the combined script to smoothly incorporate every analyst script, to work effortsly on a given ifc-model.

Analyst scripts included in main.py file:
-   
-   
-   
-   

---

## 03 Markdown file

A markdown file has been added in the A3 folder describing the tool itself and relating it to advanced building design.
(not done yet)

Name of file: **A3_structural_tool.md**


---

## An IDS

The IDS file is included in the subfolder "rules" in the main repository. It will also be included in the main-folder with the script and model itself. 

The IDS-file is named "script_requirements.ids".

The script checks if the model contains relevant element properties (walls, beams etc.) and if they have properties like **dimensions** and **ID**.


---

## 1. As is BPMN diagram

A BPMN diagram describing how the entire structural main-script is working has been added in the A3-folder.

Use an online viewer or program to see the bpmn-diagram.

Name of file: **A3_as_is.bpmn**


---

## 2. Aim

The aim for the entire structural main.py script is to validate claims made by each analyst group. These analyst group claims are then "generalized" so they can be applied to any given building/scenario. 

The entire main.py script will then take all analyst scripts into account to create a cohesive program, that can take an ifc-file as an input, and then output relevant structural properties.

The aim is to determine the structural capacity of beams and columns and applying loads derived from the floor space on them. The utilization can then be determined. 

Requirements in regard to wall, beam and column dimensions are also investigated.


---

## 3. To be BPMN diagram

A BPMN diagram describing how the entire structural main-script is supposed/wished to be working has been added in the A3-folder.

It describes how the different analyst scripts in the end will be working together. (not done entirely yet)

Use an online viewer or program to see the bpmn-diagram.

Name of file: **A3_to_be.bpmn**


---

## 4. The tool

Overall, the tool performs a structural analysis of a given building, using ifc-properties like "walls", "beams" and "columns" to determined load and capacity of structural members. 

For the walls, 

It takes 


---

## 5. Output

The output of th program is a list/report/sheet of the structural members and their utilization. 

Each structural member will have its own column, and the most utilied member(s) will be shown first.

For walls, fire requirements are shown as "upheld" or "not upheld".

---
=======
 # BIMmanager group "Structural"

