# Library Data Automation Project

## 1. Project Introduction

### Background
The library currently performs data quality checks and reporting manually. This process is time-consuming, prone to human error, and difficult to scale as data volumes increase. There is also limited automation, which prevents stakeholders, librarians, and users from accessing up-to-date information.

### Project Aim
The aim of this project is to design and implement an **automated data processing pipeline** using Python, GitHub, and Azure DevOps. The solution will clean, validate, and transform library data, producing a presentation-ready dataset for reporting in Power BI.

### Objectives
- Reduce manual effort through automation  
- Improve data quality, consistency, and reliability  
- Enable repeatable and auditable data transformations  
- Provide timely insights for operational and strategic decision-making  

---

## 2. Project Timeline & Phases

| Phase | Description | Duration |
|-----|------------|----------|
| Planning & Exploration | Requirements gathering, data exploration, architecture design | 10 days |
| Data Storage & Cleaning | Data quality checks, table definition, validation, reporting | 10 days |
| Test & Development | Python development and unit testing | 5 days |
| Deployment | CI/CD pipeline setup | 3 days |
| Automation | Automated pipeline execution | 3 days |
| Reporting & Visualisation | Power BI dashboards and insights | 7 days |
| Technical Documentation | Final documentation and handover | 2 days |

---

## 3. Architecture Overview

<img width="741" height="137" alt="image" src="https://github.com/user-attachments/assets/8758a4cc-80ba-40eb-a6de-77f8397015ce" />


## 4. Dev Notes
Cleaning logic created and stored in the Repo. 
Begun creation of Unit Tests to confim function performance

## 5. Docker
Required files are in docker_data_clean
app_refactored.py modified to write to a pair of CSV's at time of run
To run appropriately, mount the volume where the uncleaned csv's reside, this will also be the volume where cleased csv's are written to
syntax is : docker run -it -v "C:\Users\Admin\Desktop\M5-2026-01-06\data:/app/data" dataclean

Next phase of development is to allow docker to write to the SQL storage - this is in docker_data_clean_sql


-it = interactive mode 
-v  = the volume to be mounted
 

