from fastapi import APIRouter, Depends
from src.schemas.autotrack import GetAutoTrackDTO, AutoTrackFilterData, CreateAutoTrackDTO, FilterEngine, FilterWeelDrive
from src.repositories.autotrack import AutoTracksRepository

router = APIRouter(
    tags=['Tracks'],
    prefix='/autotracks'
)

repository = AutoTracksRepository()

Track1 = CreateAutoTrackDTO(
    name = '',
    price = 15000,
    sleep_places = 2,
    passengers = 4,
    shower = True,
    engine_type = FilterEngine.PETROL,
    drive_license = 'B',
    drive_type = FilterWeelDrive.FRONT_WEEL
)
repository.create(Track1)
@router.get('', response_model=list[GetAutoTrackDTO])
async def get_tracks(limit: int = 1000, offset: int = 0, filter_data: AutoTrackFilterData = Depends(AutoTrackFilterData)):
    return await repository.get_all(limit, offset, filter_data=filter_data)


@router.get('/{autotrack_id}', response_model=GetAutoTrackDTO | None)
async def get_track(autotrack_id: int):
    return await repository.get(autotrack_id)

