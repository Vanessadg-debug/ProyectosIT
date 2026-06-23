# ETL-Data-Validation-Pipeline

## Project Description
This project focuses on the design and implementation of an automated ETL (Extract, Transform, Load) pipeline to manage and analyze marketing campaign metrics. The system centralizes raw data from various sources, transforms it to ensure data integrity through 3NF normalization, and loads it into a robust SQL Server database for analysis and reporting.

## Technology Stack
- **Database:** Microsoft SQL Server (Express Edition).
- **Data Modeling:** dbdiagram.io (ERD Design).
- **Version Control:** Git & GitHub.
- **Processing Language:** Python (Pandas).

## Database Architecture
The database schema was designed following Third Normal Form (3NF) principles to minimize redundancy and maximize data consistency.

### Entity-Relationship Diagram (ERD)
![ERD Diagram](assets/dbstructure.png)

## Project Structure
- `/database`: Contains the SQL scripts for DDL (Data Definition Language) and table constraints.
- `/docs`: Project documentation and architecture design.

## Project Status

- [x] Architecture design and relational model.
- [x] Database schema implementation (DDL).
- [x] Header validation logic — 15 of 16 test cases solved.
  - [x] Missing headers (full and partial detection)
  - [x] Duplicate header detection
  - [x] Vertical offset (dynamic header repositioning)
  - [x] Horizontal offset and combined row/column offsets
  - [x] Extraneous user-added columns (automatic cleanup)
  - [ ] Combined edge-case scenario (Frankenstein case) — pending architecture refactor
- [ ] Database integration of validated data.

All test cases are self-designed using a combinatorial decision-table approach, and the suite is continuously updated as new edge cases are identified.

Developed as part of my continuous improvement in Data Engineering and Quality Assurance.
