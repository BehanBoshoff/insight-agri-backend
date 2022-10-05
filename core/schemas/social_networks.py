from typing import Optional

from pydantic import BaseModel


class SocialNetworksBase(BaseModel):
    linkedIn: Optional[str] = ""
    facebook: Optional[str] = ""
    twitter: Optional[str] = ""
    instagram: Optional[str] = ""
