# Date Extraction and Experience Calculation

This module provides functions to extract date ranges from text and calculate the total experience in years and months. The main functionalities include extracting various date formats from a string and calculating the total duration between these dates.

## Functions

### `extract_date_ranges`

This function extracts dates from a given text and parses them into `datetime` objects. It supports a variety of date formats.

**Signature:**

```python
def extract_date_ranges(text: str) -> List[datetime]:
```

**Parameters:**
- `text` (str): The input text containing date information.

**Returns:**
- `List[datetime]`: A list of parsed `datetime` objects.

**Example:**

```python
text = "Worked from 01 January 2010 to 31 December 2015, and from February 2016 to March 2019."
dates = extract_date_ranges(text)
print(dates)
```

### `calculate_total_experience`

This function calculates the total experience from a list of date ranges. It pairs the dates in the list and calculates the duration between each pair.

**Signature:**

```python
def calculate_total_experience(dates: List[datetime]) -> Tuple[int, int]:
```

**Parameters:**
- `dates` (List[datetime]): A list of `datetime` objects representing the start and end dates.

**Returns:**
- `Tuple[int, int]`: A tuple containing the total years and months of experience.

**Example:**

```python
dates = [datetime(2010, 1, 1), datetime(2015, 12, 31), datetime(2016, 2, 1), datetime(2019, 3, 1)]
total_years, total_months = calculate_total_experience(dates)
print(f"Total Experience: {total_years} years and {total_months} months")
```

## Usage

1. **Extract Dates:**

   Use the `extract_date_ranges` function to extract dates from a text string. This function uses a regular expression pattern to identify various date formats in the text and attempts to parse them into `datetime` objects.

2. **Calculate Experience:**

   Use the `calculate_total_experience` function to calculate the total experience in years and months from the extracted date ranges. The function pairs the dates and calculates the duration between each pair, summing up the total experience.

## Examples

### Example 1: Extracting Dates

```python
text = "I worked at Company A from 01/01/2010 to 31/12/2015, and at Company B from March 2016 to July 2019."
dates = extract_date_ranges(text)
print(dates)
# Output: [datetime(2010, 1, 1), datetime(2015, 12, 31), datetime(2016, 3, 1), datetime(2019, 7, 1)]
```

### Example 2: Calculating Experience

```python
dates = [datetime(2010, 1, 1), datetime(2015, 12, 31), datetime(2016, 2, 1), datetime(2019, 3, 1)]
total_years, total_months = calculate_total_experience(dates)
print(f"Total Experience: {total_years} years and {total_months} months")
# Output: Total Experience: 8 years and 2 months
```

This module provides a straightforward way to handle date extraction and experience calculation, making it useful for processing resumes, job applications, and other documents containing date ranges.
