# Global User Onboarding Analytics

## 📌 Project Overview

This project analyzes 5,000 global user sign-up profiles to identify demographic patterns, regional data quality trends, and KYC compliance gaps. The analysis provides actionable insights for marketing optimization, product localization, and fraud prevention.

**Dataset:** 5,000 user profiles from the Random User Generator API.

---

## 🎯 Business Questions Answered

| Question                    | Answer                                                 |
| :-------------------------- | :----------------------------------------------------- |
| Who are our users?          | Mostly 60+ (37.9%), balanced gender split (51.2% male) |
| Where are they from?        | 21 countries, Mexico top (5.2%), no country dominates  |
| How many have IDs?          | 81.5% completed, 916 users (18.5%) missing             |
| Which age groups need help? | 18-25 (25.0% missing rate)                             |
| Which regions need help?    | "Other" (50.0%) and Oceania (49.7%)                    |

---

## 📊 Key Insights

### Demographics

- **Average Age:** 53 years
- **Gender:** 51.2% Male, 48.8% Female
- **Top Country:** Mexico (5.2%)
- **Total Countries:** 21

### KYC Compliance

- **Overall ID Completion:** 81.5%
- **Highest Missing Rate:** 18-25 age group (25.0%)
- **Highest Missing Region:** "Other" (50.0%)
- **Users Needing ID:** 916

### Data Quality

- **Features are independent** (no multicollinearity)
- **Missing Data:** Only `id_value` had missing values (handled)
- **Duplicates:** Removed 0 duplicate email records

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kusman123/global-user-onboarding-analytics.git
   cd global-user-onboarding-analytics
   ```
