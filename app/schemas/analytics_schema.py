from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class PageViewSchema(BaseModel):
    id: int
    path: str
    user_agent: Optional[str] = None
    ip_hash: str
    referrer: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class DailyMetricSchema(BaseModel):
    id: int
    date: date
    page_views: int
    unique_visitors: int
    
    class Config:
        from_attributes = True

class AnalyticsSummarySchema(BaseModel):
    total_views: int
    unique_visitors: int
    today_views: int
    top_pages: list[dict]
