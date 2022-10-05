from typing import Optional

from pydantic import BaseModel


class AddressBase(BaseModel):
    addressLine: Optional[str] = ""
    city: Optional[str] = ""
    province: Optional[str] = ""
    postCode: Optional[str] = ""
