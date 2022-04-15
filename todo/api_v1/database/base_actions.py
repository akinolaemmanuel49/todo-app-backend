from sqlalchemy.orm import Session


def save_to_db(db: Session, instance: object) -> object:
    """
    Save to database
    """
    db.add(instance)
    db.commit()
    return instance


def delete_from_db(db: Session, instance: object) -> object:
    """
    Delete from database
    """
    db.delete(instance)
    db.commit()
    return instance
