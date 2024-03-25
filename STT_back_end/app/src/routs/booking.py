from fastapi import APIRouter, Depends
from src.schemas.booking import CreateBookingDTO, GetBookingDTO, UpdateBookingDTO, BookingFilterData
from src.repositories.booking import BookingRepository

router = APIRouter(
    tags=['Booking'],
    prefix='/booking'
)

repository = BookingRepository()


@router.get('/{transaction_type}', response_model=list[GetBookingDTO])
async def get_donation_transactions(limit: int = 1000, offset: int = 0):
    return await repository.get_all(limit, offset, filter_data=filter_data)


@router.post('/{transaction_type}', response_model=GetBookingDTO | None)
async def create_donation_transactions(data: CreateDonationTransactionDTO):
    return await repository.create(transaction_type, data)


@router.get('/{transaction_type}/{transaction_id}', response_model=GetDonationTransactionWithRelatedDTO | None)
async def get_donation_transaction(transaction_type: TransactionType, transaction_id: int):
    return await repository.get(transaction_type, transaction_id)


@router.delete('/{transaction_type}/{transaction_id}')
async def delete_donation_transactions(transaction_type: TransactionType, transaction_id: int):
    await repository.delete(transaction_type, transaction_id)


@router.patch('/{transaction_type}/{transaction_id}')
async def change_donation_transaction(transaction_type: TransactionType, transaction_id: int, data: UpdateDonationTransactionDTO):
    await repository.update(transaction_type, transaction_id, data)


@router.post('/{transaction_type}/{transaction_id}/respond/{related_transaction_id}')
async def bind_donation_transactions(transaction_type: TransactionType, transaction_id: int, related_transaction_id: int):
    await repository.bind_transactions(transaction_type, transaction_id, related_transaction_id)


@router.post('/{transaction_type}/{transaction_id}/respond/{related_transaction_id}/complete')
async def bind_donation_transactions(transaction_type: TransactionType, transaction_id: int, related_transaction_id: int):
    await repository.change_binding_transaction_status(transaction_type, transaction_id, related_transaction_id, DonationTransactionStatus.COMPLETED)



