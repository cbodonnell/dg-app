from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def create_round(db: Session, round_info: schemas.RoundInfoCreate):
    round_db = models.RoundInfo(
        course=round_info.course,
        datetime=round_info.datetime,
        isactive=round_info.isactive,
    )
    db.add(round_db)
    db.flush()

    for player in round_info.players:
        player_db = models.PlayerInfo(
            round_id=round_db.id,
            player=player.player,
        )
        for hole, score in player.scores.items():
            setattr(player_db, hole, score)
        db.add(player_db)
    db.commit()
    db.refresh(round_db)

    return convert_info_response(round_db)

def get_round(db: Session, round_id: int) -> models.RoundInfo:
    round_db = db.query(models.RoundInfo).filter(models.RoundInfo.id == round_id).first()
    if round_db is None:
        raise HTTPException(status_code=404, detail="Round not found")
    return round_db

def update_round(db: Session, round_id: int, round_info: schemas.RoundInfoUpdate) -> models.RoundInfo:
    round_db = get_round(db, round_id)
    if round_db is None:
        raise HTTPException(status_code=404, detail="Round not found")

    if round_info.course:
        round_db.course = round_info.course
    if round_info.datetime:
        round_db.datetime = round_info.datetime
    if round_info.isactive is not None:
        round_db.isactive = round_info.isactive

    for player_update in round_info.players:
        player_db = next((p for p in round_db.players if p.player == player_update.player), None)
        if player_db is None:
            raise HTTPException(status_code=404, detail=f"Player {player_update.player} not found")
        if player_update.scores:
            for hole, score in player_update.scores.items():
                setattr(player_db, hole, score)

    db.commit()
    db.refresh(round_db)
    return round_db

def delete_round(db: Session, round_id: int):
    round_db = db.query(models.RoundInfo).filter(models.RoundInfo.id == round_id).first()
    if round_db is None:
        return None
    db.query(models.PlayerInfo).filter(models.PlayerInfo.round_id == round_id).delete()
    db.delete(round_db)
    db.commit()
    return round_id

def convert_info_response(round_info: models.RoundInfo) -> schemas.RoundInfoResponse:
    players = [
        schemas.PlayerInfoResponse(
            id=player.id,
            player=player.player,
            scores={f"h{i}_score": getattr(player, f"h{i}_score") for i in range(1, 19)},
        )
        for player in round_info.players
    ]

    return schemas.RoundInfoResponse(
        id=round_info.id,
        course=round_info.course,
        datetime=round_info.datetime,
        isactive=round_info.isactive,
        players=players,
    )
