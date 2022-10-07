from typing import List

from sqlalchemy.orm import Session

from db.models.address import Address


def get_addresses(addresses: List[Address], db: Session) -> List[Address]:
    db_addresses = []
    for address in addresses:
        db_address = (
            db.query(Address)
            .filter(
                Address.addressLine == address.addressLine,
                Address.city == address.city,
                Address.postCode == address.postCode,
                Address.province == address.province,
            )
            .first()
        )
        if db_address:
            db_addresses.append(db_address)
    return db_addresses


def get_base_address(db: Session) -> Address:
    address = db.query(Address).filter(Address.id == 1).first()
    return address
