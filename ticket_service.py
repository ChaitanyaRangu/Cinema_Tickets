
from purchase_exceptions import InvalidPurchaseException
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService
import constants




class TicketService:

    def __init__(self):
        self.type_to_count_dict = {}
        self.seat_reservation_service = SeatReservationService()
        self.ticket_payment_service = TicketPaymentService()

    def purchase_tickets(self, account_id, ticket_type_requests):

        self.__validating_accountid_and_requests(account_id, ticket_type_requests)

        self.__populate_dictionary_with_requests(ticket_type_requests)

        self.__validate_total_tickets()

        self.__call_payment_and_seatbooking_services(account_id)

    def __call_payment_and_seatbooking_services(self, account_id):

        # caluculate the ammount to be paid
        total_ammount = self.__caluculate_total_ammount_to_be_paid()

        # caluculate the no of seats to be booked
        total_seats = self.__caluculate_total_number_of_seats()

        # calling payment service and booking service
        self.seat_reservation_service.reserve_seat(account_id, total_seats)
        self.ticket_payment_service.make_payment(account_id, total_ammount)

    def __validate_total_tickets(self):

        if self.type_to_count_dict.get("ADULT",0) == 0:
            raise InvalidPurchaseException("Atleast One Adult must be present")
        if self.type_to_count_dict.get("ADULT", 0) < self.type_to_count_dict.get("INFANT",0):
            raise InvalidPurchaseException("No of Adults must be greater than Infants")
        if self.type_to_count_dict.get("ADULT", 0) + self.type_to_count_dict.get("CHILD", 0) + self.type_to_count_dict.get("INFANT", 0) > constants.maximum_tickets:
            raise InvalidPurchaseException("Total No tickets in a attempt must be less than or equal to 20")


    def __caluculate_total_number_of_seats(self):
        return self.type_to_count_dict.get("ADULT", 0) + self.type_to_count_dict.get("CHILD", 0)

    def __caluculate_total_ammount_to_be_paid(self):
        total_ammount = 0

        for tickets_type, no_of_tickets in self.type_to_count_dict.items():
            total_ammount += no_of_tickets* constants.type_to_price_dict.get(tickets_type,0)

        return total_ammount

    def __populate_dictionary_with_requests(self, ticket_type_requests):

        for request in ticket_type_requests:
            if not self.type_to_count_dict.get(request.ticket_type):
                self.type_to_count_dict[request.ticket_type] = request.number_of_tickets
            else:
                self.type_to_count_dict[request.ticket_type] = request.number_of_tickets + self.type_to_count_dict.get(request.ticket_type)


    def __validating_accountid_and_requests(self, account_id, ticket_type_requests):

        self.__validate_accountid(account_id)
        self.__validate_ticket_type_requests(ticket_type_requests)


    def __validate_accountid(self, account_id):

        if not isinstance(account_id, int):
            raise TypeError("account_id must be an integer")

        if account_id < constants.minimum_account_id:
            raise InvalidPurchaseException("Account Id must be a positive Integer")

    def __validate_ticket_type_requests(self, ticket_type_requests):

        if(len(ticket_type_requests)==0):
            raise TypeError("ticket requets must be atleast one")