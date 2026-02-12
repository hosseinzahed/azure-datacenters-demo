from pydantic import BaseModel


class Datacenter(BaseModel):
    """Model representing a datacenter."""

    id: int
    name: str
    country: str
    city: str

    class Config:
        from_attributes = True
