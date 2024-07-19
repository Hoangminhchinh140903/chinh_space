from datetime import datetime
import re
from typing import List, Tuple

def extract_date_ranges(text: str) -> List[datetime]:
    # Enhanced regex pattern to capture various date formats
    date_pattern = re.compile(
        r'(\b\d{1,2}\s+\w+\s+\d{4}|\b\w+\s+\d{4}|\b\d{1,2}/\d{1,2}/\d{2,4}|\b\d{1,2}-\d{1,2}-\d{2,4}|\b\d{1,2}\.\d{1,2}\.\d{2,4}|\b\d{4}-\d{2}-\d{2}|\b\w+\s+\d{2,4}|\b\d{4}/\d{1,2}/\d{1,2})',
        re.IGNORECASE
    )
    dates = date_pattern.findall(text)
    parsed_dates = []

    # Try to parse extracted dates into datetime objects using multiple formats
    date_formats = [
        "%d %B %Y", "%B %Y", "%d/%m/%Y", "%d/%m/%y", "%d-%m-%Y", "%d-%m-%y", "%d.%m.%Y", 
        "%d.%m.%y", "%Y-%m-%d", "%y.%m.%d", "%b %Y", "%Y/%m/%d"
    ]
    for date_str in dates:
        for fmt in date_formats:
            try:
                parsed_date = datetime.strptime(date_str, fmt)
                parsed_dates.append(parsed_date)
                break
            except ValueError:
                continue

    return parsed_dates

def calculate_total_experience(dates: List[datetime]) -> Tuple[int, int]:
    total_years = 0
    total_months = 0

    for i in range(0, len(dates), 2):
        if i + 1 < len(dates):
            start_date = dates[i]
            end_date = dates[i + 1]

            # Calculate year difference
            year_diff = end_date.year - start_date.year

            # Calculate month difference
            month_diff = end_date.month - start_date.month

            # Adjust year and month difference if necessary
            if month_diff < 0:
                year_diff -= 1
                month_diff += 12

            total_years += year_diff
            total_months += month_diff

    # Normalize months to years and months
    total_years += total_months // 12
    total_months = total_months % 12

    return total_years, total_months
