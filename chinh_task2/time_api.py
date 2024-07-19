from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from module import extract_date_ranges, calculate_total_experience

app = FastAPI()

class DateRangeText(BaseModel):
    text: str

class DateRanges(BaseModel):
    ranges: List[DateRangeText]

class ExperienceOutput(BaseModel):
    years: int
    months: int

@app.post("/calculate", response_model=ExperienceOutput)
async def calculate_date_difference(date_ranges: DateRanges):
    total_years = 0
    total_months = 0

    for date_range_text in date_ranges.ranges:
        try:
            dates = extract_date_ranges(date_range_text.text)
            if not dates or len(dates) % 2 != 0:
                raise HTTPException(status_code=400, detail="Input wrong date format")

            years, months = calculate_total_experience(dates)
            total_years += years
            total_months += months
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    # Normalize months to years and months
    total_years += total_months // 12
    total_months = total_months % 12

    return {"years": total_years, "months": total_months}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
