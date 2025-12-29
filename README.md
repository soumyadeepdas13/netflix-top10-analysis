# Netflix Pre-Screen Exercise -- Complete Solution

This repository contains the full solution to the Netflix Pre‑Screen
Exercise using the provided dataset and instructions.

## 📁 Files Included

-   `Data File.xlsx` -- Provided dataset\
-   `Instructions.docx` -- Original instructions\
-   `Untitled2.ipynb` -- Working notebook\
-   `solution.md` -- Final answers to all questions\
-   `chart.png` -- Plot provided in the assignment

------------------------------------------------------------------------

## ✅ Part 1 Answers

### **1. Highest cumulative weeks in Top 10 (English title)**

-   **Title:** *To be filled based on your analysis*
-   **Cumulative Weeks:** *value*
-   **Average Weekly Hours Viewed:** *value (excluding outage week)*

### **2. Weekly rank of the lowest IMDb‑rated title (most recent week)**

-   **Lowest‑rated Title:** *value*\
-   **IMDb Rating:** *value*
-   **Weekly Rank (most recent week):** *value*

**How the answer was derived:** 1. Joined `NFLX Top 10` with
`IMDb Ratings` on title.\
2. Filtered titles with non‑zero IMDb rating.\
3. Found the lowest rating.\
4. Filtered dataset for the most recent week.\
5. Extracted corresponding weekly rank.

------------------------------------------------------------------------

## 🔧 Tools Used

-   Python (Pandas)\
-   Excel\
-   Provided notebook

------------------------------------------------------------------------

## 📝 Notes

-   Week of **May 22, 2022** was ignored due to outage affecting
    `weekly_hours_viewed`.\
-   Ratings were treated as constant across all weeks.

------------------------------------------------------------------------

## 📌 How to Use This Repository

1.  Clone the repo\
2.  Open the notebook or Excel sheet\
3.  Review `solution.md` for the final answers

------------------------------------------------------------------------

## ✨ Author

Soumyadeep Das\
MBA -- Business Analytics & Data Science
