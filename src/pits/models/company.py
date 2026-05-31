"""企业信息数据模型"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CompanyInfo:
    name: str = ""
    legal_representative: str = ""
    registered_capital: str = ""
    establishment_date: str = ""
    unified_social_credit_code: str = ""
    business_scope: str = ""
    contact: str = ""
    phone: str = ""
    address: str = ""
    certifications: List[str] = field(default_factory=list)
    past_projects: List[dict] = field(default_factory=list)
    key_personnel: List[dict] = field(default_factory=list)
